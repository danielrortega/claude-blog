# Template: Perguntas Frequentes / Base de Conhecimento

**ID do template:** faq-knowledge
**Extensão alvo:** 1.500 a 2.000 palavras
**Tipo de conteúdo:** conjunto abrangente de perguntas organizadas por categoria, com respostas extraíveis
**Intenção de busca principal:** informacional ("o que é", "como funciona", "por que", "posso", "devo")

## Quando usar este template

Use quando:
- Um tema gera muitas perguntas recorrentes em fóruns, canais de suporte ou busca
- Cada pergunta pode ser respondida de forma clara e direta, sem faixa fixa de palavras
- O conteúdo precisa ser otimizado para destaques do Google e citações por IA
- As consultas são formuladas como perguntas ("como faço", "qual a diferença entre", "por que")
- Você quer criar uma página de referência linkável, para a qual outros conteúdos apontem

NÃO use para:
- Instruções passo a passo (use tutorial)
- Análise de evento recente (use news-analysis)
- Estudos com dados próprios (use data-research)
- Temas com menos de 10 perguntas significativas (raso demais para o formato)

**Nota de SEO:** este template é otimizado para blocos de pergunta e resposta
visíveis e autossuficientes. Perguntas visíveis podem favorecer a extração para
destaques e citações por IA, mas o schema FAQPage não gera destaque de resultado
e deve ser secundário aos schemas Article, Person, Organization e BreadcrumbList.

---

## Formato do título

```
[Tema]: Perguntas Frequentes ([Ano])
```

**Exemplos:**
- "Claude Code: Perguntas Frequentes (2026)"
- "Revisão de Código Assistida por IA: Perguntas Frequentes (2026)"
- "SEO para Blog Técnico: Perguntas Frequentes (2026)"

**Regras do título:**
- Nomeie o tema explicitamente
- Inclua "Perguntas Frequentes" (expressão exata para correspondência de busca)
- Inclua o ano (sinaliza atualidade; atualize anualmente)
- Fique abaixo de 60 caracteres para exibição completa no resultado de busca, quando possível

**Formatos alternativos de título:**
- "FAQ de [Tema]: [N] Perguntas Respondidas ([Ano])"
- "[Tema] para [Público]: [N] Dúvidas Comuns Respondidas ([Ano])"
- "[Tema] Explicado: [N] Dúvidas Comuns Respondidas"

---

## Estrutura seção a seção

---

### Introdução (100 a 150 palavras)

[ANSWER-FIRST] Apresente o tema e estabeleça por que essas perguntas importam.
Use estatística verificada apenas quando ela melhorar de fato essa explicação.

```markdown
# [Tema]: Perguntas Frequentes ([Ano])

[ANSWER-FIRST] [Tema] é [definição ou descrição em uma frase]. [Por que importa, em 1 frase].

[STAT quando útil: dado sobre a relevância do tema: taxa de adoção, volume de busca, tamanho de mercado ou frequência dessas dúvidas]

Estas perguntas frequentes cobrem as [N] dúvidas mais comuns sobre [tema], organizadas em [N] categorias:

1. **[Nome da categoria 1]** - [O que essas perguntas cobrem]
2. **[Nome da categoria 2]** - [O que essas perguntas cobrem]
3. **[Nome da categoria 3]** - [O que essas perguntas cobrem]
4. **[Nome da categoria 4]** - [O que essas perguntas cobrem]

[INFO-GAIN: por que estas perguntas frequentes existem: que lacuna preenchem frente aos recursos existentes, ou que perspectiva própria trazem]

> **Última atualização:** [Data]. [Com que frequência esta página é atualizada].
```

**Regras:**
- A introdução deve ser de leitura rápida: o leitor vai pular direto para a dúvida dele
- Inclua um sumário por meio da lista de categorias
- Informe quando a página foi atualizada pela última vez (sinal de confiança)
- Inclua uma estatística que estabeleça a relevância do tema, quando houver e tiver fonte

---

### Categoria 1: perguntas de "primeiros passos" (quantidade conforme a necessidade)

Perguntas de base para quem está chegando. Cada pergunta é um H2.

```markdown
## Primeiros passos com [Tema]

### O que é [tema/ferramenta/conceito]?

[ANSWER-FIRST] [Tema] é [definição clara, sem jargão, dimensionada ao conceito]. [Acrescente contexto sobre a finalidade ou o caso de uso principal, quando ajudar].

[STAT: dado de adoção ou uso que valide a relevância]

[INTERNAL-LINK: link para guia introdutório ou conteúdo panorâmico, para quem precisa de mais profundidade]

---

### Quem deveria usar [tema/ferramenta]?

[ANSWER-FIRST] [Tema] é mais adequado para [público específico] que precisa de [resultado específico]. [Uma frase sobre para quem NÃO serve, para o leitor se autoidentificar].

**Ideal para:**
- [Segmento 1]: [Por quê]
- [Segmento 2]: [Por quê]

**Não indicado para:**
- [Segmento]: [Por que não]

---

### Como começo com [tema]?

[ANSWER-FIRST] Para começar com [tema], [primeiro passo em uma frase]. [Segundo passo]. Toda a configuração leva cerca de [tempo].

[INTERNAL-LINK: link para o tutorial detalhado de configuração]

---

### Quanto custa [tema/ferramenta]?

[ANSWER-FIRST] [Tema/ferramenta] [resumo de preço em uma frase: gratuito, freemium, faixas pagas]. [Uma frase sobre o que a camada gratuita inclui ou sobre a base de cobrança].

[STAT: comparação de preço ou referência de valor, se pertinente]

[INTERNAL-LINK: link para comparação ou guia detalhado de preços, se houver]
```

