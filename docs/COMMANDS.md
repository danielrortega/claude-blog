# Referência de Comandos

Referência completa de 32 diretórios de skill (1 orquestrador + 31 sub-skills);
30 comandos voltados ao usuário. O `blog-chart` é somente interno, invocado a
partir de blog-write e blog-rewrite.
Todo comando é invocado pelo orquestrador principal
(`skills/blog/SKILL.md`), que roteia para a sub-skill adequada.

> **Para fluxos detalhados além da tabela panorâmica abaixo, consulte
> diretamente o `SKILL.md` de cada sub-skill. As seções deste arquivo estão
> abreviadas no caso dos comandos das v1.7.0 e v1.8.0, que chegaram depois de o
> documento ter sido escrito; a tabela panorâmica abaixo é a lista canônica de
> comandos.**

## Visão geral dos comandos

```
/blog <comando> [argumentos]
```

| Comando | Sub-skill | Descrição |
|---------|-----------|-----------|
| `write <topic>` | blog-write | Escreve um post novo do zero (v1.9.0: itera pelo contrato de entrega de 5 portões até a nota atingir 90 ou mais com zero P0, no máximo 3 iterações) |
| `rewrite <file>` | blog-rewrite | Otimiza um post existente (v1.9.0: mesmo contrato de entrega; a reescrita precisa pontuar pelo menos tanto quanto o original) |
| `analyze <file-or-url>` | blog-analyze | Audita a qualidade do post com nota de 0 a 100 |
| `brief <topic>` | blog-brief | Gera um briefing de conteúdo detalhado |
| `calendar [monthly\|quarterly]` | blog-calendar | Gera um calendário editorial |
| `strategy <niche>` | blog-strategy | Estratégia de blog e geração de temas |
| `outline <topic>` | blog-outline | Geração de roteiro informado por resultados de busca |
| `seo-check <file>` | blog-seo-check | Validação de SEO após a escrita |
| `schema <file>` | blog-schema | Gera marcação de schema JSON-LD |
| `repurpose <file>` | blog-repurpose | Reaproveita o conteúdo para outras plataformas |
| `geo <file>` | blog-geo | Auditoria de otimização para citação por IA |
| `audit [directory]` | blog-audit | Avaliação de saúde do blog inteiro |
| `image [generate\|edit\|setup]` | blog-image | Geração e edição de imagem por IA via Gemini |
| `cannibalization [directory]` | blog-cannibalization | Detecta sobreposição de palavra-chave entre posts |
| `factcheck <file>` | blog-factcheck | Verifica estatísticas contra as fontes citadas |
| `persona [create\|list\|use\|show]` | blog-persona | Gerencia personas de escrita e perfis de voz |
| `taxonomy [sync\|audit\|suggest]` | blog-taxonomy | Gestão de tags e categorias no CMS |
| `notebooklm <question>` | blog-notebooklm | Consulta o NotebookLM para pesquisa ancorada em fonte |
| `audio [generate\|voices\|setup]` | blog-audio | Gera narração em áudio via Gemini TTS |
| `google [command] [args]` | blog-google | Dados de API do Google: PSI, CrUX, GSC, GA4, NLP, YouTube, palavras-chave |
| `cluster [plan\|execute] <seed>` | blog-cluster | Planejamento e execução de cluster semântico de temas (v1.7.0) |
| `multilingual <topic> --languages <codes>` | blog-multilingual | Escreve, traduz, localiza e emite hreflang (v1.7.0) |
| `translate <file> --to <codes>` | blog-translate | Tradução otimizada para SEO com preservação de formato (v1.7.0) |
| `localize <file> --locale <code>` | blog-localize | Adaptação cultural profunda por localidade (v1.7.0) |
| `locale-audit <directory>` | blog-locale-audit | QA de conteúdo multilíngue (v1.7.0) |
| `flow [find\|optimize\|win\|prompts\|sync]` | blog-flow | Prompts do framework FLOW (v1.7.0) |
| `brand [init\|show\|update]` | blog-brand | Gera o contexto BRAND.md + VOICE.md carregado automaticamente por todas as sub-skills (v1.8.0) |
| `discourse <topic>` | blog-discourse | Pesquisa de discurso dos últimos 30 dias sem API; produz DISCOURSE.md (v1.8.0) |
| `style learn <paths>` | blog-style | Aprende o perfil de voz do autor a partir de posts existentes (v1.10.0) |
| `decay <current-gsc> <previous-gsc>` | blog-decay | Detecta decaimento de conteúdo: queda de 20%+ no trimestre a partir de exportações do GSC (v1.10.0) |
| `update <file>` | blog-rewrite | Atualiza um post existente com estatísticas novas (roteia para rewrite) |

