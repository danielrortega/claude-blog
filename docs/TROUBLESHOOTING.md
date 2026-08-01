# Solução de Problemas

Problemas comuns do `claude-blog`, suas causas e correções. Os itens estão
agrupados por categoria e ordenados do mais ao menos frequente.

---

## Problemas de instalação

### "Comando não encontrado" depois da instalação

**Sintoma**: rodar `/blog write` não produz resposta, ou aparece um erro de
skill não encontrada.

**Causa**: o Claude Code guarda em cache as definições de skill na inicialização.
Skills novas só são detectadas depois que a CLI é reiniciada.

**Correção**:
1. Feche o Claude Code por completo (saia da CLI ou feche o terminal)
2. Reabra o Claude Code
3. Tente `/blog write <tema>` de novo

### Erros no script Python

**Sintoma**: `/blog analyze` falha ao rodar o `analyze_blog.py`, ou o script sai
com erro de importação.

**Causa**: as dependências Python não estão instaladas.

**Correção**:
```bash
pip install -r requirements.txt
```

Ou instale as dependências centrais individualmente:
```bash
pip install textstat beautifulsoup4 lxml jsonschema
```

### textstat ou beautifulsoup4 ausentes

**Sintoma**: o `analyze_blog.py` roda, mas reporta
`ModuleNotFoundError: No module named 'textstat'` ou semelhante.

**Causa**: as dependências Python opcionais não estão instaladas.

**Comportamento**: o script de análise foi feito para **degradar com elegância**.
Sem as dependências opcionais, ele recorre ao modo básico:

| Dependência | Quando ausente | Alternativa |
|-------------|----------------|-------------|
| textstat | Sem notas de Flesch e Gunning Fog | Heurística de tamanho de frase |
| beautifulsoup4 | Sem parsing de schema em HTML | Detecção por regex |
| lxml | O BeautifulSoup usa o html.parser | Mais lento, mas funcional |
| spacy | Sem análise de entidades nomeadas | Pulado (recurso opcional) |
| sentence-transformers | Sem similaridade semântica | Pulado (recurso opcional) |
| scikit-learn | Sem agrupamento de temas | Pulado (recurso opcional) |
| language-tool-python | Sem checagem gramatical | Pulado (recurso opcional) |

O script produz resultados com menos detalhe, mas não quebra. Instale as
dependências para funcionalidade completa:

```bash
pip install -r requirements.txt  # Dependências centrais
# Opcionais (instale individualmente, conforme a necessidade):
pip install spacy sentence-transformers scikit-learn language-tool-python
```

### Permissão negada no install.sh

**Sintoma**: `./install.sh` devolve "Permission denied".

**Correção**:
```bash
chmod +x install.sh
./install.sh
```

### Windows: a política de execução do PowerShell bloqueia a instalação

**Sintoma**: o `install.ps1` falha com "running scripts is disabled on this
system".

**Correção**:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-WebRequest `
  -Uri https://raw.githubusercontent.com/AgriciDaniel/claude-blog/main/install.ps1 `
  -OutFile install.ps1
Get-FileHash ./install.ps1 -Algorithm SHA256
pwsh -File ./install.ps1
```

Inspecione o arquivo baixado e compare o digest com a documentação da release
antes de executar.

---

## Problemas de qualidade de conteúdo

### Notas baixas (abaixo de 60)

**Sintoma**: `/blog analyze` devolve nota abaixo de 60 (classificação "Refazer").

**Causas comuns e correções**:

| Problema | Impacto | Correção |
|----------|---------|----------|
| Afirmações importantes sem clareza ou respaldo | Pontos de prontidão e de conteúdo variam | Declare o ponto cedo e acrescente evidência verificada onde necessário; sem extensão fixa |
| Estatística inventada | Problema crítico de integridade | Remova ou substitua por respaldo verificado |
| Imagens ausentes | Depende do contexto | Acrescente imagem só quando ela melhorar o entendimento |
| Gráficos ausentes | Depende do contexto | Acrescente gráfico só quando as relações de dados exigirem |
| Sem seção de perguntas frequentes | Sem penalidade na nota | Acrescente perguntas só quando dúvidas reais justificarem |
| Ritmo difícil de parágrafo | Apenas consultivo | Divida ou junte trechos quando a compreensão melhorar |
| `lastUpdated` ausente | Sem penalidade automática | Acrescente só depois de uma atualização substantiva, e mantenha verdadeiro |
| Autopromoção excessiva | Problema editorial | Remova a promoção que distrai da tarefa do leitor |

**Fluxo rápido de correção**:
```
1. /blog analyze <arquivo>           # Obtém a nota e os problemas
2. /blog rewrite <arquivo>           # Corrige a maioria automaticamente
3. /blog analyze <arquivo>           # Verifica a melhora
```

### Ponto de seção importante não detectado

**Sintoma**: o relatório de nota diz que uma seção importante não tem um ponto
claro e sustentado, mesmo contendo dados.

**Causa**: uma afirmação relevante precisa de respaldo de fonte perto o bastante
para o leitor identificar o que a fonte comprova. Coloque a evidência onde ela
melhor sustenta a compreensão; ela pode aparecer no primeiro parágrafo ou num
posterior.

**Exemplo de posicionamento sustentado**:
```markdown
## Como a busca por IA afeta o tráfego de blog?

