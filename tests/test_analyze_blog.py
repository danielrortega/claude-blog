"""Tests for the blog quality analyzer script."""

import copy
import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

import analyze_blog


# ---------------------------------------------------------------------------
# Frontmatter parsing
# ---------------------------------------------------------------------------


class TestExtractFrontmatter:
    def test_extracts_yaml_frontmatter(self, sample_blog_post):
        fm = analyze_blog.extract_frontmatter(sample_blog_post)
        assert fm["title"] == "How to Optimize Your Blog for AI Citations"
        assert fm["author"] == "Jane Doe"

    def test_returns_empty_dict_without_frontmatter(self, sample_post_no_frontmatter):
        fm = analyze_blog.extract_frontmatter(sample_post_no_frontmatter)
        assert fm == {}

    def test_strips_quotes_from_values(self):
        content = '---\ntitle: "Quoted Title"\nauthor: \'Single Quoted\'\n---\n'
        fm = analyze_blog.extract_frontmatter(content)
        assert fm["title"] == "Quoted Title"
        assert fm["author"] == "Single Quoted"


class TestStripFrontmatter:
    def test_removes_frontmatter(self, sample_blog_post):
        stripped = analyze_blog.strip_frontmatter(sample_blog_post)
        assert "---" not in stripped.split("\n")[0]
        assert "# How to Optimize" in stripped

    def test_no_frontmatter_returns_unchanged(self, sample_post_no_frontmatter):
        stripped = analyze_blog.strip_frontmatter(sample_post_no_frontmatter)
        assert stripped == sample_post_no_frontmatter


# ---------------------------------------------------------------------------
# Heading analysis
# ---------------------------------------------------------------------------


class TestAnalyzeHeadings:
    def test_counts_heading_levels(self, sample_blog_post):
        result = analyze_blog.analyze_headings(sample_blog_post)
        assert result["h1_count"] == 1
        assert result["h2_count"] >= 3
        assert result["h3_count"] >= 1

    def test_detects_question_headings(self, sample_blog_post):
        result = analyze_blog.analyze_headings(sample_blog_post)
        assert result["h2_question_count"] >= 2
        assert result["h2_question_ratio"] > 0

    def test_clean_hierarchy(self):
        content = "# Title\n\n## Section\n\n### Sub\n\n## Another\n"
        result = analyze_blog.analyze_headings(content)
        assert result["hierarchy_clean"] is True

    def test_dirty_hierarchy(self):
        content = "# Title\n\n### Skipped H2\n\n## Section\n"
        result = analyze_blog.analyze_headings(content)
        assert result["hierarchy_clean"] is False

    def test_empty_content(self):
        result = analyze_blog.analyze_headings("")
        assert result["total"] == 0


# ---------------------------------------------------------------------------
# Paragraph analysis
# ---------------------------------------------------------------------------


class TestAnalyzeParagraphs:
    def test_counts_paragraphs(self, sample_blog_post):
        result = analyze_blog.analyze_paragraphs(sample_blog_post)
        assert result["total_paragraphs"] > 0

    def test_calculates_avg_word_count(self, sample_blog_post):
        result = analyze_blog.analyze_paragraphs(sample_blog_post)
        assert result["avg_word_count"] > 0

    def test_ignores_short_paragraphs(self):
        content = "One.\n\nTwo.\n\nThree words here.\n\n" + (
            "This is a paragraph with enough words to be counted by the analyzer. " * 3
        )
        result = analyze_blog.analyze_paragraphs(content)
        assert result["total_paragraphs"] == 1

    def test_detects_over_150(self):
        long_para = " ".join(["word"] * 160)
        content = f"\n\n{long_para}\n\n"
        result = analyze_blog.analyze_paragraphs(content)
        assert result["over_150_words"] >= 1

    def test_empty_content(self):
        result = analyze_blog.analyze_paragraphs("")
        assert result["total_paragraphs"] == 0
        assert result["avg_word_count"] == 0


# ---------------------------------------------------------------------------
# Image analysis
# ---------------------------------------------------------------------------


class TestAnalyzeImages:
    def test_detects_markdown_images(self):
        content = "![Alt text](image.jpg)\n![Another](photo.png)\n"
        result = analyze_blog.analyze_images(content)
        assert result["count"] == 2

    def test_detects_missing_alt_text(self):
        content = "![](image.jpg)\n![Good alt](photo.png)\n"
        result = analyze_blog.analyze_images(content)
        assert result["without_alt_text"] >= 1

    def test_no_images(self):
        result = analyze_blog.analyze_images("No images here.")
        assert result["count"] == 0


