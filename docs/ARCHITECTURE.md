# Arquitetura

Documentação de desenho do sistema do `claude-blog`, cobrindo tipos de componente,
fluxo de dados, metodologia de pontuação, convenções de arquivo e pontos de extensão.

O Claude Blog Brain é vendorizado em `./brain` como um brain Obsidian autocontido e com evidência exigida. Ele não faz parte do payload do plugin; todo o ferramental de skill segue restrito a `skills/`.

---

## Visão geral do sistema

```
                        +-----------------------------+
                        |      Entrada do usuário     |
                        |   /blog <comando> [args]    |
                        +-------------+---------------+
                                      |
                                      v
                        +-----------------------------+
                        |    Orquestrador principal   |
                        |      skills/blog/SKILL.md          |
                        |                             |
                        |  - Interpretação de comando |
                        |  - Detecção de plataforma   |
                        |  - Roteamento de sub-skill  |
                        |  - Imposição dos portões    |
                        +------+----------+-----------+
                               |          |
              +----------------+          +----------------+
              |                                            |
              v                                            v
+----------------------------+            +---------------------------+
|  32 diretórios de skill    |            |  Referências sob demanda  |
|  1 orquestrador + 31       |            |  skills/blog/references/*.md     |
|  sub-skills                |            |  skills/blog/templates/*.md      |
|  write    rewrite          |            |                           |
|  analyze  brief            |            |  22 referências carregadas|
|  calendar strategy         |            |  sob demanda (padrão RAG) |
|  outline  seo-check        |            |  12 templates de conteúdo |
|  schema   repurpose        |            +---------------------------+
|  geo      audit            |
|  image    cannibalization  |
|  factcheck persona         |
|  taxonomy notebooklm       |
|  audio    google           |
|  cluster  flow             |
|  multilingual translate    |
|  localize locale-audit     |
|  brand    discourse        |
|  style    decay            |
|  chart (interno)           |
+------+----------+----------+
       |          |
       v          v
+------------------+  +------------------------+
|  5 subagentes    |  |  17 scripts na raiz    |
|  agents/*.md     |  |  scripts/*.py          |
|                  |  |                        |
|  blog-researcher |  |  analyze_blog          |
|  blog-writer     |  |  blog_preflight (1.9)  |
|  blog-seo        |  |  blog_render (1.9)     |
|  blog-reviewer   |  |  blog_hygiene (1.11)   |
|  blog-translator |  |  ai_citation_score     |
|                  |  |  content_decay         |
|                  |  |  quality_gate          |
|                  |  |  style_learn           |
|                  |  |                        |
|                  |  |  generate_hero (1.9)   |
|                  |  |  cognitive_load        |
+------------------+  |  discourse_research    |
                      |  load_untrusted_root   |
                      |  lint_prose            |
                      |  sync_flow             |
                      +------------------------+
```

---

## Tipos de componente

### 1. Orquestrador principal

**Arquivo**: `skills/blog/SKILL.md`

O ponto de entrada de todos os comandos `/blog`. Responsabilidades:

- Interpretar a entrada do usuário para identificar o subcomando e os argumentos
- Detectar a plataforma de blog pela estrutura do projeto (MDX, Hugo, Jekyll etc.)
- Rotear para a sub-skill adequada
- Impor os portões de qualidade (regras duras que nunca deixam passar conteúdo que as viole)
- Carregar arquivos de referência sob demanda

O orquestrador é uma skill do Claude Code com frontmatter YAML definindo nome,
descrição, expressões de acionamento e ferramentas permitidas.

### 2. Diretórios de skill (32 no total: 1 orquestrador + 31 sub-skills; 30 comandos voltados ao usuário)

**Local**: `skills/blog-*/SKILL.md` (e `skills/blog/SKILL.md` no caso do orquestrador)

Cada sub-skill é uma skill autônoma do Claude Code, com seus próprios:

- Frontmatter YAML (name, description, user-invokable, argument-hint, metadata.version)
- Fluxo detalhado (instruções passo a passo)
- Especificações de entrada e saída
- Checagens de qualidade

