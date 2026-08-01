# Templates de Conteúdo

Guia de referência dos 12 templates por tipo de conteúdo incluídos no
`claude-blog`. Os templates dão a planta estrutural de cada tipo de artigo,
garantindo qualidade e otimização consistentes em todo o conteúdo.

---

## Visão geral dos templates

| Template | Tipo de conteúdo | Extensão alvo | Melhor para |
|----------|------------------|---------------|-------------|
| how-to-guide.md | Guia prático | 2.000-2.500 | Tutoriais passo a passo, guias de processo |
| listicle.md | Lista | 1.500-2.000 | Listas ranqueadas, coleções curadas |
| case-study.md | Estudo de caso | 2.000-3.000 | Resultados de cliente, retrospectivas de projeto |
| comparison.md | Comparação | 1.500-2.000 | X versus Y, avaliação de ferramentas |
| pillar-page.md | Página pilar | 3.000-4.000 | Guias abrangentes de tema |
| product-review.md | Análise de produto | 1.500-2.500 | Análises de ferramenta, avaliação de software |
| thought-leadership.md | Artigo de opinião | 2.000-3.000 | Análise de setor, peças opinativas |
| roundup.md | Compilação de especialistas | 2.000-2.500 | Coleções multifonte, relatórios de tendência |
| tutorial.md | Tutorial | 2.500-3.500 | Passo a passo de código, demonstrações técnicas |
| news-analysis.md | Análise de notícia | 800-1.500 | Atualizações do setor, mudanças de algoritmo |
| data-research.md | Dados e pesquisa | 2.500-3.500 | Pesquisa própria, resultados de enquete |
| faq-knowledge.md | Perguntas frequentes / base de conhecimento | 1.500-2.000 | Conteúdo de referência, coleções de perguntas |

---

## Como os templates funcionam

Templates são plantas estruturais, não formulários de preencher lacunas. Cada um
define:

1. **Estrutura de seções**: o esqueleto de H2 e H3 do tipo de conteúdo
2. **Pedidos de resposta antecipada**: orientação para abrir cada seção com dado
3. **Pedidos de cobertura**: completude dependente da intenção, sem enchimento
4. **Marcadores de ganho de informação**: onde dado próprio ou perspectiva singular é necessário
5. **Posicionamento de elementos visuais**: onde gráficos e imagens devem aparecer
6. **Zona opcional de perguntas**: onde cabem dúvidas reais ainda não respondidas
7. **Zonas de link**: onde links internos e externos ficam mais naturais

---

## Anatomia da estrutura de um template

Todo template segue uma estrutura interna consistente:

```
# [Nome do template]

## Metadados
- Tipo de conteúdo: [tipo]
- Extensão: [faixa]
- Seções H2: [quantidade]
- Gráficos: [quantidade]
- Imagens: [quantidade]
- Perguntas opcionais: [quantidade conforme a necessidade do leitor]

## Estrutura de seções

### Frontmatter
[Campos obrigatórios para este tipo de conteúdo]

### Introdução (100 a 150 palavras)
- Gancho: [tipo de gancho que funciona melhor]
- Problema ou oportunidade: [orientação de enquadramento]
- Promessa: [o que o leitor aprende]

### H2: [Padrão da seção] (extensão)
ANSWER-FIRST: [orientação para o parágrafo de abertura com dado]
CONTENT: [o que cobrir no corpo]
INFO-GAIN: [onde a perspectiva singular é necessária]
VISUAL: [tipo de gráfico ou sugestão de imagem]

[... seções H2 adicionais ...]

### Zona opcional de perguntas (quantidade conforme a necessidade)
[Orientação de perguntas visíveis específica deste tipo de conteúdo; omita quando
for repetir o artigo. A presença de perguntas não rende pontuação.]

### Conclusão (100 a 150 palavras)
[Padrão de fechamento deste tipo de conteúdo]

## Notas de otimização
[Dicas de SEO e GEO específicas do tipo de conteúdo]
```

### Marcadores de seção

Os marcadores permanecem em inglês: são lidos pelo `blog-writer`, não são prosa.

