# Template: Pesquisa de Dados (estudo com dados próprios)

**ID do template:** data-research
**Extensão alvo:** 2.000 a 3.000 palavras
**Tipo de conteúdo:** estudo com dados próprios, visualizações e achados acionáveis
**Intenção de busca principal:** informacional ("estudo", "dados", "estatísticas", "pesquisa", "benchmark")

## Quando usar este template

Use quando:
- Você tem dados próprios de pesquisas, experimentos, análise de ferramentas ou fontes proprietárias
- O estudo revela achados que confrontam suposições ou preenchem lacunas de conhecimento
- Você consegue apresentar números, percentuais e comparações específicos
- As consultas de busca incluem "estatísticas", "dados", "estudo", "pesquisa", "benchmark", "quantos"
- Os dados são singulares o bastante para outros sites quererem citá-los (potencial de links)

NÃO use para:
- Instruções passo a passo (use tutorial)
- Comentário de evento recente (use news-analysis)
- Conteúdo de referência ou perguntas frequentes (use faq-knowledge)
- Análise inteiramente baseada em dados de terceiros (escreva um news-analysis)

**Nota sobre valor:** pesquisa própria pode ser útil quando metodologia, evidência,
limitações e resultados são transparentes. O template em si não garante
ranqueamento, links nem citação por IA.

---

## Formato do título

```
[Título do Estudo]: Analisamos [N] [Coisas] - Principais Achados
```

**Exemplos:**
- "Estudo de Revisão de Código por IA: Achados de 10.000 Pull Requests"
- "Benchmark de SEO para Blogs: Lições de 500 Blogs Técnicos"
- "Pesquisa de Ferramentas de Desenvolvimento: O Que 2.000 Engenheiros Relataram"

**Regras do título:**
- Inclua o tamanho específico da amostra (N): é o seu sinal de credibilidade
- Nomeie o que foi analisado (pull requests, blogs, engenheiros)
- "Analisamos/Estudamos/Pesquisamos" estabelece pesquisa própria
- Use uma promessa específica de achado em vez de formulação genérica de revelação
- Fique abaixo de 70 caracteres para exibição no resultado de busca, quando possível

**Formatos alternativos de título:**
- "[N] [Coisas] Analisadas: [Achado Central] (Estudo [Ano])"
- "O Estado de [Tema]: Análise de [N] [Unidades]"
- "[Tema] em Números: O Que Revelam [N] [Coisas]"

---

## Estrutura seção a seção

---

### Caixa de resumo, opcional

[ANSWER-FIRST] Resuma os achados mais importantes para o leitor. Inclua números
apenas onde estiverem verificados e forem necessários para entender o resultado.
Use o espaço que a completude exigir, sem encher linguiça.

```markdown
> **Em resumo:** analisamos [N] [coisas] e encontramos [Achado 1 com número específico].
> [Achado 2 com número específico]. O mais surpreendente: [Achado 3 com número específico].
> [Implicação para o leitor em uma frase].
```

**Regras:**
- Declare com clareza o resultado principal e a implicação prática.
- Mantenha o contexto de metodologia ou limitação quando a omissão puder enganar.
- Não force número, enquadramento de surpresa nem quantidade fixa de achados.
- Não faça previsão de desempenho de citação.

---

### Principais achados (200 a 300 palavras)

[ANSWER-FIRST] Apresente os achados de destaque comprovados como marcadores úteis.
Cada marcador precisa manter contexto suficiente para não induzir a erro quando
reaproveitado; não vale quantidade fixa nem previsão de citação.

```markdown
## Principais achados

[ANSWER-FIRST] Nossa análise de [N] [coisas] ao longo de [período] revelou [N] padrões centrais.

[VISUAL: horizontal-bar chart com os 5 a 7 principais achados ordenados por magnitude ou importância]

1. **[Achado como estatística]:** [Uma frase de contexto]. ([N]% da [amostra])
2. **[Achado como estatística]:** [Uma frase de contexto]. ([N]% da [amostra])
3. **[Achado como estatística]:** [Uma frase de contexto]. ([N]% da [amostra])
4. **[Achado como estatística]:** [Uma frase de contexto]. ([N]% da [amostra])
5. **[Achado como estatística]:** [Uma frase de contexto]. ([N]% da [amostra])
6. **[Achado como estatística]:** [Uma frase de contexto]. ([N]% da [amostra])
7. **[Achado como estatística]:** [Uma frase de contexto]. ([N]% da [amostra])
```

