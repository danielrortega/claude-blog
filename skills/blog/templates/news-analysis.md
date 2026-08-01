# Template: Análise de Notícia (comentário de evento recente)

**ID do template:** news-analysis
**Extensão alvo:** 800 a 1.200 palavras
**Tipo de conteúdo:** análise de evento recente com implicações acionáveis
**Intenção de busca principal:** informacional / navegacional ("o que aconteceu", "o que significa X", "reação a")

## Quando usar este template

Use quando:
- Um evento, anúncio ou lançamento relevante acabou de ocorrer
- O público precisa de análise rápida e opinativa, não de um resumo
- Você consegue publicar em 2 a 4 horas do evento
- As consultas de busca vão combinar o nome do evento com "o que significa", "implicações", "análise"
- Você tem uma perspectiva ou competência clara que agrega além do comunicado oficial

NÃO use para:
- Conteúdo perene do tipo "como fazer" (use o tutorial)
- Pesquisa própria ou estudo de dados (use data-research)
- Conteúdo de referência ou perguntas frequentes (use faq-knowledge)
- Eventos com mais de 2 semanas (a janela deste formato já passou)

**Prioridade de velocidade:** este template privilegia rapidez de publicação sobre profundidade. Publique rápido e atualize depois, se necessário.

---

## Formato do título

```
[Evento/Anúncio]: O Que Significa para [Público]
```

**Exemplos:**
- "Lançamento do GPT-5 da OpenAI: O Que Significa para Quem Desenvolve com IA"
- "Core Update de Março de 2026 do Google: O Que Significa para Quem Cria Conteúdo"
- "Anúncio do React 20: O Que Significa para Times de Frontend"

**Regras do título:**
- Nomeie o evento explicitamente (as pessoas buscam pelo nome do evento)
- Especifique o público que deveria se importar
- Fique abaixo de 60 caracteres para exibição completa no resultado de busca, quando possível
- Evite isca de clique: o próprio evento já é o gancho

**Formatos alternativos de título:**
- "[N] Coisas Que [Público] Precisa Saber Sobre [Evento]"
- "[Evento] Explicado: [Declaração de Impacto]"
- "Destrinchando [Evento]: Implicações para [Público]"

---

## Estrutura seção a seção

---

### Caixa de resumo (concisa; a extensão acompanha o material)

[ANSWER-FIRST] Condense as implicações centrais em 2 a 3 frases. Foque no que o leitor precisa saber e fazer, não em recontar o evento.

```markdown
> **Em resumo:** [Nome do evento] [o que aconteceu, em uma oração]. As maiores
> implicações para [público] são [implicação 1] e [implicação 2]. [Recomendação
> ou previsão em uma frase]. [Ação a tomar agora].
```

**Regras:**
- Presuma que o leitor já viu a manchete: não repita a notícia
- Comece pelas implicações, não pelo que aconteceu
- Inclua uma recomendação acionável

---

### O que aconteceu (100 a 150 palavras)

[ANSWER-FIRST] Exponha os fatos do evento com concisão. Esta é a seção objetiva: guarde a opinião para depois.

```markdown
## O que aconteceu

[ANSWER-FIRST] Em [data], [organização/pessoa] [anunciou/lançou/alterou] [algo específico].
[1 a 2 frases de detalhe factual].

**Fatos principais:**
- [Fato 1 com atribuição de fonte]
- [Fato 2 com atribuição de fonte]
- [Fato 3 com atribuição de fonte]

> "[Citação direta do anúncio ou de figura central]" - [Atribuição]

[STAT: um dado que estabeleça escala ou relevância: número de usuários, tamanho de mercado, taxa de adoção]
```

**Regras:**
- Cite fonte para toda afirmação factual
- Inclua ao menos uma citação direta de fonte primária
- Mantenha a seção objetiva: ainda sem análise
- Inclua datas e números de versão específicos

---

### Por que isso importa (200 a 300 palavras)

[ANSWER-FIRST] Abra com uma declaração clara de por que o evento é relevante: não apenas o que é, mas por que o leitor deve se importar agora.

