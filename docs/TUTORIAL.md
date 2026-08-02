# Tutorial: do zero ao blog publicado

Passo a passo completo de como montar a programação de um blog e depois produzir
cada postagem. Este documento é didático: cada etapa diz **qual comando rodar**,
**o que esperar de saída** e **qual arquivo de referência** o Claude carrega
naquele momento.

Se você quer apenas a lista seca de comandos, use
[`COMMANDS.md`](COMMANDS.md). Se quer entender a arquitetura por trás,
use [`ARCHITECTURE.md`](ARCHITECTURE.md). Este arquivo é o caminho do meio: a
ordem em que as coisas acontecem na prática.

---

## Como ler este tutorial

O trabalho se divide em duas coisas bem diferentes, e confundi-las é o erro mais
comum de quem começa:

**A programação** é o trabalho de estratégia que você faz uma vez e revisita a
cada trimestre. Define sobre o que o blog fala, com que voz, em que ordem e para
quem. Corresponde às Fases 0 e 1.

**A postagem** é o ciclo que se repete a cada artigo. Corresponde às Fases 2 e 3.

A Fase 4 é manutenção contínua, que só começa a importar quando você já tem
volume publicado.

> **Antes de começar**: instale o plugin conforme
> [`INSTALLATION.md`](INSTALLATION.md) e reinicie o Claude Code. Sem reiniciar,
> os comandos `/blog` não aparecem.

---

## Fase 0: preparar o terreno (uma vez por projeto)

Esta fase existe para que o Claude pare de perguntar as mesmas coisas a cada
invocação. Tudo que você definir aqui vira contexto carregado automaticamente
depois.

### Passo 0.1: definir a marca e a voz

```
/blog brand init
```

Roda uma entrevista curta e grava dois arquivos na raiz do projeto:

| Arquivo | O que guarda |
|---|---|
| `BRAND.md` | Público, posicionamento, regras editoriais, expressões proibidas, diferenciação frente a concorrentes |
| `VOICE.md` | Assinatura de tom, regras lexicais, padrões de título |

A partir daí, **toda** sub-skill de redação, revisão e auditoria carrega esses
arquivos sozinha. Você não precisa repetir "escreva no tom X" nunca mais.

Para conferir ou ajustar depois:

```
/blog brand show
/blog brand update
```

> **Cuidado com privacidade**: se o `BRAND.md` contiver posicionamento
> confidencial e o repositório for público, acrescente-o ao `.gitignore`. Veja
> [`PRIVACY.md`](PRIVACY.md).

> **Se você já tem material de marca**, não rode `init` do zero. Gere a partir
> dos documentos que já existem, senão passam a existir duas fontes de verdade
> divergindo.

### Passo 0.2: ensinar sua voz a partir do que você já escreveu

Se você já tem posts publicados, este passo vale mais que a entrevista:

```
/blog style learn ./posts-antigos/
```

Analisa de 5 a 10 posts e constrói um perfil de voz do autor, que alimenta o
`/blog write` e o `/blog persona`. É a diferença entre o Claude descrever sua
voz e o Claude **imitar** sua voz.

### Passo 0.3: criar personas de escrita (opcional)

```
/blog persona create
/blog persona list
/blog persona use <nome>
/blog persona show <nome>
```

Use quando o blog tem mais de um autor, ou quando o mesmo autor escreve para
públicos diferentes (por exemplo, um tom para iniciantes e outro para
especialistas). As personas ficam em `skills/blog/references/personas/`.

### Passo 0.4: conectar dados do Google (opcional, mas recomendado)

```
/blog google
```

São 13 subcomandos em 4 níveis de credencial, cobrindo PageSpeed Insights, CrUX,
Search Console, GA4, NLP, YouTube e Planejador de Palavras-chave. A configuração
está em [`skills/blog-google/references/auth-setup.md`](../skills/blog-google/references/auth-setup.md).

Sem isso o blog funciona; com isso, as Fases 1 e 4 deixam de ser adivinhação.

---

## Fase 1: montar a programação (uma vez por trimestre)

### Passo 1.1: definir a estratégia

```
/blog strategy "azeite de oliva artesanal"
```

