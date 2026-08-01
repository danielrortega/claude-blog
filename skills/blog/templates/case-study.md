# Template: Estudo de Caso

**Nome do template:** Estudo de caso (narrativa focada em resultados)
**Extensão alvo:** 1.500 a 2.000 palavras
**Descrição:** Análise narrativa de um projeto, campanha ou iniciativa específica, documentando o desafio, a estratégia, a execução e os resultados mensuráveis. Feito para construir credibilidade, demonstrar competência por resultados reais e ranquear para "estudo de caso [tema]", "como a [empresa] conseguiu [resultado]" e consultas de cauda longa do tipo problema-solução.

## Quando usar este template

- **Objetivos de conteúdo:** construir confiança e autoridade por resultados documentados, gerar oportunidades demonstrando competência, criar material de referência para conversas comerciais, atrair links de publicações do setor
- **Intenção de busca:** informacional / investigação comercial: o leitor quer prova de que a estratégia funciona antes de se comprometer com ela
- **Melhor para:** casos de sucesso de clientes, retrospectivas internas de projeto, transformações antes e depois, validação de estratégia, documentação de processo
- **Evite quando:** você não tem métricas específicas ou resultados mensuráveis (histórias vagas de "deu certo" não servem), ou quando o retratado não autorizou ser citado

---

## Estrutura seção a seção

---

### Título (H1)

**Formato:** "Como a [Empresa/Equipe] [Conseguiu Resultado Específico] em [Prazo]"

**Exemplos:**
- "Como a Acme Corp Reduziu a Latência da API em 73% em 6 Semanas"
- "Como uma Equipe de 3 Pessoas Chegou a 1 Milhão de Usuários Mensais em 90 Dias"
- "Como Cortamos o Tempo de Build de 12 Minutos para 45 Segundos"

**Regras:**
- Inclua a métrica específica do resultado no título: é ela que fisga
- Inclua o prazo para criar urgência e credibilidade
- Use o nome da empresa ou equipe se for conhecido; use "Nós" em casos internos
- Fique abaixo de 70 caracteres sempre que possível

---

### Caixa de resumo (concisa; a extensão acompanha o material)

[ANSWER-FIRST] Este é o estudo de caso inteiro comprimido numa caixa só. Comece pelo número do resultado principal.

**Formato:** uma caixa de destaque visualmente distinta (citação, fundo colorido ou seção com borda), colocada logo depois do título.

**Estrutura:**
1. **Métrica principal** (1 frase): o resultado mais impressionante.
2. **Como** (1 frase): a estratégia central em linguagem simples.
3. **Prazo** (expressão): quanto tempo levou.

**Exemplo:**
> **Em resumo:** a Acme Corp reduziu o tempo de resposta da API de 1.200ms para 320ms (melhora de 73%) migrando de uma API REST monolítica para um gateway GraphQL com cache de borda. A migração foi concluída em 6 semanas, sem indisponibilidade, com uma equipe de 2 pessoas.

[STAT: a métrica principal que ancora o estudo de caso inteiro]

---

### Introdução (100 a 150 palavras)

[ANSWER-FIRST] Abra com a métrica do resultado já na primeira frase. Não construa até chegar nela. Comece por ela.

**Estrutura:**
1. **Abertura pelo resultado** (1 frase): declare o desfecho principal com números específicos.
2. **Contexto** (2 a 3 frases): quem é o retratado? Qual a escala? Por que isso importa para o leitor?
3. **Enquadramento do risco** (1 frase): o que estava em jogo se o problema não fosse resolvido?
4. **Promessa** (1 frase): o que o leitor vai aprender com este estudo de caso.

[STAT: métrica secundária que dá dimensão ao resultado principal, por exemplo economia de custo, tempo economizado, melhora na satisfação]

[INFO-GAIN: detalhe de contexto] Compartilhe um detalhe específico da empresa ou do projeto que torne o caso próximo do leitor: tamanho da equipe, restrição de orçamento, pilha tecnológica, setor.

[INTERNAL-LINK] Link para um post base relacionado: "Para entender o funcionamento de [estratégia/tecnologia], veja nosso [Guia sobre X]."

---

### O desafio (200 a 250 palavras)

[ANSWER-FIRST] Abra com o sintoma mais doloroso do problema: aquilo que fez alguém dizer "precisamos resolver isso".

**Estrutura:**
1. **Dor** (1 a 2 frases): o problema concreto e sentido. Use detalhes específicos: taxa de erro, reclamações, impacto na receita.
2. **Causa raiz** (2 a 3 frases): o que de fato causava o problema, no nível técnico ou estratégico?
3. **Dimensão do impacto** (1 a 2 frases): quantifique o estrago: quantos usuários afetados, quanta receita em risco, quantas horas de engenharia desperdiçadas.
4. **Tentativas frustradas** (2 a 3 frases): o que já tinha sido tentado e por que não funcionou. Isso cria tensão narrativa e mostra que a solução final não era a escolha óbvia.
5. **Ponto de virada** (1 frase): o que disparou a decisão de tentar outro caminho?

