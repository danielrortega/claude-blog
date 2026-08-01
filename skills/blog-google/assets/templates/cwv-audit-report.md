# Auditoria de Core Web Vitals

**URL/Origem:** {target}
**Estratégia:** {strategy}

## Dados de campo do CrUX (média móvel de 28 dias)

Dados reais de experiência de usuários do Chrome, vindos do Chrome UX Report.

| Métrica | Valor p75 | Classificação | Limite "bom" | Distribuição |
|---------|-----------|---------------|--------------|--------------|
| LCP | {lcp_value} | {lcp_rating} | ≤ 2.500ms | Bom: {lcp_good}% / Precisa melhorar: {lcp_ni}% / Ruim: {lcp_poor}% |
| INP | {inp_value} | {inp_rating} | ≤ 200ms | Bom: {inp_good}% / Precisa melhorar: {inp_ni}% / Ruim: {inp_poor}% |
| CLS | {cls_value} | {cls_rating} | ≤ 0,1 | Bom: {cls_good}% / Precisa melhorar: {cls_ni}% / Ruim: {cls_poor}% |
| FCP | {fcp_value} | {fcp_rating} | ≤ 1.800ms | Bom: {fcp_good}% / Precisa melhorar: {fcp_ni}% / Ruim: {fcp_poor}% |
| TTFB | {ttfb_value} | {ttfb_rating} | ≤ 800ms | Bom: {ttfb_good}% / Precisa melhorar: {ttfb_ni}% / Ruim: {ttfb_poor}% |

**Período de coleta:** {collection_start} a {collection_end}

## Notas de laboratório do Lighthouse

| Categoria | Nota |
|-----------|------|
| Desempenho | {perf_score}/100 |
| Acessibilidade | {a11y_score}/100 |
| Boas práticas | {bp_score}/100 |
| SEO | {seo_score}/100 |

## Tendências do histórico CrUX (25 semanas)

| Métrica | Direção | Variação | Mais antigo → Mais recente |
|---------|---------|----------|----------------------------|
{trends_table}

## Principais oportunidades

| Oportunidade | Economia estimada |
|--------------|-------------------|
{opportunities_table}

## Recomendações

{recommendations}

---
*Os dados do CrUX são atualizados diariamente por volta das 04:00 UTC. Média móvel de 28 dias.*
*O INP substituiu o FID como Core Web Vital de responsividade em 12 de março de 2024.*
*Gerado em {timestamp}.*