# ---------------------------------------------------------------------------
# AI content detection
# ---------------------------------------------------------------------------


class TestAISignals:
    def test_detects_ai_phrases(self):
        content = "In today's digital landscape, it's important to note that we must dive into this topic."
        sentences_info = analyze_blog.analyze_sentences(content)
        result = analyze_blog.analyze_ai_signals(content, sentences_info)
        assert result["ai_phrase_count"] > 0

    def test_clean_content_low_signals(self):
        content = "Blog optimization requires structured content. Statistics from Ahrefs show 43% improvement."
        sentences_info = analyze_blog.analyze_sentences(content)
        result = analyze_blog.analyze_ai_signals(content, sentences_info)
        assert result["ai_phrase_count"] == 0


class TestAITriggerWords:
    def test_detects_trigger_words(self):
        text = "We must delve into this multifaceted topic to illuminate the nuanced landscape."
        result = analyze_blog.analyze_ai_trigger_words(text)
        assert result["trigger_count"] > 0
        assert len(result["found"]) > 0

    def test_clean_text(self):
        text = "This article explains how to write better blog posts using data."
        result = analyze_blog.analyze_ai_trigger_words(text)
        assert result["trigger_count"] == 0


# ---------------------------------------------------------------------------
# Citation analysis
# ---------------------------------------------------------------------------


class TestAnalyzeCitations:
    def test_detects_inline_citations(self):
        content = "According to a study (Source, 2025), AI citations increased by 340%."
        result = analyze_blog.analyze_citations(content)
        assert result["total_statistics"] >= 1

    def test_no_statistics(self):
        content = "No numbers or statistics in this text at all."
        result = analyze_blog.analyze_citations(content)
        assert result["total_statistics"] == 0

    def test_tier_classification_uses_hostname_not_substring(self):
        attacker = "https://attacker.example/post?source=nih.gov"
        trusted = "https://www.nih.gov/research"
        assert analyze_blog._classify_source_tier(attacker) == 3
        assert analyze_blog._classify_source_tier(trusted) == 1


# ---------------------------------------------------------------------------
# FAQ analysis
# ---------------------------------------------------------------------------


class TestAnalyzeFAQ:
    def test_detects_faq_section(self, sample_blog_post):
        result = analyze_blog.analyze_faq(sample_blog_post)
        assert result["has_faq_section"] is True
        assert result["faq_item_count"] >= 2

    def test_no_faq(self):
        content = "# Title\n\n## Section\n\nJust regular content."
        result = analyze_blog.analyze_faq(content)
        assert result["has_faq_section"] is False


# ---------------------------------------------------------------------------
# Freshness analysis
# ---------------------------------------------------------------------------


class TestAnalyzeFreshness:
    def test_detects_dates(self):
        fm = {"date": "2026-01-15", "lastUpdated": "2026-02-10"}
        result = analyze_blog.analyze_freshness(fm)
        assert result["has_date"] is True
        assert result["has_last_updated"] is True

    def test_no_dates(self):
        result = analyze_blog.analyze_freshness({})
        assert result["has_date"] is False
        assert result["has_last_updated"] is False


# ---------------------------------------------------------------------------
# Readability analysis
# ---------------------------------------------------------------------------


class TestAnalyzeReadability:
    def test_flesch_score(self, sample_blog_post):
        stripped = analyze_blog.strip_frontmatter(sample_blog_post)
        result = analyze_blog.analyze_readability(stripped)
        assert "flesch_reading_ease" in result

    def test_reading_time(self, sample_blog_post):
        stripped = analyze_blog.strip_frontmatter(sample_blog_post)
        result = analyze_blog.analyze_readability(stripped)
        assert result["reading_time_minutes"] > 0


# ---------------------------------------------------------------------------
# Sentence analysis
# ---------------------------------------------------------------------------


class TestAnalyzeSentences:
    def test_detects_over_25_word_sentences(self):
        long = "This is a very " + "very " * 20 + "long sentence that goes on and on."
        short = "Short one."
        text = f"{long} {short}"
        result = analyze_blog.analyze_sentences(text)
        assert result["over_25_count"] >= 1

    def test_burstiness(self):
        text = "Short. Also short. This one is a bit longer than the others. Tiny."
        result = analyze_blog.analyze_sentences(text)
        assert "burstiness" in result