Apelido: `/blog update <arquivo>` roteia para `/blog rewrite <arquivo>` nas
atualizações focadas em atualidade.

---

## /blog brand (v1.8.0)

Gera `BRAND.md` e `VOICE.md` na raiz do projeto por meio de uma entrevista curta.
Esses arquivos são carregados automaticamente como contexto não confiável, com
cerca, por toda sub-skill de redação, revisão e auditoria, dando ao agente
guardrails duráveis de marca e de voz sem precisar reperguntar a cada invocação.

```
/blog brand init              # entrevista interativa, escreve BRAND.md + VOICE.md
/blog brand show              # imprime o BRAND.md e o VOICE.md atuais
/blog brand update            # refaz um trecho específico da entrevista
```

Ao rodar `/blog brand` sem subcomando: cai em `show` se qualquer um dos arquivos
já existir na raiz do projeto, e em `init` caso contrário.

O contrato de carregamento automático (cerca, higienização, preservação de
fronteira de ferramenta e procedência) está documentado na seção
"Untrusted-Data Contract" de `skills/blog/SKILL.md`. Veja
`skills/blog-brand/SKILL.md` para o roteiro completo da entrevista e o schema de
saída.

---

## /blog discourse (v1.8.0)

Pesquisa o que profissionais reais estão dizendo sobre um tema nos últimos 30
(ou 90) dias em Reddit, X / Twitter, YouTube, Hacker News, dev.to, Medium,
GitHub, Stack Overflow e Substack. Sem API: usa WebSearch com operadores de site
direcionados por plataforma, mais filtros de recência. Produz um `DISCOURSE.md`
na raiz do projeto, carregado automaticamente pelas invocações seguintes de
`/blog write`, `/blog brief` e `/blog strategy`.

```
/blog discourse <tema>                           # janela padrão de 30 dias
/blog discourse <tema> --days 90                 # amplia para 90 dias
/blog discourse <tema> --feed-into brief         # encadeia no /blog brief
/blog discourse <tema> --feed-into write         # encadeia no /blog write
/blog discourse <tema> --feed-into strategy      # encadeia no /blog strategy
/blog discourse <tema> --input results.json      # pula a busca, usa resultados já coletados
```

Fases do fluxo (detalhe completo em `skills/blog-discourse/SKILL.md`):

1. **Pré-voo do tema** (obrigatório): roda as quatro checagens de armadilha de
   palavra-chave de `research-quality.md` (compra por perfil demográfico,
   armadilha numérica, literal demais, substantivo único genérico). Recusar temas
   armadilha economiza chamadas de WebSearch.
2. **Decomposição**: divide em consultas distintas (entidade principal,
   contraponto, discurso de quem pratica, entidades tangenciais, âncora temporal).
3. **WebSearch direcionado por plataforma**: 4 a 8 buscas no subconjunto
   relevante das 9 plataformas.
4. **Coleta de resultados**: captura os resultados num arquivo temporário criado
   por `mkstemp`. Aplica o **contrato de dado não confiável do WebSearch**
   (higieniza trechos com padrões em forma de instrução; nunca segue diretivas
   presentes no conteúdo capturado).
5. **Geração do briefing**: o `scripts/discourse_research.py` agrupa por tema,
   classifica nos baldes NEW / CONSENSUS / NICHE / SPECIFICS, aplica as 6 LEIS do
   contrato de síntese e escreve o `DISCOURSE.md` de forma atômica.

