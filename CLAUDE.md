# Claude Blog - Skill de Criação e Otimização de Blog

## Visão geral do projeto

Este repositório contém o **Claude Blog**, uma skill Tier 4 do Claude Code para criação,
otimização e gestão de conteúdo de blog. Segue o padrão aberto Agent Skills e a
arquitetura de 3 camadas (diretiva, orquestração, execução). São 32 diretórios de skill
(1 orquestrador + 31 sub-skills), 30 comandos `/blog` voltados ao usuário, 5 subagentes
especializados, 12 templates de conteúdo e 22 reference docs, com dupla otimização para
ranqueamento no Google (linha do tempo de core e spam updates de 2026, E-E-A-T) e para
citação por IA (GEO/AEO). Inclui integração com o framework FLOW, planejamento e execução
de cluster semântico de temas, publicação multilíngue (Pro Hub Challenge v1.7.0),
carregamento automático dos arquivos de contexto BRAND.md/VOICE.md/DISCOURSE.md na raiz do
projeto (v1.8.0, delimitados por `scripts/load_untrusted_root.py` com nonces CSPRNG, v1.8.3
em diante), higiene de prosa imposta pela CI via `scripts/lint_prose.py` (v1.8.4 em diante)
e o Blog Delivery Contract de 5 portões (v1.9.0,
`skills/blog/references/blog-delivery-contract.md`), que roda o `blog_preflight.py` mais um
agente `blog-reviewer` BLOQUEANTE entre cada rascunho e o usuário.

## Arquitetura