# ---------------------------------------------------------------------------
# Link analysis
# ---------------------------------------------------------------------------


class TestAnalyzeLinks:
    def test_counts_internal_and_external(self):
        content = "[internal](/about) and [external](https://example.com/page)"
        result = analyze_blog.analyze_links(content)
        assert result["internal_count"] >= 1
        assert result["external_count"] >= 1

    def test_no_links(self):
        result = analyze_blog.analyze_links("No links here.")
        assert result["internal_count"] == 0
        assert result["external_count"] == 0


# ---------------------------------------------------------------------------
# Schema analysis
# ---------------------------------------------------------------------------


class TestAnalyzeSchema:
    def test_detects_json_ld(self, sample_post_with_schema):
        result = analyze_blog.analyze_schema(sample_post_with_schema)
        assert result["schema_count"] >= 1
        assert result["has_blogposting"] is True

    def test_no_schema(self):
        result = analyze_blog.analyze_schema("# Simple post\n\nNo schema here.")
        assert result["schema_count"] == 0

    @pytest.mark.parametrize("schema_type", ["FAQPage", "HowTo", "SpecialAnnouncement"])
    def test_ineligible_schema_does_not_raise_technical_schema_score(
        self, tmp_path, schema_type
    ):
        base = """---
title: Source Review
author: Jane Doe
---
# Source Review

## Evidence

This review links [primary guidance](https://example.gov/guidance).
"""
        schema = f"""
<script type="application/ld+json">
{{"@context": "https://schema.org", "@type": "{schema_type}"}}
</script>
"""
        base_path = tmp_path / "base.md"
        schema_path = tmp_path / "schema.md"
        base_path.write_text(base, encoding="utf-8")
        schema_path.write_text(base + schema, encoding="utf-8")

        base_result = analyze_blog.analyze_file(str(base_path))
        schema_result = analyze_blog.analyze_file(str(schema_path))

        assert schema_result["score"]["category_details"]["technical_elements"][
            "breakdown"
        ]["schema"] == base_result["score"]["category_details"][
            "technical_elements"
        ]["breakdown"]["schema"]


# ---------------------------------------------------------------------------
# Self-promotion analysis
# ---------------------------------------------------------------------------


class TestAnalyzeSelfPromotion:
    def test_no_promotions(self):
        result = analyze_blog.analyze_self_promotion("Generic content without brands.")
        assert result["exceeds_limit"] is False
        assert result["self_promotion_patterns"] == 0

    def test_returns_expected_keys(self):
        result = analyze_blog.analyze_self_promotion("Some content.", brand_name="Acme")
        assert "self_promotion_patterns" in result
        assert "exceeds_limit" in result


# ---------------------------------------------------------------------------
# Passive voice analysis
# ---------------------------------------------------------------------------


class TestAnalyzePassiveVoice:
    def test_detects_passive(self):
        text = "The report was written by the team. The data was analyzed carefully."
        result = analyze_blog.analyze_passive_voice(text)
        assert result["passive_count"] >= 1

    def test_active_voice(self):
        text = "The team wrote the report. Analysts reviewed the data."
        result = analyze_blog.analyze_passive_voice(text)
        assert result["passive_count"] == 0


# ---------------------------------------------------------------------------
# Transition words
# ---------------------------------------------------------------------------


class TestAnalyzeTransitionWords:
    def test_detects_transitions(self):
        text = "First, set up your blog. However, you should also consider SEO. Therefore, optimize early."
        result = analyze_blog.analyze_transition_words(text)
        assert result["transition_count"] >= 2

    def test_no_transitions(self):
        text = "Set up blog. Consider SEO. Optimize."
        result = analyze_blog.analyze_transition_words(text)
        assert result["transition_count"] == 0


# ---------------------------------------------------------------------------
# File analysis (integration)
# ---------------------------------------------------------------------------