| Marcador | Finalidade |
|----------|------------|
| `ANSWER-FIRST:` | Orientação para declarar o ponto da seção cedo e sustentar as afirmações relevantes; sem extensão fixa nem cota de estatística |
| `CONTENT:` | Que temas e subtemas cobrir no corpo da seção |
| `INFO-GAIN:` | Onde dado próprio, experiência direta ou perspectiva singular é necessário |
| `VISUAL:` | Tipo de gráfico recomendado ou posicionamento de imagem |
| `FAQ-ZONE:` | Onde uma seção opcional de perguntas visíveis pode entrar, quando a necessidade do leitor justificar |
| `LINK-ZONE:` | Lugares naturais para links internos ou externos |

---

## Como o /blog write escolhe o template

Quando o `/blog write` é invocado, o orquestrador escolhe um template com base em:

### 1. Pedido explícito do usuário

Se a pessoa especifica um tipo de conteúdo, aquele template é usado diretamente:

```
/blog write "10 Melhores Ferramentas de CI/CD para 2026"   --> listicle.md
/blog write "Como Configurar Monitoramento no Kubernetes"  --> how-to-guide.md
/blog write estudo de caso: migração da Acme Corp          --> case-study.md
```

### 2. Análise do tema

Se nenhum tipo for especificado, o orquestrador analisa o tema:

| Sinal do tema | Template escolhido |
|---------------|--------------------|
| "Como fazer...", "Guia de..." | how-to-guide.md |
| Números no título ("10 Melhores...", "7 Formas...") | listicle.md |
| "X versus Y", "comparado", "alternativa" | comparison.md |
| "Análise", "testado", "na prática" | product-review.md |
| Nome de empresa ou projeto mais "resultados" | case-study.md |
| Tema amplo, "guia completo", "tudo sobre" | pillar-page.md |
| "Tutorial", "passo a passo" | tutorial.md |
| Evento de notícia, atualização, anúncio | news-analysis.md |
| Enquete, estudo, dados, pesquisa | data-research.md |
| "Perguntas frequentes", "dúvidas sobre" | faq-knowledge.md |
| Tendência do setor, previsão, opinião | thought-leadership.md |
| Citações de especialistas, coleção, compilação | roundup.md |

### 3. Padrão

Se o tema for ambíguo, o orquestrador recorre ao `how-to-guide.md`, o template
mais versátil, e confirma com o usuário.

---

## Detalhes de cada template

### how-to-guide.md

Melhor para guias passo a passo em que o leitor quer realizar algo.

```
Estrutura:
  Introdução (gancho com dado de dificuldade ou tempo)
  H2: Por que isso importa (contexto e dados)
  H2: Pré-requisitos / o que você precisa
  H2: Passo 1 - [Ação] (resposta antecipada com taxa de sucesso)
  H2: Passo 2 - [Ação]
  H2: Passo 3 - [Ação]
  H2: Erros comuns a evitar
  H2: Perguntas opcionais (quantidade conforme a necessidade)
  Conclusão (principais conclusões e próximo passo)

Visuais: fluxograma de processo, gráfico comparativo antes e depois
Imagens: capturas de tela ou banco de imagens para cada passo importante
```

### listicle.md

Melhor para listas ranqueadas, coleções de ferramentas e recomendações curadas.

```
Estrutura:
  Introdução (gancho com o total de itens)
  H2: [Item 1] - [Diferencial central]
  H2: [Item 2] - [Diferencial central]
  ... (5 a 15 itens, conforme a profundidade)
  H2: Como avaliamos [categoria]
  H2: Perguntas opcionais (quantidade conforme a necessidade)
  Conclusão (escolha principal e tabela comparativa)

Visuais: gráfico de barras comparativo, gráfico de rosca de participação
Imagens: logo ou captura por item, ou imagem comparativa agrupada
```

### case-study.md

Melhor para mostrar resultados reais com métricas específicas.

```
Estrutura:
  Introdução (dado do resultado principal)
  H2: O desafio
  H2: A abordagem / solução
  H2: Detalhes da implementação
  H2: Resultados (métricas e linha do tempo)
  H2: Principais conclusões
  H2: Perguntas opcionais (quantidade conforme a necessidade)
  Conclusão (chamada para saber mais)

Visuais: gráfico de barras antes e depois, linha do tempo ou gráfico de linhas
Imagens: capturas de tela, painéis, fotos de equipe ou processo
Ganho de informação: métricas reais do projeto (crítico)
```

### comparison.md

