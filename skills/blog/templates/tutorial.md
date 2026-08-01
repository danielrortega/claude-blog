# Template: Tutorial (passo a passo de código ou ferramenta)

**ID do template:** tutorial
**Extensão alvo:** 2.000 a 3.000 palavras
**Tipo de conteúdo:** passo a passo técnico com instruções detalhadas
**Intenção de busca principal:** informacional / transacional ("como fazer", "tutorial", "guia", "configurar")

## Quando usar este template

Use quando:
- Você vai ensinar a construir, configurar ou implementar algo específico
- O resultado é um código funcionando, uma ferramenta configurada ou uma instalação concluída
- O público precisa acompanhar passo a passo
- As consultas de busca incluem "como fazer", "tutorial", "passo a passo", "configurar", "instalar"
- Você tem prática com a ferramenta ou tecnologia e pode compartilhar dicas de otimização

NÃO use para:
- Peças de estratégia ou opinião de alto nível (use news-analysis ou data-research)
- Conteúdo de referência ou perguntas frequentes (use faq-knowledge)
- Conteúdo sem passos concretos e reproduzíveis

---

## Formato do título

```
Tutorial de [Ferramenta/Tecnologia]: [Resultado Específico] em [Ano]
```

**Exemplos:**
- "Tutorial de Claude Code: Construindo um Pipeline de Automação de Blog em 2026"
- "Tutorial de Next.js 15: Rota de API com Server Components em 2026"
- "Tutorial de Docker Compose: Ambiente de Desenvolvimento Multi-Contêiner em 2026"

**Regras do título:**
- Inclua o nome da ferramenta ou tecnologia principal
- Declare o resultado específico que o leitor vai alcançar
- Inclua o ano atual como sinal de atualidade
- Fique abaixo de 60 caracteres para exibição completa no resultado de busca, quando possível

---

## Estrutura seção a seção

---

### Caixa de resumo (concisa; a extensão acompanha o material)

[ANSWER-FIRST] Resuma em 2 a 3 frases o que o leitor vai construir ou alcançar. Declare o resultado final, a ferramenta principal e o tempo aproximado. Esta caixa precisa funcionar como trecho autossuficiente.

```markdown
> **Em resumo:** [O que você vai construir, em uma frase]. Usando [ferramenta/tecnologia principal],
> você vai [resultado específico] em cerca de [estimativa de tempo]. Ao final, você terá
> [entregável concreto]. Não é preciso experiência prévia com [ferramenta] além de [pré-requisito mínimo].
```

[INFO-GAIN: diga o que torna este tutorial diferente dos existentes: abordagem própria, método atualizado ou contexto de uso real]

---

### Pré-requisitos (100 a 150 palavras)

[ANSWER-FIRST] Declare exatamente o que o leitor precisa antes de começar. Seja específico quanto às versões.

**Inclua:**
- Ferramentas necessárias com número exato de versão
- Notas de compatibilidade com sistema operacional
- Nível de conhecimento prévio (iniciante, intermediário, avançado)
- Contas ou chaves de API necessárias
- Tempo estimado de conclusão

```markdown
**Você vai precisar de:**
- [Ferramenta 1] v[X.X] ou superior ([link de instalação])
- [Ferramenta 2] v[X.X] ou superior ([link de instalação])
- [Conta/chave de API] ([link de cadastro])
- Familiaridade básica com [conceito]
- Cerca de [N] minutos

**Testado em:** [detalhes do sistema e do ambiente]
```

[STAT: taxa de adoção ou métrica de popularidade da ferramenta principal, validando a relevância do tutorial]

---

### O que vamos construir (100 a 150 palavras)

[ANSWER-FIRST] Descreva o resultado final em termos concretos. O que o produto pronto faz? Qual a aparência dele?

```markdown
Veja como fica o [projeto] finalizado:

[IMAGE: captura de tela ou demonstração do projeto concluído]

**O que ele faz:**
- [Capacidade 1]
- [Capacidade 2]
- [Capacidade 3]

**Visão geral da arquitetura:**
[VISUAL: simple-diagram mostrando componentes e fluxo de dados]
```

[INTERNAL-LINK: link para tutoriais pré-requisito ou conceitos de base]

---

### Configuração inicial (200 a 300 palavras)

[ANSWER-FIRST] Diga o que a configuração realiza e quanto tempo leva.

