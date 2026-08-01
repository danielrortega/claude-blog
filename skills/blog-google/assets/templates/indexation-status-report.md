# Relatório de status de indexação de URLs

**Propriedade:** {property}
**URLs inspecionadas:** {total_urls}

## Resumo

| Situação | Quantidade | Percentual |
|----------|------------|-----------|
| Indexadas (PASS) | {pass_count} | {pass_pct}% |
| Não indexadas (FAIL) | {fail_count} | {fail_pct}% |
| Neutras | {neutral_count} | {neutral_pct}% |
| Erros | {error_count} | {error_pct}% |

## Resultados detalhados

| URL | Veredito | Estado de cobertura | Estado de fetch | Canônica do Google | Último rastreio |
|-----|----------|---------------------|-----------------|--------------------|-----------------|
{results_table}

## Divergências de canônica

URLs em que o Google escolheu uma canônica diferente da declarada:

| URL | Canônica declarada | Canônica do Google |
|-----|--------------------|--------------------|
{canonical_mismatches_table}

## Problemas recorrentes

| Problema | Quantidade | Prioridade | Ação |
|----------|------------|------------|------|
{issues_table}

## Rich results detectados

| URL | Tipo de rich result | Situação |
|-----|---------------------|----------|
{rich_results_table}

---
*API de inspeção de URL: 2.000 inspeções por dia por site, 600 por minuto.*
*Gerado em {timestamp} pela API de inspeção de URL do Google Search Console.*