```
claude-blog/
  CLAUDE.md                          # Instruções do projeto (este arquivo)
  docs/CONTRIBUTORS.md               # Atribuição do Pro Hub Challenge e decisões de integração
  CHANGELOG.md                       # Formato Keep a Changelog
  .claude-plugin/plugin.json         # Manifesto do plugin (v2.1.1)
  .claude-plugin/marketplace.json    # Catálogo de marketplace para distribuição
  .mcp.example.json                  # Exemplo de config MCP (versionado; .mcp.json está no gitignore)
  pyproject.toml                     # Empacotamento Python (3.11+)
  brain/                             # Brain Obsidian vendorizado, autocontido e com evidência exigida; não é payload do plugin; o ferramental fica em skills/
  scripts/analyze_blog.py            # Pontuação de qualidade em 5 categorias (biblioteca padrão)
  scripts/blog_preflight.py          # Executor do contrato de entrega de 5 portões (v1.9.0)
  scripts/blog_render.py             # Renderizador md -> html -> pdf; JSON-LD à prova de XSS (v1.9.0)
  scripts/blog_hygiene.py            # Higiene determinística opcional: carregamento tardio de imagens + sumário automático (v1.11.0)
  scripts/cognitive_load.py          # Analisador de densidade de conceitos por seção (v1.8.0)
  scripts/discourse_research.py      # Síntese de briefing de discurso a partir de JSON de resultados de busca (v1.8.0)
  scripts/generate_hero.py           # Escada de imagem principal: Banana -> Gemini -> banco de imagens -> Openverse (v1.9.0)
  scripts/load_untrusted_root.py     # Auxiliar de cerca imposta por código para BRAND/VOICE/DISCOURSE (v1.8.3)
  scripts/lint_prose.py              # Linter de higiene de prosa ciente de cercas (v1.8.4; imposto pela CI)
  scripts/sync_flow.py               # Puxa as referências do FLOW (biblioteca padrão, em caixa de areia)
  scripts/ai_citation_score.py       # Heurística de prontidão para citação por IA, 0-100
  scripts/content_decay.py           # Detector de decaimento de conteúdo via GSC: queda de 20%+ no trimestre (v1.10.0)
  scripts/quality_gate.py            # Portão de pre-commit: barra posts com nota abaixo de 70 (v1.10.0)
  scripts/style_learn.py             # Aprendiz de perfil de voz do autor a partir de posts de amostra (v1.10.0)
  scripts/consistency_check.py       # Validação local de referências e do lock do FLOW
  scripts/dependency_smoke.py        # Checagens offline de inicialização de dependências opcionais
  scripts/validate_public_release.py # Validação somente leitura da worktree pública
  skills/                            # 32 diretórios de skill (1 orquestrador + 31 sub-skills)
    blog/SKILL.md                   # Orquestrador principal, roteamento, pontuação
      references/                   # 22 arquivos de conhecimento sob demanda (5 na v1.8.0, 1 na v1.9.0)
      templates/                    # 12 templates de conteúdo
      scripts/                     # Scripts Python de análise
    blog-write/SKILL.md            # Escreve artigos novos do zero
    blog-rewrite/SKILL.md         # Otimiza posts existentes
    blog-analyze/SKILL.md         # Pontuação de 100 pontos em 5 categorias
    blog-brief/SKILL.md           # Briefings de conteúdo detalhados
    blog-outline/SKILL.md         # Roteiros informados por resultados de busca
    blog-calendar/SKILL.md        # Calendários editoriais
    blog-strategy/SKILL.md        # Posicionamento e planejamento do blog
    blog-seo-check/SKILL.md      # Validação de SEO após a escrita
    blog-schema/SKILL.md          # Geração de schema JSON-LD
    blog-chart/SKILL.md           # Visualizações de dados em SVG inline
    blog-repurpose/SKILL.md       # Reaproveitamento em várias plataformas
    blog-geo/SKILL.md             # Otimização para citação por IA
    blog-audit/SKILL.md           # Avaliação de saúde do blog inteiro
    blog-image/                    # Geração de imagem por IA via Gemini
      SKILL.md                    # Sub-skill de geração de imagem
      references/                 # 3 reference docs (modelos, ferramentas, prompts)
      scripts/                    # Scripts de configuração e validação de MCP
    blog-cannibalization/SKILL.md # Detecção de sobreposição de palavra-chave
    blog-factcheck/SKILL.md       # Verificação de estatísticas
    blog-persona/SKILL.md         # Gestão de personas de escrita
    blog-taxonomy/SKILL.md        # Gestão de taxonomia no CMS
    blog-notebooklm/               # Pesquisa ancorada em fonte via NotebookLM
      SKILL.md                    # Sub-skill de consulta ao NotebookLM
      references/                 # 2 reference docs (comandos, solução de problemas)
      scripts/                    # 10 scripts Python + requirements.txt
    blog-audio/                    # Narração em áudio via Gemini TTS
      SKILL.md                    # Sub-skill de geração de áudio
      references/                 # 1 reference doc (catálogo de 30 vozes)
      scripts/                    # 5 scripts Python + requirements.txt
    blog-google/                   # Integração com APIs do Google
      SKILL.md                    # Sub-skill de API do Google (13 comandos, 4 níveis)
      references/                 # 3 reference docs (autenticação, API, cotas)
      scripts/                    # 11 scripts de API do Google + wrapper de venv
      assets/templates/           # 3 templates de relatório
    blog-cluster/                  # Planejamento e execução de cluster semântico (v1.7.0)
      SKILL.md                    # Orquestrador de planejamento e execução de cluster
      references/                 # 3 reference docs (clusterização semântica, arquitetura, execução)
    blog-flow/                     # Prompts do framework FLOW (v1.7.0)
      SKILL.md                    # Orquestrador do FLOW (find/optimize/win/prompts/sync)
      references/                 # Sincronizadas de github.com/AgriciDaniel/flow (CC BY 4.0)
    blog-multilingual/             # Publicação internacional em um comando (v1.7.0)
      SKILL.md                    # Orquestrador multilíngue
    blog-translate/                # Tradução otimizada para SEO (v1.7.0)
      SKILL.md
      references/                 # Regras de tradução + perfis de adaptação cultural
    blog-localize/                 # Adaptação cultural profunda (v1.7.0)
      SKILL.md
    blog-locale-audit/             # QA de conteúdo multilíngue (v1.7.0)
      SKILL.md
    blog-brand/SKILL.md            # Arquivos de contexto BRAND.md + VOICE.md (v1.8.0)
    blog-discourse/SKILL.md        # Pesquisa de discurso dos últimos 30 dias (v1.8.0)
    blog-style/SKILL.md            # Aprendiz de perfil de voz do autor (v1.10.0)
    blog-decay/SKILL.md            # Detector de decaimento de conteúdo via GSC (v1.10.0)
  agents/                            # 5 subagentes especializados
    blog-researcher.md              # Pesquisa de estatísticas e fontes
    blog-writer.md                  # Geração de conteúdo
    blog-seo.md                     # Validação de SEO
    blog-reviewer.md                # Pontuação de qualidade (sem Bash, após endurecimento da v1.7.0)
    blog-translator.md              # Tradução multilíngue (sem Bash, v1.7.0)
  tests/                             # Mais de 250 checagens pytest, incluindo as suítes de contrato de entrega e de segurança
```

## Comandos

