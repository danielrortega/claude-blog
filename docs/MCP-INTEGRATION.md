# Guia de Integração MCP

Integrações opcionais de servidor Model Context Protocol (MCP) que estendem o
`claude-blog` com dados ao vivo de plataformas de SEO, serviços de analytics e
ferramentas de monitoramento de desempenho.

**Importante**: o `claude-blog` funciona por completo sem nenhum servidor MCP.
Estas integrações são acréscimos opcionais para equipes que já usam essas
plataformas.

---

## Panorama

```
                    +---------------------------+
                    |      claude-blog          |
                    |    comandos /blog          |
                    +------+----+----+----------+
                           |    |    |
              +------------+    |    +------------+
              |                 |                  |
              v                 v                  v
  +-----------------+  +----------------+  +------------------+
  | DataForSEO MCP  |  | Servidores MCP |  | Servidores MCP   |
  | (recomendado)   |  | individuais    |  | próprios         |
  |                 |  |                |  |                  |
  | - Dados de SERP |  | - GSC          |  | - Analytics      |
  | - Palavras-chave|  | - Ahrefs       |  | - APIs de CMS    |
  | - Backlinks     |  | - Semrush      |  | - Dados próprios |
  | - On-page       |  | - PageSpeed    |  |                  |
  | - Dados de domínio |              |  |                  |
  | - Conteúdo      |  |                |  |                  |
  | - Otimização IA |  |                |  |                  |
  +-----------------+  +----------------+  +------------------+
```

---

## Nano Banana MCP - geração de imagem por IA

**O servidor nanobanana-mcp habilita geração de imagem por IA** dentro dos fluxos
de blog. Quando configurado, `/blog write` e `/blog rewrite` podem gerar imagens
principais próprias, ilustrações inline e cartões de prévia social via Gemini,
além da curadoria de fotos de banco em Pixabay, Unsplash e Pexels.

### O que habilita

| Recurso | Sem o nanobanana-mcp | Com o nanobanana-mcp |
|---------|----------------------|----------------------|
| Imagens principais e de capa | Só banco de imagens | Banco de imagens mais imagens próprias geradas por IA |
| Ilustrações inline | Só banco de imagens | Banco de imagens mais ilustrações por IA específicas do tema |
| Cartões OG e sociais | Recorte de banco de imagens | Prévias sociais próprias geradas por IA |
| Edição de imagem | Indisponível | Edita imagens existentes do blog (recorte, realce, mudança de estilo) |
| Uso avulso | Indisponível | `/blog image generate <ideia>` para qualquer necessidade de imagem |

### Configuração

O script de configuração grava por padrão nas configurações globais privadas do
usuário no Claude Code (mais seguro; nunca chega ao git). Para usar um
`.mcp.json` local do projeto, opte explicitamente com `--project` (o script se
recusa a gravar uma chave literal em arquivo versionado).

```bash
# Recomendado: grava ~/.claude/settings.json (privado do usuário, modo 0600)
python3 skills/blog-image/scripts/setup_image_mcp.py --key SUA_CHAVE

# Local do projeto (apenas expansão de variável, NUNCA guarda a chave literal)
python3 skills/blog-image/scripts/setup_image_mcp.py --key SUA_CHAVE --project
# Depois exporte a chave no shell, para a expansão de variável resolver:
export GOOGLE_AI_API_KEY="sua-chave-do-aistudio.google.com"
```

Obtenha uma chave gratuita em: https://aistudio.google.com/apikey

> **Segurança**: o `.mcp.json` está no gitignore desde 2026-04-27. Um template
> versionado `.mcp.example.json` fica ao lado. O script de configuração fixa a
> versão do pacote nanobanana-mcp (`@ycse/nanobanana-mcp@1.1.1`) para mitigar
> risco de cadeia de suprimentos na atualização automática do `npx -y`.

### Verificar a configuração

```bash
python3 skills/blog-image/scripts/validate_image_setup.py
```

### Requisitos

- Node.js 18+ (para o `npx`)
- Chave de API do Google AI (camada gratuita: cerca de 10 requisições por minuto, cerca de 500 imagens por dia)

---

## DataForSEO MCP (recomendado)