Nota de segurança: o script impõe validação estrita de entrada (schema JSON,
lista permitida de esquema de URL, remoção de caracteres de controle, limite
MAX_STRING_FIELD) e leituras de arquivo resistentes a TOCTOU (O_NOFOLLOW em
POSIX). Veja `tests/test_security_v1_8_0.py` e a passagem de endurecimento da
v1.8.1 para o modelo de ameaças.

---

## /blog write

Escreve um post novo do zero, totalmente otimizado para ranqueamento no Google e
para plataformas de citação por IA.

### Uso

```
/blog write <tema>
/blog write "Como Otimizar para Busca por IA em 2026"
/blog write monitoramento kubernetes --format mdx --words 3000
```

### Fluxo

1. **Esclarecimento do tema**: pergunta público, palavra-chave, extensão, plataforma
2. **Pesquisa**: dispara o agente `blog-researcher` para achar 8 a 12 estatísticas e imagens
3. **Roteiro**: gera roteiro estruturado e apresenta para aprovação
4. **Geração de gráficos**: cria 2 a 4 gráficos SVG pelo `blog-chart` embutido
5. **Redação**: dispara o agente `blog-writer` para o artigo completo
6. **Checagem de qualidade**: verifica os 6 pilares de otimização
7. **Entrega**: salva o arquivo e apresenta o resumo

### Saída

Um post completo no formato detectado (Markdown, MDX ou HTML), com:

- Frontmatter YAML (title, description, coverImage, ogImage, date, tags)
- Tratamento orientado ao propósito nas seções importantes, com evidência onde necessário
- 8 a 12 estatísticas com fonte, de níveis 1 a 3
- 3 a 5 imagens inline do Pixabay, Unsplash ou Pexels
- 2 a 4 gráficos SVG de visualização de dados
- Perguntas frequentes opcionais, quando dúvidas reais de leitor justificarem
- Marcadores de link interno

### Comandos relacionados

- `/blog brief`: gere um briefing primeiro e alimente o `/blog write` com ele
- `/blog analyze`: pontue o post finalizado
- `/blog seo-check`: valide o SEO depois de escrever

---

## /blog rewrite

Otimiza um post existente para ranqueamento e citação por IA, preservando a voz
e a perspectiva próprias do autor.

### Uso

```
/blog rewrite <arquivo>
/blog rewrite content/blog/meu-post.mdx
/blog rewrite posts/artigo-antigo.md
```

### Fluxo

1. **Auditoria**: lê o arquivo e o pontua contra a lista de verificação de qualidade
2. **Plano**: apresenta o plano de otimização seção a seção para aprovação
3. **Pesquisa**: encontra estatísticas substitutas para dados inventados ou sem fonte
4. **Geração de gráficos**: acrescenta gráficos SVG se o post tiver menos de 2
5. **Reescrita**: clarifica as seções importantes, ajusta parágrafos e acrescenta perguntas só quando úteis
6. **Verificação**: confirma que todos os portões de qualidade passam
7. **Resumo**: reporta as notas antes e depois e as mudanças feitas

### Saída

O arquivo reescrito no formato original, com:

- `lastUpdated` verdadeiro, apenas quando fatos, métodos ou recomendações mudaram de fato
- Tratamento claro e apoiado em evidência nas seções importantes
- Estatísticas inventadas substituídas por dados com fonte
- Imagens e gráficos acrescentados onde necessário
- Perguntas frequentes acrescentadas ou melhoradas só quando servem a dúvidas reais
- Autopromoção reduzida a no máximo 1 menção à marca

### Comandos relacionados

- `/blog analyze`: audite antes de reescrever, para conhecer a nota de partida
- `/blog update`: apelido para reescrita focada em atualidade

---

## /blog analyze

Audita a qualidade de um post com nota de 0 a 100 em 6 categorias, com
recomendações priorizadas de melhoria.

### Uso

```
/blog analyze <arquivo>
/blog analyze <url>
/blog analyze content/blog/ --batch
```

### Tipos de entrada

| Entrada | Comportamento |
|---------|---------------|
| Arquivo local (`.md`, `.mdx`, `.html`) | Lê e analisa diretamente |
| URL | Busca por WebFetch e extrai o conteúdo |
| Diretório (com `--batch`) | Varre todos os arquivos e produz tabela-resumo |

### Saída