class TestAnalyzeFile:
    def test_analyzes_real_file(self, tmp_path, sample_blog_post):
        post_file = tmp_path / "test-post.md"
        post_file.write_text(sample_blog_post)
        result = analyze_blog.analyze_file(str(post_file))
        assert "score" in result
        assert "headings" in result
        assert result["score"]["total"] >= 0

    def test_nonexistent_file(self):
        result = analyze_blog.analyze_file("/nonexistent/file.md")
        assert "error" in result

    def test_style_diagnostics_do_not_change_quality_score(self, tmp_path):
        base = """---
title: Evidence Based Content Review for Product Teams
description: A sourced review that explains how product teams evaluate content decisions with transparent evidence and practical examples.
author: Jane Doe
---
# Evidence Based Content Review

## Evidence review process

**Evidence review** is a documented check of a claim, its source, and its
practical implication. For example, teams can compare a public benchmark with
their own measurements and cite the [NIH](https://nih.gov/research) when a
health claim depends on primary guidance.

## Decision record

The decision record states what changed and why. It links the source, names the
assumption, and gives reviewers a useful example.
"""
        styled = base.replace(
            "The decision record states what changed and why.",
            "Furthermore, delve into the robust landscape with care.",
        )
        base_path = tmp_path / "base.md"
        styled_path = tmp_path / "styled.md"
        base_path.write_text(base, encoding="utf-8")
        styled_path.write_text(styled, encoding="utf-8")

        base_result = analyze_blog.analyze_file(str(base_path))
        styled_result = analyze_blog.analyze_file(str(styled_path))

        assert (
            base_result["score"]["category_details"]["content_quality"]["breakdown"]["grammar_antipattern"]
            == styled_result["score"]["category_details"]["content_quality"]["breakdown"]["grammar_antipattern"]
        )
        assert styled_result["ai_trigger_words"]["trigger_count"] > 0
        assert styled_result["ai_signals"]["likely_ai"] is None
        issue_text = " ".join(item["issue"] for item in styled_result["score"]["issues"]).lower()
        assert "trigger word" not in issue_text

    def test_faq_last_updated_and_padding_do_not_add_ai_points(self, tmp_path):
        base = """---
title: Evidence Based Content Review for Product Teams
description: A sourced review that explains how product teams evaluate content decisions with transparent evidence and practical examples.
author: Jane Doe
date: 2026-07-01
---
# Evidence Based Content Review

## Evidence review process

**Evidence review** is a documented check with a public source
[NIH](https://nih.gov/research) and a practical example for editors.

## Decision record

The record explains the decision and links [CDC guidance](https://cdc.gov/guidance).

## Publication check

Editors verify the claim, source, and reader action before publication.
"""
        padded = base.replace(
            "date: 2026-07-01",
            "date: 2026-07-01\nlastUpdated: 2026-07-23",
        ) + "\n## FAQ\n\n### Is this required?\n\n" + " ".join(["padding"] * 150)
        base_path = tmp_path / "base.md"
        padded_path = tmp_path / "padded.md"
        base_path.write_text(base, encoding="utf-8")
        padded_path.write_text(padded, encoding="utf-8")

        base_result = analyze_blog.analyze_file(str(base_path))
        padded_result = analyze_blog.analyze_file(str(padded_path))

        assert (
            base_result["score"]["categories"]["ai_citation_readiness"]
            == padded_result["score"]["categories"]["ai_citation_readiness"]
        )
        assert padded_result["methodology"]["calibrated_probability"] is False

    def test_neutral_sourced_article_is_not_told_to_claim_testing(self, tmp_path):
        post = """---
title: Neutral Source Review for Editorial Teams
description: A neutral and sourced explanation of editorial review methods for teams that need transparent, practical publishing decisions.
author: Jane Doe
---
# Neutral Source Review

## Source selection

Editors use primary guidance from the [CDC](https://cdc.gov/guidance) and
document how each source supports the page.

## Reader decision

The review explains the tradeoff with a concrete example and a clear next step.
"""
        path = tmp_path / "neutral.md"
        path.write_text(post, encoding="utf-8")

        result = analyze_blog.analyze_file(str(path))
        issue_text = " ".join(item["issue"] for item in result["score"]["issues"]).lower()

        assert "add \"we tested\"" not in issue_text
        assert "in our experience" not in issue_text
        assert "word count" not in issue_text

    def test_paragraph_padding_metric_does_not_change_score(self, tmp_path, sample_blog_post):
        post_file = tmp_path / "post.md"
        post_file.write_text(sample_blog_post, encoding="utf-8")
        analysis = analyze_blog.analyze_file(str(post_file))
        padded_metrics = copy.deepcopy(analysis)
        padded_metrics["paragraphs"]["max_word_count"] += 1_000
        padded_metrics["paragraphs"]["over_100_words"] += 1
        padded_metrics["paragraphs"]["over_150_words"] += 1

        baseline_score = analyze_blog.calculate_score(analysis)
        padded_score = analyze_blog.calculate_score(padded_metrics)

        assert padded_score["total"] == baseline_score["total"]
        assert padded_score["category_details"]["content_quality"]["breakdown"][
            "structure"
        ] == baseline_score["category_details"]["content_quality"]["breakdown"][
            "structure"
        ]
        assert padded_score["category_details"]["technical_elements"]["breakdown"][
            "mobile"
        ] == baseline_score["category_details"]["technical_elements"]["breakdown"][
            "mobile"
        ]

    def test_seo_length_number_and_exact_keyword_padding_add_no_points(self, tmp_path):
        base = """---
title: Evidence Review
description: Evidence review explains source decisions for editors.
author: Jane Doe
---
# Evidence Review

## Source decisions

Evidence review helps editors connect each material claim to supporting
guidance and explain the reader's next decision.
"""
        variants = {
            "base.md": base,
            "number.md": base.replace(
                "source decisions for editors.",
                "source decisions for editors in 2026.",
            ),
            "title-length.md": base.replace(
                "title: Evidence Review",
                "title: Evidence Review: Evidence Review for Evidence Review",
            ),
            "keyword.md": base.replace(
                "author: Jane Doe",
                "author: Jane Doe\nkeyword: evidence review",
            ).replace(
                "Evidence review helps editors",
                "Evidence review. Evidence review helps editors",
            ),
        }
        results = {}
        for name, content in variants.items():
            path = tmp_path / name
            path.write_text(content, encoding="utf-8")
            results[name] = analyze_blog.analyze_file(str(path))

        base_seo = results["base.md"]["score"]["category_details"][
            "seo_optimization"
        ]
        assert base_seo["breakdown"]["title"] == 4
        assert base_seo["breakdown"]["headings"] == 5
        assert base_seo["breakdown"]["keyword_placement"] == 4
        assert base_seo["breakdown"]["meta_description"] == 3
        for name in ("number.md", "title-length.md", "keyword.md"):
            seo = results[name]["score"]["category_details"]["seo_optimization"]
            assert seo["score"] == base_seo["score"]
            assert seo["breakdown"]["title"] == base_seo["breakdown"]["title"]
            assert seo["breakdown"]["keyword_placement"] == base_seo["breakdown"][
                "keyword_placement"
            ]
            assert seo["breakdown"]["meta_description"] == base_seo["breakdown"][
                "meta_description"
            ]