**O DataForSEO é a integração MCP recomendada para o `claude-blog`.** Ele oferece
uma API unificada cobrindo dados de resultados de busca, pesquisa de
palavras-chave, análise de backlinks, auditoria on-page, analytics de domínio,
análise de conteúdo e otimização para IA, dispensando integrações separadas de
Ahrefs, Semrush, GSC e PageSpeed.

### O que habilita

| Recurso | Sem o DataForSEO MCP | Com o DataForSEO MCP |
|---------|----------------------|----------------------|
| Análise de resultados de busca | Só WebSearch | Resultados ao vivo de Google, Bing e Yahoo com todos os recursos (AI Overviews, "As pessoas também perguntam" etc.) |
| Pesquisa de palavras-chave | Indisponível | Volume de busca, CPC, concorrência, dificuldade e intenção |
| Análise de backlinks | Indisponível | Domínios referenciadores, texto âncora, nota de spam, links novos e perdidos |
| Auditoria on-page | Revisão manual | Rastreio automatizado, meta tags, Core Web Vitals, notas do Lighthouse |
| Analytics de domínio | Indisponível | Detecção de tecnologia, dados de WHOIS, análise de domínio de concorrentes |
| Análise de conteúdo | Só pontuação de qualidade | Análise de sentimento, densidade de palavra-chave, pontuação de qualidade |
| Otimização para IA | Auditoria de conteúdo GEO | Rastreamento de menções em LLM, coleta no ChatGPT, métricas de visibilidade em IA |
| Pesquisa de concorrentes | Só WebSearch | Palavras-chave ranqueadas, estimativa de tráfego, análise de lacuna de conteúdo |

### Fluxos ampliados

**`/blog brief` com dados do DataForSEO**:

Os briefings de conteúdo passam a incluir métricas reais do DataForSEO Labs:

```
Palavras-chave alvo (DataForSEO Labs)
- Principal: "kubernetes monitoring" - 2.400/mês, KD 45, intenção: informacional
- Secundária: "k8s observability" - 890/mês, KD 32, intenção: informacional
- Pergunta: "how to monitor kubernetes" - 720/mês, KD 28

Análise dos resultados de busca dos concorrentes
| Posição  | Domínio             | Backlinks | Palavras   |
|----------|---------------------|-----------|------------|
| #1       | competitor-a.com    | 142       | 3.200      |
| #2       | competitor-b.com    | 89        | 2.800      |
| #3       | competitor-c.com    | 67        | 4.100      |
```

**`/blog strategy` com dados do DataForSEO**:

Os documentos de estratégia ganham inteligência competitiva:

```
Comparação de domínios (DataForSEO Labs)
| Domínio          | Tráfego orgânico | Palavras-chave | Backlinks | Rank |
|------------------|------------------|----------------|-----------|------|
| competitor-a.com | 45.000/mês       | 2.340          | 12.400    | 52   |
| competitor-b.com | 28.000/mês       | 1.200          | 8.900     | 47   |
| seu-site.com     | 3.200/mês        | 380            | 1.100     | 31   |

Lacuna de conteúdo: 234 palavras-chave em que os concorrentes ranqueiam e você não
```

**`/blog geo` com dados de otimização para IA do DataForSEO**:

As auditorias de citação por IA passam a incluir métricas de visibilidade em LLM:

```
Relatório de visibilidade em IA (DataForSEO AI Optimization)
| Métrica               | Valor | Observações                |
|-----------------------|-------|----------------------------|
| Menções em LLM        | 12    | Em ChatGPT e Gemini        |
| AI Overview presente  | Sim   | Em 3 de 5 palavras-chave   |
| Sentimento da marca   | 0,72  | Positivo                   |
| URLs citadas          | 4     | Páginas citadas diretamente|
```

### Configuração

**Instalação em um comando (recomendado):**

Carregue as credenciais de um arquivo local de segredos primeiro, para não
escrevê-las na linha de comando:

```bash
set -a
. ~/.config/dataforseo.env
set +a
```

```bash
claude mcp add dataforseo \
  --env DATAFORSEO_USERNAME="${DATAFORSEO_USERNAME}" \
  --env DATAFORSEO_PASSWORD="${DATAFORSEO_PASSWORD}" \
  -- npx -y dataforseo-mcp-server
```