| Sub-skill | Responsabilidade | Introduzida |
|-----------|------------------|-------------|
| blog-write | Geração de artigo novo com otimização completa (v1.9.0: itera pelo contrato de entrega de 5 portões até a nota atingir 90 ou mais com zero P0, no máximo 3 iterações) | v1.0.0 |
| blog-rewrite | Otimização de post existente preservando a voz do autor (v1.9.0: mesmo contrato de entrega) | v1.0.0 |
| blog-analyze | Auditoria de qualidade com pontuação de 100 pontos em 5 categorias | v1.0.0 |
| blog-brief | Geração de briefing de conteúdo com pesquisa | v1.0.0 |
| blog-calendar | Planejamento de calendário editorial | v1.0.0 |
| blog-strategy | Posicionamento do blog e arquitetura de conteúdo | v1.0.0 |
| blog-outline | Geração de roteiro informado por resultados de busca | v1.0.0 |
| blog-seo-check | Validação de SEO após a escrita | v1.0.0 |
| blog-schema | Geração de marcação de schema JSON-LD | v1.0.0 |
| blog-repurpose | Reaproveitamento de conteúdo entre plataformas | v1.0.0 |
| blog-geo | Auditoria de otimização para citação por IA | v1.0.0 |
| blog-audit | Avaliação de saúde do blog inteiro | v1.0.0 |
| blog-chart | Gráficos SVG inline (somente interno, invocado por write e rewrite) | v1.0.0 |
| blog-image | Geração de imagem por IA via Gemini (nanobanana-mcp) | v1.4.0 |
| blog-cannibalization | Detecção de sobreposição de palavra-chave entre posts | v1.4.x |
| blog-factcheck | Verificação de estatísticas contra as fontes citadas | v1.4.x |
| blog-persona | Gestão de persona de escrita e perfil de voz | v1.4.x |
| blog-taxonomy | Gestão de tags e categorias no CMS (WordPress, Shopify, Ghost, Strapi, Sanity) | v1.4.x |
| blog-notebooklm | Pesquisa ancorada em fonte via NotebookLM | v1.5.0 |
| blog-audio | Narração em áudio via Gemini TTS (30 vozes, mais de 80 idiomas) | v1.6.0 |
| blog-google | Integração com APIs do Google (PSI, CrUX, GSC, GA4, NLP, YouTube, Ads) | v1.6.5 |
| blog-cluster | Planejamento e execução de cluster semântico de temas (eixo e raios) | v1.7.0 |
| blog-flow | Prompts do framework FLOW (find / optimize / win / prompts / sync) | v1.7.0 |
| blog-multilingual | Escrita, tradução, localização e hreflang multilíngues num comando só | v1.7.0 |
| blog-translate | Tradução otimizada para SEO com preservação de formato | v1.7.0 |
| blog-localize | Adaptação cultural profunda por localidade | v1.7.0 |
| blog-locale-audit | QA de conteúdo multilíngue (completude, hreflang, paridade, atualidade) | v1.7.0 |
| blog-brand | Gera o contexto BRAND.md + VOICE.md carregado automaticamente por todas as sub-skills | v1.8.0 |
| blog-discourse | Pesquisa de discurso dos últimos 30 dias sem API (Reddit, X, YouTube etc.) | v1.8.0 |
| blog-style | Aprende perfis de voz do autor a partir de posts existentes | v1.10.0 |
| blog-decay | Detecta decaimento de conteúdo no GSC e prioriza candidatos a atualização | v1.10.0 |

### 3. Subagentes (5)

**Local**: `agents/blog-*.md`

Agentes especializados disparados pelas sub-skills por meio da ferramenta `Task`
do Claude Code. Cada agente tem um papel focado e um conjunto restrito de
ferramentas. Nenhum deles tem acesso a Bash; o endurecimento da v1.7.0 removeu o
Bash do frontmatter dos agentes para limitar o raio de alcance (veja
`agents/blog-reviewer.md` e `agents/blog-translator.md`).

| Agente | Ferramentas | Papel |
|--------|-------------|-------|
| blog-researcher | WebSearch, WebFetch, Read, Grep, Glob | Encontra estatísticas, imagens e dados da concorrência |
| blog-writer | Read, Write, Edit, Grep, Glob | Escreve e reescreve conteúdo otimizado |
| blog-seo | Read, Grep, Glob | Análise e validação técnica de SEO |
| blog-reviewer | Read, Grep, Glob | Revisão e pontuação de qualidade; **BLOQUEANTE na v1.9.0** (emite a linha `BLOCKING: true\|false (motivo)`, lida pelo Gate 4 do `scripts/blog_preflight.py`) |
| blog-translator | Read, Write, Edit, Grep, Glob | Tradução multilíngue (v1.7.0; sem Bash, por segurança de raio de alcance) |