Este é o comando que define **sobre o que o blog fala**. Ele produz um documento
com segmentos de público, pilares de conteúdo, posicionamento competitivo,
canais de distribuição, indicadores e um roadmap de 90 dias.

Referências carregadas: `geo-optimization.md`, `google-landscape-2026.md`.

Rode antes de qualquer outra coisa de planejamento. Um calendário sem estratégia
é só uma lista de ideias soltas.

### Passo 1.2: descobrir o que as pessoas estão realmente dizendo

```
/blog discourse "acidez do azeite"
/blog discourse "acidez do azeite" --days 90
```

Pesquisa Reddit, X, YouTube, Hacker News, dev.to, Medium, GitHub, Stack Overflow
e Substack nos últimos 30 (ou 90) dias, sem precisar de API. Grava um
`DISCOURSE.md` na raiz, carregado automaticamente pelo `/blog write`,
`/blog brief` e `/blog strategy` depois.

Referência: `research-quality.md` (as quatro checagens de armadilha de
palavra-chave rodam antes de qualquer busca).

Para encadear direto na próxima etapa:

```
/blog discourse "acidez do azeite" --feed-into brief
```

Este passo é o que separa um blog que repete o consenso de um que responde a
dúvidas reais.

### Passo 1.3: planejar o cluster de temas

```
/blog cluster plan "azeite extra virgem"
```

Desenha a arquitetura de eixo e raios: uma página pilar ampla mais os artigos de
apoio que apontam para ela. É assim que se constrói autoridade de tema em vez de
posts isolados.

Referências: [`semantic-clustering.md`](../skills/blog-cluster/references/semantic-clustering.md),
[`cluster-architecture.md`](../skills/blog-cluster/references/cluster-architecture.md).

Para executar o cluster inteiro depois de aprovar o plano:

```
/blog cluster execute <caminho-do-plano>
```

### Passo 1.4: transformar em calendário

```
/blog calendar quarterly
/blog calendar monthly
```

Converte a estratégia e o cluster num cronograma real, com tipo de post
(novo ou atualização), palavra-chave alvo, cluster e situação. Inclui a fila de
atualização por atualidade e ganchos sazonais.

### Passo 1.5: checar canibalização antes de escrever

```
/blog cannibalization ./content/blog/
```

Se você já tem posts publicados, rode antes de aprovar o calendário. Detecta
palavras-chave em que dois posts seus competem entre si, com recomendação de
fundir ou diferenciar. É muito mais barato ajustar a pauta agora que despublicar
depois.

**Ao fim da Fase 1** você tem: estratégia escrita, discurso mapeado, cluster
desenhado, calendário com datas e nenhuma sobreposição planejada.

---

## Fase 2: produzir uma postagem

Este é o ciclo que se repete. Vou usar um post de exemplo:
"Como a acidez do azeite indica qualidade".

### Passo 2.1: briefing

```
/blog brief "como a acidez do azeite indica qualidade"
```

Produz o documento de trabalho: palavras-chave (principal, secundárias,
perguntas), análise dos concorrentes que ranqueiam, 8 a 12 estatísticas já
pesquisadas com fonte, plano de elementos visuais, lacunas a explorar e
oportunidades de link interno.

Salva em `briefs/[slug]-brief.md`.

Referências: `content-rules.md`, `geo-optimization.md`.

> **Vale sempre gerar o briefing?** Se o tema é novo para você, sim: a pesquisa
> feita aqui é reaproveitada pelo `/blog write` e economiza uma rodada inteira.
> Se você domina o assunto e já tem os dados, pule direto para o roteiro.

### Passo 2.2: roteiro (alternativa leve ao briefing)

```
/blog outline "como a acidez do azeite indica qualidade"
```

Analisa o que ranqueia hoje e devolve a estrutura de seções, com marcadores de
onde entram imagem e gráfico. É o briefing sem a pesquisa completa.

### Passo 2.3: verificar as estatísticas antes de usar

```
/blog factcheck briefs/acidez-azeite-brief.md
```