| Comando | Finalidade |
|---------|------------|
| `/blog write` | Escreve artigos novos otimizados para ranqueamento e citação por IA |
| `/blog rewrite` | Otimiza posts existentes com estatísticas com fonte; `/blog update` é apelido daqui |
| `/blog analyze` | Pontuação de 100 pontos em 5 categorias, com evidência e diagnósticos de estilo, não detecção de autoria |
| `/blog brief` | Briefings de conteúdo detalhados, com análise competitiva |
| `/blog outline` | Roteiros informados por resultados de busca, com hierarquia de títulos |
| `/blog calendar` | Calendários editoriais com clusters de temas |
| `/blog strategy` | Posicionamento do blog e planejamento de conteúdo |
| `/blog seo-check` | Lista de verificação de SEO após a escrita |
| `/blog schema` | Geração de marcação de schema JSON-LD |
| `/blog repurpose` | Reaproveitamento de conteúdo em várias plataformas |
| `/blog geo` | Auditoria de otimização para citação por IA |
| `/blog image` | Geração e edição de imagens por IA via Gemini |
| `/blog audit` | Avaliação de saúde do blog inteiro |
| `/blog cannibalization` | Detecta sobreposição de palavra-chave entre posts |
| `/blog factcheck` | Verifica estatísticas contra as fontes citadas |
| `/blog persona` | Gerencia personas de escrita e perfis de voz |
| `/blog taxonomy` | Gestão de tags e categorias no CMS |
| `/blog notebooklm` | Consulta o NotebookLM para pesquisa ancorada em fonte |
| `/blog audio` | Gera narração em áudio via Gemini TTS |
| `/blog google` | Dados de API do Google: PSI, CrUX, GSC, GA4, NLP, YouTube, palavras-chave |
| `/blog cluster` | Planejamento e execução de cluster semântico de temas (v1.7.0) |
| `/blog multilingual` | Escreve, traduz, localiza e emite hreflang num comando só (v1.7.0) |
| `/blog translate` | Tradução otimizada para SEO com preservação de formato (v1.7.0) |
| `/blog localize` | Adaptação cultural profunda por localidade (v1.7.0) |
| `/blog locale-audit` | QA de conteúdo multilíngue (v1.7.0) |
| `/blog flow` | Prompts do framework FLOW: find, optimize, win, índice de prompts, sync (v1.7.0) |
| `/blog brand` | Gera BRAND.md + VOICE.md, carregados automaticamente por todas as sub-skills (v1.8.0) |
| `/blog discourse` | Pesquisa de discurso dos últimos 30 dias sem API; produz DISCOURSE.md (v1.8.0) |
| `/blog style` | Aprende o perfil de voz do autor a partir de posts existentes (v1.10.0) |
| `/blog decay` | Detecta decaimento de conteúdo a partir de exportações do GSC (v1.10.0) |

Capacidade interna: o `blog-chart` gera gráficos SVG inline para `/blog write`
e `/blog rewrite`; não é um comando de usuário de primeiro nível.

## Regras de desenvolvimento

- Mantenha os arquivos SKILL.md abaixo de 500 linhas / 5000 tokens
- Frontmatter do SKILL.md: apenas campos válidos (name, description, user-invokable, argument-hint, compatibility, license, metadata, disable-model-invocation). NÃO use `allowed-tools`; não é campo da especificação do Claude Code
- Novos arquivos de referência devem ser focados e ter menos de 200 linhas. As referências abrangentes já existentes (platform-guides, schema-stack, content-templates, distribution-playbook) estão dispensadas dessa diretriz
- Os scripts precisam ter docstring, interface de linha de comando e saída JSON
- Use nomenclatura kebab-case em todos os diretórios de skill
- Agentes são invocados pela ferramenta Task, nunca por Bash
- Python 3.11+ obrigatório; dependências no pyproject.toml
- Teste com `python3 -m pytest tests/` após alterações
- Rode `claude plugin validate .` antes de enviar mudanças no plugin
- Rode `python3 scripts/lint_prose.py` localmente para pegar caracteres de prosa proibidos antes da CI (v1.8.4 em diante)
- Carregamento de arquivos da raiz do projeto (BRAND.md/VOICE.md/DISCOURSE.md): use `scripts/load_untrusted_root.py` via Bash; nunca monte uma cerca na mão (v1.8.3 em diante)
- As skills do plugin são descobertas automaticamente no diretório `skills/` (não liste no plugin.json)

## Distribuição

### Marketplace oficial da Anthropic
Envie em: claude.ai/settings/plugins/submit ou platform.claude.com/plugins/submit

### Marketplace auto-hospedado
```
/plugin marketplace add AgriciDaniel/claude-blog
/plugin install claude-blog@agricidaniel-blog
```

### Instalação avulsa (sem marketplace)
```bash
curl -fsSLo install.sh \
  https://raw.githubusercontent.com/AgriciDaniel/claude-blog/v2.1.1/install.sh
# Compare o digest SHA-256 com o valor publicado no README.md.
CLAUDE_BLOG_REF=v2.1.1 bash ./install.sh
```

## Post de release

Depois de cortar uma nova release (tag git + `gh release create`), rode:

```
/release-blog
```

Isso gera um post em https://claude-blog.md/blog/, cuida da geração da imagem de capa, dos metadados de SEO, do schema de FAQ, do link building interno, das atualizações de sitemap e llms.txt, e do deploy na Vercel.