# ---------------------------------------------------------------------------
# Language-specific structural cues
#
# Every regex below was English-only at some point, so a Portuguese post using
# the same rhetorical structure matched nothing and silently lost the points.
# These tests pin both directions: Portuguese is detected, English is unchanged.
# ---------------------------------------------------------------------------


class TestPortugueseStructuralCues:
    @pytest.fixture(autouse=True)
    def _restore_language(self):
        yield
        analyze_blog.configure_language("en")

    def test_faq_heading_detected_in_portuguese(self):
        analyze_blog.configure_language("pt")
        for heading in ("## Perguntas Frequentes", "## Dúvidas Comuns", "## FAQ"):
            result = analyze_blog.analyze_faq(f"{heading}\n\n### Isso funciona?\n")
            assert result["has_faq_section"], heading

    def test_english_faq_heading_still_detected(self):
        analyze_blog.configure_language("en")
        result = analyze_blog.analyze_faq("## Frequently Asked Questions\n\n### Does it?\n")
        assert result["has_faq_section"]

    def test_example_markers_counted_in_portuguese(self):
        analyze_blog.configure_language("pt")
        text = "Por exemplo, o azeite oxida. Considere o caso do calor. Suponha 40 graus."
        assert analyze_blog.analyze_engagement(text)["example_count"] >= 3

    def test_english_example_markers_unchanged(self):
        analyze_blog.configure_language("en")
        text = "For example, oil oxidizes. Consider heat. Such as at 40 degrees."
        assert analyze_blog.analyze_engagement(text)["example_count"] >= 3

    def test_entity_definition_matches_portuguese_copula(self):
        analyze_blog.configure_language("pt")
        content = (
            "**Acidez livre** é a proporção de ácidos graxos soltos.\n"
            "**Peróxidos** significam oxidação.\n"
            "**Cultivar** se refere a variedade botânica.\n"
        )
        found = len(re.findall(f"(?i){analyze_blog.ENTITY_DEFINITION}", content))
        assert found >= 3, f"expected 3 pt definitions, found {found}"

    def test_entity_definition_still_matches_english(self):
        analyze_blog.configure_language("en")
        content = "**Free acidity** is the share of loose fatty acids.\n"
        assert re.search(f"(?i){analyze_blog.ENTITY_DEFINITION}", content)

    def test_trust_patterns_match_portuguese(self):
        analyze_blog.configure_language("pt")
        body = "Sobre nós: somos produtores. Fale conosco. Revisado por um engenheiro."
        for key in ("about", "contact", "editorial"):
            assert re.search(
                f"(?i){analyze_blog.TRUST_PATTERNS[key]}", body
            ), f"pt trust pattern '{key}' did not match"

    def test_topic_terms_keep_accented_words_whole(self):
        analyze_blog.configure_language("pt")
        terms = analyze_blog._topic_terms("Otimização e manutenção da produção")
        assert "otimização" in terms
        assert "manutenção" in terms
        # The old ASCII-only tokenizer fragmented these into "otimiza"/"o".
        assert not any(t in {"otimiza", "manuten", "produ"} for t in terms)

    def test_portuguese_function_words_are_not_topic_terms(self):
        analyze_blog.configure_language("pt")
        terms = analyze_blog._topic_terms("O guia de azeite para quem não sabe")
        assert "azeite" in terms
        assert not ({"de", "para", "que", "não", "o"} & terms)

    def test_english_topic_terms_unchanged(self):
        analyze_blog.configure_language("en")
        terms = analyze_blog._topic_terms("The guide to olive oil for beginners")
        assert "olive" in terms and "beginners" in terms
        assert not ({"the", "for"} & terms)


