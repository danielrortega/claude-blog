# claude-blog v2.1.1: Roteiro de Demonstração

Fluxo de demonstração de ponta a ponta que exercita todas as integrações
conectadas: incorporação do YouTube (blog-google), pesquisa de palavras-chave
(DataForSEO MCP), geração de imagem por IA (banana / blog-image via
nanobanana-mcp), gráficos SVG inline (blog-chart) e SVGs animados (svg-animate).

> **Nota de segurança**: esta demonstração usa o padrão de expansão de variáveis
> de ambiente mais credenciais carregáveis por `source`, que fecha as auditorias
> VULN-001 e VULN-003. `.mcp.json` e `.env.local` estão ambos em `chmod 0600` e no
> gitignore. As credenciais por skill ficam em
> `~/.config/claude-seo/google-api.json` (também em modo 0600). A lista completa
> de endurecimento está em [SECURITY.md](../.github/SECURITY.md).

---

## Pré-voo (rode uma vez por sessão de shell)

Os servidores MCP em `.mcp.json` referenciam variáveis de ambiente do shell. Elas
são preenchidas fazendo `source` do `.env.local`, que está no gitignore. Reinicie
o Claude Code depois do `source`, para o subprocesso MCP herdar os valores.

```bash
cd ~/claude-blog
source .env.local
echo "GOOGLE_AI_API_KEY length: ${#GOOGLE_AI_API_KEY}"     # deve imprimir 39
echo "DATAFORSEO_USERNAME set:  ${DATAFORSEO_USERNAME:+yes}"  # deve imprimir yes
# Depois reinicie o Claude Code para os servidores MCP pegarem as variáveis
```

Para uma configuração persistente entre sessões de shell, acrescente as mesmas
linhas `export` ao `~/.bashrc`. Mas atenção: elas ficarão visíveis a todo programa
que você iniciar a partir daquele shell.

---

## O que está conectado (verificado)

| Componente | Skill / Script | Situação |
|---|---|---|
| Google Search Console + inspeção de URL | `blog-google google_auth --check` | Nível 1 detectado |
| PageSpeed Insights + CrUX + histórico do CrUX | `blog-google pagespeed_check / crux_history` | Nível 1 detectado |
| Busca no YouTube + aprofundamento de vídeo | `blog-google youtube_search` | Chave de API ativa |
| Tráfego orgânico no GA4 | `blog-google ga4_report` | Exige `ga4_property_id` em google-api.json |
| Geração de imagem nanobanana (Diretor de Criação) | Skill `/banana`, `/blog image` | MCP conectado, precisa reiniciar |
| DataForSEO: resultados ao vivo, palavras-chave, backlinks, visibilidade em IA | Skill `seo-dataforseo` (no claude-seo) | MCP conectado, precisa reiniciar |
| Gráficos SVG inline (modo escuro) | Capacidade interna `blog-chart` + skill `/svg-chart` | Python puro, já funciona |
| SVGs animados (SMIL) | Skill `/svg-animate` | SVG puro, já funciona |
| Execução de cluster de temas | `/blog cluster` | Padrão eixo e raios |
| Publicação multilíngue | `/blog multilingual --languages de,fr,es` | Dispara o agente tradutor |

---

## Verificação (sem chamadas de API, executável agora)

```bash
# 1. Validação estrutural do nanobanana (8/8 devem passar)
python3 skills/blog-image/scripts/validate_image_setup.py

# 2. Detecção de nível da API do Google
python3 skills/blog-google/scripts/google_auth.py --tier --json

# 3. Validação do plugin
claude plugin validate .

# 4. Suíte completa de testes
python -m pytest tests/ -q

# 5. Gráfico SVG local de amostra
ls -la demo-output/demo-chart.svg demo-output/demo-animated.svg
```

---

## Fluxo A: post completo com todos os recursos (recomendado)

Use numa sessão ao vivo para exercitar todas as integrações conectadas.
Cada passo é um comando de barra. Tempo total estimado: 8 a 12 minutos.

```
1. /blog brief "Citações em busca por IA: como se destacar no ChatGPT e no Perplexity"
   -> Gera um briefing com público, intenção e ângulos competitivos.
      (Ainda sem API externa; trabalho puro de LLM.)

2. /seo dataforseo keywords "citações em busca por IA" --limit 30
   -> Dados de palavra-chave ao vivo (volume, dificuldade, intenção).
      Consome créditos do DataForSEO.

3. /seo dataforseo serp "como ser citado no ChatGPT"
   -> Resultados de busca ao vivo, incluindo AI Overviews.
      Consome créditos do DataForSEO.

4. /blog google youtube search "AI search citations 2025" --max-results 5
   -> Vídeos candidatos do YouTube com dados de adequação editorial.
      Use um vídeo apenas quando for relevante, correto, útil e elegível.
      Cota gratuita.

5. /blog write "citações em busca por IA" --brief
   -> Escreve o post completo. Durante a escrita, ele vai:
      - invocar a capacidade interna blog-chart para gerar gráficos SVG inline
      - chamar /blog image (nanobanana) para gerar a capa e a imagem principal
      - embutir vídeos do YouTube via carregamento tardio com srcdoc (cerca de 5KB)
      - acrescentar JSON-LD coerente com o conteúdo; FAQPage apenas quando as
        perguntas visíveis justificarem
      - reforçar as explicações apoiadas em evidência e o material original comprovado

6. /blog seo-check <caminho_de_saida>
   -> Valida título, meta, títulos de seção, schema e texto alternativo.

7. /blog geo <caminho_de_saida>
   -> Auditoria de prontidão para citação por IA (citabilidade dos trechos,
      âncoras de ano, ponderação por nível de fonte).

8. /blog analyze <caminho_de_saida>
   -> Nota de qualidade de 100 pontos em 5 categorias.
```