Busca as URLs citadas e pontua cada afirmação como correspondência exata,
paráfrase ou não encontrada. Rodar **antes** de escrever é mais barato que
descobrir no Gate 4 que metade dos números não se sustenta.

Para produto regulado (alimento, bebida, saúde, agropecuária) este passo não é
opcional. O revisor bloqueia por alegação regulada sem fonte resolvível,
independentemente da nota.

### Passo 2.4: escrever

```
/blog write "como a acidez do azeite indica qualidade"
/blog write "como a acidez do azeite indica qualidade" --format mdx --words 2000
```

Aqui acontece o trabalho pesado. O orquestrador:

1. Esclarece público, palavra-chave, extensão e plataforma
2. Dispara o agente `blog-researcher` para estatísticas e imagens
3. Apresenta o roteiro para sua aprovação
4. Gera de 2 a 4 gráficos SVG pelo `blog-chart` (capacidade interna, não é comando)
5. Dispara o agente `blog-writer` para o artigo
6. **Roda o contrato de entrega de 5 portões**
7. Salva e apresenta o resumo

Referências: `content-rules.md`, `visual-media.md`, `quality-scoring.md`, mais o
template escolhido automaticamente entre os 12 de `skills/blog/templates/`.

#### O contrato de 5 portões, que roda sozinho

Você não vê o rascunho antes disso passar. É o ponto central do projeto:

| Portão | O que exige | Se falhar |
|---|---|---|
| 1. Descoberta de capacidades | Ferramentas, agentes e dependências conhecidos antes de escrever | Bloqueia |
| 2. Completude de formato | Existem `.md`, `.html`, `.pdf` e uma imagem principal real | Bloqueia |
| 3. Verificação visual | Capturas em 375, 768 e 1280; JSON-LD válido; modo escuro; SVG sem transbordar | Bloqueia |
| 4. Revisão de conteúdo | Nota do `blog-reviewer` em 90 ou mais, com zero P0 | Bloqueia e itera |
| 5. Ativos e links | Imagens resolvem, `og:image` existe, links devolvem 200, contagem bate com o schema | Bloqueia |

O orquestrador itera até 3 vezes em qualquer falha antes de escalar para você.
A especificação completa está em
[`blog-delivery-contract.md`](../skills/blog/references/blog-delivery-contract.md).

**Saída**: uma pasta de artefatos com o markdown, o HTML renderizado, o PDF, o
`hero.<ext>`, as capturas por largura, o `review.md` e o `preflight-report.json`.

### Passo 2.5: gerar ou ajustar imagens

```
/blog image generate "azeite sendo servido, luz natural, editorial"
/blog image edit ./hero.png "recortar em 1200x630"
/blog image setup
```

O `/blog write` já chama a geração de imagem sozinho quando o MCP está
configurado. Use o comando avulso quando quiser uma imagem específica, ou
refazer a que veio.

Referências: [`gemini-models.md`](../skills/blog-image/references/gemini-models.md),
[`prompt-engineering-blog.md`](../skills/blog-image/references/prompt-engineering-blog.md).

Sem configuração de MCP, o fluxo cai para banco de imagens (Pixabay, Unsplash,
Pexels) e continua funcionando.

### Passo 2.6: validar o SEO técnico

```
/blog seo-check content/blog/acidez-azeite.mdx
```

Checa title, meta description, hierarquia de títulos, presença da palavra-chave,
quantidade de links internos, texto alternativo, schema e Open Graph.

Referências: `google-landscape-2026.md`, `schema-stack.md`, `internal-linking.md`.

### Passo 2.7: gerar o schema

```
/blog schema content/blog/acidez-azeite.mdx
```

Produz o JSON-LD: `BlogPosting` sempre, mais `FAQPage`, `BreadcrumbList`,
`Person` e `Organization` quando aplicável.

Referência: `schema-stack.md`.

> Prefira schema no código-fonte ou renderizado no servidor. JSON-LD injetado
> por JavaScript funciona no Google quando chega ao DOM renderizado, mas outros
> rastreadores variam.

### Passo 2.8: auditar a prontidão para citação por IA

```
/blog geo content/blog/acidez-azeite.mdx
```