class TestByteOrderMarkHandling:
    """A UTF-8 BOM must never hide the frontmatter block.

    Windows editors and `Set-Content -Encoding utf8` under Windows PowerShell
    5.1 write UTF-8 with a BOM. The U+FEFF lands in front of the opening
    `---`, so the `^---` anchor in extract_frontmatter() stops matching and
    title, description, tags, author and lang are all silently lost at once.
    Measured cost on a short pt-BR post before the fix: 50 -> 36 of 100, with
    SEO 17 -> 7 and E-E-A-T 4 -> 0.
    """

    POST = (
        "---\n"
        "title: Como escolher azeite extra virgem\n"
        "description: Guia para escolher azeite de oliva no Brasil.\n"
        "lang: pt\n"
        "---\n"
        "\n"
        "## Resumo rápido\n"
        "\n"
        "O azeite extra virgem é um produto regulado. Por exemplo, a acidez\n"
        "precisa constar em laudo assinado pelo laboratório.\n"
    )

    def _read(self, tmp_path, encoding):
        path = tmp_path / f"post-{encoding}.md"
        path.write_text(self.POST, encoding=encoding)
        return analyze_blog._read_safely(path)

    def test_bom_is_stripped_on_read(self, tmp_path):
        content = self._read(tmp_path, "utf-8-sig")
        assert not content.startswith("﻿")
        assert content.startswith("---")

    def test_frontmatter_survives_a_bom(self, tmp_path):
        fm = analyze_blog.extract_frontmatter(self._read(tmp_path, "utf-8-sig"))
        assert fm.get("lang") == "pt"
        assert fm.get("title") == "Como escolher azeite extra virgem"

    def test_bom_and_bomless_reads_are_identical(self, tmp_path):
        assert self._read(tmp_path, "utf-8-sig") == self._read(tmp_path, "utf-8")


class TestDependencyNotice:
    """A package that is present but fails to import must not be reported as
    missing. Saying "pip install textstat" when textstat is installed sends
    the operator down the wrong path; the real cause was an ImportError raised
    from inside the package."""

    def test_broken_import_is_reported_with_its_own_error(self, monkeypatch, capsys):
        monkeypatch.setattr(analyze_blog, "HAS_TEXTSTAT", False)
        monkeypatch.setattr(
            analyze_blog,
            "_IMPORT_ERRORS",
            {"textstat": "Blocked import of regex from current working directory"},
        )
        analyze_blog._print_dependency_notice()
        err = capsys.readouterr().err
        assert "installed but failed to import" in err
        assert "Blocked import of regex" in err
        assert "pip install textstat" not in err

    def test_absent_package_still_suggests_pip(self, monkeypatch, capsys):
        monkeypatch.setattr(analyze_blog, "HAS_TEXTSTAT", False)
        monkeypatch.setattr(analyze_blog, "_IMPORT_ERRORS", {})
        analyze_blog._print_dependency_notice()
        err = capsys.readouterr().err
        assert "pip install textstat" in err
