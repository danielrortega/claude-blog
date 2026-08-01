# Política de Privacidade

O **Claude Blog** é um plugin do Claude Code que roda inteiramente na sua máquina local. Ele não coleta, armazena, transmite nem compartilha dados pessoais ou informações de uso.

## O que este plugin NÃO faz

- Não coleta métricas de uso nem telemetria
- Não envia dados a servidor externo (exceto quando você usa explicitamente busca na web, chamadas de API a plataformas de CMS ou servidores MCP que você mesmo configurou)
- Não cria contas nem exige autenticação
- Não armazena cookies nem identificadores de rastreamento
- Não acessa dados além dos arquivos e URLs que você fornece

## Serviços de terceiros

Quando você invoca certos comandos explicitamente, o plugin pode interagir com serviços externos **em seu nome e sob seu controle**:

| Recurso | Serviço | Quando |
|---------|---------|--------|
| Geração de imagem por IA | API do Google Gemini (via nanobanana-mcp) | Somente ao rodar `/blog image` com sua própria chave de API configurada |
| Narração em áudio | API de TTS do Google Gemini | Somente ao rodar `/blog audio` com sua própria chave de API configurada |
| Pesquisa e captura na web | Buscadores, páginas públicas | Usado pela maioria dos comandos para pesquisa, análise de resultados, verificação de links e checagem de fontes (`/blog write`, `/blog rewrite`, `/blog analyze`, `/blog brief`, `/blog outline`, `/blog strategy`, `/blog seo-check`, `/blog factcheck`, `/blog geo`, `/blog calendar`, `/blog persona`, `/blog cannibalization`) |
| Dados de resultado de busca e palavra-chave | API DataForSEO (cerca de US$ 0,01 por chamada) | Somente ao rodar `/blog cannibalization --api` com suas próprias credenciais DataForSEO. O modo local (padrão) não exige API |
| Sincronização de taxonomia de CMS | APIs de WordPress, Shopify, Ghost, Strapi, Sanity | Somente ao rodar `/blog taxonomy` com suas próprias credenciais de CMS |
| Pesquisa no NotebookLM | Google NotebookLM | Somente ao rodar `/blog notebooklm` com sua própria configuração |
| Dados de API do Google | Google PageSpeed Insights, CrUX, Search Console, GA4, YouTube Data API, Cloud NLP, Planejador de Palavras-chave, e Indexing API apenas para URLs de JobPosting ou transmissão ao vivo | Somente ao rodar comandos `/blog google` com suas próprias credenciais em `~/.config/claude-seo/google-api.json` |

Todas as chaves de API e credenciais ficam armazenadas localmente, nas suas variáveis de ambiente ou em arquivos `.env`. Este plugin nunca transmite suas credenciais a nenhuma parte além do serviço que você está chamando explicitamente.

## Residência dos dados

Todo conteúdo gerado (posts, imagens, arquivos de áudio, relatórios de análise) é salvo apenas no seu sistema de arquivos local.

## Arquivos de contexto na raiz do projeto (v1.8.0)

Três arquivos opcionais podem ser criados na raiz de qualquer projeto que use este plugin. Eles são lidos pelo orquestrador quando presentes e ignorados em silêncio quando ausentes. NUNCA são transmitidos para fora da sua máquina:

| Arquivo | Criado por | Finalidade | Nota de privacidade |
|---|---|---|---|
| `BRAND.md` | `/blog brand init` | Público, posicionamento, regras editoriais, expressões proibidas, diferenciação frente a concorrentes | Pode conter posicionamento confidencial. Acrescente ao `.gitignore` se o repositório for público e o contexto de marca não for. |
| `VOICE.md` | `/blog brand init` | Assinatura de tom, regras lexicais, padrões de título | Em geral seguro para commitar; espelha o JSON da persona. |
| `DISCOURSE.md` | `/blog discourse <tema>` | Briefing de pesquisa de discurso entre plataformas sobre um tema | O tema e o briefing ficam visíveis apenas localmente. O script que produz o arquivo (`scripts/discourse_research.py`) lê resultados de busca já coletados de um arquivo temporário que você indica e emite o briefing. O script em si não faz chamadas de rede. |

Se algum desses arquivos contiver informação confidencial (posicionamento de concorrentes, estratégia interna de produto, pesquisa de discurso sobre temas privados), acrescente-o ao `.gitignore` antes de commitar.

## Contato

Para dúvidas de privacidade, abra uma issue em: https://github.com/AgriciDaniel/claude-blog/issues

## Última atualização

2026-05-17