**Ou servidor remoto (sem instalação local):**

```bash
DATAFORSEO_BASIC_AUTH="$(printf '%s:%s' "$DATAFORSEO_USERNAME" "$DATAFORSEO_PASSWORD" | base64)"
claude mcp add --transport http dataforseo https://mcp.dataforseo.com/http \
  --header "Authorization: Basic ${DATAFORSEO_BASIC_AUTH}"
```

**Ou acrescente manualmente ao `~/.claude/settings.json`:**

```json
{
  "mcpServers": {
    "dataforseo": {
      "command": "npx",
      "args": ["-y", "dataforseo-mcp-server"],
      "env": {
        "DATAFORSEO_USERNAME": "${DATAFORSEO_USERNAME}",
        "DATAFORSEO_PASSWORD": "${DATAFORSEO_PASSWORD}",
        "ENABLED_MODULES": "SERP,KEYWORDS_DATA,ONPAGE,DATAFORSEO_LABS,BACKLINKS,DOMAIN_ANALYTICS,BUSINESS_DATA,CONTENT_ANALYSIS,AI_OPTIMIZATION"
      }
    }
  }
}
```

### Boas práticas

1. **Guarde as credenciais em variáveis de ambiente** (não no settings.json):
   ```bash
   # Guarde DATAFORSEO_USERNAME e DATAFORSEO_PASSWORD neste arquivo em modo 0600.
   chmod 600 ~/.config/dataforseo.env
   set -a
   . ~/.config/dataforseo.env
   set +a
   ```

2. **Use filtragem de campos** para reduzir o consumo de tokens (cerca de 75%):
   Crie um arquivo JSON de configuração de campos e defina `FIELD_CONFIG_PATH`:
   ```json
   {
     "env": {
       "FIELD_CONFIG_PATH": "/caminho/para/dataforseo-field-config.json"
     }
   }
   ```
   Uma configuração de campos abrangente está disponível no repositório em
   `skills/seo/dataforseo-field-config.json` (se você usa a skill companheira `/seo`).

3. **Habilite apenas os módulos necessários** via `ENABLED_MODULES`, para reduzir
   a quantidade de ferramentas disponíveis e melhorar a relevância das respostas.

### Módulos disponíveis

| Módulo | O que fornece |
|--------|---------------|
| `SERP` | Resultados ao vivo de Google, Bing e Yahoo com todos os recursos de busca |
| `KEYWORDS_DATA` | Volume de busca, CPC e concorrência do Google Ads |
| `DATAFORSEO_LABS` | Pesquisa de palavra-chave, análise de domínio, dados de concorrentes |
| `BACKLINKS` | Perfis de backlink, domínios referenciadores, texto âncora |
| `ONPAGE` | Rastreio de site, análise de meta, Core Web Vitals, Lighthouse |
| `DOMAIN_ANALYTICS` | Detecção de tecnologia, registros WHOIS |
| `BUSINESS_DATA` | Fichas do Google Maps, avaliações, informações de negócio |
| `CONTENT_ANALYSIS` | Citações de marca, análise de sentimento, tendências de expressão |
| `AI_OPTIMIZATION` | Rastreamento de menções em LLM, coleta no ChatGPT, descoberta de palavra-chave em IA |

### Requisitos de configuração