```
Relatório de qualidade do post: [Título]

Nota: 78/100 - Bom

Detalhamento da nota
| Categoria                | Nota  | Máx |
|--------------------------|-------|-----|
| Qualidade de conteúdo    | 21    | 25  |
| Formato resposta primeiro| 15    | 20  |
| Estatísticas e citações  | 18    | 20  |
| Elementos visuais        | 10    | 15  |
| Schema e estrutura       | 7     | 10  |
| Atualidade e confiança   | 7     | 10  |

Problemas encontrados (priorizados: Crítico > Alto > Médio > Baixo)
Ações recomendadas (as 3 correções de maior impacto)
```

### Saída em modo lote

Quando recebe um diretório, produz uma tabela-resumo ranqueada de todos os posts,
com notas, classificações e principais problemas. Os posts são ordenados da menor
nota para a maior, funcionando como fila de prioridade de otimização.

### Script Python

O script `analyze_blog.py` fornece métricas automatizadas:

```bash
python3 ~/.claude/skills/blog/scripts/analyze_blog.py post.md
python3 ~/.claude/skills/blog/scripts/analyze_blog.py posts/ --batch
python3 ~/.claude/skills/blog/scripts/analyze_blog.py post.md -o relatorio.json
python3 ~/.claude/skills/blog/scripts/analyze_blog.py post.md --lang pt
```

### Comandos relacionados

- `/blog rewrite`: aplica automaticamente as correções recomendadas
- `/blog audit`: avaliação do site inteiro (mais ampla que a análise de arquivo único)

---

## /blog brief

Gera um briefing de conteúdo abrangente, com palavras-chave, análise
competitiva, pesquisa de estatísticas, planejamento de elementos visuais e um
roteiro estruturado.

### Uso

```
/blog brief <tema>
/blog brief "otimização de custo de nuvem para startups"
/blog brief otimizacao-busca-ia --audience "gerentes de marketing"
```

### Fluxo

1. **Coleta do tema**: reúne tema, público, intenção e contexto de negócio
2. **Pesquisa de palavras-chave**: principal, 3 a 5 secundárias, 3 a 5 perguntas
3. **Análise competitiva**: analisa as 3 a 5 páginas mais bem ranqueadas
4. **Pesquisa de estatísticas**: encontra 8 a 12 dados com fonte
5. **Geração do briefing**: briefing completo com roteiro e recomendações

### Saída

Um documento de briefing detalhado, salvo em `briefs/[slug]-brief.md`, contendo:

- Palavras-chave alvo (principal, secundárias, perguntas)
- Análise da intenção de busca
- Parâmetros de conteúdo (extensão, formato, quantidade de gráficos e imagens)
- Opções recomendadas de título e meta description
- Roteiro completo com orientação por seção
- Tabela de estatísticas com fontes já pesquisadas
- Plano de elementos visuais (tipos de gráfico, termos de busca de imagem)
- Lacunas da concorrência a explorar
- Oportunidades de link interno
- Sinais de E-E-A-T a incluir
- Notas de distribuição (Reddit, YouTube, redes sociais)

### Comandos relacionados

- `/blog write`: escreve o artigo usando o briefing gerado
- `/blog strategy`: planejamento de nível mais alto, antes dos briefings individuais
- `/blog outline`: roteiro mais leve, sem a pesquisa completa

---

## /blog calendar

Gera um calendário editorial com clusters de temas, cronogramas de publicação,
planos de atualização por atualidade e oportunidades sazonais.

### Uso

```
/blog calendar
/blog calendar monthly
/blog calendar quarterly
/blog calendar --niche "ferramentas devops" --cadence 3
```

### Formatos de saída

**Calendário mensal**: tabela semana a semana com tipo de post (Novo/Atualização),
título, cluster de tema, palavra-chave alvo e situação. Inclui a fila de
atualização por atualidade e os ganchos sazonais.

**Calendário trimestral**: plano de três meses com foco de cluster por mês, metas
de velocidade de conteúdo, objetivos trimestrais e plano de distribuição.

### Recursos principais

