# Colaboradores

O Claude Blog é construído por [@AgriciDaniel](https://github.com/AgriciDaniel) com contribuições da comunidade AI Marketing Hub.

## v1.8.1 até v1.8.6: endurecimento por auditoria hostil (2026-05-17)

Sete rodadas de reauditoria hostil (trilhas de cibersegurança, GitHub, documentação, qualidade de código e cobertura de testes) encontraram, a cada rodada, defeitos que as anteriores deixaram passar. Cada rodada foi executada por passagens paralelas de revisão, com exigência de evidência em arquivo e linha. O próprio padrão de auditoria está documentado nas entradas v1.8.1 a v1.8.6 do `CHANGELOG.md`.

- **v1.8.1**: fechou 27 achados de uma auditoria em três trilhas (bug catastrófico de regex em `parse_engagement`, injeção indireta de prompt no carregamento automático da raiz do projeto, endurecimento contra travessia de caminho, atribuição no NOTICE).
- **v1.8.2**: contrato de nonce por carregamento e limpeza de travessões ASCII em todo o projeto (feita por script, deixou passar os travessões unicode).
- **v1.8.3**: defesa de nonce COM CAPACIDADE DE CÓDIGO via `scripts/load_untrusted_root.py`, mais 6 quebras HIGH de prosa e fechamento de negação de serviço O(n^2).
- **v1.8.4**: linter de higiene de prosa na CI (`scripts/lint_prose.py`), checagem de coerência de versão e 30 travessões unicode limpos (a limpeza da v1.8.2 e v1.8.3 não pegava unicode).
- **v1.8.5**: atualizações de CLAUDE.md e ARCHITECTURE.md, `tests/test_lint_prose.py`, instrução de autoridade de nonce MAIS EXTERNA e teste de regressão de coerência de comandos.
- **v1.8.6**: correção de sincronia do instalador (os auxiliares da v1.8.0 em diante nunca eram copiados pelo install.sh), 10 versões defasadas de SKILL.md de sub-skills resolvidas, teste de coerência de sub-skill, tratamento de cerca com 4 crases e regex de versão tolerante a aspas YAML.

Arco de nota calibrada: 68/100 (v1.8.0) -> platô em torno de 91/100 (v1.8.5) -> cerca de 96/100 (teto da v1.8.6 pelo kernel de /best-practices; 100/100 é estruturalmente inalcançável, conforme a análise de assíntota no CHANGELOG v1.8.5).

## v1.8.0: adaptação de metodologia do impeccable (2026-05-16)

Quatro metodologias editoriais da v1.8.0 são adaptadas do plugin de design de frontend [impeccable](https://github.com/pbakaus/impeccable) (v3.1.1, Apache 2.0, de [Paul Bakaus](https://github.com/pbakaus)).

| Metodologia | Origem no impeccable | Adaptada no claude-blog |
|---|---|---|
| Detecção de dois níveis de conteúdo genérico de IA (primeira ordem + reflexo de segunda ordem) | `skills/impeccable/SKILL.md` (checagem de reflexo por categoria) | `skills/blog/references/ai-slop-detection.md` |
| Rubrica heurística ordinal de 0 a 4 com severidade P0 a P3 | `skills/impeccable/reference/heuristics-scoring.md` | `skills/blog/references/editorial-heuristics.md` |
| Avaliação de carga cognitiva (intrínseca / estranha / relevante, teto de 4 itens na memória de trabalho) | `skills/impeccable/reference/cognitive-load.md` | `skills/blog/references/cognitive-load.md` + `scripts/cognitive_load.py` |
| Padrão durável de carregamento de contexto (PRODUCT.md / DESIGN.md carregados automaticamente por todo comando) | `skills/impeccable/scripts/load-context.mjs` + `reference/teach.md` | `skills/blog-brand/SKILL.md` (BRAND.md + VOICE.md) |

O impeccable lapida interfaces de usuário; esta release aplica os mesmos modelos mentais à prosa. Nenhum código foi copiado literalmente: a adaptação é no nível da metodologia. Cada arquivo de referência adaptado remete à sua origem no impeccable na seção de atribuição.

Licença da origem: Apache 2.0. O claude-blog segue licenciado sob MIT; a exigência de atribuição da Apache 2.0 é cumprida pelas linhas de crédito em cada arquivo adaptado mais esta seção.

## v1.8.0 (continuação): adaptação de metodologia do last30days-skill (2026-05-16)

Três metodologias de disciplina de pesquisa da v1.8.0 são adaptadas do plugin [last30days-skill](https://github.com/mvanhorn/last30days-skill) (v3.2.1, MIT, de [Matt Van Horn](https://github.com/mvanhorn)).

| Metodologia | Origem no last30days-skill | Adaptada no claude-blog |
|---|---|---|
| Pesquisa de discurso multiplataforma (Reddit / HN / X / YouTube etc.) | `skills/last30days/SKILL.md` + `scripts/last30days.py` (movido a API) | `skills/blog-discourse/SKILL.md` + `scripts/discourse_research.py` (sem API, WebSearch mais operadores de site) |
| Rubrica de qualidade de pesquisa em 5 dimensões (fundamentação, especificidade, cobertura, acionabilidade, formato) | `docs/search-quality-eval.md` mais a pontuação do SKILL.md | `skills/blog/references/research-quality.md` |
| Contrato de voz de síntese: 6 LEIS portáveis das 8 originais (sem bloco final de fontes, sem títulos inventados, sem travessões, sem despejo bruto de agrupamentos, citações inline `[nome](url)`, afirmações discretas) | seção "VOICE CONTRACT LAW" de `skills/last30days/SKILL.md` | `skills/blog/references/synthesis-contract.md`. A LEI 5 (repasse de rodapé do motor) e a LEI 7 (flag `--plan` obrigatória) são específicas do runtime do last30days e não foram portadas de propósito. |
| Classes de armadilha de palavra-chave no pré-voo (compra por perfil demográfico, armadilha numérica, literal demais, substantivo único genérico) | "Step 0.45" de `skills/last30days/SKILL.md` | embutidas em `research-quality.md` |
| Padrão de decomposição de tema por entidade nomeada (Passo 0.55) | "Step 0.55" de `skills/last30days/SKILL.md` | embutido em `research-quality.md`, referenciado por `agents/blog-researcher.md` |
| Conceito de ranqueamento com atualidade em primeiro lugar | seção de ranqueamento e pontuação de `skills/last30days/SKILL.md` | tabela de piso de atualidade em `research-quality.md` (30 e 90 dias) |

O projeto de origem é um motor sofisticado de pesquisa multiplataforma, que chama as APIs de Reddit, X, YouTube, TikTok, Hacker News, Polymarket, GitHub, Bluesky e outras, e pontua os resultados por engajamento ao vivo (votos, curtidas, dinheiro em mercados de previsão). O claude-blog porta a metodologia editorial sem o encanamento de API: o `blog-discourse` roda sobre resultados de WebSearch com operadores de site direcionados por plataforma (por exemplo, `site:reddit.com`, `site:news.ycombinator.com`, `site:x.com`), funcionando em qualquer ambiente sem chaves.

Licença da origem: MIT. O claude-blog segue licenciado sob MIT. A atribuição é cortesia sob a MIT, não exigência estrita; o crédito consta em cada arquivo adaptado mais esta seção.

## v1.7.0: release comunitária do Pro Hub Challenge (2026-04-27)

Em março de 2026, a comunidade AI Marketing Hub Pro realizou o primeiro Pro Hub Challenge: os membros construíram skills e extensões para os ecossistemas claude-blog e claude-seo. Seis submissões foram auditadas de forma independente (segurança, funcionalidade, qualidade de código, documentação, dependências, descobribilidade do SKILL.md e inovação). Cinco alcançaram nível Proficiente ou acima. Depois de revisão de segurança e reimplementação em sala limpa, na voz e na postura de segurança do claude-blog, duas submissões foram integradas como skills centrais na v1.7.0.

### Integradas como skills centrais

| Colaborador | Submissão original | Integrada como | Nota |
|---|---|---|---|
| **Lutfiya Miller** (vencedora) | [semantic-cluster-engine](https://github.com/Drfiya/semantic-cluster-engine) | `blog-cluster` (motor de planejamento e execução de cluster semântico de temas) | 95 / 100 Exemplar |
| **Chris Mueller** | [claude-blog-multilingual](https://github.com/Chriss54/multilingual-int) | `blog-multilingual`, `blog-translate`, `blog-localize`, `blog-locale-audit` mais o agente `blog-translator` | 85 / 100 Proficiente |

O motor de cluster foi a submissão de maior nota de todo o desafio. O desenho de Lutfiya (arquitetura Plan mais Execute, com injeção de contexto de cluster em cada escrita de post) foi preservado integralmente; removemos estilo e prompts de imagem específicos de marca, endurecemos a saída HTML contra XSS e passamos a rotear pelas sub-skills existentes do claude-blog.

A suíte multilíngue de Chris foi a submissão mais nativa de blog: quatro skills voltadas ao usuário, desenhadas explicitamente para o claude-blog. A auditoria apontou um instalador `curl | bash` e o tratamento de credenciais; ambos foram removidos neste porte. A referência compartilhada `cultural-adaptation.md` é referenciada, não duplicada, pelo `blog-localize`. O agente `blog-translator` é entregue sem acesso a `Bash` (pela lição da v1.9.6 do claude-seo: raio de alcance de injeção de prompt).

### Reconhecidas (não integradas no claude-blog v1.7.0)

| Colaborador | Submissão original | Situação |
|---|---|---|
| **Florian Schmitz** | [claude-sxo-skill](https://github.com/tools-enerix/claude-sxo-skill) | 91,7 Exemplar. Integrada ao [claude-seo v1.9.0](https://github.com/AgriciDaniel/claude-seo/releases/tag/v1.9.0) como `seo-sxo`. A adaptação para blog foi adiada até o analisador poder ser separado das dependências de construtor de página e DataForSEO. |
| **Dan Colta** | [seo-drift-monitor](https://github.com/dancolta/seo-drift-monitor) | 49 Inadequada. Rejeitada na auditoria (chave de API do Google embutida no código). O conceito (linha de base mais diff ao longo do tempo) é interessante; uma implementação em sala limpa do lado do blog está no roadmap. |
| **Matej Marjanovic** | [omnichannel-seo](https://github.com/matej-marjanovic/claude-seo) | 78,3 Proficiente. SEO de e-commerce mais DataForSEO Merchant. Integrada ao claude-seo v1.9.0; não é nativa de blog. |
| **Benjamin Samar** | seo-dungeon | 78,3 Proficiente. Gamificação de SEO. Revisada; não integrada. |

## v1.7.0: integração do framework FLOW

Lançada em **2026-04-27**.

- **Projeto de origem:** [FLOW](https://github.com/AgriciDaniel/flow) de Daniel Agrici, v1.0.0 (2026-04-25)
- **Licença:** CC BY 4.0 (conteúdo dos prompts) mais MIT (código da skill)
- **O que acrescenta:** 30 prompts de IA aplicáveis a blog (find: 5, leverage: 1, optimize: 21, win: 3), além do documento do framework FLOW e da bibliografia
- **Skill:** `blog-flow`
- **Comandos:** `/blog flow [find|optimize|win|prompts|sync]`
- **Mecanismo de sincronia:** `scripts/sync_flow.py` puxa do GitHub. Apenas biblioteca padrão. Apenas HTTPS. Host restrito a `api.github.com`. Limite de 5 MB. Escritas atômicas. Proteção contra travessia de caminho. API do GitHub anônima por padrão. Suporta `--dry-run` e fixação com `--ref <sha>`. Detecção de desvio por lockfile SHA-256.
- **Cabeçalhos de licença:** todo arquivo markdown sincronizado (e o README de índice gerado automaticamente) carrega um comentário HTML creditando Daniel Agrici / FLOW / CC BY 4.0.

Os prompts de estágio local (Perfil da Empresa no Google, citações, auditorias locais) foram excluídos de propósito: miram trabalho de negócio físico, não de blog. Para o estágio local, use o `seo-flow` do `claude-seo`.

## v1.7.0: guardrails mecânicos de segurança

Lançados em **2026-04-27**.

Um novo módulo pytest (`tests/test_security_guardrails.py`) impõe quatro invariantes a cada execução de teste:

1. Nenhum agente concede a ferramenta `Bash` no frontmatter (raio de alcance de injeção de prompt).
2. Nenhum `SKILL.md` inclui o campo inválido `allowed-tools`.
3. Os nomes de skill são únicos em todo o repositório (sem roteamento duplicado).
4. O script de sincronia do FLOW preserva os seis invariantes de segurança (lista permitida de host, limite de tamanho, flag de simulação, fixação de referência, lockfile, injeção de cabeçalho de licença, proteção contra travessia de caminho).

Achado pré-existente fechado: `agents/blog-reviewer.md` tinha `Bash` na lista de ferramentas (usado apenas para contagem de palavras e correspondência de padrões que o `Grep` já cobre). Removido.

## Como creditar um colaborador num post

Ao escrever sobre um colaborador, linke para:

- O **repositório da submissão original** (a URL do GitHub na tabela acima)
- A skill integrada neste repositório: `https://github.com/AgriciDaniel/claude-blog/tree/main/skills/<nome-da-skill>/`
- Este arquivo `CONTRIBUTORS.md` como fonte canônica de atribuição

## Comunidade

- **Comunidade gratuita:** https://www.skool.com/ai-marketing-hub
- **Comunidade Pro:** https://www.skool.com/ai-marketing-hub-pro