```markdown
## Por que isso importa

[ANSWER-FIRST] [Evento] importa porque [razão central, específica e opinativa].

[2 a 3 parágrafos de análise cobrindo:]

**Contexto:** como isso se compara a eventos anteriores nessa área? Que padrão ele confirma ou rompe?

[STAT: dado de mercado, métrica de adoção ou tendência que contextualize o evento]

**Relevância:** o que diferencia isso de atualizações e anúncios de rotina? Que limiar foi cruzado?

[INFO-GAIN: sua análise ou previsão especializada; é aqui que você conquista a atenção do leitor frente à cobertura genérica]

**Comparação:**
| Antes de [Evento] | Depois de [Evento] |
|-------------------|--------------------|
| [Estado anterior] | [Novo estado] |
| [Estado anterior] | [Novo estado] |
| [Estado anterior] | [Novo estado] |
```

**Regras:**
- Seja opinativo: "isso importa porque", não "isso talvez importe"
- Compare a um evento anterior ou a uma linha de base, para o leitor entender a escala
- Inclua ao menos um dado de contexto
- O [INFO-GAIN] aqui é sua perspectiva própria: faça valer

---

### O que isso significa para [Público] (200 a 300 palavras)

[ANSWER-FIRST] Traduza o evento em implicações específicas para o público-alvo. Seja concreto sobre o que muda para ele.

```markdown
## O que isso significa para [Público]

[ANSWER-FIRST] Para [público], o impacto imediato é [mudança específica]. Veja como isso afeta seu trabalho.

### Impacto 1: [Mudança específica]

[2 a 3 frases explicando a implicação com exemplos concretos]

### Impacto 2: [Mudança específica]

[2 a 3 frases explicando a implicação com exemplos concretos]

### Impacto 3: [Mudança específica]

[2 a 3 frases explicando a implicação com exemplos concretos]

[INFO-GAIN: previsão ou implicação não óbvia baseada em competência própria: "O que a maior parte da cobertura está deixando passar é..."]

[INTERNAL-LINK: link para conteúdo seu que ajude o leitor a entender os conceitos de base]
```

**Regras:**
- Use o nome real do público no título (por exemplo, "O que isso significa para times de frontend")
- Cada impacto deve ser uma mudança concreta, não observação vaga
- Inclua ao menos uma implicação não óbvia: é o seu diferencial
- Linke seu conteúdo existente onde ele oferecer contexto mais profundo

---

### O que fazer agora (150 a 200 palavras)

[ANSWER-FIRST] Dê ao leitor de 3 a 5 passos concretos, ordenados por prioridade, do mais urgente ao menos.

```markdown
## O que fazer agora

[ANSWER-FIRST] Estes são [N] passos a tomar em resposta a [evento], ordenados por urgência.

1. **[Imediato: hoje ou esta semana]:** [Ação específica com explicação breve]
2. **[Curto prazo: este mês]:** [Ação específica com explicação breve]
3. **[Médio prazo: este trimestre]:** [Ação específica com explicação breve]
4. **[Se aplicável]:** [Ação específica com explicação breve]
5. **[Se aplicável]:** [Ação específica com explicação breve]

**NÃO faça:**
- [Reação exagerada comum a evitar]
- [Ação precipitada a evitar]

[INTERNAL-LINK: link para tutorial ou guia que ajude nas ações recomendadas]
```

**Regras:**
- Ordene por urgência: o que fazer hoje contra o que fazer neste trimestre?
- Seja específico o bastante para o leitor agir sem pesquisar mais
- Inclua itens de "NÃO faça" para evitar reação exagerada (isso demonstra credibilidade)
- Linke seu próprio conteúdo que ajude a agir

---

### O quadro maior (100 a 150 palavras)

[ANSWER-FIRST] Afaste a lente. Situe o evento no contexto de tendências mais amplas do setor.

