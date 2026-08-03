#!/usr/bin/env python3
"""Compara o repositorio original com este fork e classifica o que da para trazer.

Este fork carrega traducao para portugues e correcoes proprias em 83 arquivos.
Um `git merge upstream/main` cego nao serve: onde o upstream reescreve um
arquivo inteiro que traduzimos, o git aceita a versao em ingles sem marcar
conflito, e a traducao some em silencio. Entao a decisao vem antes da mescla.

Cada arquivo mexido pelo upstream cai em uma categoria:

    seguro    nunca tocamos este arquivo; a versao do upstream pode entrar
    revisar   nos mexemos e o upstream tambem; exige trabalho manual
    novo      nao existe neste fork; pode entrar, talvez precise de traducao
    removido  o upstream apagou; decidir caso a caso

O ponto de comparacao fica em `.upstream-sync.json`, na raiz. Sem esse arquivo
a base e o ponto de divergencia entre os dois repositorios.

Uso:
    python3 scripts/check_upstream.py
    python3 scripts/check_upstream.py --format json
    python3 scripts/check_upstream.py --apply-safe
    python3 scripts/check_upstream.py --mark-reviewed
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass, asdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEDGER = ROOT / ".upstream-sync.json"
DEFAULT_REMOTE = "upstream"
DEFAULT_URL = "https://github.com/AgriciDaniel/claude-blog.git"

# Um arquivo novo debaixo destes prefixos chega em ingles e precisa de
# traducao antes de ser util aqui. Nao bloqueia nada, apenas sinaliza.
PT_PENDING_PREFIXES = ("docs/", "agents/", "skills/blog/templates/", "README.md", "CLAUDE.md")

# O upstream mexer aqui merece destaque no relatorio: sao os arquivos onde uma
# regressao passa despercebida com mais facilidade.
CRITICAL = ("scripts/analyze_blog.py", "agents/blog-reviewer.md", "install.ps1", "install.sh")


class UpstreamError(RuntimeError):
    """Falha esperada, reportada sem stack trace."""


@dataclass
class Change:
    path: str
    status: str          # A, M, D, R...
    category: str        # seguro | revisar | novo | removido
    pt_pending: bool
    critical: bool


def _git(*args: str, check: bool = True) -> str:
    """Roda git na raiz do repositorio, sem shell."""
    proc = subprocess.run(
        ["git", "-C", str(ROOT), *args],
        capture_output=True, text=True,
    )
    if check and proc.returncode != 0:
        raise UpstreamError(f"git {' '.join(args)} falhou: {proc.stderr.strip()}")
    return proc.stdout.strip()


def ensure_remote(remote: str, url: str) -> None:
    existing = _git("remote").splitlines()
    if remote not in existing:
        _git("remote", "add", remote, url)


def fetch(remote: str, branch: str) -> None:
    _git("fetch", remote, branch, "--quiet")


def read_ledger() -> dict:
    if not LEDGER.exists():
        return {}
    try:
        return json.loads(LEDGER.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError as exc:
        raise UpstreamError(f"{LEDGER.name} ilegivel: {exc}") from exc


def write_ledger(sha: str, note: str) -> None:
    LEDGER.write_text(
        json.dumps(
            {"last_reviewed_upstream": sha, "reviewed_on": date.today().isoformat(), "note": note},
            indent=2, ensure_ascii=False,
        ) + "\n",
        encoding="utf-8",
    )


def _we_touched(path: str, fork_point: str, ours: str) -> bool:
    """True quando este fork alterou o arquivo depois da divergencia."""
    proc = subprocess.run(
        ["git", "-C", str(ROOT), "diff", "--quiet", fork_point, ours, "--", path],
        capture_output=True, text=True,
    )
    # 0 = igual, 1 = diferente. Qualquer outra coisa e erro do git.
    return proc.returncode == 1


def _exists_here(path: str, ref: str) -> bool:
    proc = subprocess.run(
        ["git", "-C", str(ROOT), "cat-file", "-e", f"{ref}:{path}"],
        capture_output=True, text=True,
    )
    return proc.returncode == 0


def classify(base: str, upstream_ref: str, ours: str, fork_point: str) -> list[Change]:
    raw = _git("diff", "--name-status", f"{base}..{upstream_ref}")
    changes: list[Change] = []
    for line in raw.splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        status = parts[0]
        path = parts[-1]  # renomeacao traz origem e destino; o destino interessa

        if status.startswith("D"):
            category = "removido"
        elif not _exists_here(path, ours):
            category = "novo"
        elif _we_touched(path, fork_point, ours):
            category = "revisar"
        else:
            category = "seguro"

        changes.append(Change(
            path=path,
            status=status,
            category=category,
            pt_pending=category in ("novo", "seguro") and path.startswith(PT_PENDING_PREFIXES),
            critical=path in CRITICAL,
        ))
    return sorted(changes, key=lambda c: (c.category != "revisar", c.path))


def apply_safe(changes: list[Change], upstream_ref: str) -> list[str]:
    """Traz para a arvore de trabalho so o que nao reverte nada nosso."""
    take = [c.path for c in changes if c.category in ("seguro", "novo")]
    if take:
        _git("checkout", upstream_ref, "--", *take)
    return take


def render_table(changes: list[Change], base: str, upstream_ref: str, commits: int) -> str:
    if not changes:
        return f"Nada novo no upstream desde {base[:7]}."

    counts: dict[str, int] = {}
    for c in changes:
        counts[c.category] = counts.get(c.category, 0) + 1

    out = [
        f"{commits} commit(s) no upstream desde {base[:7]} (ate {upstream_ref}).",
        "",
        f"{'categoria':<10} {'arquivo':<52} notas",
        "-" * 82,
    ]
    for c in changes:
        notas = []
        if c.critical:
            notas.append("CRITICO")
        if c.pt_pending:
            notas.append("traduzir")
        if c.status.startswith("R"):
            notas.append("renomeado")
        out.append(f"{c.category:<10} {c.path:<52} {' '.join(notas)}")

    out += ["", "Resumo: " + ", ".join(f"{n} {k}" for k, n in sorted(counts.items()))]
    if counts.get("revisar"):
        out += [
            "",
            "Os arquivos em 'revisar' foram alterados dos dois lados. Aplique a",
            "intencao da mudanca sobre a versao daqui, em vez de trocar o arquivo",
            "inteiro, para nao perder a traducao. O procedimento esta em",
            "docs/UPSTREAM-SYNC.md, secao Aplicacao, passo 2.",
        ]
    return "\n".join(out)


def main() -> int:
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--remote", default=DEFAULT_REMOTE, help="remoto do repositorio original")
    p.add_argument("--url", default=DEFAULT_URL, help="URL usada se o remoto nao existir")
    p.add_argument("--branch", default="main", help="branch do upstream a comparar")
    p.add_argument("--ours", default="HEAD", help="referencia deste fork")
    p.add_argument("--format", choices=("table", "json"), default="table")
    p.add_argument("--no-fetch", action="store_true", help="nao busca do remoto")
    p.add_argument("--apply-safe", action="store_true",
                   help="traz para a arvore de trabalho os arquivos 'seguro' e 'novo'")
    p.add_argument("--mark-reviewed", action="store_true",
                   help="grava o HEAD do upstream como ponto ja revisado")
    args = p.parse_args()

    try:
        ensure_remote(args.remote, args.url)
        if not args.no_fetch:
            fetch(args.remote, args.branch)

        upstream_ref = f"{args.remote}/{args.branch}"
        upstream_sha = _git("rev-parse", upstream_ref)
        ours = _git("rev-parse", args.ours)
        fork_point = _git("merge-base", ours, upstream_ref)
        base = read_ledger().get("last_reviewed_upstream") or fork_point
        # Um ledger apontando para um commit que sumiu do upstream (rebase,
        # force-push) inutilizaria toda a comparacao. Cair para o ponto de
        # divergencia mostra demais, o que e melhor do que mostrar de menos.
        if subprocess.run(["git", "-C", str(ROOT), "cat-file", "-e", f"{base}^{{commit}}"],
                          capture_output=True).returncode != 0:
            print(f"Aviso: base {base[:7]} nao existe mais no upstream; usando o ponto de divergencia.",
                  file=sys.stderr)
            base = fork_point

        commits = int(_git("rev-list", "--count", f"{base}..{upstream_ref}") or 0)
        changes = classify(base, upstream_ref, ours, fork_point)

        applied: list[str] = []
        if args.apply_safe:
            applied = apply_safe(changes, upstream_ref)

        if args.mark_reviewed:
            write_ledger(upstream_sha, "revisado por scripts/check_upstream.py")

        if args.format == "json":
            print(json.dumps({
                "base": base,
                "upstream": upstream_sha,
                "ours": ours,
                "fork_point": fork_point,
                "commits_ahead": commits,
                "changes": [asdict(c) for c in changes],
                "applied": applied,
            }, indent=2, ensure_ascii=False))
        else:
            print(render_table(changes, base, upstream_sha, commits))
            if applied:
                print(f"\nAplicados na arvore de trabalho: {len(applied)} arquivo(s). "
                      f"Revise com 'git diff --cached' antes de commitar.")
        return 0
    except UpstreamError as exc:
        print(f"erro: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