- **Desenho de cluster de temas**: 3 a 5 clusters de conteúdo pilar e de apoio
- **Agendamento de atualidade**: ciclos de atualização de 30 dias para posts prioritários
- **Mix de conteúdo**: equilibra posts novos com atualizações
- **Ganchos sazonais**: eventos do setor, temas em alta, lançamentos de relatórios

### Comandos relacionados

- `/blog strategy`: defina pilares e posicionamento antes de planejar o calendário
- `/blog brief`: crie briefings para os itens do calendário

---

## /blog strategy

Desenvolve uma estratégia de blog abrangente, com pilares de conteúdo,
mapeamento de público, análise do cenário competitivo e planejamento de
distribuição.

### Uso

```
/blog strategy <nicho>
/blog strategy "marketing B2B SaaS"
/blog strategy ecommerce --competitors "shopify,bigcommerce,woocommerce"
```

### Fluxo

1. **Descoberta**: contexto de negócio, objetivos, estado atual, concorrentes
2. **Cenário competitivo**: analisa os blogs dos concorrentes e a visibilidade em IA
3. **Mapeamento de público**: 2 a 3 segmentos com dores e comportamento de busca
4. **Desenho dos pilares de conteúdo**: 3 a 5 pilares com temas de palavra-chave
5. **Diferenciação**: planos de experiência direta e de dados próprios
6. **Canais de distribuição**: YouTube, Reddit, análises, publicações
7. **Arcabouço de medição**: SEO tradicional mais métricas de citação por IA
8. **Documento de estratégia**: do resumo executivo ao roadmap de 90 dias

### Saída

Um documento completo de estratégia com:

- Segmentos de público com análise de comportamento em IA
- Pilares de conteúdo com estimativa de quantidade de posts
- Posicionamento competitivo e lacunas
- Prioridades de canal de distribuição, com táticas
- Recomendações de velocidade de conteúdo
- Roadmap de implementação de 90 dias
- Indicadores de SEO, citação por IA, qualidade e impacto no negócio

### Comandos relacionados

- `/blog calendar`: transforma a estratégia em cronograma de publicação
- `/blog brief`: cria briefings para os temas identificados na estratégia

---

## /blog outline

Gera um roteiro de conteúdo informado por resultados de busca, analisando o que
ranqueia hoje para a palavra-chave alvo.

### Uso

```
/blog outline <tema>
/blog outline "boas práticas de react server components"
```

### Saída

Um roteiro estruturado com:

- Títulos de seção H2 na forma que melhor acompanha a intenção do leitor
- Orientação orientada ao propósito nas seções importantes
- Marcadores de posicionamento de imagem e gráfico
- Sugestões de perguntas frequentes
- Metas de extensão por seção

### Comandos relacionados

- `/blog brief`: briefing completo com pesquisa (o roteiro é um subconjunto)
- `/blog write`: escreve direto a partir do roteiro

---

## /blog seo-check

Validação de SEO após a escrita, checando os elementos técnicos além da
qualidade de conteúdo.

### Uso

```
/blog seo-check <arquivo>
/blog seo-check content/blog/post-novo.mdx
```

### Checagens realizadas

- Clareza do meta title e adequação à página
- Meta description precisa e específica da página
- Hierarquia de títulos (H1 > H2 > H3, sem saltos)
- Presença da palavra-chave no título, nos H2 e na meta description
- Quantidade de links internos (alvo de 5 a 10 a cada 2.000 palavras)
- Completude do texto alternativo das imagens
- Presença de marcação de schema (BlogPosting, FAQPage)
- Meta tags de Open Graph e Twitter Card
- Veracidade de `lastUpdated` e `dateModified` após mudanças substantivas

### Comandos relacionados

- `/blog analyze`: auditoria completa de qualidade (conteúdo, SEO e citações)
- `/blog schema`: gera a marcação de schema ausente

---

## /blog schema

Gera marcação de dado estruturado JSON-LD para um post.

### Uso

```
/blog schema <arquivo>
/blog schema content/blog/meu-post.mdx
```

### Tipos de schema gerados

| Tipo de schema | Quando é gerado |
|----------------|-----------------|
| BlogPosting | Sempre (principal) |
| FAQPage | Quando há seção de perguntas detectada |
| BreadcrumbList | Quando a estrutura do site está disponível |
| Person | Quando há informação de autor disponível |
| Organization | Quando há contexto de empresa disponível |