**Regras:**
- Cada marcador precisa ser autossuficiente, citável fora de contexto
- Destaque o dado em negrito e siga com uma frase de contexto
- Ordene por magnitude de impacto ou surpresa, não pela ordem do estudo
- Coloque o gráfico logo de início: o leitor quer primeiro o panorama

---

### Metodologia (200 a 300 palavras)

[ANSWER-FIRST] Declare exatamente o que você estudou, como estudou e por que o leitor deve confiar nos resultados.

```markdown
## Metodologia

[ANSWER-FIRST] Analisamos [N] [coisas] coletadas de [fonte] entre [data inicial] e [data final] usando [abordagem de análise].

### Fonte dos dados

[De onde vieram os dados, como foram coletados, critérios de seleção]

[INFO-GAIN: fonte de dados proprietária ou método de coleta singular, documentado
o bastante para o leitor avaliar e, quando possível, reproduzir o trabalho]

### Amostra

| Parâmetro | Valor |
|-----------|-------|
| Tamanho da amostra | [N] |
| Período | [Início] a [Fim] |
| Fonte | [Origem] |
| Critério de seleção | [Como os itens foram escolhidos] |
| Exclusões | [O que foi filtrado e por quê] |

### Abordagem de análise

[1 a 2 parágrafos sobre como os dados foram analisados: ferramentas usadas, métodos estatísticos, abordagem de categorização]

### Limitações

- [Limitação 1]: [Como pode afetar os achados]
- [Limitação 2]: [Como pode afetar os achados]
- [Limitação 3]: [Como pode afetar os achados]
```

**Regras:**
- Seja transparente sobre as limitações: isso constrói credibilidade
- O [INFO-GAIN] aqui é sua fonte ou método singular de dados
- Inclua detalhe suficiente para outro pesquisador avaliar (não necessariamente reproduzir) o estudo
- Declare os critérios de exclusão explicitamente: o leitor vai perguntar sobre viés de seleção

**Procedência das afirmações:**

Dê a cada estatística contexto e detalhe de fonte suficientes para identificá-la,
verificá-la e interpretá-la. Detalhes relevantes podem incluir o publicador ou
título do relatório, data de publicação ou período do estudo, metodologia e
limitações, uma URL estável e a data de consulta para material mutável ou sem
data. Não se exige um formato fixo de citação. Descarte estatísticas não
verificáveis e substitua as contraditas por alternativas verificadas. Referência:
`skills/blog/references/flow-alignment.md`.

---

### Seções de achado (300 a 400 palavras cada, 4 achados)

Cada achado usa um H2 alinhado à intenção. Perguntas e achados declarativos são
igualmente válidos. Siga esta estrutura em cada um:

```markdown
## [Achado como pergunta]?

[ANSWER-FIRST] [Declare o achado como estatística específica já na frase de abertura. Por exemplo, "78% dos blogs técnicos que ranqueiam na primeira página usam..."]

[2 a 3 parágrafos de análise detalhada:]

**Os dados:**

[VISUAL: gráfico adequado ao achado; varie os tipos entre os achados]

Tipos de gráfico sugeridos por achado:
- Achado 1: barras horizontais (comparação)
- Achado 2: linhas (tendência ao longo do tempo)
- Achado 3: dispersão (correlação)
- Achado 4: barras empilhadas (composição)

**O que isso significa:** [Interpretação dos dados: que padrão isso revela?]

**Como se compara:** [Comparação com benchmarks do setor, pesquisas anteriores ou senso comum]

| Este estudo | Benchmark do setor | Diferença |
|-------------|--------------------|-----------|
| [Nosso achado] | [Benchmark] | [Variação] |

[STAT: dado de apoio de fonte externa que valide ou contraste com o achado]

**Implicação prática:** [O que o leitor deve fazer diferente a partir deste achado?]

[INTERNAL-LINK: link para conteúdo que ajude o leitor a agir sobre este achado]
```