[STAT: métrica que quantifica a gravidade do problema antes da solução]

[INFO-GAIN: detalhe da tentativa frustrada] Documente uma tentativa que falhou com detalhe suficiente para o leitor aprender com ela. O que foi tentado, o que aconteceu, por que falhou.

[IMAGE] Diagrama ou captura de tela do estado "antes": a arquitetura quebrada, o painel de métricas ruim, os logs de erro.

**Exemplo de abertura:**
> "No pico de tráfego, a API da Acme devolvia erro 500 em 12% das requisições, e o maior cliente corporativo tinha dado 30 dias de prazo para resolver ou cancelaria o contrato anual de US$ 2 milhões."

---

### A estratégia (300 a 400 palavras)

[ANSWER-FIRST] Abra com a decisão estratégica central em uma frase: qual caminho foi escolhido e a razão mais importante para isso.

**Estrutura:**
1. **Escolha estratégica** (1 a 2 frases): que abordagem foi selecionada? Nomeie a metodologia, tecnologia ou framework.
2. **Por que essa abordagem** (3 a 4 frases): o que a tornou a escolha certa frente às alternativas? Retome as tentativas frustradas da seção anterior. Inclua os critérios específicos usados na decisão.
3. **Decisões-chave** (3 a 5 marcadores ou subseções): destrinche as 3 a 5 decisões mais importantes da formulação da estratégia. Cada uma deve trazer a decisão, as alternativas consideradas e o raciocínio.
4. **Avaliação de risco** (1 a 2 frases): quais eram os riscos conhecidos e como foram mitigados?

[INFO-GAIN: documentação de processo] Esta é a seção de maior valor. Documente o processo de decisão com especificidade suficiente para outra equipe reproduzir o raciocínio. Inclua:
- Critérios de seleção usados para avaliar as opções
- Trade-offs discutidos e ponderados explicitamente
- Frameworks, planilhas de pontuação ou ferramentas de avaliação usados
- Quem participou da decisão e que perspectivas trouxe

[VISUAL: decision-matrix] Se couber, inclua uma tabela com as opções avaliadas, os critérios e as notas que levaram à escolha final.

[STAT: dado de apoio que justificou a escolha estratégica, por exemplo benchmark, dado do setor, análise de concorrente]

[INTERNAL-LINK] Link para um guia detalhado sobre a estratégia ou tecnologia escolhida: "Escrevemos um guia completo sobre [estratégia/tecnologia]: leia aqui."

**Exemplo:**
> "A equipe optou por migrar de REST para GraphQL, não por modismo, mas porque a análise mostrou que 78% das chamadas de API buscavam de 3 a 10 vezes mais dados do que o necessário, e o padrão BFF (Backend for Frontend) que tinham tentado antes acrescentava latência em vez de reduzir."

---

### A implementação (200 a 300 palavras)

[ANSWER-FIRST] Abra com o prazo total e o tamanho da equipe: "Uma equipe de [N] pessoas concluiu a implementação em [prazo]."

**Estrutura:**
1. **Equipe e prazo** (1 a 2 frases): quem fez o trabalho, quanto tempo levou e como foi faseado.
2. **Execução passo a passo** (lista numerada): 4 a 6 passos-chave em ordem cronológica. Cada passo traz o que foi feito, as ferramentas usadas e os imprevistos.
3. **Ferramentas e tecnologia** (lista com marcadores): ferramentas, serviços e tecnologias específicos.
4. **Momento crítico** (1 a 2 frases): um momento em que quase deu errado ou em que uma percepção inesperada mudou o plano.

[IMAGE] Diagrama de arquitetura, linha do tempo ou captura da implementação em andamento.

[INFO-GAIN: detalhe de implementação] Compartilhe um detalhe técnico ou operacional que fez diferença material: uma configuração, um truque de migração, um processo de coordenação. O tipo de detalhe que economiza horas de outra pessoa.

[STAT: métrica de eficiência da implementação: tempo gasto, custo, iterações necessárias]

**Exemplo de passo:**
> 3. **Camada de cache de borda no ar** (semanas 3 e 4): configuramos Cloudflare Workers como camada de cache entre o gateway GraphQL e os servidores de origem. Usamos stale-while-revalidate com TTL de 60s: essa mudança sozinha respondeu por 40% da redução total de latência.

---

### Os resultados (200 a 300 palavras)

[ANSWER-FIRST] Abra retomando a métrica principal e expanda imediatamente com 2 a 3 métricas de apoio. Use o formato antes e depois.

**Estrutura:**
1. **Resultado principal** (1 frase): a métrica primária, no formato antes -> depois, com variação percentual.
2. **Métricas de apoio** (lista com marcadores): 3 a 5 desfechos mensuráveis adicionais, cada um com valores de antes e depois.
3. **Impacto no negócio** (1 a 2 frases): traduza as métricas técnicas em resultados de negócio (receita retida, clientes preservados, horas liberadas).
4. **Prazo** (1 frase): quando os resultados foram medidos em relação ao fim da implementação.
5. **Benefícios inesperados** (1 a 2 frases): ganhos que não estavam nos objetivos originais.

