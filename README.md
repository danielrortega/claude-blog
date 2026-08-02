# Skill de Escrita de Blog com IA e Otimização de SEO para o Claude Code (`claude-blog`)

<p align="center">
  <img src="assets/cover-blog.svg" alt="Capa do Claude Blog: escrita de blog com IA, otimização de SEO, prontidão para citação por IA e um contrato de entrega de 5 portões para o Claude Code" width="100%">
</p>

<p align="center">
  <a href="https://agentskills.io"><img src="https://img.shields.io/badge/Agent%20Skills-Compatible-blue" alt="Agent Skill"></a>
  <a href="https://github.com/AgriciDaniel/claude-blog/releases"><img src="https://img.shields.io/github/v/release/AgriciDaniel/claude-blog?label=public%20release" alt="Versão"></a>
  <a href="https://github.com/AgriciDaniel/claude-blog/actions"><img src="https://img.shields.io/github/actions/workflow/status/AgriciDaniel/claude-blog/ci.yml?branch=main&label=public%20CI" alt="CI"></a>
  <a href="https://github.com/AgriciDaniel/claude-blog/stargazers"><img src="https://img.shields.io/github/stars/AgriciDaniel/claude-blog?style=social" alt="Estrelas no GitHub"></a>
  <a href="https://github.com/AgriciDaniel/claude-blog/discussions"><img src="https://img.shields.io/badge/Community-GitHub%20Discussions-blue" alt="GitHub Discussions"></a>
  <img src="https://img.shields.io/badge/License-MIT-green" alt="Licença: MIT">
  <img src="https://img.shields.io/badge/Python-3.11%2B-blue" alt="Python 3.11+">
  <img src="https://img.shields.io/badge/Skill%20Dirs-32-orange" alt="Diretórios de skill: 32">
  <img src="https://img.shields.io/badge/Sub--Skills-31-orange" alt="Sub-skills: 31">
  <img src="https://img.shields.io/badge/Commands-30-blueviolet" alt="Comandos voltados ao usuário: 30">
  <img src="https://img.shields.io/badge/Tests-250%2B%20passing-brightgreen" alt="Testes: mais de 250 passando">
</p>

**O claude-blog é um conjunto de skills do Claude Code que escreve, otimiza, audita, localiza e atualiza conteúdo de blog em escala.** Cada artigo é avaliado quanto à utilidade alinhada ao Google e a heurísticas internas de prontidão para citação por IA. A versão 2.1.1 foi preparada em 2026-07-23.

A promessa central é simples: você nunca é o primeiro revisor. Um Blog Delivery Contract de 5 portões pontua cada rascunho contra uma rubrica de 100 pontos, bloqueia a entrega abaixo de 90, verifica artefatos e links, e itera até 3 vezes antes de escalar.