1. [Conta DataForSEO](https://dataforseo.com/) com credenciais de API
2. Node.js 18+ (para o `npx dataforseo-mcp-server`)
3. Usuário e senha de API do painel do DataForSEO

---

## Integrações MCP individuais alternativas

Os servidores MCP a seguir podem ser usados no lugar do DataForSEO, ou junto com
ele, por equipes que já têm conta nessas plataformas.

## Google Search Console MCP

### O que habilita

| Recurso | Sem o GSC MCP | Com o GSC MCP |
|---------|---------------|---------------|
| Detecção de decaimento de conteúdo | Checagem manual | Automatizada: sinaliza posts com queda de 20%+ de tráfego no trimestre |
| Acompanhamento de palavra-chave | Indisponível | Ranqueamento e CTR ao vivo |
| Análise de consultas | Indisponível | As consultas reais que trazem tráfego |
| Impacto do AI Overview | Indisponível | Mudanças de CTR quando o AI Overview aparece |
| Agendamento de atualidade | Por tempo (30 dias) | Guiado por dado (queda real de desempenho) |

### Fluxos ampliados

**`/blog audit` com dados do GSC**:

Em vez de pontuar os posts apenas por qualidade de conteúdo, a auditoria passa a
incorporar dados reais de desempenho:

```
Auditoria de blog: 47 posts analisados

| Post              | Qualidade | Tráfego (trim.) | CTR    | Ação             |
|-------------------|-----------|-----------------|--------|------------------|
| ai-search-guide   | 85/100    | -35%            | 1,2%   | Decaimento!      |
| kubernetes-setup  | 72/100    | +12%            | 3,1%   | Ajustes de qualidade |
| react-patterns    | 91/100    | -5%             | 4,2%   | Monitorar        |
```

**`/blog calendar` com dados do GSC**:

Os calendários editoriais passam a priorizar atualizações pelo decaimento real de
tráfego, em vez de ciclos arbitrários de 30 dias:

```
Fila de atualização por atualidade (guiada por dado)
| Post              | Atualizado há | Variação de tráfego | Prioridade |
|-------------------|---------------|---------------------|------------|
| ai-search-guide   | 45 dias       | -35% no trimestre   | Crítica    |
| seo-strategy      | 60 dias       | -22% no trimestre   | Alta       |
| blog-writing-tips | 30 dias       | +5% no trimestre    | Baixa      |
```

### Configuração

Acrescente o servidor MCP do GSC às configurações do Claude Code
(`~/.claude/settings.json`):

```json
{
  "mcpServers": {
    "google-search-console": {
      "command": "npx",
      "args": ["-y", "@anthropic/gsc-mcp-server"],
      "env": {
        "GSC_CREDENTIALS_PATH": "/caminho/para/credentials.json"
      }
    }
  }
}
```

**Requisitos de configuração**:
1. Projeto no Google Cloud com a API do Search Console habilitada
2. Credenciais OAuth ou chave de conta de serviço
3. Site verificado no Google Search Console

---

## Ahrefs MCP

### O que habilita

| Recurso | Sem o Ahrefs MCP | Com o Ahrefs MCP |
|---------|------------------|------------------|
| Análise de backlinks | Indisponível | Domínios referenciadores, distribuição de texto âncora |
| Pesquisa de palavras-chave | Só WebSearch | Volume de busca, dificuldade, recursos de resultado |
| Monitoramento de concorrentes | WebSearch manual | Análise de lacuna e acompanhamento automatizados |
| Análise de lacuna de conteúdo | Indisponível | Palavras-chave em que os concorrentes ranqueiam e você não |
| Domain Rating | Indisponível | Acompanhamento de DR ao vivo |

### Fluxos ampliados

**`/blog brief` com dados do Ahrefs**:

Os briefings de conteúdo podem incluir métricas precisas de palavra-chave:

```
Palavras-chave alvo
- Principal: "kubernetes monitoring" (2.400/mês, KD 45)
- Secundária: "k8s observability" (890/mês, KD 32)
- Pergunta: "how to monitor kubernetes clusters" (720/mês, KD 28)

Lacuna de conteúdo frente aos concorrentes
| Palavra-chave                 | Concorrente A | Concorrente B | Você |
|-------------------------------|---------------|---------------|------|
| kubernetes alerting setup     | #3            | #7            |  -   |
| prometheus vs datadog         | #5            | #2            |  -   |
| k8s monitoring best practices | #1            | #4            | #12  |
```

**`/blog strategy` com dados do Ahrefs**:

Os documentos de estratégia ganham inteligência competitiva com métricas reais:

```
Cenário competitivo
| Concorrente      | DR  | Posts | Tráfego médio/post | Palavras-chave |
|------------------|-----|-------|--------------------|----------------|
| competitor-a.com | 72  | 340   | 2.100              | 890            |
| competitor-b.com | 65  | 180   | 1.400              | 520            |
| seu-site.com     | 45  | 47    | 380                | 120            |

Oportunidade: 234 palavras-chave em que os concorrentes ranqueiam e você não
```

### Configuração

```json
{
  "mcpServers": {
    "ahrefs": {
      "command": "npx",
      "args": ["-y", "@anthropic/ahrefs-mcp-server"],
      "env": {
        "AHREFS_API_KEY": "sua-chave-de-api"
      }
    }
  }
}
```

**Requisitos de configuração**:
1. Conta Ahrefs com acesso à API (plano Standard ou superior)
2. Chave de API do painel do Ahrefs

---

## Semrush MCP

### O que habilita

| Recurso | Sem o Semrush MCP | Com o Semrush MCP |
|---------|-------------------|-------------------|
| Análise de lacuna de palavra-chave | Indisponível | Sobreposição lado a lado com os concorrentes |
| Acompanhamento de posição | Indisponível | Rastreamento diário de posição das palavras-chave alvo |
| Pesquisa de temas | Só WebSearch | Dados do Topic Research do Semrush |
| Auditoria de conteúdo | Só pontuação de qualidade | Qualidade mais tráfego e dados de palavra-chave |

### Fluxos ampliados

**`/blog strategy` com dados do Semrush**:

Pesquisa de temas apoiada no agrupamento de palavras-chave do Semrush:

```
Pilar de conteúdo: monitoramento de Kubernetes
| Cluster de tema        | Palavras-chave | Volume total | KD médio | Nota de lacuna |
|------------------------|----------------|--------------|----------|----------------|
| Instalação e config    | 34             | 12.400       | 38       | Alta           |
| Comparação de ferramentas | 22          | 8.900        | 52       | Média          |
| Boas práticas          | 18             | 6.200        | 41       | Alta           |
| Solução de problemas   | 45             | 15.100       | 29       | Baixa          |
```

### Configuração

```json
{
  "mcpServers": {
    "semrush": {
      "command": "npx",
      "args": ["-y", "@anthropic/semrush-mcp-server"],
      "env": {
        "SEMRUSH_API_KEY": "sua-chave-de-api"
      }
    }
  }
}
```

---

## PageSpeed Insights MCP

### O que habilita

| Recurso | Sem o PSI MCP | Com o PSI MCP |
|---------|---------------|---------------|
| Core Web Vitals | Indisponível | Medições de LCP, FID, CLS e INP |
| Monitoramento de TTFB | Indisponível | Tempo de resposta do servidor (crítico para rastreadores de IA) |
| Pontuação de desempenho | Indisponível | Nota de desempenho do Lighthouse |
| Prontidão para rastreio de IA | Checagem manual | Verificação automatizada de TTFB abaixo de 200ms |

### Fluxos ampliados

**`/blog geo` com dados do PageSpeed**:

As auditorias de citação por IA podem incluir checagens técnicas de desempenho:

```
Prontidão para rastreadores de IA
| Métrica  | Valor  | Alvo         | Situação |
|----------|--------|--------------|----------|
| TTFB     | 145ms  | abaixo de 200ms | Passa |
| LCP      | 2,1s   | abaixo de 2,5s  | Passa |
| CLS      | 0,08   | abaixo de 0,1   | Passa |
| Só JS?   | Não    | Não             | Passa |

Suas páginas estão acessíveis aos rastreadores de IA (GPTBot, ClaudeBot, PerplexityBot).
```

### Configuração

```json
{
  "mcpServers": {
    "pagespeed": {
      "command": "npx",
      "args": ["-y", "@anthropic/pagespeed-mcp-server"],
      "env": {
        "PAGESPEED_API_KEY": "sua-chave-de-api-do-google"
      }
    }
  }
}
```

**Requisitos de configuração**:
1. Projeto no Google Cloud com a API do PageSpeed Insights habilitada
2. Chave de API do Google Cloud Console

---

## Como configurar servidores MCP

Os servidores MCP são configurados no arquivo de configurações do Claude Code. O
local depende da sua instalação:

### Local do arquivo de configurações

| Plataforma | Caminho |
|------------|---------|
| Linux/macOS | `~/.claude/settings.json` |
| Windows | `%USERPROFILE%\.claude\settings.json` |

### Acrescentar um servidor MCP

Edite o `settings.json` para acrescentar servidores sob a chave `mcpServers`:

```json
{
  "mcpServers": {
    "nome-do-servidor": {
      "command": "npx",
      "args": ["-y", "nome-do-pacote"],
      "env": {
        "API_KEY": "sua-chave"
      }
    }
  }
}
```

### Verificar a conexão MCP

Depois de acrescentar um servidor MCP:
1. Reinicie o Claude Code
2. O servidor deve aparecer entre as ferramentas disponíveis
3. Teste com uma consulta simples relacionada à função dele

### Variáveis de ambiente para chaves de API

Nunca versione chaves de API. Use variáveis de ambiente:

```bash
# Acrescente ao ~/.bashrc ou ~/.zshrc
export AHREFS_API_KEY="sua-chave"
export SEMRUSH_API_KEY="sua-chave"
export GSC_CREDENTIALS_PATH="/caminho/para/credentials.json"
export PAGESPEED_API_KEY="sua-chave"
```

Depois referencie-as nas configurações:

```json
{
  "mcpServers": {
    "ahrefs": {
      "command": "npx",
      "args": ["-y", "@anthropic/ahrefs-mcp-server"],
      "env": {
        "AHREFS_API_KEY": "${AHREFS_API_KEY}"
      }
    }
  }
}
```

---

## Fluxos de exemplo

### Detecção de decaimento de conteúdo (GSC mais auditoria de blog)

Combine dados do Google Search Console com a pontuação de qualidade do
`claude-blog` para identificar posts que precisam de atenção imediata:

```
1. /blog audit content/blog/         # Notas de qualidade de todos os posts
2. O GSC MCP fornece dados de tráfego # Variação de tráfego no trimestre
3. O relatório combinado identifica:
   - Alta qualidade com tráfego caindo  --> precisa de atualização
   - Baixa qualidade com tráfego caindo --> precisa de reescrita completa
   - Baixa qualidade com tráfego estável --> otimizar para citação por IA
4. /blog calendar                     # Cronograma de atualização já priorizado
```

### Estratégia de conteúdo informada pela concorrência (Ahrefs mais strategy)

Use dados do Ahrefs para ancorar sua estratégia em inteligência competitiva:

```
1. /blog strategy "seu-nicho"        # Estratégia base a partir da análise
2. O Ahrefs MCP fornece:
   - Ranqueamento de palavra-chave dos concorrentes
   - Palavras-chave de lacuna de conteúdo
   - Oportunidades de backlink
3. O documento de estratégia inclui:
   - Temas pilares apoiados em dados
   - Alvos específicos de palavra-chave com volume e dificuldade
   - Mapeamento das fraquezas dos concorrentes
4. /blog calendar                     # Plano de execução com alvos de palavra-chave
```

### Auditoria de GEO otimizada por desempenho (PSI mais geo)

Valide ao mesmo tempo a qualidade do conteúdo e a prontidão técnica para
rastreadores de IA:

```
1. /blog geo content/blog/post.mdx   # Auditoria de GEO no nível do conteúdo
2. O PageSpeed MCP fornece:
   - Medição de TTFB (precisa ficar abaixo de 200ms)
   - Checagem de renderização por JavaScript
   - Notas de Core Web Vitals
3. O relatório combinado cobre:
   - Otimização de conteúdo (resposta antecipada, atualidade, perguntas)
   - Otimização técnica (TTFB, renderização no servidor, robots.txt)
   - Verificação de acessibilidade aos rastreadores de IA
```

---

## Roadmap

| Integração | Situação | Prioridade |
|------------|----------|------------|
| Nano Banana (Gemini) | **Disponível** | Geração de imagem por IA para conteúdo de blog |
| DataForSEO | **Disponível** | Recomendada: cobre resultados de busca, palavras-chave, backlinks, on-page, domínio, conteúdo e otimização para IA |
| Google Search Console | **Disponível** (via `/blog google gsc`) | Dados próprios de tráfego e CTR |
| Google Analytics (GA4) | **Disponível** (via `/blog google ga4`) | Relatórios de tráfego orgânico |
| API REST do WordPress | Futuro | Baixa |
| Contentful / Sanity CMS | Futuro | Baixa |

Contribuições da comunidade para implementações de servidor MCP são bem-vindas.