**Estrutura:**
1. Preparação do ambiente (estrutura de diretórios, inicialização do projeto)
2. Instalação das dependências
3. Arquivos de configuração
4. Verificação de que a configuração está correta

```markdown
## Preparando seu ambiente

[ANSWER-FIRST] A preparação leva cerca de [N] minutos e deixa seu [ambiente/ferramenta] pronto para [os passos do tutorial].

### Passo 1: [Inicializar/Criar/Clonar]

[Explicação breve do que isso faz e por quê]

\`\`\`bash
# [Comentário descritivo]
[comando 1]
[comando 2]
\`\`\`

### Passo 2: [Instalar dependências]

\`\`\`bash
# [Comentário descritivo]
[comando]
\`\`\`

### Passo 3: [Configurar]

\`\`\`[linguagem]
// [nome do arquivo de configuração]
{
  [configuração com comentários inline]
}
\`\`\`

[IMAGE: captura da configuração concluída / saída esperada no terminal]

**Verifique sua configuração:**

\`\`\`bash
[comando de verificação]
\`\`\`

Saída esperada:
\`\`\`
[saída esperada]
\`\`\`
```

**Erros comuns de configuração:**

| Erro | Causa | Correção |
|------|-------|----------|
| [Mensagem de erro] | [Por que acontece] | [Como corrigir] |
| [Mensagem de erro] | [Por que acontece] | [Como corrigir] |

---

### Seções passo a passo (300 a 400 palavras cada, 4 a 6 passos)

Cada passo é um título H2. Siga esta estrutura em todos:

```markdown
## Passo [N]: [Verbo de ação] + [O que você está fazendo]

[ANSWER-FIRST] Neste passo você vai [o que ele realiza], para que [por que importa no resultado final].

[Explicação breve do conceito por trás do passo, no máximo 2 a 3 frases]

\`\`\`[linguagem]
// [arquivo onde este código entra]

[bloco de código com comentários inline detalhados]

// [Explique as linhas não óbvias]
\`\`\`

[IMAGE: captura mostrando o resultado deste passo]

**O que acabou de acontecer:** [explicação de 1 a 2 frases sobre o que o código faz]

**Saída esperada:**

\`\`\`
[saída do terminal ou resultado no navegador]
\`\`\`

[INFO-GAIN: dicas de otimização vindas da prática: o que ajustar, considerações de desempenho ou adaptações de uso real que você descobriu]

> **Atenção:** [Erro comum neste passo e como evitá-lo]

[INTERNAL-LINK: link para explicação mais profunda dos conceitos-chave usados neste passo]
```

**Regras das seções de passo:**
- Cada passo deve produzir um resultado visível e testável
- Os blocos de código precisam ser completos e prontos para copiar e colar (sem reticências ou atalhos com "...")
- Inclua o nome do arquivo onde o código deve ficar
- Mostre a saída esperada, para o leitor confirmar que está no caminho
- Trate o erro mais comum de cada passo ali mesmo
- Cada passo se apoia no anterior: nunca pule dependências

---

### Teste e verificação (200 a 300 palavras)

[ANSWER-FIRST] Descreva como verificar que o projeto completo funciona como esperado.

```markdown
## Testando seu [projeto]

[ANSWER-FIRST] Rode estes [N] testes para confirmar que tudo funciona.

### Teste rápido de fumaça

\`\`\`bash
[comando único que verifica a funcionalidade básica]
\`\`\`

Resultado esperado:
\`\`\`
[saída esperada]
\`\`\`

### Suíte completa de testes

\`\`\`bash
[comando para rodar todos os testes]
\`\`\`

[IMAGE: captura dos testes passando]

### Lista de verificação manual

- [ ] [Checagem 1]: [Como verificar]
- [ ] [Checagem 2]: [Como verificar]
- [ ] [Checagem 3]: [Como verificar]

[VISUAL: fluxograma do processo de verificação, se for complexo]
```

---

### Solução de problemas (200 a 300 palavras)

[ANSWER-FIRST] Liste os problemas mais comuns e suas soluções.