**Regras das seções de achado:**
- Comece sempre pelo dado: nunca enterre a informação principal
- Cada achado precisa da própria visualização (varie os tipos de gráfico)
- Compare a um benchmark ou pesquisa anterior para dar contexto
- Termine com a implicação prática: o "e daí?" para o leitor
- Varie os tipos de gráfico entre os achados: não use o mesmo 4 vezes

---

### Surpresas e pontos fora da curva (150 a 200 palavras)

[ANSWER-FIRST] Destaque achados inesperados ou que confrontem suposições comuns. Esta seção constrói credibilidade: mostra que você seguiu os dados em vez de confirmar uma narrativa.

```markdown
## Surpresas e pontos fora da curva

[ANSWER-FIRST] [N] achados contrariaram nossas hipóteses iniciais ou o senso comum.

**Surpresa 1: [Achado contraintuitivo]**
Esperávamos [resultado esperado], mas os dados mostraram [resultado real]. [Explicação breve de por que isso pode ocorrer].

**Surpresa 2: [Ponto fora da curva ou anomalia]**
[Descrição do ponto fora da curva e do que ele pode indicar]

[INFO-GAIN: reflexão honesta sobre o que foi inesperado; isso demonstra rigor intelectual e torna o estudo mais confiável]

> **O que isso nos diz:** [Meta-percepção de 1 a 2 frases sobre o que as surpresas revelam]
```

**Regras:**
- Inclua ao menos 2 surpresas ou pontos fora da curva
- Seja honesto sobre o que contrariou as expectativas
- Ofereça uma hipótese para a surpresa, mas sinalize que é especulação
- Esta seção costuma ser a parte mais compartilhada de um estudo de dados

---

### Limitações e pesquisa futura (100 a 150 palavras)

[ANSWER-FIRST] Reconheça o que o estudo não cobre e que perguntas seguem abertas.

```markdown
## Limitações e pesquisa futura

[ANSWER-FIRST] Este estudo tem [N] limitações centrais que o leitor deve considerar ao aplicar os achados.

**O que este estudo não cobre:**
- [Limitação 1]: [Explicação breve]
- [Limitação 2]: [Explicação breve]

**Perguntas abertas para pesquisa futura:**
- [Pergunta 1]
- [Pergunta 2]
- [Pergunta 3]

[STAT: se aplicável, cite um estudo relacionado que trate uma dessas lacunas]
```

**Regras:**
- Esta seção constrói confiança: seja genuinamente transparente
- Separe limitações (o que enfraquece os achados) de fronteiras de escopo (o que estava fora da intenção do estudo)
- Sugira direções específicas de pesquisa futura (talvez você escreva esses desdobramentos)

---

### Implicações e recomendações (200 a 300 palavras)

[ANSWER-FIRST] Traduza os achados em recomendações específicas e acionáveis.

```markdown
## Implicações e recomendações

[ANSWER-FIRST] Com base nos nossos achados, [público] deveria [recomendação de maior prioridade].

### Para [Segmento de público 1]:

1. **[Recomendação]:** com base em [Achado], [ação específica]. [Impacto esperado].
2. **[Recomendação]:** com base em [Achado], [ação específica]. [Impacto esperado].

### Para [Segmento de público 2]:

1. **[Recomendação]:** com base em [Achado], [ação específica]. [Impacto esperado].
2. **[Recomendação]:** com base em [Achado], [ação específica]. [Impacto esperado].

[INTERNAL-LINK: link para tutorial ou guia que ajude a implementar estas recomendações]

[VISUAL: infográfico de resumo ou matriz de decisão, se aplicável]
```