### Saída

Blocos `<script>` de JSON-LD prontos para injeção no `<head>` da página ou em um
componente. Inclui `datePublished`, `dateModified`, `author`, `image` e os itens
de perguntas frequentes.

### Importante

Prefira schema no código-fonte ou em HTML renderizado no servidor, por
portabilidade: a capacidade de renderização varia entre rastreadores. Para o
Google Search, JSON-LD gerado por JavaScript é aceitável quando chega ao DOM
renderizado, corresponde ao conteúdo visível e passa na validação. Verifique
individualmente os demais rastreadores alvo.

### Comandos relacionados

- `/blog seo-check`: valida a presença e a correção do schema
- `/blog analyze`: checa o schema como parte da auditoria completa

---

## /blog repurpose

Reaproveita um post em conteúdo para outras plataformas e formatos.

### Uso

```
/blog repurpose <arquivo>
/blog repurpose content/blog/guia-busca-ia.mdx
```

### Formatos de saída

| Plataforma | Formato |
|------------|---------|
| Twitter/X | Thread (5 a 10 posts com as percepções centrais) |
| LinkedIn | Artigo ou publicação com recorte profissional |
| Reddit | Publicação que abre discussão em subreddits pertinentes |
| YouTube | Roteiro de vídeo com os pontos de fala |
| Newsletter | Versão em resumo por e-mail, com chamada para ação |
| Podcast | Roteiro de entrevista ou conversa baseado no conteúdo do post |

### Comandos relacionados

- `/blog strategy`: identifica os canais de distribuição para o reaproveitamento
- `/blog write`: cria o post original a ser reaproveitado

---

## /blog geo

Auditoria de otimização para citação por IA. Analisa um post especificamente
quanto à visibilidade em plataformas de IA (ChatGPT, Perplexity, AI Overviews do
Google).

### Uso

```
/blog geo <arquivo>
/blog geo content/blog/meu-post.mdx
```

### Checagens realizadas

- Tratamento autossuficiente e apoiado em evidência das afirmações importantes
- Manutenção substantiva quando fatos, métodos ou recomendações mudam
- Perguntas visíveis opcionais, sem ganho de rich result no Google nem de nota de prontidão
- Qualidade do nível de autoridade das fontes
- Estrutura útil ao leitor e contexto suficiente para as afirmações importantes se sustentarem sozinhas
- Dependência de JavaScript e compatibilidade de renderização com os rastreadores alvo
- Acesso de rastreador de IA no `robots.txt` (GPTBot, ClaudeBot, PerplexityBot)
- Recomendações opcionais de canal de público (YouTube, Reddit, análises)

### Comandos relacionados

- `/blog analyze`: auditoria completa de qualidade, incluindo métricas de GEO
- `/blog rewrite`: aplica as otimizações de GEO automaticamente

---

## /blog audit

Avaliação de saúde do blog inteiro. Varre um diretório completo de posts e
produz um relatório abrangente.

### Uso

```
/blog audit
/blog audit content/blog/
/blog audit posts/ --format markdown
```

### Saída

- **Tabela-resumo**: cada post pontuado e classificado
- **Fila de prioridade**: posts ordenados da menor nota para a maior
- **Detalhamento por categoria**: médias do site em cada categoria de pontuação
- **Problemas recorrentes**: os mais frequentes em todos os posts
- **Relatório de atualidade**: posts atrasados para atualização (mais de 30 dias)
- **Cobertura de temas**: análise de cluster e identificação de lacunas

### Comandos relacionados

- `/blog analyze`: auditoria de arquivo único (o audit é a versão em lote)
- `/blog calendar`: planeja conteúdo a partir dos achados da auditoria
- `/blog rewrite`: corrige os posts identificados pela auditoria

---

## /blog update

Apelido de `/blog rewrite` num modo focado em atualidade. Minimiza mudanças
estruturais e concentra-se em atualizar dados e sinais.

### Uso

```
/blog update <arquivo>
/blog update content/blog/post-antigo.mdx
```

### O que faz