Melhor para avaliações X versus Y e comparação de ferramentas.

```
Estrutura:
  Introdução (dado de contexto de mercado)
  H2: Tabela comparativa rápida
  H2: Panorama do [Produto A]
  H2: Panorama do [Produto B]
  H2: Comparação funcionalidade a funcionalidade
  H2: Comparação de preços
  H2: Qual você deve escolher?
  H2: Perguntas opcionais (quantidade conforme a necessidade)
  Conclusão (matriz de recomendação)

Visuais: gráfico radar de funcionalidades, gráfico de barras de preço
Imagens: capturas do produto, comparações de interface
```

### pillar-page.md

Melhor para guias abrangentes que servem de eixo para clusters de temas.

```
Estrutura:
  Introdução (escopo e dado de autoridade)
  H2: O que é [Tema]? (definição e contexto)
  H2: Por que [Tema] importa em 2026
  H2: [Subtema central 1] (cobertura detalhada)
  H2: [Subtema central 2]
  H2: [Subtema central 3]
  H2: [Subtema central 4]
  H2: [Tema avançado]
  H2: Ferramentas e recursos
  H2: Perguntas opcionais (quantidade conforme a necessidade)
  Conclusão (trilha de aprendizado e próximos passos)

Visuais: 3 a 4 gráficos (tipos variados), diagrama panorâmico do tema
Imagens: 5 ou mais distribuídas ao longo do texto
Links: link building interno pesado para as páginas de apoio do cluster
```

### product-review.md

Melhor para análises práticas de ferramenta com resultados reais de teste.

```
Estrutura:
  Introdução (dado do veredito, por exemplo nota de desempenho)
  H2: Veredito rápido
  H2: O que é o [Produto]?
  H2: Instalação e primeiras impressões
  H2: Funcionalidades testadas
  H2: Resultados de desempenho
  H2: Preço e custo-benefício
  H2: Prós e contras
  H2: Para quem serve?
  H2: Perguntas opcionais (quantidade conforme a necessidade)
  Conclusão (nota final e recomendação)

Visuais: gráfico de benchmark de desempenho, comparação de preços
Imagens: capturas do teste real (crítico para E-E-A-T)
Ganho de informação: dados de teste em primeira mão (precisa demonstrar experiência)
```

### thought-leadership.md

Melhor para análise de setor e peças opinativas voltadas ao futuro.

```
Estrutura:
  Introdução (dado de tendência que monta o palco)
  H2: O cenário atual
  H2: O que está mudando (análise e dados)
  H2: Por que isso importa
  H2: Evidência e interpretação (perspectiva própria comprovada quando
      fornecida, senão análise diferenciada com fonte)
  H2: O que fazer a respeito (conselho acionável)
  H2: Olhando adiante (previsões)
  H2: Perguntas opcionais (quantidade conforme a necessidade)
  Conclusão (tese central e chamada para ação)

Visuais: gráfico de linha de tendência, gráfico de virada de mercado
Ganho de informação: perspectiva pessoal comprovada quando disponível, ou
síntese diferenciada com fonte e análise claramente enquadrada
```

### roundup.md

Melhor para reunir percepções de várias fontes ou especialistas.

```
Estrutura:
  Introdução (tema e dado da quantidade de fontes)
  H2: Achado principal 1 (síntese de várias fontes)
  H2: Achado principal 2
  H2: Achado principal 3
  H2: Perspectivas dos especialistas
  H2: O que isso significa para [público]
  H2: Perguntas opcionais (quantidade conforme a necessidade)
  Conclusão (síntese e itens de ação)

Visuais: gráfico comparativo multifonte, agregação de tendência
```

### tutorial.md

Melhor para passo a passo técnico com exemplos de código.

```
Estrutura:
  Introdução (o que você vai construir e a pilha tecnológica)
  H2: Pré-requisitos e configuração
  H2: Passo 1 - [Fundação]
  H2: Passo 2 - [Funcionalidade central]
  H2: Passo 3 - [Integração]
  H2: Passo 4 - [Teste e publicação]
  H2: Solução de problemas comuns
  H2: Perguntas opcionais (quantidade conforme a necessidade)
  Conclusão (link do repositório completo e extensões)

Visuais: diagrama de arquitetura (SVG), gráfico de desempenho
Imagens: capturas de terminal, resultados na interface
Especial: blocos de código com destaque de sintaxe ao longo de todo o texto
```