Os agentes são definidos como arquivos markdown com frontmatter YAML
especificando nome, descrição e ferramentas disponíveis.

### 4. Arquivos de referência (22)

**Local**: `skills/blog/references/*.md`

Documentos de conhecimento carregados sob demanda (estilo RAG, não pré-carregados
no contexto). São 22 reference docs em `skills/blog/references/` cobrindo cenário
de SEO, GEO/AEO, regras de conteúdo, mídia visual, schema, E-E-A-T, guias de
plataforma, distribuição, links internos, prompts do FLOW, incorporação de vídeo,
detecção de conteúdo genérico de IA, heurísticas editoriais, carga cognitiva,
qualidade de pesquisa, contrato de síntese e a especificação do contrato de
entrega da v1.9.0.

Para listar o conjunto atual:

```bash
ls skills/blog/references/*.md
```

A lista exata não é enumerada aqui de propósito, para este documento não ficar
defasado frente à realidade do sistema de arquivos. O teste
`test_reference_count_coherence` verifica que a contagem declarada em
`skills/blog/SKILL.md` bate com a quantidade real de arquivos, de modo que toda
contagem documentada se sincroniza sozinha.

### 5. Templates de conteúdo (12)

**Local**: `skills/blog/templates/*.md`

Templates estruturais para diferentes tipos de conteúdo. Cada um define a
estrutura de seções, as metas de extensão e a orientação específica de formato.
Veja [TEMPLATES.md](TEMPLATES.md) para a referência completa.

### 6. Scripts Python na raiz (14)

**Local**: `scripts/*.py`

CLIs autônomas que o orquestrador chama via Bash. Cada uma tem argparse,
docstring, saída JSON e dependências apenas da biblioteca padrão ou fixadas de
forma restrita.

| Script | Finalidade | Introduzido |
|---|---|---|
| `analyze_blog.py` | Pontuação de qualidade de 100 pontos em 5 categorias; modo em lote; saída JSON, markdown ou tabela | v1.0.0 |
| `ai_citation_score.py` | Heurística não calibrada de prontidão para citação por IA, 0 a 100 por post | v1.10.0 |
| `blog_hygiene.py` | Higiene determinística opcional: carregamento tardio de imagens e sumário automático | v1.11.0 |
| `blog_preflight.py` | Roda o contrato de entrega de 5 portões (portões 1, 2, 3 e 5; lê a saída do 4) | v1.9.0 |
| `blog_render.py` | Renderizador md -> html -> pdf; JSON-LD à prova de XSS via `</`->`<\/`; recusa de symlink com O_NOFOLLOW; validação de frontmatter | v1.9.0 |
| `cognitive_load.py` | Analisador de densidade de conceitos por seção (entidades, números, jargão, referências adiante, profundidade de oração) | v1.8.0 |
| `content_decay.py` | Detector de decaimento de conteúdo via GSC: queda de 20%+ no trimestre | v1.10.0 |
| `discourse_research.py` | Síntese de briefing de discurso a partir de JSON de busca; parsing com profundidade limitada; proteção contra travessia de caminho | v1.8.0 |
| `generate_hero.py` | Escada de imagem principal: Banana MCP -> API do Gemini -> Unsplash/Pexels/Pixabay -> Openverse | v1.9.0 |
| `load_untrusted_root.py` | Cerca imposta por código para BRAND/VOICE/DISCOURSE com nonces CSPRNG; O_NOFOLLOW e limite de tamanho | v1.8.3 |
| `lint_prose.py` | Linter de higiene de prosa ciente de cercas (sem travessão, meia-risca ou ` -- `); imposto pela CI | v1.8.4 |
| `quality_gate.py` | Portão de pre-commit: barra posts com nota abaixo de 70 | v1.10.0 |
| `style_learn.py` | Aprendiz de perfil de voz do autor a partir de posts de amostra | v1.10.0 |
| `sync_flow.py` | Puxa os prompts de referência do FLOW da origem; em caixa de areia; só biblioteca padrão | v1.7.0 |