[VISUAL: grouped-bar chart] Comparação antes e depois de 3 a 5 métricas-chave. Use um gráfico de barras agrupadas com rótulos claros, mostrando os valores lado a lado.

[STAT: todas as métricas de resultado com números específicos de antes e depois]

[IMAGE] Captura do estado "depois": o painel melhorado, os logs limpos, o gráfico de desempenho.

**Exemplo:**
> | Métrica | Antes | Depois | Variação |
> |---------|-------|--------|----------|
> | Tempo de resposta da API (p95) | 1.200ms | 320ms | -73% |
> | Taxa de erro (5xx) | 12% | 0,3% | -97,5% |
> | Custo de infraestrutura | US$ 8.400/mês | US$ 3.200/mês | -62% |
> | Satisfação do cliente (NPS) | 24 | 67 | +179% |

---

### Principais conclusões (150 a 200 palavras)

[ANSWER-FIRST] Abra com a lição mais transferível: "A maior lição deste projeto é [X]."

**Formato:** 3 a 5 conclusões numeradas, cada uma como uma percepção em negrito seguida de 1 a 2 frases de explicação.

**Critérios para cada conclusão:**
- Precisa ser **transferível**: aplicável à situação do leitor, não só a este caso
- Precisa ser **específica**: conselho acionável, não lugar-comum
- Precisa ser **conquistada**: ancorada no que de fato aconteceu neste caso

[INFO-GAIN: lição contraintuitiva ou surpreendente] Inclua pelo menos uma conclusão que contrarie o senso comum ou o conselho corrente da área.

**Exemplo:**
> **1. Meça o problema antes de desenhar a solução.**
> A equipe passou a primeira semana só instrumentando: acrescentou log e tracing detalhados antes de escrever uma linha de código de migração. O investimento se pagou ao revelar que o gargalo real não estava onde imaginavam (consultas ao banco), e sim no custo de serialização.

[INTERNAL-LINK] Ligue cada conclusão a um post aprofundado onde o leitor possa se aprofundar naquele princípio.

---

### Perguntas do leitor, opcionais (quantidade conforme a necessidade)

[FAQ]

**Formato:** cada pergunta como H3, resposta em 2 a 4 frases.

**Critérios de seleção das perguntas:**
1. **Pergunta de aplicabilidade:** "Essa abordagem funcionaria em [outro contexto]?" (trata a transferibilidade)
2. **Pergunta de recursos:** "Qual foi o orçamento e o tamanho da equipe?" (trata a viabilidade)
3. **Pergunta de alternativa:** "O que você faria diferente se começasse de novo?" (demonstra reflexão honesta)

[STAT quando útil: uma métrica verificada que melhore de fato a resposta]

**Exemplo:**

#### Essa abordagem funcionaria para uma equipe menor?

[Resposta de 2 a 4 frases sobre como a estratégia se adapta a escalas menores, com modificações específicas.]

#### Qual foi o custo total do projeto?

[Resposta de 2 a 4 frases com abertura transparente de custo: horas da equipe, ferramentas, infraestrutura, custo de oportunidade.]

#### O que você faria diferente?

[Resposta de 2 a 4 frases com reflexão honesta: isso constrói confiança e demonstra competência real.]

---

## Lista de verificação do template

Antes de publicar, confirme:

- [ ] O título traz métrica específica, prazo e sujeito
- [ ] A caixa de resumo está presente e traz o resultado principal em menos de 60 palavras
- [ ] A introdução abre com a métrica do resultado, não com contexto de fundo
- [ ] A seção do desafio quantifica o problema com números específicos
- [ ] A seção do desafio documenta pelo menos uma tentativa anterior frustrada
- [ ] A seção da estratégia explica *por que* essa abordagem foi escolhida em vez das alternativas
- [ ] A seção da estratégia traz detalhe de processo suficiente para replicação [INFO-GAIN: documentação de processo]
- [ ] A seção de implementação traz ferramentas, prazo e tamanho da equipe específicos
- [ ] A seção de resultados tem métricas de antes e depois para pelo menos 3 indicadores
- [ ] Os resultados incluem um [VISUAL: grouped-bar chart] para a comparação antes e depois
- [ ] As conclusões são transferíveis, específicas e ancoradas no caso
- [ ] Pelo menos 3 elementos [INFO-GAIN] com processo original ou dado observacional
- [ ] As estatísticas são opcionais, relevantes ao caso e verificadas quando usadas
- [ ] As perguntas frequentes tratam aplicabilidade, viabilidade e reflexão honesta
- [ ] Todas as zonas [INTERNAL-LINK] têm links contextuais para conteúdo relacionado
- [ ] A cobertura atende à intenção de estudo de caso sem encher linguiça
- [ ] O retratado autorizou ser citado (ou o caso foi anonimizado)
- [ ] A meta description resume com precisão o caso e o resultado visíveis