```markdown
## O quadro maior

[ANSWER-FIRST] [Evento] faz parte de um movimento maior rumo a [padrão mais amplo].

[1 a 2 parágrafos conectando o evento a:]
- Direção do setor ou tendências macro
- Eventos anteriores que formam um padrão
- O que isso sinaliza sobre o futuro

[INTERNAL-LINK: link para seu conteúdo de estratégia ou análise de tendência que cubra o contexto mais amplo]

[VISUAL: linha do tempo situando este evento entre eventos relacionados, se aplicável]
```

**Regras:**
- Esta seção é onde você demonstra pensamento estratégico
- Conecte a no máximo 1 ou 2 tendências mais amplas: não estique demais
- Termine com uma afirmação de futuro (previsão ou pergunta a acompanhar)

---

### Perguntas do leitor, opcionais (quantidade conforme a necessidade)

[ANSWER-FIRST] em cada pergunta. Otimize para as consultas exatas que as pessoas farão nas horas e dias seguintes ao evento.

```markdown
## Perguntas frequentes

### [Pergunta 1 - a dúvida mais óbvia sobre o evento]?

[ANSWER-FIRST] [Resposta direta em 1 a 2 frases]. [Detalhe breve de apoio].

### [Pergunta 2 - dúvida prática sobre o que fazer]?

[ANSWER-FIRST] [Resposta direta em 1 a 2 frases]. [Detalhe breve de apoio].

[INTERNAL-LINK: link para conteúdo detalhado de como fazer, se pertinente]

### [Pergunta 3 - dúvida de futuro sobre o que vem a seguir]?

[ANSWER-FIRST] [Resposta direta em 1 a 2 frases]. [Detalhe breve de apoio].

[STAT: dado que sustente a resposta]
```

**Regras das perguntas frequentes:**
- Use perguntas que as pessoas estão de fato buscando agora
- As respostas precisam ser autossuficientes e extraíveis para destaques de busca e citações por IA
- Mantenha as respostas concisas e completas; o Google não exige extensão mínima
- Inclua apenas perguntas que acrescentem material útil; a quantidade segue a necessidade do leitor

---

### Referências e notas de consulta

```markdown
## Referências e notas de consulta

- [Título da fonte 1]([URL]) - [Organização], [Data], consultado em AAAA-MM-DD
- [Título da fonte 2]([URL]) - [Organização], [Data], consultado em AAAA-MM-DD
- [Título da fonte 3]([URL]) - [Organização], [Data], consultado em AAAA-MM-DD
- [Título da fonte 4]([URL]) - [Organização], [Data], consultado em AAAA-MM-DD
```

**Regras:**
- Toda afirmação factual do artigo precisa de citação inline
- As notas de consulta dão procedência e não devem duplicar as citações inline como despejo bruto de fontes
- Prefira fontes primárias (anúncios oficiais, comunicados) à cobertura secundária
- Inclua a data de cada fonte
- Mire em no mínimo 4 a 8 fontes

---

## Lista de verificação de conteúdo

Antes de publicar, confirme:

- [ ] Publicado em 2 a 4 horas do evento
- [ ] O título nomeia o evento explicitamente e especifica o público
- [ ] O resumo foca nas implicações, não em repetir a notícia
- [ ] A seção "O que aconteceu" é puramente factual, com citação de fontes
- [ ] Há ao menos uma citação direta de fonte primária
- [ ] As estatísticas aparecem apenas quando relevantes à análise e estão verificadas
- [ ] Ao menos 2 seções [INFO-GAIN] com análise ou previsão próprias
- [ ] "O que fazer agora" traz de 3 a 5 passos concretos e priorizados
- [ ] Ao menos 3 zonas [INTERNAL-LINK] conectando a conteúdo existente
- [ ] As perguntas frequentes correspondem a consultas reais sobre o evento
- [ ] Todas as fontes listadas com URL e data
- [ ] A análise é opinativa e se diferencia da cobertura genérica
- [ ] A seção "NÃO faça" está incluída, para evitar reação exagerada
- [ ] O conteúdo tem menos de 1.200 palavras (resista à vontade de explicar demais)