**Regras:**
- Amarre cada recomendação diretamente a um achado específico (cite-o)
- Seja específico o bastante para o leitor agir
- Segmente as recomendações por público, se o estudo tiver alcance amplo
- Inclua o impacto esperado quando possível

---

### Perguntas do leitor, opcionais (quantidade conforme a necessidade)

[ANSWER-FIRST] em cada pergunta. Antecipe dúvidas sobre metodologia, aplicabilidade e achados específicos.

```markdown
## Perguntas frequentes

### Como estes dados foram coletados?

[ANSWER-FIRST] [Resposta direta em 1 a 2 frases]. Veja a seção [Metodologia](#metodologia) para os detalhes completos.

### Isso se aplica a [público/contexto específico]?

[ANSWER-FIRST] [Resposta direta com esclarecimento de escopo]. [Ressalvas].

### Como isso se compara a [estudo anterior/benchmark do setor]?

[ANSWER-FIRST] [Comparação direta com números específicos]. [Diferença central explicada].

[STAT: dado comparativo]

### Posso citar esta pesquisa?

[ANSWER-FIRST] Sim. Cite como: [Seu nome/organização], "[Título do estudo]", [Nome da publicação], [Data]. [Link para esta página].

### Quando estes dados serão atualizados?

[ANSWER-FIRST] [Resposta direta com prazo ou condições de atualização].
```

**Regras das perguntas frequentes:**
- Inclua uma pergunta de metodologia (a dúvida mais comum do leitor)
- Inclua uma pergunta de escopo e aplicabilidade
- Inclua uma pergunta sobre citação (incentiva links de volta)
- As respostas devem ser concisas e completas; o Google não exige extensão mínima

---

### Apêndice de dados

```markdown
## Apêndice de dados

### Tabela-resumo dos dados

| [Categoria] | [Métrica 1] | [Métrica 2] | [Métrica 3] |
|-------------|-------------|-------------|-------------|
| [Linha 1] | [Valor] | [Valor] | [Valor] |
| [Linha 2] | [Valor] | [Valor] | [Valor] |
| [Linha 3] | [Valor] | [Valor] | [Valor] |
| ... | ... | ... | ... |

**Baixar os dados brutos:** [Link para CSV ou planilha, se aplicável]

**Formato de citação:**
> [Seu nome/organização]. "[Título do estudo]." [Nome da publicação], [Data]. [URL].
```

**Regras:**
- Inclua no mínimo uma tabela-resumo
- Ofereça download dos dados brutos, se possível (aumenta o potencial de links)
- Forneça um formato de citação (facilita a referência por terceiros)
- Coloque a data em destaque (estudos de dados têm prazo de validade)

---

## Lista de verificação de conteúdo

Antes de publicar, confirme:

- [ ] O título traz o tamanho específico da amostra (N)
- [ ] O resumo opcional descreve com precisão o resultado e as limitações relevantes
- [ ] Os principais achados trazem o que o leitor precisa, com respaldo
- [ ] A metodologia inclui tamanho da amostra, período, fonte e limitações
- [ ] Ao menos 1 [INFO-GAIN] na metodologia (dado ou método proprietário)
- [ ] 4 seções de achado, cada uma com um tipo de gráfico diferente
- [ ] Todo achado abre com um dado específico (resposta antecipada)
- [ ] Todo achado inclui comparação com benchmark
- [ ] Todo achado termina com uma implicação prática
- [ ] Ao menos 4 marcadores [VISUAL] com tipos variados de gráfico
- [ ] Estatísticas externas aparecem apenas quando relevantes e verificadas; não
      há mínimo aplicável
- [ ] A seção de surpresas traz 2 ou mais achados contraintuitivos
- [ ] As limitações estão declaradas com honestidade
- [ ] As recomendações estão amarradas a achados específicos
- [ ] Ao menos 3 zonas [INTERNAL-LINK]
- [ ] As perguntas frequentes incluem metodologia e citação
- [ ] Apêndice de dados com tabela-resumo e formato de citação
- [ ] Todos os dados verificados e cálculos conferidos duas vezes