1. Atualiza as estatísticas para os dados mais recentes disponíveis (2025-2026)
2. Acrescenta os desenvolvimentos ocorridos desde a última atualização
3. Renova as imagens com mais de 1 ano
4. Atualiza o `lastUpdated` apenas depois de mudanças substantivas de conteúdo
5. Preserva a estrutura existente (reescritas mínimas)
6. Faz apenas as mudanças necessárias para exatidão factual e valor ao leitor; sem meta de percentual de alteração

### Comandos relacionados

- `/blog rewrite`: reescrita completa (mais agressiva que o update)
- `/blog audit`: encontra os posts que precisam de atualização

---

## /blog image

**Finalidade**: geração e edição de imagem por IA pelo servidor nanobanana-mcp (Gemini).

```
/blog image generate <descrição>
/blog image edit <caminho> <instruções>
/blog image setup
```

**Fluxo**: veja `skills/blog-image/SKILL.md`: padrão de Diretor de Criação com o
briefing de raciocínio de 6 componentes (sujeito, ação, contexto, composição,
iluminação, estilo). O subcomando `setup` usa `--global` por padrão (grava um
`~/.claude/settings.json` privado do usuário, modo 0600), conforme a correção da
auditoria VULN-001.

---

## /blog cannibalization

**Finalidade**: detectar sobreposição de palavra-chave entre os posts de um diretório.

```
/blog cannibalization [diretório]
```

**Fluxo**: veja `skills/blog-cannibalization/SKILL.md`.

---

## /blog factcheck

**Finalidade**: verificar as estatísticas de um rascunho contra as fontes citadas.

```
/blog factcheck <caminho-do-arquivo>
```

**Fluxo**: veja `skills/blog-factcheck/SKILL.md`.

---

## /blog persona

**Finalidade**: gerenciar personas de escrita e perfis de voz.

```
/blog persona create
/blog persona list
/blog persona use <nome>
/blog persona show <nome>
```

**Fluxo**: veja `skills/blog-persona/SKILL.md`. As personas ficam em
`skills/blog/references/personas/`.

---

## /blog taxonomy

**Finalidade**: gestão de tags e categorias no CMS para conteúdo de blog.

```
/blog taxonomy sync
/blog taxonomy audit
/blog taxonomy suggest
```

**Fluxo**: veja `skills/blog-taxonomy/SKILL.md`.

---

## /blog notebooklm

**Finalidade**: consultar o NotebookLM para pesquisa ancorada em fonte, por
automação de navegador com patchright.

```
/blog notebooklm <pergunta>
```

**Fluxo**: veja `skills/blog-notebooklm/SKILL.md`. Os cookies em
`~/.claude/skills/blog-notebooklm/data/` são gravados em modo 0600, conforme a
correção da auditoria VULN-004.

---

## /blog audio

**Finalidade**: gerar narração em áudio via Gemini TTS.

```
/blog audio generate <caminho-do-arquivo>
/blog audio voices
/blog audio setup
```

**Fluxo**: veja `skills/blog-audio/SKILL.md`. Catálogo de 30 vozes nas referências.

---

## /blog google

**Finalidade**: integração com dados de API do Google (PSI, CrUX, GSC, GA4, NLP,
YouTube, palavras-chave). O uso da Indexing API se limita a URLs de JobPosting ou
de transmissão ao vivo.

```
/blog google <comando> [args]
```

**Fluxo**: veja `skills/blog-google/SKILL.md`. São 13 comandos em 4 níveis de
credencial. Proteção de CSRF no estado OAuth e armazenamento de token em modo
0600, conforme as correções das auditorias VULN-002 e VULN-008. Os escopos padrão
são somente leitura (`gsc_readonly + ga4`); use `--scopes` para elevar.

---

## /blog cluster (v1.7.0)

**Finalidade**: planejamento e execução de cluster semântico de temas.
Arquitetura de eixo e raios com contexto de cluster compartilhado.

```
/blog cluster <tema-semente>
```