Verifica se as afirmações importantes se sustentam sozinhas quando extraídas,
se a estrutura favorece a extração, se o `robots.txt` libera GPTBot, ClaudeBot e
PerplexityBot, e se há dependência de JavaScript.

Referências: `geo-optimization.md`, `ai-crawler-guide.md`.

### Passo 2.9: pontuar

```
/blog analyze content/blog/acidez-azeite.mdx
/blog analyze content/blog/acidez-azeite.mdx --lang pt
```

Nota de 0 a 100 em 5 categorias, com recomendações priorizadas.

Referência: `quality-scoring.md`, `editorial-heuristics.md`.

> **Conteúdo em português**: a detecção de idioma é automática por arquivo
> (frontmatter `lang` primeiro, depois palavras funcionais), mas passe
> `--lang pt` explicitamente quando o texto for curto ou misturar idiomas.
> A faixa de legibilidade em português é calibração fundamentada, ainda não
> validada contra posts publicados; trate os 7 pontos de legibilidade como
> indicativos até calibrar `READABILITY_BANDS` com o seu próprio material.

### Passo 2.10: corrigir e repetir

```
/blog rewrite content/blog/acidez-azeite.mdx
```

Aplica as correções automaticamente, preservando sua voz. A reescrita passa pelo
mesmo contrato de 5 portões e precisa pontuar pelo menos tanto quanto o original.

---

## Fase 3: publicar e distribuir

### Passo 3.1: organizar tags e categorias

```
/blog taxonomy suggest
/blog taxonomy sync
/blog taxonomy audit
```

Sincroniza com WordPress, Shopify, Ghost, Strapi e Sanity via API autenticada.

### Passo 3.2: reaproveitar em outras plataformas

```
/blog repurpose content/blog/acidez-azeite.mdx
```

Gera thread para X, post para LinkedIn, publicação para Reddit, roteiro de vídeo
para YouTube, versão para newsletter e roteiro de podcast.

Referência: `distribution-playbook.md`.

### Passo 3.3: gerar a versão em áudio

```
/blog audio generate content/blog/acidez-azeite.mdx
/blog audio voices
/blog audio setup
```

Narração por Gemini TTS, em modo resumo, artigo completo ou diálogo entre dois
locutores. O catálogo de 30 vozes está em
[`voices.md`](../skills/blog-audio/references/voices.md).

### Passo 3.4: publicar em outros idiomas

O caminho de um comando só:

```
/blog multilingual "como a acidez do azeite indica qualidade" --languages en,es,it
```

Escreve, traduz, localiza e emite o hreflang de uma vez.

Se preferir controlar cada etapa:

```
/blog translate content/blog/acidez-azeite.mdx --to en,es
/blog localize content/blog/acidez-azeite.en.mdx --locale en-US
/blog locale-audit ./content/blog/
```

Referências: [`translation-rules.md`](../skills/blog-translate/references/translation-rules.md),
[`cultural-adaptation.md`](../skills/blog-translate/references/cultural-adaptation.md).

O `locale-audit` checa completude, correção de hreflang, paridade de meta tags e
atualidade entre as versões. Rode sempre depois de traduzir.

---

## Fase 4: manter o blog vivo

Esta fase só faz sentido depois de alguns meses publicando.

### Passo 4.1: auditar o site inteiro

```
/blog audit ./content/blog/
```

Pontua todos os posts, ordena do pior para o melhor como fila de prioridade,
mostra médias por categoria, problemas recorrentes e cobertura de temas.

### Passo 4.2: detectar decaimento de tráfego

```
/blog decay gsc-atual.json gsc-anterior.json
```

Compara duas exportações do Search Console e sinaliza posts com queda de 20% ou
mais no trimestre, sugerindo atualizar, consolidar ou podar.

É o comando que diz **em que ordem** mexer no que já existe. Sem ele, você
atualiza por palpite.

### Passo 4.3: atualizar o que decaiu

```
/blog update content/blog/acidez-azeite.mdx
```

Apelido do `rewrite` em modo de atualidade: mexe nos dados e nos sinais,
preserva a estrutura. Só atualiza o `lastUpdated` depois de mudança substantiva.