---

## Fluxo de dados

### Fluxo de escrita

```
/blog write "tema"
      |
      v
  Orquestrador (skills/blog/SKILL.md)
      |
      +-- Carrega: references/content-rules.md
      |            references/visual-media.md
      |            templates/[selecionado automaticamente].md
      |
      +-- Dispara: agente blog-researcher
      |   |
      |   +-- WebSearch: encontra 8 a 12 estatísticas
      |   +-- WebSearch: encontra 3 a 5 imagens do Pixabay/Unsplash
      |   +-- WebFetch: verifica fontes e URLs
      |   +-- Devolve: dados estruturados de pesquisa
      |
      +-- Apresenta o roteiro para aprovação do usuário
      |
      +-- Invoca: blog-chart (2 a 4 gráficos, embutido)
      |
      +-- Dispara: agente blog-writer
      |   |
      |   +-- Escreve o artigo completo com:
      |   |   - Formatação de resposta antecipada
      |   |   - Estatísticas com fonte
      |   |   - Imagens embutidas
      |   |   - Gráficos embutidos
      |   |   - Seção de perguntas frequentes
      |   +-- Devolve: artigo completo
      |
      +-- Verificação de qualidade (5 categorias, 100 pontos)
      |
      +-- v1.9.0: contrato de entrega de 5 portões (blog_preflight.py)
      |     Portão 1 Descoberta de capacidades -> capabilities.json
      |     Portão 2 Completude de formato     -> .md + .html + .pdf + hero.<ext>
      |     Portão 3 Verificação visual        -> patchright/playwright, 3 larguras
      |     Portão 4 Revisão de conteúdo       -> agente blog-reviewer (BLOQUEANTE)
      |     Portão 5 Ativos e links            -> imagens, links, schema, contagem
      |     Se algum portão BLOQUEAR: itera até 3 vezes e então escala ao usuário
      |
      +-- Grava o arquivo no projeto do usuário
      |
      v
  Resumo de entrega (8 artefatos: md, html, pdf, hero, 4 capturas por largura, review.md, preflight-report.json)
```

### Fluxo de análise

```
/blog analyze "arquivo.md"
      |
      v
  Orquestrador --> sub-skill blog-analyze
      |
      +-- Lê o arquivo alvo
      |
      +-- Carrega: references/quality-scoring.md
      |
      +-- Roda: analyze_blog.py (se houver Python disponível)
      |   |
      |   +-- Devolve: métricas em JSON
      |
      +-- Pontuação manual (5 categorias, 100 pontos)
      |
      +-- Gera recomendações priorizadas
      |
      v
  Relatório de qualidade com nota e itens de ação
```

---

## Carregamento de referências sob demanda (padrão RAG)

Os arquivos de referência NÃO são pré-carregados no contexto. O orquestrador e as
sub-skills os carregam seletivamente conforme a tarefa em curso:

```
Tarefa                  Referências carregadas
------                  ----------------------
/blog write             content-rules, visual-media, quality-scoring
/blog rewrite           content-rules, quality-scoring
/blog analyze           quality-scoring
/blog brief             content-rules, geo-optimization
/blog strategy          geo-optimization, google-landscape-2026
/blog geo               geo-optimization, ai-crawler-guide
/blog schema            schema-stack
/blog seo-check         google-landscape-2026, schema-stack
```

Esse padrão mantém o uso de contexto eficiente. Só é carregado o conhecimento
relevante à operação atual.

---

## Metodologia de pontuação

A qualidade do blog é medida em 5 categorias que somam 100 pontos. Tanto o script
`analyze_blog.py` quanto a sub-skill `blog-analyze` usam este arcabouço.

### Pesos por categoria

```
Qualidade de conteúdo (30) ############################--
Sinais de SEO (25)         #########################-----
E-E-A-T (15)               ###############---------------
Técnico (15)               ###############---------------
Citação por IA (15)        ###############---------------
                           |    |    |    |    |    |
                           0   20   40   60   80  100
```

### Faixas de pontuação

| Nota | Classificação | Ação |
|------|---------------|------|
| 90-100 | Excepcional | Publicar como está (o contrato da v1.9.0 entrega VERDE) |
| 80-89 | Forte | Ajustes menores; o orquestrador itera se o Gate 4 exigir 90 ou mais |
| 70-79 | Aceitável | Lacunas relevantes; iterar |
| 60-69 | Abaixo do padrão | Melhorias significativas necessárias |
| Menos de 60 | Refazer | Reescrita completa recomendada |