---

### Categoria 2: perguntas de "como funciona" (quantidade conforme a necessidade)

Perguntas funcionais sobre mecânica e capacidades.

```markdown
## Como [Tema] funciona

### Como funciona [tema/funcionalidade]?

[ANSWER-FIRST] [Tema/funcionalidade] funciona por meio de [mecanismo explicado por completo, sem jargão desnecessário]. [Acrescente detalhe técnico para quem precisa de profundidade].

[VISUAL: simple-diagram mostrando o funcionamento, se aplicável]

[INTERNAL-LINK: link para conteúdo técnico aprofundado]

---

### Qual a diferença entre [A] e [B]?

[ANSWER-FIRST] A diferença central é [distinção-chave em uma frase]. [A] é [característica], enquanto [B] é [característica].

| Aspecto | [A] | [B] |
|---------|-----|-----|
| [Ponto de comparação 1] | [Valor de A] | [Valor de B] |
| [Ponto de comparação 2] | [Valor de A] | [Valor de B] |
| [Ponto de comparação 3] | [Valor de A] | [Valor de B] |
| **Melhor para** | [Caso de uso] | [Caso de uso] |

[STAT: dado de uso ou desempenho comparando A e B, se disponível]

---

### [Tema/ferramenta] consegue fazer [capacidade específica]?

[ANSWER-FIRST] [Sim/Não], [tema/ferramenta] [consegue/não consegue] [capacidade] [porque, razão em uma frase]. [Uma frase sobre contornos ou alternativas, se "não", ou sobre limitações, se "sim"].

---

### Quais as limitações de [tema/ferramenta]?

[ANSWER-FIRST] As principais limitações de [tema/ferramenta] são [as 2 ou 3 maiores, em uma frase]. [Uma frase sobre se essas limitações estão sendo tratadas].

**Limitações atuais:**
1. **[Limitação 1]:** [Explicação breve]
2. **[Limitação 2]:** [Explicação breve]
3. **[Limitação 3]:** [Explicação breve]

[INFO-GAIN: avaliação honesta baseada em uso prático: o que o marketing não conta]
```

---

### Categoria 3: perguntas de "problemas comuns" (quantidade conforme a necessidade)

Perguntas de solução de problemas para quem travou.

```markdown
## Problemas comuns e soluções

### Por que [tema/ferramenta] está [não funcionando / lento / dando erro]?

[ANSWER-FIRST] A causa mais comum de [problema] é [causa raiz em uma frase]. [Correção em uma frase].

**Causas comuns e correções:**

| Causa | Correção |
|-------|----------|
| [Causa 1] | [Correção 1] |
| [Causa 2] | [Correção 2] |
| [Causa 3] | [Correção 3] |

[INTERNAL-LINK: link para o guia detalhado de solução de problemas]

---

### Como corrijo [mensagem de erro específica]?

[ANSWER-FIRST] [Mensagem de erro] normalmente significa [o que significa]. Corrija com [ação específica em uma frase].

```[linguagem]
# [Comando ou código de correção]
[correção específica]
```

[STAT: quão comum é esse erro, se houver dado]

---

### Como migro de [ferramenta/versão antiga] para [nova]?

[ANSWER-FIRST] Para migrar de [antiga] para [nova], [passos gerais em uma frase]. A migração leva cerca de [tempo] num [projeto/configuração] típico.

**Passos da migração:**
1. [Passo 1]
2. [Passo 2]
3. [Passo 3]

[INTERNAL-LINK: link para o tutorial detalhado de migração]

---

### Onde consigo ajuda com [tema/ferramenta]?

[ANSWER-FIRST] Os melhores lugares para obter ajuda com [tema/ferramenta] são [os 2 ou 3 principais recursos]. [Uma frase sobre tempo de resposta ou qualidade da comunidade].

**Recursos de ajuda:**
- **[Recurso 1]:** [Descrição e link]
- **[Recurso 2]:** [Descrição e link]
- **[Recurso 3]:** [Descrição e link]
```

---

### Categoria 4: perguntas "avançadas" (quantidade conforme a necessidade)

Perguntas de quem já tem prática e busca entendimento mais profundo.