### news-analysis.md

Melhor para comentário oportuno sobre eventos e atualizações do setor.

```
Estrutura:
  Introdução (a notícia e o dado de impacto)
  H2: O que aconteceu
  H2: Por que importa
  H2: Quem é afetado
  H2: O que fazer agora (ações imediatas)
  H2: Perguntas opcionais (quantidade conforme a necessidade)
  Conclusão (perspectiva)

Visuais: 1 a 2 gráficos (visualização de impacto)
Observação: formato mais curto (800 a 1.500 palavras), velocidade importa
```

### data-research.md

Melhor para pesquisa própria, enquetes e análise de dados.

```
Estrutura:
  Introdução (achado principal)
  H2: Metodologia
  H2: Achado principal 1 (dados e análise)
  H2: Achado principal 2
  H2: Achado principal 3
  H2: Implicações
  H2: Limitações
  H2: Perguntas opcionais (quantidade conforme a necessidade)
  Conclusão (resumo dos achados e acesso aos dados)

Visuais: 3 a 4 gráficos (as visualizações são o centro)
Ganho de informação: o dado próprio é toda a proposta de valor
```

### faq-knowledge.md

Melhor para conteúdo abrangente de referência em perguntas e respostas.

```
Estrutura:
  Introdução (escopo do tema e dado sobre as dúvidas comuns)
  H2: Perguntas de [Categoria 1]
    H3: Pergunta 1? (resposta concisa e completa, com respaldo onde necessário)
    H3: Pergunta 2?
  H2: Perguntas de [Categoria 2]
    H3: Pergunta 3?
    H3: Pergunta 4?
  H2: Perguntas de [Categoria 3]
  Conclusão (recursos adicionais)

Visuais: 1 a 2 gráficos de resumo
Especial: use estatísticas apenas quando relevantes, verificadas e úteis
Schema: FAQPage é marcação opcional de conteúdo visível, sem ganho na nota de prontidão
```

---

## Como personalizar templates

### Modificar um template existente

1. Vá até `~/.claude/skills/blog/templates/`
2. Abra o arquivo de template que quer alterar
3. Ajuste a estrutura de seções, as extensões ou a orientação
4. As mudanças valem de imediato (não precisa reiniciar)

### Criar um template novo

1. Copie um template existente como ponto de partida:
   ```bash
   cp ~/.claude/skills/blog/templates/how-to-guide.md \
      ~/.claude/skills/blog/templates/meu-tipo-personalizado.md
   ```
2. Defina a estrutura de seções do seu tipo de conteúdo
3. Acrescente os marcadores `ANSWER-FIRST:`, `VISUAL:` e `INFO-GAIN:`
4. Defina metas de extensão adequadas
5. Acrescente uma entrada de sinal de tema na lógica de seleção de template

### Boas práticas de template

- Mantenha cada seção focada em um único assunto
- Coloque os marcadores `VISUAL:` onde os dados naturalmente sustentam um gráfico
- Use os marcadores `INFO-GAIN:` com generosidade: são essas as seções que
  diferenciam seu conteúdo do consenso gerado por IA
- Defina extensões realistas, compatíveis com a profundidade natural do tipo de conteúdo
- Inclua uma zona de perguntas só quando dúvidas reais de leitor justificarem; mantenha uma conclusão quando o tipo de conteúdo se beneficiar dela

---

## Integração entre template e pontuação

Os templates guiam a criação; o sistema de pontuação valida o resultado.
O mapeamento entre recursos do template e categorias de pontuação:

| Recurso do template | Categoria de pontuação | Pontos em jogo |
|---------------------|------------------------|----------------|
| Estrutura de seções | Schema e estrutura | 10 |
| Marcadores orientados ao propósito | Aderência ao propósito e utilidade ao leitor | 20 |
| Posicionamento visual | Elementos visuais | 15 |
| Zona opcional de perguntas | Só utilidade ao leitor; sem efeito na nota de Google ou IA | 0 |
| Marcadores de ganho de informação | Qualidade de conteúdo | 25 |
| Orientação de citação | Estatísticas e citações | 20 |

Um template bem seguido produz naturalmente conteúdo com nota 75 ou mais, sem
passagens adicionais de otimização.