```markdown
## Solução de problemas

[ANSWER-FIRST] Estes são os [N] problemas mais comuns e como resolvê-los.

| Problema | Sintoma | Solução |
|----------|---------|---------|
| [Problema 1] | [O que você vê] | [Correção exata, com comando] |
| [Problema 2] | [O que você vê] | [Correção exata, com comando] |
| [Problema 3] | [O que você vê] | [Correção exata, com comando] |
| [Problema 4] | [O que você vê] | [Correção exata, com comando] |
| [Problema 5] | [O que você vê] | [Correção exata, com comando] |

[INFO-GAIN: casos extremos ou problemas específicos de ambiente descobertos em teste real]

**Ainda travado?** [Link para comunidade, rastreador de issues ou canal de suporte]
```

[STAT: percentual de usuários que encontra cada problema, quando disponível na documentação ou em fóruns]

---

### Próximos passos (100 a 150 palavras)

[ANSWER-FIRST] Diga ao leitor o que fazer em seguida para ampliar ou aproveitar o que aprendeu.

```markdown
## Próximos passos

[ANSWER-FIRST] Agora que você tem um [projeto] funcionando, veja como levá-lo adiante.

**Amplie este projeto:**
- [Melhoria 1]: [Descrição breve] - [INTERNAL-LINK para tutorial relacionado]
- [Melhoria 2]: [Descrição breve] - [INTERNAL-LINK para tutorial relacionado]
- [Melhoria 3]: [Descrição breve]

**Tutoriais relacionados:**
- [INTERNAL-LINK: tutorial pré-requisito ou de base]
- [INTERNAL-LINK: tutorial avançado que parte deste]
- [INTERNAL-LINK: abordagem alternativa ou ferramenta complementar]

**Recursos oficiais:**
- [Link para a documentação oficial]
- [Link para o repositório no GitHub ou exemplos]
```

---

### Perguntas técnicas, opcionais (quantidade conforme a necessidade)

[ANSWER-FIRST] em cada pergunta. Cada resposta precisa ser autossuficiente e extraível.

```markdown
## Perguntas frequentes

### [Pergunta 1 - formulada como as pessoas buscariam]?

[ANSWER-FIRST] [Resposta direta em 1 a 2 frases]. [Detalhe de apoio ou exemplo].

[STAT: dado relevante, se aplicável]

### [Pergunta 2]?

[ANSWER-FIRST] [Resposta direta em 1 a 2 frases]. [Detalhe de apoio ou trecho de código].

### [Pergunta 3]?

[ANSWER-FIRST] [Resposta direta em 1 a 2 frases]. [Comparação ou recomendação].

[INTERNAL-LINK: link para conteúdo que trata a pergunta em profundidade]
```

**Regras das perguntas frequentes:**
- Formule as perguntas exatamente como as pessoas digitariam num buscador
- Responda já na primeira frase, sem rodeios
- Inclua trechos de código nas respostas quando for pertinente
- Responda de forma direta e completa; o Google não exige extensão mínima

---

### Referência do código-fonte completo

```markdown
## Código-fonte completo

[Bloco expansível ou link para o fonte completo]

<details>
<summary>Clique para expandir o código-fonte completo</summary>

\`\`\`[linguagem]
[Código-fonte completo, executável e comentado]
\`\`\`

</details>

**Repositório no GitHub:** [link, se aplicável]
```

---

## Lista de verificação de conteúdo

Antes de publicar, confirme:

- [ ] O título traz o nome da ferramenta, o resultado específico e o ano
- [ ] O resumo opcional é conciso, útil e factualmente sustentado
- [ ] Todos os pré-requisitos estão listados com versões exatas
- [ ] Todo bloco de código é completo e pronto para copiar e colar
- [ ] Todo passo produz um resultado visível e testável
- [ ] A saída esperada aparece depois de cada bloco de código
- [ ] Ao menos 4 marcadores [IMAGE] posicionados nos momentos visuais decisivos
- [ ] Ao menos 2 seções [INFO-GAIN] com dicas ou experiência próprias
- [ ] As estatísticas são opcionais, relevantes ao tutorial e verificadas quando usadas
- [ ] Ao menos 1 marcador [VISUAL] para diagrama de arquitetura ou de fluxo
- [ ] A tabela de solução de problemas tem 5 ou mais erros comuns
- [ ] As perguntas frequentes opcionais refletem dúvidas reais de leitor
- [ ] Zonas [INTERNAL-LINK] posicionadas em pré-requisitos, passos, próximos passos e perguntas frequentes
- [ ] O código-fonte completo está incluído no fim
- [ ] Todo o código foi testado e verificado antes da publicação