```markdown
## Tópicos avançados

### Como faço [caso de uso avançado]?

[ANSWER-FIRST] Para [caso de uso avançado], [abordagem em uma frase]. Isso exige [conhecimento ou configuração pré-requisito].

[Explicação técnica breve, 2 a 3 frases]

```[linguagem]
# Exemplo de implementação
[trecho de código mostrando a abordagem]
```

[INTERNAL-LINK: link para o tutorial avançado que cobre isso em detalhe]

[INFO-GAIN: dica de especialista ou abordagem não óbvia baseada em uso real]

---

### Quais as boas práticas de [tema] em produção?

[ANSWER-FIRST] As [N] principais boas práticas de [tema] em produção são [lista breve em uma frase]. [Uma frase sobre por que elas importam].

1. **[Prática 1]:** [Explicação breve com justificativa]
2. **[Prática 2]:** [Explicação breve com justificativa]
3. **[Prática 3]:** [Explicação breve com justificativa]

[STAT: dado sobre o impacto de seguir essas práticas: redução de erro, ganho de desempenho]

---

### Como [tema] se compara a [alternativa] em [caso de uso específico]?

[ANSWER-FIRST] Para [caso de uso específico], [tema] é [melhor/pior/equivalente] frente a [alternativa] porque [razão central]. [Uma frase de nuance].

| Critério | [Tema] | [Alternativa] |
|----------|--------|---------------|
| [Critério 1] | [Nota/valor] | [Nota/valor] |
| [Critério 2] | [Nota/valor] | [Nota/valor] |
| [Critério 3] | [Nota/valor] | [Nota/valor] |
| **Veredito** | [Resumo] | [Resumo] |

[INTERNAL-LINK: link para conteúdo comparativo detalhado]
```

---

### Recursos relacionados (100 palavras)

```markdown
## Recursos relacionados

Explore estes recursos para se aprofundar em [tema]:

- **[Título do guia detalhado]** - [Descrição em uma frase] [INTERNAL-LINK]
- **[Título do tutorial]** - [Descrição em uma frase] [INTERNAL-LINK]
- **[Título da comparação ou análise]** - [Descrição em uma frase] [INTERNAL-LINK]
- **[Documentação oficial]** - [Descrição em uma frase com link externo]
- **[Comunidade ou fórum]** - [Descrição em uma frase com link externo]
```

**Regras:**
- Misture links internos (seu conteúdo) com externos (documentação oficial, comunidades)
- Priorize os links internos: esta é uma página-eixo
- Mantenha cada descrição em uma frase

---

### Ainda com dúvidas? (50 palavras)

```markdown
## Ainda com dúvidas?

Não encontrou o que procurava? [Forma de contato, por exemplo "Deixe um comentário abaixo", "Entre na nossa comunidade em [link]", "Fale com a gente no [plataforma]"]. Atualizamos estas perguntas frequentes [frequência: mensalmente/trimestralmente] com base nas dúvidas dos leitores.

[IMAGE: gráfico opcional de chamada para ação ou selo de comunidade]
```

---

## Notas sobre dado estruturado

O schema FAQPage é marcação de entidade opcional para perguntas visíveis. Article
ou BlogPosting, Person, Organization e BreadcrumbList seguem sendo a base. Quando
usar FAQPage, gere JSON-LD válido a partir das perguntas visíveis:

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[Texto da pergunta]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Texto da resposta: use a frase do ANSWER-FIRST mais o detalhe de apoio]"
      }
    }
  ]
}
```

**Regras:**
- Se gerar FAQPage, inclua no schema todas as perguntas H2 visíveis
- Use o texto do [ANSWER-FIRST] como resposta no schema
- O schema pode conter todas as perguntas visíveis, desde que o tamanho do JSON siga razoável
- Teste o FAQPage com o Schema.org Validator e valide a consistência de entidade. Use
  o Rich Results Test do Google somente para tipos de página elegíveis a rich results.

---

## Lista de verificação de conteúdo

Antes de publicar, confirme:

- [ ] O título traz o nome do tema, "Perguntas Frequentes" e o ano
- [ ] A introdução traz uma estatística sobre a relevância do tema, quando disponível e com fonte
- [ ] As perguntas estão organizadas em 3 ou 4 categorias lógicas
- [ ] Toda pergunta está formulada exatamente como as pessoas buscariam
- [ ] Toda resposta abre com [ANSWER-FIRST] (resposta direta na primeira frase)
- [ ] Cada resposta é completa e autossuficiente; extensão sozinha não aprova nem reprova
- [ ] Cada resposta é extraível como trecho isolado (sem referências do tipo "como dito acima")
- [ ] A quantidade de perguntas acompanha a necessidade demonstrada do leitor, sem enchimento
- [ ] As estatísticas são opcionais, relevantes à resposta e verificadas quando usadas
- [ ] Ao menos 2 marcadores [INFO-GAIN] com experiência ou percepção próprias
- [ ] Ao menos 6 zonas [INTERNAL-LINK] conectando a conteúdo detalhado
- [ ] Ao menos 1 marcador [VISUAL] (tabela comparativa ou diagrama)
- [ ] A seção de recursos relacionados tem de 3 a 5 links
- [ ] Seção "Ainda com dúvidas?" com caminho claro de contato ou comunidade
- [ ] O dado estruturado FAQPage é opcional e gerado apenas a partir das perguntas visíveis
- [ ] Nenhuma resposta remete a outra resposta (cada uma se sustenta sozinha)
- [ ] Todas as respostas são claras o bastante para se sustentarem em destaques de busca ou citações por IA