Esta é a distribuição pública, sob licença MIT, em
[`AgriciDaniel/claude-blog`](https://github.com/AgriciDaniel/claude-blog).
O fluxo de publicação está documentado em
[`docs/PUBLISHING.md`](docs/PUBLISHING.md).

**Blog:** [Veja como o claude-blog funciona](https://agricidaniel.com/blog/claude-code-blog-writer)

<p align="center">
  <strong><a href="https://youtu.be/7Q4GaSgUFHo">Assistir ao vídeo no YouTube</a></strong>
</p>

## Demonstração

<p align="center">
  <img src="assets/blog-command-demo.gif" alt="Demonstração de comandos do claude-blog: roteamento dos subcomandos /blog pelo orquestrador" width="100%">
</p>

<p align="center">
  <img src="assets/blog-write-demo.gif" alt="Demonstração do /blog write: geração de artigo de ponta a ponta com o contrato de entrega de 5 portões" width="100%">
</p>

[Assista à demonstração original no YouTube](https://www.youtube.com/watch?v=AeLC4iutG8w).

## O que é

O claude-blog é um motor de blog de ciclo completo para estratégia, briefings, roteiros, escrita, reescrita, análise, schema, prontidão para citação por IA, auditoria de site, clusters de temas, publicação multilíngue, narração em áudio e detecção de decaimento de conteúdo.

Formato atual da v2.1.1: **32 diretórios de skill = 1 orquestrador + 31 sub-skills; 30 comandos /blog voltados ao usuário (o `blog-chart` é interno, não é comando).** Inclui também 5 agentes especializados, validadores de consistência do repositório e de release pública, 22 referências centrais, 12 templates, uma suíte com mais de 250 testes e o Claude Blog Brain empacotado em `./brain`.

Todo rascunho é entregue como pasta de artefatos, com o fonte markdown, o HTML renderizado, o PDF, um `hero.<ext>` real, 3 capturas em diferentes larguras, `review.md` e `preflight-report.json`. O renderizador usa tratamento de JSON-LD à prova de XSS, CSS ciente de modo escuro e a mesma origem para todo formato de saída.

## Para quem é

**Blogueiros e criadores solo** conseguem publicar posts de alta qualidade sem gastar horas com SEO, schema, checagem de fontes e links internos.

**Times de marketing e agências** conseguem rodar fluxos consistentes de múltiplos posts entre marcas, idiomas, autores e plataformas com `/blog cluster`, `/blog multilingual`, `/blog persona`, `/blog brand` e `/blog discourse`.

**Quem constrói skills para o Claude Code** encontra aqui uma arquitetura de referência Tier 4 do Agent Skills, com roteamento por orquestrador, despacho de sub-skills, repasse a agentes, portões de entrega impostos por código, endurecimento do instalador e checagens de coerência na CI.

## Onde um plugin de skill do Claude Code deve se instalar?

A maioria dos plugins de skill do Claude Code instaláveis pelo usuário deve ir para `~/.claude/skills/<nome>/` no caso do conteúdo da skill, `~/.claude/agents/<nome>.md` no caso de agentes, e `~/.claude/scripts/<auxiliar>.py` no caso de auxiliares Python.

Esta resposta foi mantida de propósito no README porque demonstra o padrão de escrita para GEO e SEO que o claude-blog produz: resumo com resposta antecipada, caminhos explícitos, estrutura pronta para citação e uma seção compacta em formato de pergunta que sistemas de IA conseguem citar sem contexto extra.

Um espécime condensado de artigo gerado:

```markdown
---
title: "Where Should a Claude Code Skill Plugin Install Itself?"
description: "A working answer to the install-path question..."
date: "2026-05-18"
author: "Daniel Agrici"
tags: [claude-code, skills, plugins, installation]
canonical: "https://example.com/blog/skill-plugin-install-path"
---

## Where Should a Claude Code Skill Plugin Install Itself?

The short answer: most user-installable Claude Code skill plugins
should ship to `~/.claude/skills/<name>/` for skill content,
`~/.claude/agents/<name>.md` for agents, and
`~/.claude/scripts/<helper>.py` for any Python helpers.

### Key Takeaways
- `~/.claude/skills/` is the SKILL.md surface area.
- `~/.claude/agents/` holds agent markdown files.
- The full article includes sourced citations, FAQ, and schema JSON-LD.
```

## Arquitetura

<p align="center">
  <img src="assets/diagrams/01-architecture-B.svg" alt="Arquitetura do claude-blog: comando do usuário passando por roteamento no orquestrador, execução de sub-skill, despacho de agentes, scripts e contrato de entrega de 5 portões" width="100%">
</p>

O orquestrador em `skills/blog/SKILL.md` interpreta a entrada `/blog`, detecta a plataforma alvo, carrega apenas as referências necessárias, roteia para uma sub-skill e coordena agentes e scripts por meio do contrato de entrega.

| Camada | Quantidade | Onde |
|---|---:|---|
| Diretórios de skill | 32 | `skills/blog` mais `skills/blog-*` |
| Orquestrador | 1 | `skills/blog/SKILL.md` |
| Sub-skills | 31 | `skills/blog-*/SKILL.md` |
| Comandos `/blog` voltados ao usuário | 30 | tabela de roteamento em `skills/blog/SKILL.md` |
| Sub-skill somente interna | 1 | `skills/blog-chart/SKILL.md` |
| Agentes especializados | 5 | `agents/blog-*.md` |
| Scripts na raiz | 14 | `scripts/*.py` |
| Referências | 22 | `skills/blog/references/*.md` |
| Templates | 12 | `skills/blog/templates/*.md` |
| Testes | 252 | `tests/` |

Mais detalhes de arquitetura em [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

## Contrato de entrega de 5 portões

<p align="center">
  <img src="assets/diagrams/02-pipeline-B.svg" alt="Pipeline do contrato de entrega de 5 portões: descoberta de capacidades, completude de formato, verificação visual, revisão de conteúdo, integridade de ativos e links, e então entrega ao usuário" width="100%">
</p>

Todo resultado de `/blog write` e `/blog rewrite` precisa passar pelo contrato de entrega antes de ser mostrado ao usuário.

| Portão | O que exige | Implementação |
|---|---|---|
| 1. Descoberta de capacidades | Ferramentas, agentes, variáveis de ambiente e dependências opcionais são conhecidos antes da escrita | `scripts/blog_preflight.py --gate 1` |
| 2. Completude de formato | Existem `.md`, `.html`, `.pdf` e uma imagem principal real | `scripts/blog_render.py`, `scripts/generate_hero.py` |
| 3. Verificação visual | As capturas renderizam a 375, 768 e 1280 de largura, o JSON-LD é válido, o modo escuro se sustenta e os SVGs não transbordam | `patchright` ou `playwright` |
| 4. Revisão de conteúdo | A nota do `blog-reviewer` é 90 ou mais, com zero problemas P0 | `agents/blog-reviewer.md` |
| 5. Integridade de ativos e links | As imagens resolvem, existe `og:image`, os links devolvem 200, a contagem de palavras bate com o schema dentro de 5% | `scripts/blog_preflight.py --gate 5` |

Escada da imagem principal: Banana MCP, API direta do Gemini, APIs premium de banco de imagens, depois Openverse. A primeira fonte que funcionar vence. Especificação completa: [`skills/blog/references/blog-delivery-contract.md`](skills/blog/references/blog-delivery-contract.md).

## Ecossistema de sub-skills

<p align="center">
  <img src="assets/diagrams/03-sub-skill-map-A.svg" alt="Ecossistema de sub-skills do claude-blog: um orquestrador, 31 sub-skills, 30 comandos voltados ao usuário e o apoio interno do blog-chart, agrupados por fluxos de escrita, qualidade, busca, mídia, multilíngue e distribuição" width="100%">
</p>

O ecossistema é modular de propósito. A maioria dos comandos são sub-skills voltadas ao usuário. O `blog-chart` é somente interno, e o `blog-image` pode ser chamado tanto pelo usuário quanto internamente pelos fluxos de escrita e reescrita.

## Comandos

Primeira execução: `/blog strategy <nicho>` para delimitar o site, `/blog write <tema>` para gerar um artigo com portões, e `/blog analyze <arquivo-ou-url>` para pontuar um post existente.

| Comando | O que faz |
|---|---|
| `/blog write <tema>` | Escreve um post novo do zero |
| `/blog rewrite <arquivo>` | Reescreve e otimiza um post existente |
| `/blog analyze <arquivo-ou-url>` | Audita a qualidade do post com nota de 0 a 100 |
| `/blog brief <tema>` | Gera um briefing de conteúdo detalhado |
| `/blog calendar [monthly\|quarterly]` | Gera um calendário editorial |
| `/blog strategy <nicho>` | Estratégia de blog e geração de temas |
| `/blog outline <tema>` | Gera roteiro de conteúdo informado por resultados de busca |
| `/blog seo-check <arquivo>` | Lista de verificação de SEO após a escrita |
| `/blog schema <arquivo>` | Gera marcação de schema JSON-LD |
| `/blog repurpose <arquivo>` | Reaproveita o conteúdo para outras plataformas |
| `/blog geo <arquivo>` | Auditoria de prontidão para citação por IA |
| `/blog audit [diretório]` | Avaliação de saúde do blog inteiro |
| `/blog cannibalization [dir]` | Detecta canibalização de palavra-chave entre posts |
| `/blog factcheck <arquivo>` | Verifica estatísticas contra as fontes citadas |
| `/blog image [generate\|edit\|setup]` | Geração e edição de imagem por IA via Gemini |
| `/blog persona [create\|list\|use\|show]` | Gerencia personas de escrita e perfis de voz |
| `/blog brand [init\|show\|update]` | Gera os arquivos de contexto BRAND.md + VOICE.md, carregados automaticamente por todas as sub-skills |
| `/blog discourse <tema>` | Pesquisa o que as pessoas estão de fato dizendo sobre um tema nos últimos 30 dias; produz DISCOURSE.md (v1.8.0, sem API) |
| `/blog taxonomy [suggest\|sync\|audit]` | Gestão de tags e categorias entre plataformas de CMS |
| `/blog notebooklm <pergunta>` | Consulta o NotebookLM para pesquisa ancorada em fonte |
| `/blog audio [generate\|voices\|setup]` | Gera narração em áudio dos posts |
| `/blog google [comando] [args]` | Dados de API do Google: PSI, CrUX, GSC, GA4, NLP, YouTube, palavras-chave |
| `/blog update <arquivo>` | Atualiza um post existente com dados novos (roteia para rewrite) |
| `/blog cluster [plan\|execute] <semente-ou-plano>` | Planejamento e execução de cluster semântico de temas (eixo e raios) |
| `/blog multilingual <tema> --languages <códigos>` | Escreve, traduz, localiza e emite hreflang num comando só |
| `/blog translate <arquivo> --to <códigos>` | Tradução otimizada para SEO com preservação de formato |
| `/blog localize <arquivo> --locale <código>` | Adaptação cultural profunda (DACH, FR, ES, JA, personalizada) |
| `/blog locale-audit <diretório>` | QA de conteúdo multilíngue (completude, hreflang, paridade, atualidade) |
| `/blog flow [find\|optimize\|win\|prompts\|sync]` | Prompts do framework FLOW (guiados por evidência, 30 aplicáveis a blog) |
| `/blog style learn <caminhos>` | Aprende o perfil de voz do autor a partir de 5 a 10 posts (alimenta blog-write e blog-persona) |
| `/blog decay <gsc-atual> <gsc-anterior>` | Detecta decaimento de conteúdo: sinaliza queda de 20%+ de tráfego no trimestre a partir de exportações do GSC |

O `/blog update` é um apelido de atualização roteado para o `blog-rewrite`; a contagem do projeto continua em 30 comandos `/blog` voltados ao usuário. O `blog-chart` segue somente interno.

Referência completa: [`docs/COMMANDS.md`](docs/COMMANDS.md).

## Framework FLOW

<p align="center">
  <img src="assets/diagrams/04-framework-B.svg" alt="Roda radial do framework FLOW: Find, Leverage, Optimize, Win, com as superfícies de comando do claude-blog para Find, Optimize e Win, e apoio por prompts para Leverage" width="100%">
</p>

O claude-blog integra o framework FLOW de [`AgriciDaniel/flow`](https://github.com/AgriciDaniel/flow) (CC BY 4.0). FLOW significa **Find, Leverage, Optimize, Win**. A skill expõe Find, Optimize e Win como comandos `/blog flow`; Leverage está disponível como família de prompts por `/blog flow prompts` e é aplicado dentro dos fluxos de redação, reaproveitamento e distribuição.

## Recursos

### Destaques das v1.10 e v1.11

- **Contrato de entrega de 5 portões**: portões impostos por código antes da apresentação, cobrindo formato, visuais, revisão, ativos e links.
- **Heurística de prontidão para citação por IA**: `scripts/ai_citation_score.py` produz visões editoriais não calibradas de 0 a 100 para AI Overview, Perplexity e ChatGPT, e alimenta o `/blog geo`.
- **Aprendizado de estilo de escrita**: `/blog style learn <caminhos>` constrói um perfil de voz do autor a partir de 5 a 10 posts.
- **Detecção de decaimento de conteúdo**: `/blog decay <gsc-atual> <gsc-anterior>` sinaliza quedas de 20%+ de tráfego no trimestre e sugere ações de atualizar, consolidar ou podar.
- **Portão de qualidade em pre-commit**: `scripts/quality_gate.py` e `.pre-commit-config.yaml` barram posts com nota abaixo de 70 antes do commit.
- **Contexto de marca e de discurso**: `/blog brand` escreve `BRAND.md` e `VOICE.md`; `/blog discourse` escreve `DISCOURSE.md`. O orquestrador os carrega por tratamento de dado não confiável, com cerca e vínculo por nonce.
- **Multilíngue e clusters de temas**: `/blog multilingual`, `/blog translate`, `/blog localize`, `/blog locale-audit` e `/blog cluster` sustentam publicação internacional em eixo e raios.
- **Higiene determinística de blog**: `scripts/blog_hygiene.py` pode acrescentar carregamento tardio de imagens e um sumário, sem substituir a revisão humana.

### 12 templates de conteúdo

Selecionados automaticamente por tema e intenção: guia prático, lista, estudo de caso, comparação, página pilar, análise de produto, artigo de opinião, compilação de especialistas, tutorial, análise de notícia, pesquisa de dados e base de conhecimento em perguntas frequentes.

### Pontuação de qualidade em 5 categorias

| Categoria | Pontos | Foco |
|---|---:|---|
| Qualidade de conteúdo | 30 | Profundidade, legibilidade, originalidade, engajamento |
| Otimização de SEO | 25 | Títulos de seção, título, palavras-chave, links, meta |
| Sinais de E-E-A-T | 15 | Autor, citações, confiança, base de evidência |
| Elementos técnicos | 15 | Schema, imagens, velocidade, mobile, tags OG |
| Prontidão para citação por IA | 15 | Citabilidade apoiada em evidência, aderência ao propósito, clareza de entidade |

Faixas de pontuação: Excepcional (90-100), Forte (80-89), Aceitável (70-79), Abaixo do padrão (60-69), Refazer (menos de 60). O contrato de entrega bloqueia a entrega abaixo de 90.

### Mais capacidades

- Diagnósticos editoriais consultivos de variação de tamanho de frase, listas de expressões configuradas e amostragem de vocabulário; eles nunca inferem autoria nem afetam a nota.
- Escrita guiada por persona, com dimensões de tom do NNGroup, faixas de legibilidade e aplicação de estilo.
- Verificação de fontes no `/blog factcheck`, com pontuação de confiança em correspondência exata, paráfrase e não encontrado.
- Detecção de sobreposição de palavra-chave no `/blog cannibalization`, com recomendação de fundir ou diferenciar.
- Gestão de taxonomia de CMS para WordPress, Shopify, Ghost, Strapi e Sanity.
- Dupla otimização para Google e citação por IA, incluindo explicações apoiadas em evidência, estrutura alinhada à intenção, perguntas visíveis opcionais, links internos, schema e manutenção substantiva.
- Mídia visual por geração de imagem no Gemini, curadoria verificada de banco de imagens, gráficos SVG, incorporação de YouTube e exigência de texto alternativo.
- Integração com APIs do Google em PageSpeed Insights, CrUX, Search Console, GA4, NLP, YouTube, inspeção de URL e Planejador de Palavras-chave. O uso da Indexing API se restringe a URLs de JobPosting ou de transmissão ao vivo.
- Pesquisa no NotebookLM para respostas ancoradas nos documentos que você enviou.
- Narração em áudio por Gemini TTS, nos modos resumo, artigo completo e diálogo entre dois locutores.
- Suporte de plataforma a Next.js MDX, Astro, Hugo, Jekyll, WordPress, Ghost, 11ty, Gatsby e HTML estático.

### Referências de metodologia

| Referência | Finalidade |
|---|---|
| `ai-slop-detection.md` | Revisão consultiva de padrão editorial em dois níveis; nunca um classificador de autoria nem entrada de pontuação |
| `editorial-heuristics.md` | Pontuação de 0 a 4 adaptada de Nielsen, com severidade P0 a P3 |
| `cognitive-load.md` | Pontuação de densidade de conceitos por seção |
| `research-quality.md` | Checagens de nível de fonte, atualidade e qualidade de síntese |
| `synthesis-contract.md` | LEIS de síntese de pesquisa para saída segura quanto a citações |

A atribuição das adaptações está em [`CONTRIBUTORS.md`](docs/CONTRIBUTORS.md).

## Procedência do Brain

O Claude Blog Brain é vendorizado em `./brain` como um brain Obsidian autocontido e com evidência exigida. Ele não faz parte do payload do plugin; todo o ferramental de skill segue restrito a `skills/`. As atualizações derivadas do brain chegam por mudanças revisadas de referência, script e documentação.

## Instalação

Instalação como plugin para o Claude Code 1.0.33 ou superior:

```bash
/plugin marketplace add AgriciDaniel/claude-blog
/plugin install claude-blog@agricidaniel-blog
```

Fluxo recomendado de clonar, verificar e instalar:

```bash
git clone https://github.com/AgriciDaniel/claude-blog.git
cd claude-blog
git checkout v2.1.1
chmod +x install.sh
./install.sh
```

Instalação em um comando no Unix e no macOS:

```bash
curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-blog/main/install.sh | CLAUDE_BLOG_REF=v2.1.1 bash
```

Instalação em um comando no PowerShell do Windows:

```powershell
$env:CLAUDE_BLOG_REF = "v2.1.1"
irm https://raw.githubusercontent.com/AgriciDaniel/claude-blog/main/install.ps1 -OutFile install.ps1
pwsh -File ./install.ps1
```

Verifique a integridade do instalador antes de executar:

```bash
curl -fsSL -o install.sh https://raw.githubusercontent.com/AgriciDaniel/claude-blog/main/install.sh
echo "b4fcd5aa6767529bc8d11017699bd8211519c93b0d6c28c5cf032f76ada98381  install.sh" | sha256sum -c
CLAUDE_BLOG_REF=v2.1.1 bash install.sh
```

O SHA-256 acima corresponde ao `install.sh` atual no HEAD da `main`; o `CLAUDE_BLOG_REF` fixa o clone do repositório feito pelo instalador. Confira contra [o arquivo canônico](https://github.com/AgriciDaniel/claude-blog/blob/main/install.sh) antes de executar. O hash correspondente do `install.ps1` é `9532d3014aa24468d8dd309e19acb5557c9cc7e4edab718381c26515aab48a79`.

Reinicie o Claude Code após a instalação para ativar.

Desinstalação no Unix e no macOS:

```bash
chmod +x uninstall.sh
./uninstall.sh
```

Desinstalação no PowerShell do Windows:

```powershell
.\uninstall.ps1
```

Detalhes de instalação: [`docs/INSTALLATION.md`](docs/INSTALLATION.md).

## Requisitos

- CLI do [Claude Code](https://docs.anthropic.com/en/docs/claude-code) instalada e configurada.
- Python 3.11+ para a pontuação de qualidade, os executores do contrato de entrega, os renderizadores e o lint.
- Opcional: `pip install -r requirements.txt` para análise avançada, pontuação de legibilidade, detecção de schema e fluxos de mídia.

### Portões automatizados de qualidade na CI

1. **pytest**: a suíte completa de segurança, comportamento, regressão, instalador e contrato de entrega.
2. **Validação do plugin**: `claude plugin validate .` mais checagens de manifesto, marketplace e frontmatter.
3. **Lint de caminho defasado**: pega desvios em `references/`, `templates/`, documentação de comandos e payloads do instalador.
4. **Higiene de prosa**: `scripts/lint_prose.py` impede travessão, meia-risca e hífen duplo ASCII na prosa.
5. **Coerência de versão**: todas as superfícies canônicas de versão precisam bater com a versão da release.
6. **Coerência de comandos**: `skills/blog/SKILL.md` e [`docs/COMMANDS.md`](docs/COMMANDS.md) precisam declarar o mesmo conjunto de comandos.
7. **Consistência do repositório**: valida alvos de referência locais, travas de prompt do FLOW e reporta recursos órfãos sem bloquear.
8. **Teste de fumaça de dependências travadas por hash**: instala as travas de áudio e do NotebookLM com `--require-hashes` e então inicializa google-genai, Patchright e o preflight, sem chamadas de API nem abertura de navegador.
9. **Validação do brain**: mudanças em `brain/**` rodam a suíte pytest dele, o lint do vault e uma auditoria apenas informativa.

Rode localmente antes de enviar:

```bash
python3 -m pytest tests/
python3 scripts/lint_prose.py
claude plugin validate .
```

## Como o claude-blog se compara?

O claude-blog é um pipeline estruturado. Prompt direto num LLM é tiro único. Ferramentas SaaS hospedadas são de código fechado. Os trade-offs são:

| Capacidade | claude-blog | Prompt direto no Claude ou ChatGPT | Copy.ai ou Jasper | Construir do zero |
|---|:---:|:---:|:---:|:---:|
| Artigo completo em um comando, com laço de iteração | Sim | Tiro único | Sim | Não |
| Estatísticas com fonte e verificação | Sim | Não | Não | Manual |
| Otimização para citação por IA (GEO / AEO) | Sim | Não | Não | Parcial |
| Revisão de conteúdo bloqueante com nota 90 ou mais | Sim | Não | Não | Não |
| Multilíngue com hreflang num comando só | Sim | Parcial | Parcial | Não |
| Planejamento de cluster de temas | Sim | Não | Parcial | Não |
| Narração em áudio | Sim | Não | Não | Não |
| Escada de geração da imagem principal | Sim | Não | Só banco de imagens | Parcial |
| Contexto persistente de marca e voz | Sim | Por prompt | Limitado | Não |
| Código aberto, MIT, sem assinatura SaaS | Sim | Não | Não | Sim |

O claude-blog não é melhor em tudo. Prompt direto é mais rápido para um rascunho descartável. SaaS hospedado é mais fácil para quem não programa. Construir do zero é mais flexível para pipelines singulares. O claude-blog serve quando você quer conteúdo de nível de produção em escala, sem assinatura de SaaS.

## Perguntas frequentes

### O que é o claude-blog?

O claude-blog é um conjunto de skills do Claude Code para escrever, otimizar e auditar conteúdo de blog. Ele roda 32 diretórios de skill através de um contrato de entrega de 5 portões, de modo que todo artigo atinja a régua de 90/100 antes de chegar até você.

### Como o claude-blog difere de fazer prompt direto no Claude ou no ChatGPT?

Prompt direto entrega um rascunho a partir de um prompt. O claude-blog entrega um pipeline estruturado: pesquisa com estatísticas com fonte, aprovação de roteiro, geração de rascunho, pontuação de qualidade em várias passagens, revisão consultiva de padrão editorial, verificação de fatos, injeção de schema e uma revisão bloqueante que itera até 3 vezes antes da entrega.

### O claude-blog é gratuito e de código aberto?

Sim. [`AgriciDaniel/claude-blog`](https://github.com/AgriciDaniel/claude-blog)
é licenciado sob MIT e está disponível a qualquer pessoa que use o Claude Code.

### Que plataformas de blog o claude-blog suporta?

Next.js MDX, Astro, Hugo, Jekyll, WordPress, Ghost, 11ty, Gatsby e HTML estático. O orquestrador detecta a plataforma automaticamente e ajusta frontmatter, incorporação de imagem e injeção de schema.

### O claude-blog alucina estatísticas?

O fluxo foi desenhado para barrar números inventados. O `/blog factcheck` busca as URLs das fontes citadas e pontua cada afirmação como correspondência exata, paráfrase ou não encontrada. O `blog-reviewer` bloqueia a publicação quando as citações não podem ser verificadas.

### O que é o Blog Delivery Contract de 5 portões?

É um pipeline anterior à apresentação, cobrindo descoberta de capacidades, completude de formato, verificação visual, revisão de conteúdo e integridade de ativos e links. O orquestrador itera o redator até 3 vezes em qualquer falha de portão antes de escalar para você. Especificação completa: [`skills/blog/references/blog-delivery-contract.md`](skills/blog/references/blog-delivery-contract.md).

### Posso usar o claude-blog em vários idiomas?

Sim. `/blog multilingual <tema> --languages <códigos>` escreve o post, traduz preservando frontmatter e schema, roda adaptação cultural por localidade e emite tags hreflang mais um mapa de idiomas pronto para CMS.

### Como cito o claude-blog em trabalho acadêmico?

Veja [Como citar](#como-citar) ou o [`CITATION.cff`](CITATION.cff). O GitHub também expõe a citação pelo espelho público.

### É seguro instalar o claude-blog?

O fluxo recomendado baixa o instalador como arquivo, para você inspecioná-lo antes de executar. A v2.1.1 usa referências fixadas, cópias recursivas de payload com lista permitida, desinstalação apoiada em manifesto, lint de prosa, checagens de coerência de versão, checagens de consistência do repositório e testes de regressão do instalador. Veja [`SECURITY.md`](.github/SECURITY.md).

## Índice da documentação

- [Tutorial passo a passo](docs/TUTORIAL.md): do zero ao blog publicado, com a ordem em que os comandos entram.
- [Guia de instalação](docs/INSTALLATION.md): Unix, macOS, Windows, instalação manual e configuração reproduzível com `uv`.
- [Referência de comandos](docs/COMMANDS.md): referência completa com exemplos.
- [Arquitetura](docs/ARCHITECTURE.md): desenho do sistema e visão geral dos componentes.
- [Fluxo de publicação](docs/PUBLISHING.md): fluxo de release do privado ao público.
- [Templates](docs/TEMPLATES.md): referência e personalização de templates.
- [Solução de problemas](docs/TROUBLESHOOTING.md): problemas comuns e correções.
- [Integração MCP](docs/MCP-INTEGRATION.md): configuração opcional de servidor MCP.
- [Demonstração](docs/DEMO.md): exemplo completo de ponta a ponta.

## Como citar

Se você usa o claude-blog em pesquisa ou em produção, cite o projeto:

```bibtex
@software{Agrici_claude_blog_2026,
  author       = {Agrici, Daniel},
  title        = {claude-blog: AI Blog Writing and SEO Optimization Skill for Claude Code},
  year         = {2026},
  url          = {https://github.com/AgriciDaniel/claude-blog},
  version      = {2.1.1},
  license      = {MIT}
}
```

O GitHub também expõe o arquivo estruturado [`CITATION.cff`](CITATION.cff) pelo botão "Cite this repository" na página do espelho público.

## Segurança e código de conduta

- **Política de segurança e modelo de ameaças**: [`SECURITY.md`](.github/SECURITY.md). Para relatar uma vulnerabilidade em caráter privado, siga o procedimento de divulgação descrito lá.
- **Código de conduta**: [`CODE_OF_CONDUCT.md`](.github/CODE_OF_CONDUCT.md). Contributor Covenant.

## Como contribuir

Contribuições são bem-vindas. Veja [`CONTRIBUTING.md`](.github/CONTRIBUTING.md) para as diretrizes. Antes de abrir um PR:

1. Rode `python3 -m pytest tests/` e confirme que a suíte completa passa.
2. Rode `python3 scripts/lint_prose.py` e confirme zero violações.
3. Rode `claude plugin validate .`.
4. Suba as versões de forma coerente se você mexer em contagens ou comportamentos visíveis ao usuário.

## Licença

Licença MIT. Veja [`LICENSE`](LICENSE).

## Projetos relacionados

- **[Rankenstein](https://rankenstein.pro)**: fluxo de publicação de conteúdo com interface gráfica.
- **[Framework FLOW](https://github.com/AgriciDaniel/flow)**: prompts Find, Leverage, Optimize, Win guiados por evidência (CC BY 4.0).
- **[Claude Ads](https://github.com/AgriciDaniel/claude-ads)** e **[Claude SEO](https://github.com/AgriciDaniel/claude-seo)**: skills irmãs do Claude Code.
- **[AI Marketing Hub](https://www.skool.com/ai-marketing-hub)**: comunidade gratuita de marketing com IA.

## Autor

Construído por [Daniel Agrici](https://agricidaniel.com/about), AI Workflow Architect, com o Claude Code.

- [Blog](https://agricidaniel.com/blog): aprofundamentos em automação de marketing com IA.
- [YouTube](https://www.youtube.com/@AgriciDaniel): tutoriais e demonstrações.
- [Todas as ferramentas de código aberto](https://github.com/AgriciDaniel): outras skills do Claude Code.
- [AI Marketing Hub](https://www.skool.com/ai-marketing-hub): comunidade gratuita de marketing com IA.