### Passo 4.4: acompanhar os dados do Google

```
/blog google psi https://seusite.com/blog/acidez-azeite
/blog google gsc
/blog google ga4
```

### Passo 4.5: consultar sua própria base de conhecimento

```
/blog notebooklm "o que os laudos de 2025 dizem sobre acidez"
```

Pesquisa ancorada nos documentos que você subiu ao NotebookLM. Útil quando a
fonte da verdade é interna e não está na web.

### Passo 4.6: usar os prompts do framework FLOW

```
/blog flow find
/blog flow optimize
/blog flow win
/blog flow prompts
/blog flow sync
```

São 30 prompts aplicáveis a blog, organizados em Find, Leverage, Optimize e Win.
Referência: [`flow-framework.md`](../skills/blog-flow/references/flow-framework.md)
e `flow-alignment.md`.

---

## Resumo: os 30 comandos por fase

| Fase | Comando | Quando usar |
|---|---|---|
| 0 | `/blog brand` | Uma vez, no início do projeto |
| 0 | `/blog style` | Uma vez, se você já tem posts publicados |
| 0 | `/blog persona` | Quando há mais de um autor ou público |
| 0 | `/blog google` | Uma vez para configurar; depois na Fase 4 |
| 1 | `/blog strategy` | Uma vez por trimestre |
| 1 | `/blog discourse` | Por tema, antes de decidir a pauta |
| 1 | `/blog cluster` | Uma vez por pilar de conteúdo |
| 1 | `/blog calendar` | Mensal ou trimestral |
| 1 | `/blog cannibalization` | Antes de fechar a pauta |
| 2 | `/blog brief` | Por post, quando o tema é novo para você |
| 2 | `/blog outline` | Por post, alternativa leve ao briefing |
| 2 | `/blog factcheck` | Antes de escrever, e de novo antes de publicar |
| 2 | `/blog write` | O comando central |
| 2 | `/blog image` | Quando quiser imagem específica |
| 2 | `/blog seo-check` | Depois de escrever |
| 2 | `/blog schema` | Depois de escrever |
| 2 | `/blog geo` | Depois de escrever |
| 2 | `/blog analyze` | Depois de escrever, e a cada revisão |
| 2 | `/blog rewrite` | Quando a nota não fecha |
| 3 | `/blog taxonomy` | Ao publicar |
| 3 | `/blog repurpose` | Depois de publicar |
| 3 | `/blog audio` | Depois de publicar |
| 3 | `/blog multilingual` | Quando o post merece outros idiomas |
| 3 | `/blog translate` | Controle manual da tradução |
| 3 | `/blog localize` | Adaptação cultural por localidade |
| 3 | `/blog locale-audit` | Sempre depois de traduzir |
| 4 | `/blog audit` | Mensal |
| 4 | `/blog decay` | Trimestral |
| 4 | `/blog update` | Conforme o decay apontar |
| 4 | `/blog notebooklm` | Quando a fonte é interna |
| 4 | `/blog flow` | Quando precisar de um ângulo novo |

Capacidade interna, sem comando próprio: o `blog-chart` gera os gráficos SVG
dentro do `/blog write` e do `/blog rewrite`.

---

## As 22 referências e quando cada uma entra

O Claude carrega estes arquivos sob demanda, nunca todos de uma vez. Saber quais
existem ajuda a entender por que uma recomendação apareceu.