As AI Overviews causaram, inicialmente, queda de 61% no CTR orgânico em 3.119
consultas, num estudo de 2025 da Seer Interactive
([Seer Interactive](https://seerinteractive.com), 2025). Relatos posteriores de
2026 mostraram recuperação parcial do CTR em alguns conjuntos de consulta, então
trate o número como contexto histórico, não como taxa atual universal.
```

**Exemplo de atribuição sem sustentação**:
```markdown
## Como a busca por IA afeta o tráfego de blog?

O cenário da busca está mudando rapidamente. Muitos profissionais de marketing
estão preocupados com o futuro do tráfego orgânico.

Segundo a Seer Interactive, o CTR caiu 61%.
```

O problema do segundo exemplo não é a posição do parágrafo. A medição relevante
não tem citação utilizável nem contexto suficiente do estudo para ser verificada.

### Estatísticas sinalizadas como "inventadas"

**Sintoma**: o relatório de qualidade sinaliza estatísticas como inventadas ou
sem fonte.

**Causa**: o sistema de pontuação procura atribuição inline num raio de 200
caracteres do número. Citações ausentes ou malformadas disparam esse sinal.

**Formato correto de atribuição**:
```markdown
queda inicial de 61% no CTR orgânico ([Seer Interactive](https://seerinteractive.com), 2025)
```

**Formatos que podem não ser detectados**:
```markdown
Segundo um estudo recente, o CTR caiu 61%.          # Sem nome de fonte nem link
CTR caiu 61% (fonte: Seer Interactive)              # Sem URL
CTR caiu 61%. Fonte: Seer Interactive [1]           # Estilo de nota de rodapé
```

---

## Problemas de template

### Template não carrega

**Sintoma**: o `/blog write` não segue a estrutura de template esperada para o
tipo de conteúdo.

**Causas e correções**:

1. **Templates não instalados**: confirme que o diretório existe:
   ```bash
   ls ~/.claude/skills/blog/templates/
   ```
   Se estiver vazio ou ausente, rode `./install.sh` de novo.

2. **Caminho de instalação errado**: os templates precisam estar em
   `~/.claude/skills/blog/templates/`, não no diretório
   `skills/blog/templates/` do repositório.

3. **Arquivo de template corrompido**: copie de novo do repositório:
   ```bash
   cp skills/blog/templates/*.md ~/.claude/skills/blog/templates/
   ```

### Template errado escolhido

**Sintoma**: o `/blog write` escolhe um template de guia prático quando você
queria uma lista.

**Correção**: especifique o tipo de conteúdo explicitamente:
```
/blog write listicle: "10 Melhores Ferramentas de Monitoramento para 2026"
/blog write --type comparison "Datadog versus Grafana"
```

Ou declare o tipo em linguagem natural:
```
/blog write um post comparativo sobre Datadog versus Grafana
```

---

## Problemas de agente

### Agente não é disparado

**Sintoma**: a sub-skill não delega para um subagente (blog-researcher,
blog-writer etc.) e tenta fazer tudo internamente.

**Causas**:

1. **Arquivo do agente não instalado**: confira se os arquivos existem:
   ```bash
   ls ~/.claude/agents/blog-*.md
   ```
   Esperado: `blog-researcher.md`, `blog-writer.md`, `blog-seo.md`,
   `blog-reviewer.md`, `blog-translator.md`

2. **Frontmatter de skill não suportado**: `allowed-tools` não é campo válido de
   `SKILL.md` e não habilita delegação. Confira o arquivo da sub-skill:
   ```bash
   head -20 ~/.claude/skills/blog-write/SKILL.md
   ```
   Os campos válidos incluem `name`, `description`, `user-invokable`,
   `argument-hint`, `license`, `compatibility`, `metadata` e
   `disable-model-invocation`. As ferramentas do agente ficam em
   `~/.claude/agents/blog-*.md`.

3. **Versão do Claude Code**: o disparo de agente por `Task` exige uma versão
   recente do Claude Code. Atualize para a mais nova.

### Agente produz saída de baixa qualidade

**Sintoma**: o agente blog-writer produz conteúdo que não segue a formatação de
resposta antecipada ou outras regras.

**Correção**: normalmente isso significa que o agente não carregou os arquivos de
referência pertinentes. Rode o comando de novo: o orquestrador deve carregar as
referências antes de disparar o agente. Se persistir:

1. Confirme que os arquivos de referência existem:
   ```bash
   ls ~/.claude/skills/blog/references/
   ```
2. Reinstale as referências:
   ```bash
   cp skills/blog/references/*.md ~/.claude/skills/blog/references/
   ```

---

## Problemas de schema e SEO

### Detecção de schema falhando

**Sintoma**: `/blog seo-check` ou `/blog analyze` reporta "nenhum schema
detectado", mesmo que o post tenha marcação JSON-LD.

**Causas**:

1. **Schema injetado por JavaScript**: rastreadores de IA (GPTBot, ClaudeBot,
   PerplexityBot) e o script de análise não enxergam schema injetado no cliente
   por JavaScript. O schema precisa estar presente no código-fonte HTML
   (renderizado no servidor).

   **Como verificar**: desative o JavaScript no navegador e veja o código-fonte.
   Se o bloco `<script type="application/ld+json">` sumir, seu schema é injetado
   por JS.

   **Correção**: mova o schema para HTML renderizado no servidor:
   - Next.js: use `generateMetadata()` ou `<script>` no `layout.tsx`
   - Hugo: acrescente ao partial `<head>` do template
   - WordPress: use um plugin que renderize em PHP, não em JS

2. **Schema em formato errado**: o analisador procura blocos
   `<script type="application/ld+json">`. Outros formatos (Microdata, RDFa)
   podem não ser detectados.

3. **Componente FAQSchema em MDX**: se você usa um componente React como
   `<FAQSchema>`, garanta que ele renderize o JSON-LD na saída HTML, não apenas
   as perguntas visuais.

### Erros de validação de JSON-LD

**Sintoma**: o `/blog schema` gera marcação que falha na validação.

**Correção**: teste o JSON-LD gerado em:
- https://validator.schema.org/
- https://search.google.com/test/rich-results

Problemas comuns:
- Campos `@context` ou `@type` ausentes
- `dateModified` não bate com `lastUpdated` no frontmatter
- URL da imagem inacessível (devolve 404)
- O `@type` do autor deveria ser `Person`, não `Organization`

---

## Problemas específicos de plataforma

### Erros de compilação de MDX depois de write ou rewrite

**Sintoma**: o arquivo MDX gerado falha ao compilar no Next.js.

**Causas comuns**:

| Erro | Causa | Correção |
|------|-------|----------|
| `stroke-width` não é válido | Atributos HTML dentro de JSX | Converta para camelCase: `strokeWidth` |
| `class` não é válido | `class` do HTML dentro de JSX | Use `className` |
| Erro de sintaxe em `style="..."` | Estilo como string em JSX | Use objeto: `style={{...}}` |
| `{` inesperado | Chaves no texto markdown | Escape: `\{` |
| `<` no conteúdo de texto | Sinais de menor na prosa | Use `&lt;` ou envolva em crases |

**Prevenção**: quando a plataforma é detectada como MDX/Next.js, as sub-skills
usam automaticamente sintaxe compatível com JSX. Se os erros persistirem,
especifique a plataforma explicitamente:

```
/blog write "tema" --format mdx
```

### Formato de frontmatter incompatível no Hugo

**Sintoma**: o Hugo não reconhece os campos de frontmatter em YAML.

**Correção**: o Hugo usa frontmatter TOML por padrão (delimitadores `+++`). Se o
seu site Hugo usa YAML (delimitadores `---`), acrescente ao `hugo.toml`:
```toml
[markup.frontmatter]
  date = ["date"]
  lastmod = ["lastUpdated", "lastmod"]
```

---

## Problemas de desempenho

### Comandos rodando devagar

**Sintoma**: `/blog write` ou `/blog brief` demora muito para concluir.

**Causas**:
- **Fase de pesquisa**: as chamadas de WebSearch por estatísticas e imagens podem
  levar de 30 a 60 segundos, conforme o tema
- **Geração de gráfico**: cada invocação do `blog-chart` acrescenta de 10 a 20 segundos
- **Contexto grande**: carregar muitos arquivos de referência aumenta o tempo de processamento

**Mitigação**:
- Gere um briefing antes (`/blog brief`) para adiantar a pesquisa e depois use
  o `/blog write` com o briefing (pula a fase de pesquisa)
- Para análise, use o `analyze_blog.py` diretamente, para métricas automatizadas mais rápidas

### Modo em lote do analyze_blog.py lento em diretórios grandes

**Sintoma**: o modo `--batch` demora muito em diretórios com muitos arquivos.

**Correção**: o script processa os arquivos em sequência. Para diretórios
grandes, analise subconjuntos:
```bash
python3 analyze_blog.py posts/2026/ --batch    # Só os posts de 2026
python3 analyze_blog.py posts/drafts/ --batch  # Só os rascunhos
```

---

## Como obter ajuda

Se o seu problema não está listado aqui:

1. **Cheque a versão**: garanta que você tem o `claude-blog` mais recente:
   ```bash
   cd claude-blog && git pull && ./install.sh
   ```

2. **Verifique a integridade dos arquivos**: compare os instalados com o repositório:
   ```bash
   diff ~/.claude/skills/blog/SKILL.md skills/blog/SKILL.md
   ```

3. **Reinicie a instalação**: remova e instale de novo:
   ```bash
   ./uninstall.sh && ./install.sh
   ```

4. **Abra uma issue**: https://github.com/AgriciDaniel/claude-blog/issues
