# TODO - Roadmap do claude-blog

## Fase 2 (próxima)
- [x] Heurística de prontidão para citação por IA (visões editoriais não calibradas de 0 a 100 para ChatGPT, Perplexity e AI Overview; v1.10.0, revisão de veracidade na v2.1.0)

## Fase 3 (futuro)
- [ ] Integrações MCP (Ahrefs, Semrush)
- [ ] Teste A/B automatizado de títulos via integração com analytics
- [ ] Painel de desempenho de conteúdo (notas agregadas, tráfego, citações)
- [ ] Skill `blog-sxo` (metodologia SXO de Florian Schmitz, pontuação de persona no lado do conteúdo; adiada na v1.7.0 até o desacoplamento do DataForSEO)
- [ ] Skill `blog-drift` (linha de base em sala limpa mais diff do conteúdo ao longo do tempo; a submissão original foi rejeitada por chave de API embutida no código)
- [ ] Seções em `docs/COMMANDS.md` para os 6 comandos da v1.7.0 (`cluster`, `multilingual`, `translate`, `localize`, `locale-audit`, `flow`)
- [ ] Template de referência `skills/blog-cluster/templates/cluster-map.html` (hoje a skill gera a partir da especificação a cada invocação)

## Concluído
- [x] Aprendizado de estilo de escrita (`/blog style learn`, v1.10.0)
- [x] Detecção de decaimento de conteúdo (`/blog decay`, v1.10.0)
- [x] Portão de qualidade em pre-commit com nota mínima padrão de 70 (`scripts/quality_gate.py`, v1.10.0)
- [x] Fluxos de CI/CD (`.github/workflows/ci.yml`, adicionado na v1.3.0)
- [x] Google Search Console e PageSpeed Insights (sub-skill blog-google, v1.6.5)
- [x] Submissão ao marketplace de plugins (marketplace.json, v1.6.2)
- [x] Geração de imagens por IA (sub-skill blog-image com Gemini, v1.4.0)
- [x] Reaproveitamento em podcast e áudio (sub-skill blog-audio com Gemini TTS, v1.6.0)
- [x] Suporte a conteúdo multilíngue (i18n, geração de hreflang): `blog-multilingual` + `blog-translate` + `blog-localize` + `blog-locale-audit` (v1.7.0, por Chris Mueller)
- [x] Integração do framework FLOW (`blog-flow` + `scripts/sync_flow.py`, v1.7.0)
- [x] Planejamento e execução de cluster semântico de temas (`blog-cluster`, v1.7.0, vencedor do Pro Hub Challenge por Lutfiya Miller)
- [x] Guardrails mecânicos de segurança (`tests/test_security_guardrails.py`, v1.7.0)