| Referência | Assunto |
|---|---|
| `ai-crawler-guide.md` | Acesso de GPTBot, ClaudeBot e PerplexityBot |
| `ai-slop-detection.md` | Revisão de padrão editorial em dois níveis |
| `blog-delivery-contract.md` | Especificação dos 5 portões |
| `cognitive-load.md` | Densidade de conceitos por seção |
| `content-rules.md` | Regras de escrita e estrutura |
| `content-templates.md` | Catálogo comentado dos 12 templates |
| `cta-placement.md` | Onde entram as chamadas para ação |
| `distribution-playbook.md` | Canais e táticas de distribuição |
| `editorial-heuristics.md` | Rubrica de 0 a 4 com severidade P0 a P3 |
| `eeat-signals.md` | Experiência, especialização, autoridade, confiança |
| `flow-alignment.md` | Ligação com o framework FLOW |
| `geo-optimization.md` | Otimização para citação por IA |
| `google-landscape-2026.md` | Core e spam updates, política atual |
| `internal-linking.md` | Estratégia de link interno |
| `orchestration-details.md` | Detalhes de roteamento do orquestrador |
| `platform-guides.md` | Next.js, Hugo, Jekyll, WordPress, Ghost e outros |
| `quality-scoring.md` | As 5 categorias e os 100 pontos |
| `research-quality.md` | Níveis de fonte, atualidade, armadilhas de tema |
| `schema-stack.md` | JSON-LD e dados estruturados |
| `synthesis-contract.md` | LEIS de síntese para saída segura quanto a citações |
| `video-embeds.md` | Critérios de incorporação de vídeo |
| `visual-media.md` | Imagens, gráficos e texto alternativo |

Referências específicas de sub-skill ficam em `skills/blog-<nome>/references/`,
como as de cluster, tradução, imagem, áudio, Google, NotebookLM e FLOW.

---

## Os 12 templates e quando cada um é escolhido

O `/blog write` escolhe sozinho pelo tema, mas você pode forçar:

```
/blog write listicle: "7 azeites brasileiros premiados em 2026"
/blog write --type comparison "arbequina versus koroneiki"
```

| Template | Sinal que dispara |
|---|---|
| `how-to-guide.md` | "Como fazer", "Guia de" |
| `listicle.md` | Número no título |
| `case-study.md` | Nome de empresa mais "resultados" |
| `comparison.md` | "X versus Y", "comparado" |
| `pillar-page.md` | Tema amplo, "guia completo" |
| `product-review.md` | "Análise", "testado" |
| `thought-leadership.md` | Tendência, previsão, opinião |
| `roundup.md` | Citações de especialistas |
| `tutorial.md` | "Tutorial", "passo a passo" |
| `news-analysis.md` | Evento, atualização, anúncio |
| `data-research.md` | Enquete, estudo, dados próprios |
| `faq-knowledge.md` | "Perguntas frequentes", "dúvidas sobre" |

Detalhe de cada um em [`TEMPLATES.md`](TEMPLATES.md).

---

## Erros comuns de quem está começando

**Pular a Fase 0 e ir direto para `/blog write`.** Funciona, mas o Claude vai
perguntar sobre público e tom a cada post, e as respostas não se acumulam. Vinte
minutos no `/blog brand init` economizam horas depois.

**Tratar o `/blog analyze` como o portão.** O analyze é diagnóstico. Quem bloqueia
é o Gate 4 dentro do `/blog write`, que exige 90 e zero P0. Um post com 78 no
analyze nunca chegou a ser entregue.

**Rodar `/blog factcheck` só no fim.** Descobrir que a estatística central não se
sustenta depois de escrever 2.000 palavras em volta dela custa a reescrita
inteira.

**Traduzir sem rodar `/blog locale-audit`.** Hreflang errado ou meta tag faltando
numa versão derruba o conjunto todo, e o erro é invisível na leitura.

**Ignorar o `/blog decay` e atualizar por palpite.** O post que *parece* velho
raramente é o que está perdendo tráfego.

**Esperar nota alta em português sem calibrar a faixa.** A faixa de legibilidade
pt ainda não foi validada. Rode o analisador sobre uma dúzia de posts seus já
publicados, olhe os valores crus de `flesch_reading_ease` e aperte
`READABILITY_BANDS` antes de tratar os 7 pontos como verdade.

---

## Para onde ir agora

- Lista completa de comandos e argumentos: [`COMMANDS.md`](COMMANDS.md)
- Como o sistema é montado por dentro: [`ARCHITECTURE.md`](ARCHITECTURE.md)
- Estrutura de cada template: [`TEMPLATES.md`](TEMPLATES.md)
- Quando algo não funciona: [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md)
- Servidores MCP opcionais: [`MCP-INTEGRATION.md`](MCP-INTEGRATION.md)
- Exemplo completo de ponta a ponta: [`DEMO.md`](DEMO.md)
