# Guia de Instalação

Este guia cobre todos os métodos de instalação do `claude-blog`, um ecossistema de
skills do Claude Code para criação, otimização e gestão de conteúdo de blog.

## Pré-requisitos

| Requisito | Versão | Finalidade |
|-----------|--------|------------|
| [CLI do Claude Code](https://docs.anthropic.com/en/docs/claude-code) | Mais recente | Runtime de todos os comandos `/blog` |
| Python | 3.11+ | Pontuação de qualidade e executores do contrato de entrega de 5 portões (analyze_blog, blog_preflight, blog_render, generate_hero, lint_prose etc.) |
| pip | Mais recente | Gestão de dependências Python |

O Claude Code precisa estar instalado e configurado antes de instalar o
`claude-blog`. Python 3.11+ é obrigatório para a pontuação de qualidade e para os
fluxos auxiliares, incluindo `analyze_blog.py`, `blog_preflight.py`,
`blog_render.py`, `generate_hero.py`, `lint_prose.py` e checagens relacionadas.
Comandos que não invocam esses auxiliares ainda funcionam sem Python, mas
instalações de produção devem incluí-lo.

---

## Instalação rápida (um comando)

### Linux / macOS

```bash
curl -sL https://raw.githubusercontent.com/AgriciDaniel/claude-blog/main/install.sh | bash
```

### Windows (PowerShell)

```powershell
irm https://raw.githubusercontent.com/AgriciDaniel/claude-blog/main/install.ps1 -OutFile install.ps1
pwsh -File ./install.ps1
```

> Baixar o script e executá-lo como arquivo, em vez de canalizar direto para o shell, permite inspecioná-lo antes e evita um falso positivo heurístico de antivírus que alguns scanners levantam em linhas únicas do tipo `iex (irm ...)`. Veja [SECURITY.md](../.github/SECURITY.md#antivirus-false-positives).

Os dois instaladores copiam automaticamente todas as skills, agentes, referências,
templates e scripts para os diretórios corretos de configuração do Claude Code.

---

## Instalação padrão (clone do git)

```bash
git clone https://github.com/AgriciDaniel/claude-blog.git
cd claude-blog
chmod +x install.sh
./install.sh
```

### Instalar as dependências Python

Os instaladores tentam instalar os pacotes Python de `requirements.txt` quando
Python e pip estão disponíveis. Se a instalação de dependências for pulada ou
falhar, rode isto depois da instalação principal:

```bash
python3 -m pip install -r requirements.txt
```

#### Instalação reproduzível com uv (v1.9.1 em diante)

Para higiene determinística de cadeia de suprimentos, o repositório traz o
`uv.lock` (142 pacotes com hashes SHA-256 para cada wheel). Reproduza o ambiente
de desenvolvimento exato com:

```bash
pip install uv          # uma única vez
uv sync --frozen        # instala a partir do uv.lock com verificação de hash
```

Este é o caminho recomendado para CI, auditoria e qualquer contexto em que
"funciona na minha máquina" não basta. O fluxo antigo `pip install -e ".[dev]"`
continua funcionando; ele apenas resolve as dependências transitivas do zero a
cada vez.

Regenere o `uv.lock` depois de editar os limites de dependência no `pyproject.toml`:

```bash
uv lock
```

**Dependências centrais:**

| Pacote | Versão | Finalidade |
|--------|--------|------------|
| textstat | >=0.7.3 | Pontuação de legibilidade (Flesch, Gunning Fog, SMOG) |
| beautifulsoup4 | >=4.12.0 | Parsing de HTML e de schema |
| lxml | >=5.0.0 | Backend de parser XML/HTML |
| jsonschema | >=4.20.0 | Validação de schema JSON-LD |

**Dependências opcionais** (liberam recursos avançados no `analyze_blog.py`):

```bash
pip install spacy                  # Reconhecimento de entidades, PLN avançado
python -m spacy download en_core_web_sm
pip install sentence-transformers  # Similaridade semântica e detecção de duplicatas
pip install scikit-learn           # Agrupamento para canibalização de tema
pip install language-tool-python   # Checagem de gramática e estilo (requer Java)
```

O script de análise funciona sem as dependências opcionais, recorrendo
automaticamente ao modo básico.

---

## Instalação manual (arquivo por arquivo)

Se preferir não rodar o instalador, copie os arquivos manualmente para estes
caminhos. O `~` se refere ao seu diretório pessoal (`$HOME` no Unix,
`%USERPROFILE%` no Windows).

### Estrutura de diretórios

```
~/.claude/
├── skills/
│   ├── blog/
│   │   ├── SKILL.md                          # Orquestrador principal
│   │   ├── references/
│   │   │   ├── content-rules.md
│   │   │   ├── geo-optimization.md
│   │   │   ├── google-landscape-2026.md
│   │   │   ├── quality-scoring.md
│   │   │   └── visual-media.md
│   │   ├── templates/                        # 12 templates por tipo de conteúdo
│   │   │   └── *.md
│   │   └── scripts/
│   │       └── analyze_blog.py
│   ├── blog-write/SKILL.md
│   ├── blog-rewrite/SKILL.md
│   ├── blog-analyze/SKILL.md
│   ├── blog-brief/SKILL.md
│   ├── blog-calendar/SKILL.md
│   ├── blog-strategy/SKILL.md
│   ├── blog-outline/SKILL.md
│   ├── blog-seo-check/SKILL.md
│   ├── blog-schema/SKILL.md
│   ├── blog-repurpose/SKILL.md
│   ├── blog-geo/SKILL.md
│   ├── blog-audit/SKILL.md
│   ├── blog-chart/SKILL.md            # somente interno
│   ├── blog-image/SKILL.md            # v1.4.0
│   ├── blog-cannibalization/SKILL.md
│   ├── blog-factcheck/SKILL.md
│   ├── blog-persona/SKILL.md
│   ├── blog-taxonomy/SKILL.md
│   ├── blog-notebooklm/SKILL.md       # v1.5.0
│   ├── blog-audio/SKILL.md            # v1.6.0
│   ├── blog-google/SKILL.md           # v1.6.5
│   ├── blog-cluster/SKILL.md          # v1.7.0
│   ├── blog-flow/SKILL.md             # v1.7.0
│   ├── blog-multilingual/SKILL.md     # v1.7.0
│   ├── blog-translate/SKILL.md        # v1.7.0
│   ├── blog-localize/SKILL.md         # v1.7.0
│   ├── blog-locale-audit/SKILL.md     # v1.7.0
│   ├── blog-brand/SKILL.md            # v1.8.0
│   ├── blog-discourse/SKILL.md        # v1.8.0
│   ├── blog-style/SKILL.md            # v1.10.0
│   └── blog-decay/SKILL.md            # v1.10.0
└── agents/
    ├── blog-researcher.md
    ├── blog-writer.md
    ├── blog-seo.md
    ├── blog-reviewer.md
    └── blog-translator.md             # v1.7.0
```

### Comandos de cópia (Unix)

```bash
# Cria os diretórios. As sub-skills são descobertas por glob do shell, para
# nunca ficarmos defasados frente à lista de diretórios (v1.8.6: substitui o
# mkdir manual de 14 skills da v1.4.0).
mkdir -p ~/.claude/skills/blog/{references,templates,scripts}
mkdir -p ~/.claude/scripts
for d in skills/blog-*/; do
    mkdir -p "${HOME}/.claude/skills/$(basename "$d")"
done
mkdir -p ~/.claude/agents

# Skill principal
cp skills/blog/SKILL.md ~/.claude/skills/blog/SKILL.md

# Referências
cp -R skills/blog/references/. ~/.claude/skills/blog/references/

# Templates
cp -R skills/blog/templates/. ~/.claude/skills/blog/templates/

# Sub-skills e seus diretórios de payload
for d in skills/blog-*/; do
    name=$(basename "$d")
    cp "$d/SKILL.md" "${HOME}/.claude/skills/$name/SKILL.md"
    for payload in references scripts assets templates; do
        if [ -d "$d/$payload" ]; then
            mkdir -p "${HOME}/.claude/skills/$name/$payload"
            cp -R "$d/$payload"/. "${HOME}/.claude/skills/$name/$payload/"
        fi
    done
    if [ -d "${HOME}/.claude/skills/$name/scripts" ]; then
        find "${HOME}/.claude/skills/$name/scripts" -type f -name '*.py' -exec chmod +x {} +
    fi
done

# Agentes
cp agents/*.md ~/.claude/agents/

# Scripts da raiz
for f in scripts/*.py; do
    name=$(basename "$f")
    cp "$f" "${HOME}/.claude/scripts/$name"
    chmod +x "${HOME}/.claude/scripts/$name"
    if [ "$name" = "analyze_blog.py" ]; then
        cp "$f" ~/.claude/skills/blog/scripts/analyze_blog.py
        chmod +x ~/.claude/skills/blog/scripts/analyze_blog.py
    fi
done
```

---

## Opcional: geração de imagem por IA

O `claude-blog` pode gerar imagens próprias por Gemini AI (imagens principais,
ilustrações inline, cartões sociais). Isso exige o servidor nanobanana-mcp e uma
chave gratuita de API do Google AI.

### Configuração

```bash
# Obtenha sua chave gratuita em: https://aistudio.google.com/apikey
python3 skills/blog-image/scripts/setup_image_mcp.py --key SUA_CHAVE

# Verifique a configuração
python3 skills/blog-image/scripts/validate_image_setup.py
```

### Requisitos

| Requisito | Versão | Finalidade |
|-----------|--------|------------|
| Node.js | 18+ | Roda o `npx @ycse/nanobanana-mcp` |
| Chave de API do Google AI | Camada gratuita | Geração de imagem via Gemini |

Sem essa configuração, todos os comandos `/blog` funcionam normalmente usando
fotos de banco do Pixabay, Unsplash e Pexels. A geração de imagem por IA é um
acréscimo opcional.

---

## Verificação

Depois da instalação, confirme que está tudo no lugar:

### 1. Cheque os arquivos instalados

```bash
# Skill principal
ls ~/.claude/skills/blog/SKILL.md

# Os diretórios blog-* devem somar 31; o total é 32 diretórios de skill (1 orquestrador + 31 sub-skills); 30 comandos voltados ao usuário
ls ~/.claude/skills/blog-*/SKILL.md | wc -l

# Agentes (devem somar 5: blog-researcher, blog-writer, blog-seo, blog-reviewer, blog-translator)
ls ~/.claude/agents/blog-*.md | wc -l

# Referências (devem somar 22 arquivos .md)
ls ~/.claude/skills/blog/references/*.md | wc -l

# Script Python
ls ~/.claude/skills/blog/scripts/analyze_blog.py
```

### 2. Reinicie o Claude Code

Feche e reabra o Claude Code (ou reinicie a CLI) para carregar as skills novas:

```bash
# Se estiver rodando no terminal, saia e reinicie
claude
```

### 3. Teste um comando

```bash
# Dentro do Claude Code, rode:
/blog strategy "automação residencial"
```

Você deve ver o orquestrador rotear para a sub-skill `blog-strategy` e começar a
reunir contexto sobre o nicho.

### 4. Teste o script Python de análise

```bash
python3 ~/.claude/skills/blog/scripts/analyze_blog.py --help
```

Saída esperada:

```
usage: analyze_blog.py [-h] [--output OUTPUT] [--batch] input

Analyze blog post quality

positional arguments:
  input                 Blog file path or directory (with --batch)

options:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        Output file path (JSON)
  --batch               Analyze all blog files in directory
```

---

## Atualização

Puxe as mudanças mais recentes e rode o instalador de novo:

```bash
cd claude-blog
git pull
./install.sh
```

O instalador sobrescreve os arquivos existentes, então atualizar é seguro a
qualquer momento. Reinicie o Claude Code depois de atualizar.

---

## Desinstalação

### Desinstalação automatizada (Unix)

```bash
# A partir do repositório claude-blog
chmod +x uninstall.sh
./uninstall.sh
```

Isso remove:

- `~/.claude/skills/blog/` e `~/.claude/skills/blog-*/` (32 diretórios de skill: 1 orquestrador + 31 sub-skills; 30 comandos voltados ao usuário; o `blog-chart` é somente interno)
- `~/.claude/scripts/` (17 scripts na raiz: ai_citation_score, analyze_blog, blog_hygiene, blog_preflight, blog_render, cognitive_load, consistency_check, content_decay, dependency_smoke, discourse_research, generate_hero, lint_prose, load_untrusted_root, quality_gate, style_learn, sync_flow, validate_public_release)
- `~/.claude/agents/blog-*.md` (todos os 5 agentes: blog-researcher, blog-writer, blog-seo, blog-reviewer, blog-translator)

As credenciais compartilhadas do Google em `~/.config/claude-seo/` pertencem ao
usuário e podem ser usadas por outras skills. Os dois desinstaladores as deixam
intactas.

### Desinstalação manual

```bash
# Skill principal e todos os diretórios blog-* (descobre blog-* por glob)
rm -rf ~/.claude/skills/blog
rm -rf ~/.claude/skills/blog-*

# Todos os 5 agentes
rm -f ~/.claude/agents/blog-{researcher,writer,seo,reviewer,translator}.md

# Todos os 17 scripts da raiz (somente se nenhum outro plugin usar ~/.claude/scripts/)
rm -f ~/.claude/scripts/{ai_citation_score,analyze_blog,blog_hygiene,blog_preflight,blog_render,cognitive_load,consistency_check,content_decay,dependency_smoke,discourse_research,generate_hero,lint_prose,load_untrusted_root,quality_gate,style_learn,sync_flow,validate_public_release}.py
```

### Limpar as dependências Python (opcional)

```bash
pip uninstall textstat beautifulsoup4 lxml jsonschema
```

Reinicie o Claude Code depois de desinstalar para concluir a remoção.

---

## Solução de problemas de instalação

| Sintoma | Causa | Correção |
|---------|-------|----------|
| Comando `/blog` não encontrado | Claude Code não foi reiniciado | Feche e reabra o Claude Code |
| `python3: command not found` | Python não instalado ou fora do PATH | Instale o Python 3.11+ pelo seu gerenciador de pacotes |
| `pip install` falha | pip ausente ou versão errada do Python | Rode `python3 -m ensurepip --upgrade` |
| Permissão negada no `install.sh` | Script sem permissão de execução | Rode `chmod +x install.sh` |
| Arquivos fora de `~/.claude/` | Local de instalação errado | Confirme que `$HOME` aponta para seu diretório pessoal |

Para outros problemas, veja [TROUBLESHOOTING.md](TROUBLESHOOTING.md).