---

## Fluxo B: demonstrações de recurso único (quando você quer destacar uma coisa só)

### B1. "Imagem de capa a partir de um tema"

```
/banana generate "a clean editorial header for a blog post about
                  AI search citations, photorealistic, soft natural
                  light, 16:9 aspect ratio, suitable as a 1200x630
                  Open Graph image"
```

Saída: caminho de arquivo em `~/Documents/nanobanana_generated/`. O Banana atua
como Diretor de Criação e constrói o prompt de 5 componentes; a skill carrega
automaticamente `references/gemini-models.md` e `references/prompt-engineering.md`,
conforme sua regra OBRIGATÓRIA.

### B2. "Gráfico SVG inline a partir de dados"

```
/svg-chart bar from-data
[cole os dados]
ChatGPT,35
Claude,22
Perplexity,18
Gemini,15
Copilot,10
```

Dentro de `/blog write` ou `/blog rewrite`, os mesmos dados podem ser renderizados
pela capacidade interna `blog-chart`.

### B3. "SVG animado explicando um conceito"

```
/svg-animate "loading spinner for a topic-cluster build with
              progress bar and pulsing dots, 3-second loop,
              dark mode"
```

### B4. "Resultados de busca ao vivo para uma consulta"

```
/seo dataforseo serp-youtube "claude code skill"
/seo dataforseo serp "blog SEO 2026"
/seo dataforseo intent "best ai citation tool"
```

### B5. "Inteligência de backlinks"

```
/seo dataforseo backlinks ahrefs.com --limit 50
/seo dataforseo competitors search.brave.com
```

---

## Solução de problemas

| Sintoma | Causa | Correção |
|---|---|---|
| `${GOOGLE_AI_API_KEY}` aparece literal no ambiente MCP | O Claude Code foi iniciado antes do `source .env.local` | Rode `source .env.local` e reinicie o Claude Code |
| Ferramentas MCP do `dataforseo` indisponíveis | O mesmo caso acima, ou o pacote npm precisa ser baixado | Aguarde 30s na primeira chamada (o npx baixa o pacote) |
| "MCP not configured" vindo de `/blog image` | O MCP não carregou nesta sessão | Verifique se `.mcp.json` existe e reinicie o Claude Code |
| `pagespeed_check` diz "API key invalid" | Chave revogada ou limite de taxa | Confira a chave em [aistudio.google.com/apikey](https://aistudio.google.com/apikey) |
| DataForSEO devolve 401 | Usuário ou senha errados, ou conta inativa | Confira as credenciais em [app.dataforseo.com](https://app.dataforseo.com) |
| A busca no YouTube volta vazia | Cota gratuita da YouTube Data API esgotada | Aguarde a renovação da cota (meia-noite no Pacífico) |

---

## Rotação de credenciais

```bash
# 1. Edite o .env.local com os novos valores
$EDITOR .env.local

# 2. Refaça o source e reinicie o Claude Code
source .env.local && exec claude code   # ou como você costuma iniciar

# 3. Para a config do Google por skill (usada direto pelos scripts do blog-google):
$EDITOR ~/.config/claude-seo/google-api.json    # modo 0600

# 4. Para rotação permanente (em todos os shells):
# remova o antigo `export GOOGLE_AI_API_KEY=...` do ~/.bashrc
# e acrescente o novo
```

Para remover as credenciais por completo:

```bash
shred -u .env.local                              # exclusão segura
shred -u ~/.config/claude-seo/google-api.json
# o próprio .mcp.json só tem marcadores de expansão de variável, nada a destruir
```

Os scripts `uninstall.{sh,ps1}` (correção pós-auditoria VULN-805) também apagam
`~/.config/claude-seo/{oauth-token,google-api}.json` automaticamente.

---

## O que foi conectado nesta sessão

- `.mcp.json` (modo 0600, no gitignore): acrescentado o servidor `dataforseo`
  ao lado do `nanobanana-mcp` existente. Ambos fixados (`@1.1.1` e
  `@2.8.10`). Ambos apenas com expansão de variável, sem chave literal.
- `.env.local` (modo 0600, no gitignore): as credenciais literais ficam aqui.
  Faça `source` antes de iniciar o Claude Code.
- `~/.config/claude-seo/google-api.json` (modo 0600, privado do usuário):
  contém a `api_key` para os scripts do blog-google, que a leem diretamente,
  não via MCP.
- `demo-output/demo-chart.svg`: gráfico de barras SVG estático de amostra.
- `demo-output/demo-animated.svg`: SVG animado de amostra (SMIL).
- `.gitignore`: acrescentado `demo-output/`, para os artefatos da demonstração
  não poluírem o `git status`.

Nenhum arquivo versionado foi alterado. Nenhum commit. A demonstração fica local.