O contrato de entrega usa a nota mínima configurada de 70. Observações
consultivas de estilo e de extensão não bloqueiam a entrega nem inferem autoria.
Falhas de integridade e de segurança seguem bloqueantes.

### Portões de qualidade (regras duras)

Estes são inegociáveis. Conteúdo que viole qualquer um deles não pode ser publicado:

| Portão | Limite |
|--------|--------|
| Estatística inventada | Tolerância zero |
| Clareza de parágrafo | Avaliar em contexto; sem portão fixo de extensão |
| Hierarquia de títulos | Nunca pular níveis (H1 > H2 > H3) |
| Nível da fonte | Somente níveis 1 a 3 |
| Texto alternativo de imagem | Obrigatório em todas as imagens |
| Autopromoção | No máximo 1 menção à marca |
| Diversidade de gráficos | Sem tipos de gráfico repetidos no mesmo post |

---

## Detecção de plataforma

O orquestrador detecta automaticamente a plataforma de blog a partir de sinais do projeto:

| Sinal | Plataforma | Formato de saída |
|-------|------------|------------------|
| Arquivos `.mdx` + `next.config` | Next.js/MDX | Markdown compatível com JSX |
| Arquivos `.md` + `hugo.toml` | Hugo | Markdown padrão |
| Arquivos `.md` + `_config.yml` | Jekyll | Markdown com frontmatter YAML |
| Arquivos `.html` | HTML estático | HTML com marcação semântica |
| Diretório `wp-content/` | WordPress | HTML ou blocos Gutenberg |
| `ghost/` ou API do Ghost | Ghost | Mobiledoc ou HTML |
| Arquivos `.astro` | Astro | MDX ou markdown |
| Nenhum sinal detectado | Padrão | Markdown padrão |

A detecção de plataforma afeta:

- Formato e nomes de campo do frontmatter
- Sintaxe de incorporação de imagem (markdown versus componente `<Image>`)
- Formato de incorporação de gráfico (SVG em HTML versus SVG em JSX com camelCase)
- Método de injeção de schema

---

## Convenções de nomenclatura de arquivos

| Componente | Local | Nomenclatura |
|------------|-------|--------------|
| Skill principal | `skills/blog/SKILL.md` | Nome fixo |
| Sub-skills | `skills/blog-<comando>/SKILL.md` | Prefixo `blog-` mais o nome do comando |
| Agentes | `agents/blog-<papel>.md` | Prefixo `blog-` mais o nome do papel |
| Referências | `skills/blog/references/<tema>.md` | Nome do tema em kebab-case |
| Templates | `skills/blog/templates/<tipo>.md` | Tipo de conteúdo em kebab-case |
| Scripts | `scripts/<nome>.py` | Nome do script em snake-case |

---

## Pontos de extensão

### Acrescentar um comando novo

1. Crie `skills/blog-<nome>/SKILL.md` com frontmatter YAML
2. Acrescente a lógica de roteamento ao orquestrador `skills/blog/SKILL.md`
3. Atualize `install.sh` e `install.ps1` para copiar a nova sub-skill
4. Atualize `uninstall.sh` para removê-la

### Acrescentar um agente novo

1. Crie `agents/blog-<papel>.md` com frontmatter YAML
2. Defina o conjunto de ferramentas (mantenha mínimo para o papel)
3. Referencie o agente a partir das sub-skills que precisam dele

### Acrescentar uma referência nova

1. Crie `skills/blog/references/<tema>.md`
2. Documente quando carregá-la no orquestrador
3. Atualize `install.sh` para copiar o novo arquivo de referência

### Acrescentar um template novo

1. Crie `skills/blog/templates/<tipo>.md`
2. Defina estrutura de seções, marcadores e metas de extensão
3. Acrescente a lógica de seleção de template ao `blog-write`

---

## Árvore de diretórios instalada

Depois da instalação, o `claude-blog` ocupa esta estrutura dentro de `~/.claude/`:

```
~/.claude/
├── skills/
│   ├── blog/
│   │   ├── SKILL.md                    # Orquestrador principal
│   │   ├── references/
│   │   │   ├── ai-crawler-guide.md
│   │   │   ├── content-rules.md
│   │   │   ├── content-templates.md
│   │   │   ├── distribution-playbook.md
│   │   │   ├── eeat-signals.md
│   │   │   ├── geo-optimization.md
│   │   │   ├── google-landscape-2026.md
│   │   │   ├── internal-linking.md
│   │   │   ├── platform-guides.md
│   │   │   ├── quality-scoring.md
│   │   │   ├── schema-stack.md
│   │   │   └── visual-media.md
│   │   ├── templates/
│   │   │   ├── how-to-guide.md
│   │   │   ├── listicle.md
│   │   │   ├── case-study.md
│   │   │   ├── comparison.md
│   │   │   ├── pillar-page.md
│   │   │   ├── product-review.md
│   │   │   ├── thought-leadership.md
│   │   │   ├── roundup.md
│   │   │   ├── tutorial.md
│   │   │   ├── news-analysis.md
│   │   │   ├── data-research.md
│   │   │   └── faq-knowledge.md
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
│   ├── blog-chart/SKILL.md             # somente interno (geração de SVG)
│   ├── blog-image/SKILL.md             # v1.4.0
│   ├── blog-cannibalization/SKILL.md
│   ├── blog-factcheck/SKILL.md
│   ├── blog-persona/SKILL.md
│   ├── blog-taxonomy/SKILL.md
│   ├── blog-notebooklm/SKILL.md        # v1.5.0
│   ├── blog-audio/SKILL.md             # v1.6.0
│   ├── blog-google/SKILL.md            # v1.6.5
│   ├── blog-cluster/SKILL.md           # v1.7.0
│   ├── blog-flow/SKILL.md              # v1.7.0
│   ├── blog-multilingual/SKILL.md      # v1.7.0
│   ├── blog-translate/SKILL.md         # v1.7.0
│   ├── blog-localize/SKILL.md          # v1.7.0
│   ├── blog-locale-audit/SKILL.md      # v1.7.0
│   ├── blog-brand/SKILL.md             # v1.8.0
│   ├── blog-discourse/SKILL.md         # v1.8.0
│   ├── blog-style/SKILL.md             # v1.10.0
│   └── blog-decay/SKILL.md             # v1.10.0
└── agents/
    ├── blog-researcher.md
    ├── blog-writer.md
    ├── blog-seo.md
    ├── blog-reviewer.md
    └── blog-translator.md              # v1.7.0
```

**Contagem de componentes (v2.1.1)**: 32 diretórios de skill (1 orquestrador +
31 sub-skills); 30 comandos voltados ao usuário, 5 agentes (blog-researcher,
blog-writer, blog-seo, blog-reviewer, blog-translator),
22 references in `skills/blog/references/` (mais as referências por sub-skill e
os 30 prompts do FLOW sincronizados em `skills/blog-flow/references/`),
12 templates de conteúdo,
17 scripts na raiz (`scripts/analyze_blog.py`, `ai_citation_score.py`,
`blog_hygiene.py`, `blog_preflight.py`, `blog_render.py`, `cognitive_load.py`,
`content_decay.py`, `discourse_research.py`, `generate_hero.py`,
`load_untrusted_root.py`, `lint_prose.py`, `quality_gate.py`, `style_learn.py`,
`sync_flow.py`, `consistency_check.py`, `dependency_smoke.py`,
`validate_public_release.py`) mais os scripts por sub-skill em `blog-google/`,
`blog-notebooklm/`, `blog-audio/`, `blog-image/`.
A v1.8.0 em diante acrescenta três arquivos de contexto na raiz do projeto
(BRAND.md / VOICE.md / DISCOURSE.md, carregados automaticamente por
`scripts/load_untrusted_root.py` com cerca de nonce CSPRNG). A v1.8.4 em diante
impõe higiene de prosa e coerência de versão pela CI (veja `scripts/lint_prose.py`
e `tests/test_version_coherence.py`). A v1.9.0 acrescenta o contrato de entrega de
5 portões (veja `skills/blog/references/blog-delivery-contract.md`) e uma suíte
pytest com mais de 250 testes, incluindo cobertura de regressão para XSS, symlink
e frontmatter verificada por teste de mutação.