**Fluxo**: veja `skills/blog-cluster/SKILL.md`. Adaptado do
[semantic-cluster-engine](https://github.com/Drfiya/semantic-cluster-engine)
(vencedor do Pro Hub Challenge do AI Marketing Hub).

---

## /blog flow (v1.7.0)

**Finalidade**: prompts do framework FLOW (find / optimize / win / prompts / sync).

```
/blog flow find
/blog flow optimize
/blog flow win
/blog flow prompts
/blog flow sync [--ref <sha>] [--allow-drift]
```

**Fluxo**: veja `skills/blog-flow/SKILL.md`. O sync usa `scripts/sync_flow.py`
com lista permitida de host somente HTTPS, limite de 5MB, proteção contra
travessia de caminho e portão bloqueante de desvio de lockfile (conforme a
correção da auditoria VULN-018).

---

## /blog multilingual (v1.7.0)

**Finalidade**: escrever, traduzir, localizar e emitir hreflang num comando só.

```
/blog multilingual <tema> --languages de,fr,es
```

**Fluxo**: veja `skills/blog-multilingual/SKILL.md`. Orquestra blog-write,
blog-translate e blog-localize, mais o `seo-hreflang` opcional.

---

## /blog translate (v1.7.0)

**Finalidade**: tradução otimizada para SEO com preservação de formato.

```
/blog translate <caminho-do-arquivo> <idioma-destino>
```

**Fluxo**: veja `skills/blog-translate/SKILL.md`. Dispara o agente
`blog-translator` (privilégio mínimo: Read/Write/Edit/Glob/Grep, sem Bash, sem
acesso à web).

---

## /blog localize (v1.7.0)

**Finalidade**: adaptação cultural profunda por localidade (perfis DACH,
francófono, hispânico e japonês, mais template personalizado).

```
/blog localize <caminho-do-arquivo> <localidade>
```

**Fluxo**: veja `skills/blog-localize/SKILL.md`.

---

## /blog locale-audit (v1.7.0)

**Finalidade**: QA de conteúdo multilíngue (matriz de completude, correção de
hreflang, paridade de meta tags, atualidade).

```
/blog locale-audit <diretório>
```

**Fluxo**: veja `skills/blog-locale-audit/SKILL.md`.

---

## Roteamento de comandos

O orquestrador principal (`skills/blog/SKILL.md`) interpreta a entrada do usuário
e roteia para a sub-skill correta:

```
Entrada do usuário                          Roteia para
------------------                          -----------
/blog write <topic>                     --> blog-write
/blog rewrite <file>                    --> blog-rewrite
/blog analyze <file-or-url>             --> blog-analyze
/blog brief <topic>                     --> blog-brief
/blog calendar [period]                 --> blog-calendar
/blog plan [period]                     --> blog-calendar
/blog strategy <niche>                  --> blog-strategy
/blog ideation <niche>                  --> blog-strategy
/blog outline <topic>                   --> blog-outline
/blog seo-check <file>                  --> blog-seo-check
/blog schema <file>                     --> blog-schema
/blog repurpose <file>                  --> blog-repurpose
/blog geo <file>                        --> blog-geo
/blog audit [directory]                 --> blog-audit
/blog image [generate|edit]             --> blog-image
/blog update <file>                     --> blog-rewrite (modo atualidade)
/blog cannibalization [dir]             --> blog-cannibalization
/blog factcheck <file>                  --> blog-factcheck
/blog persona [create|list|use|show]    --> blog-persona
/blog brand [init|show|update]          --> blog-brand               (v1.8.0)
/blog discourse <topic>                 --> blog-discourse           (v1.8.0)
/blog taxonomy [suggest|sync|audit]     --> blog-taxonomy
/blog notebooklm <question>             --> blog-notebooklm
/blog audio [generate|voices|setup]     --> blog-audio
/blog google [command] [args]           --> blog-google
/blog cluster [plan|execute] <seed>     --> blog-cluster
/blog multilingual <topic> --languages  --> blog-multilingual
/blog translate <file> --to             --> blog-translate
/blog localize <file> --locale          --> blog-localize
/blog locale-audit <directory>          --> blog-locale-audit
/blog flow [find|optimize|win|prompts|sync] --> blog-flow
```

Se nenhum subcomando for fornecido, o orquestrador pergunta qual ação a pessoa
precisa.
