"""Testes de classificacao do comparador com o repositorio original.

A propriedade que importa e uma so: um arquivo que este fork alterou nunca
pode ser classificado como 'seguro'. Se for, o --apply-safe troca a versao
traduzida pela do upstream e a traducao some sem deixar rastro.

Os testes montam repositorios git de verdade em tmp_path, com um fork e um
upstream, em vez de simular a saida do git. A classificacao depende de
merge-base e de diff entre refs, que e justamente o que um mock esconderia.

Stdlib + pytest apenas.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "check_upstream.py"


def git(repo: Path, *args: str) -> str:
    proc = subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True, text=True, check=True,
    )
    return proc.stdout.strip()


@pytest.fixture
def cenario(tmp_path: Path) -> dict:
    """Um upstream e um fork que divergiram, com um arquivo de cada tipo."""
    up = tmp_path / "upstream"
    up.mkdir()
    git(up, "init", "-q", "-b", "main")
    git(up, "config", "user.email", "up@example.com")
    git(up, "config", "user.name", "Upstream")

    (up / "intocado.md").write_text("original\n", encoding="utf-8")
    (up / "traduzido.md").write_text("English text\n", encoding="utf-8")
    git(up, "add", "-A")
    git(up, "commit", "-q", "-m", "base")
    fork_point = git(up, "rev-parse", "HEAD")

    fork = tmp_path / "fork"
    subprocess.run(["git", "clone", "-q", str(up), str(fork)], check=True)
    git(fork, "config", "user.email", "fork@example.com")
    git(fork, "config", "user.name", "Fork")
    git(fork, "remote", "add", "upstream", str(up))

    # O fork traduz um arquivo e deixa o outro como estava.
    (fork / "traduzido.md").write_text("Texto em portugues\n", encoding="utf-8")
    git(fork, "add", "-A")
    git(fork, "commit", "-q", "-m", "traduz")

    # O upstream mexe nos dois e cria um terceiro.
    (up / "intocado.md").write_text("original + melhoria\n", encoding="utf-8")
    (up / "traduzido.md").write_text("English text, revised\n", encoding="utf-8")
    (up / "novidade.md").write_text("brand new\n", encoding="utf-8")
    git(up, "add", "-A")
    git(up, "commit", "-q", "-m", "upstream avanca")

    return {"fork": fork, "up": up, "fork_point": fork_point}


@pytest.fixture
def script_no_fork(cenario, monkeypatch):
    """check_upstream.py resolve a raiz a partir do proprio caminho, entao o
    teste importa o modulo e aponta ROOT/LEDGER para o repositorio de teste."""
    sys.path.insert(0, str(ROOT / "scripts"))
    import check_upstream

    monkeypatch.setattr(check_upstream, "ROOT", cenario["fork"])
    monkeypatch.setattr(check_upstream, "LEDGER", cenario["fork"] / ".upstream-sync.json")
    return check_upstream, cenario


def classificar(check_upstream, cenario) -> dict[str, str]:
    fork = cenario["fork"]
    git(fork, "fetch", "upstream", "main", "-q")
    ours = git(fork, "rev-parse", "HEAD")
    fork_point = git(fork, "merge-base", ours, "upstream/main")
    mudancas = check_upstream.classify(fork_point, "upstream/main", ours, fork_point)
    return {c.path: c.category for c in mudancas}


def test_arquivo_que_traduzimos_vai_para_revisar(script_no_fork):
    check_upstream, cenario = script_no_fork
    cats = classificar(check_upstream, cenario)
    assert cats["traduzido.md"] == "revisar"


def test_arquivo_que_nao_tocamos_vai_para_seguro(script_no_fork):
    check_upstream, cenario = script_no_fork
    cats = classificar(check_upstream, cenario)
    assert cats["intocado.md"] == "seguro"


def test_arquivo_inedito_vai_para_novo(script_no_fork):
    check_upstream, cenario = script_no_fork
    cats = classificar(check_upstream, cenario)
    assert cats["novidade.md"] == "novo"


def test_apply_safe_preserva_a_traducao(script_no_fork):
    """A propriedade central: depois de aplicar o seguro, o arquivo traduzido
    continua em portugues e o intocado recebeu a melhoria do upstream."""
    check_upstream, cenario = script_no_fork
    fork = cenario["fork"]
    git(fork, "fetch", "upstream", "main", "-q")
    ours = git(fork, "rev-parse", "HEAD")
    fork_point = git(fork, "merge-base", ours, "upstream/main")
    mudancas = check_upstream.classify(fork_point, "upstream/main", ours, fork_point)

    aplicados = check_upstream.apply_safe(mudancas, "upstream/main")

    assert "traduzido.md" not in aplicados
    assert (fork / "traduzido.md").read_text(encoding="utf-8") == "Texto em portugues\n"
    assert (fork / "intocado.md").read_text(encoding="utf-8") == "original + melhoria\n"
    assert (fork / "novidade.md").read_text(encoding="utf-8") == "brand new\n"


def test_ledger_ausente_cai_no_ponto_de_divergencia(script_no_fork):
    check_upstream, cenario = script_no_fork
    assert check_upstream.read_ledger() == {}


def test_ledger_e_lido_com_bom(script_no_fork):
    """O ledger pode ser editado a mao no Windows, entao um BOM nao pode
    derrubar a leitura. Mesmo motivo do utf-8-sig nos demais scripts."""
    check_upstream, cenario = script_no_fork
    check_upstream.LEDGER.write_text(
        json.dumps({"last_reviewed_upstream": "abc123"}), encoding="utf-8-sig",
    )
    assert check_upstream.read_ledger()["last_reviewed_upstream"] == "abc123"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
