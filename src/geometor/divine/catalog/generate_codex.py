"""Deterministic generator for the Golden Ratio Catalog Book Codex & JSON resources.

Builds and certifies all 45 symbolic constructions in :data:`~geometor.divine.catalog.CATALOG`,
exports publication-grade interactive ``.euclid-graphic`` SVGs, writes machine-readable
registries under ``resources/``, and emits the complete multi-track Sphinx Book Codex
under ``docsrc/constructions/``.
"""

from __future__ import annotations

import inspect
import json
import re
from pathlib import Path
from typing import Any

import sympy as sp
from geometor.model import Model, canonicalize_golden, clean_expr

from .apparatus import CITATIONS, GLOSSARY, PERSONS
from .registry import CATALOG, FAMILIES
from .render import export_catalog_svg
from .schema import (
    ConstructionSpec,
    FamilySpec,
    GoldenCertificate,
    certify_construction,
)

_ROLE_RE = re.compile(r":[a-z]+:`([^`]+)`")
_MATH_RE = re.compile(r":math:`([^`]+)`")


def _strip_rst_inline(text: str) -> str:
    """Convert inline RST roles into clean plain text for card excerpts."""

    def _repl_role(match: re.Match[str]) -> str:
        body = match.group(1).strip()
        if "<" in body and body.endswith(">"):
            return body.split("<", 1)[0].strip()
        return body

    out = _MATH_RE.sub(lambda m: m.group(1).replace("\\phi", "φ").replace("\\", ""), text)
    out = _ROLE_RE.sub(_repl_role, out)
    out = out.replace("*", "").replace("|", "")
    return " ".join(out.split())


def _field_tag_slug(field_text: str) -> str:
    mapping = {
        "Q(φ)": "field-q-phi",
        "Q(√2, φ)": "field-q-sqrt2-phi",
        "Q(√3, φ)": "field-q-sqrt3-phi",
        "Q(√φ)": "field-q-sqrt-phi",
        "Q(φ, √(10−2√5))": "field-pentagonal",
        "Q(√3, φ, √(10−2√5))": "field-pentagonal-hexagonal",
    }
    return mapping.get(field_text, "field-algebraic")


def _rst_heading(title: str, char: str) -> str:
    line = char * max(len(title), 4)
    return f"{title}\n{line}"


def _format_latex(expr: sp.Expr) -> str:
    cleaned = canonicalize_golden(clean_expr(expr))
    tex = sp.latex(cleaned)
    return tex.replace(r"\mathtt{\text{GoldenRatio}}", r"\phi")


def _render_construction_index_rst(
    spec: ConstructionSpec,
    fam: FamilySpec,
    cert: GoldenCertificate,
) -> str:
    excerpt = _strip_rst_inline(spec.enunciation)
    tags = [_field_tag_slug(spec.number_field_text)]
    if cert.detected_chains:
        tags.append("golden-chain")
    if cert.stats.constructed_lines == 0:
        tags.append("compass-only")
    tags.extend(spec.discoverers[:2])

    disc_links = ", ".join(
        f":person:`{PERSONS[d]['name']} <{d}>`" if d in PERSONS else d
        for d in spec.discoverers
    )
    cite_links = ", ".join(
        f":cite:`{CITATIONS[c]['work']} <{c}>`" if c in CITATIONS else c
        for c in spec.citations
    )
    term_links = " · ".join(
        f":term:`{GLOSSARY[t]['headword']} <{t}>`" if t in GLOSSARY else t
        for t in spec.terms
    )

    ul, vl = cert.primary_long
    us, vs = cert.primary_short
    c0, c1, c2 = cert.primary_collinear

    lines: list[str] = [
        ":type: construction",
        f":order: {spec.order}",
        f":excerpt: {excerpt}",
        f":categories: {fam.slug}",
        f":tags: {', '.join(dict.fromkeys(tags))}",
        "",
        _rst_heading(f"{spec.catalog_code} · {spec.title}", "="),
        "",
        (f"**Discoverer(s)**: {disc_links} | "
        f"**Date**: {spec.year} | "
        f"**Field**: :math:`{spec.number_field}` | "
        f"**Loci**: {cert.stats.elementary_loci} (:term:`Lemoine <geometrographie>` :math:`S = {cert.stats.lemoine_simplicity}`)"),
        "",
        ".. enunciation::",
        "",
        f"   {spec.enunciation}",
        "",
        f".. picture:: {spec.slug}.svg",
        f"   :alt: {spec.catalog_code} — {spec.title}",
        "",
        _rst_heading("Given & Constructive Steps", "-"),
        "",
        f"**Given**: {spec.given_prose}",
        "",
    ]

    for step_text in spec.steps_prose:
        lines.extend(
            [
                ".. step::",
                "",
                f"   {step_text}",
                "",
            ]
        )

    lines.extend(
        [
            _rst_heading("Exact Symbolic Proof & Certificate", "-"),
            "",
            spec.proof_prose,
            "",
            ".. list-table:: Machine-Verified Symbolic Certificate",
            "   :widths: 30 70",
            "   :header-rows: 1",
            "",
            "   * - Invariant",
            "     - Exact Symbolic Value",
            "   * - Primary Golden Ratio",
            (f"     - :g:`{ul}{vl}` :math:`/` :g:`{us}{vs}` :math:`= {_format_latex(cert.ratio_expr)}` "
            f"on collinear triple (:g:`{c0}`, :g:`{c1}`, :g:`{c2}`)"),
            "   * - Exact Segment Lengths",
            (f"     - :math:`|{ul}{vl}| = {_format_latex(cert.length_long)}`, "
            f":math:`|{us}{vs}| = {_format_latex(cert.length_short)}`"),
            "   * - Rational Trigonometry :term:`Quadrances <quadrance>`",
            (f"     - :math:`Q({ul}, {vl}) = {_format_latex(cert.q_long)}`, "
            f":math:`Q({us}, {vs}) = {_format_latex(cert.q_short)}`, "
            f":math:`Q_{{\\text{{long}}}}/Q_{{\\text{{short}}}} = {_format_latex(cert.quadrance_ratio)} = \\phi^2`"),
            "   * - Algebraic Number Field",
            f"     - :math:`{spec.number_field}`",
            "   * - :term:`Géométrographie <geometrographie>` Loci",
            (f"     - {cert.stats.given_points} given points · "
            f"{cert.stats.constructed_lines} lines · "
            f"{cert.stats.constructed_circles} circles · "
            f"{cert.stats.constructed_polygons} polygons "
            f"(elementary loci :math:`= {cert.stats.elementary_loci}`, Lemoine :math:`S = {cert.stats.lemoine_simplicity}`)"),
            "",
            _rst_heading("Automated Divine Scan", "-"),
            "",
            (f":mod:`geometor.divine.golden` detected **{len(cert.detected_sections)}** exact collinear "
            f"golden section(s) and **{len(cert.detected_chains)}** connected golden chain(s) in this model:"),
            "",
        ]
    )

    for sec in cert.detected_sections:
        p0, p1, p2 = sec.points
        l0, l1 = sec.long_segment
        s0, s1 = sec.short_segment
        lines.append(
            f"- Section (:g:`{p0}`, :g:`{p1}`, :g:`{p2}`): "
            f"long :math:`|{l0}{l1}|^2 = {_format_latex(sec.q_long)}` vs. "
            f"short :math:`|{s0}{s1}|^2 = {_format_latex(sec.q_short)}`"
        )
    lines.append("")

    if cert.detected_chains:
        lines.append("**Connected Golden Chains**:")
        lines.append("")
        for chn in cert.detected_chains:
            pts_str = " — ".join(f":g:`{pid}`" for pid in chn.points)
            lines.append(
                f"- Chain ({pts_str}) spanning {chn.section_count} overlapping golden sections "
                f"(progression ``{chn.flow}``)"
            )
        lines.append("")

    lines.extend(
        [
            _rst_heading("Historical Commentary & Attribution", "-"),
            "",
            spec.notes_prose,
            "",
            f"- **Scholarly Citations**: {cite_links}",
            (f"- **Curated Reference**: `{spec.ctk_title} <{spec.ctk_url}>`_ "
            "(curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)"),
            f"- **Concepts**: {term_links}",
            "",
            ".. toctree::",
            "   :hidden:",
            "",
            "   code",
            "",
        ]
    )
    return "\n".join(lines)


def _render_construction_code_rst(
    spec: ConstructionSpec,
    model: Model,
    cert: GoldenCertificate,
) -> str:
    src_code = inspect.getsource(spec.builder).rstrip()
    lines: list[str] = [
        _rst_heading(f"{spec.catalog_code} · Symbolic Model & Source", "="),
        "",
        f"Companion symbolic Python construction for :doc:`index` (``{spec.catalog_code}``).",
        "",
        _rst_heading("Programmatic Usage", "-"),
        "",
        ".. code-block:: python",
        "",
        "   from geometor.divine.catalog import build_construction",
        "",
        f'   model, cert = build_construction("{spec.catalog_code}")',
        "   assert cert.ratio_expr == sp.GoldenRatio",
        "",
        _rst_heading("Exact Builder Implementation", "-"),
        "",
        ".. code-block:: python",
        "",
    ]
    for code_line in src_code.splitlines():
        lines.append(f"   {code_line}" if code_line else "")

    lines.extend(
        [
            "",
            _rst_heading("Exact Symbolic Point Coordinates", "-"),
            "",
            (f"All points in ``{model.name}`` are certified free of floating-point approximations "
            f"over :math:`{spec.number_field}`:"),
            "",
            ".. list-table::",
            "   :widths: 15 42 43",
            "   :header-rows: 1",
            "",
            "   * - Point",
            "     - Exact :math:`x`",
            "     - Exact :math:`y`",
        ]
    )

    for pt in model.points:
        el = model[pt]
        if el.guide or not el.ID:
            continue
        lines.extend(
            [
                f"   * - ``{el.ID}``",
                f"     - :math:`{_format_latex(pt.x)}`",
                f"     - :math:`{_format_latex(pt.y)}`",
            ]
        )

    lines.extend(
        [
            "",
            (f"**Certified Golden Ratio**: ``{cert.primary_long[0]}{cert.primary_long[1]}`` / "
            f"``{cert.primary_short[0]}{cert.primary_short[1]}`` = ``{cert.ratio_expr}``."),
            "",
        ]
    )
    return "\n".join(lines)


def _render_family_index_rst(
    fam: FamilySpec,
    family_specs: list[ConstructionSpec],
) -> str:
    first_spec = family_specs[0]
    featured_svg = f"constructions/{fam.slug}/{first_spec.slug}/{first_spec.slug}.svg"
    lines: list[str] = [
        ":type: family",
        f":order: {fam.order}",
        f":featured_image: {featured_svg}",
        f":featured_image_alt: {fam.title}",
        f":excerpt: {fam.summary}",
        "",
        _rst_heading(f"{fam.code_prefix} · {fam.title}", "="),
        "",
        f"*{fam.subtitle}*",
        "",
        fam.overview_rst,
        "",
        _rst_heading(f"Cataloged Constructions ({len(family_specs)})", "-"),
        "",
        ".. collection::",
        "   :type: construction",
        "   :sort: order",
        "",
    ]
    return "\n".join(lines)


def _render_book_index_rst(
    total_constructions: int,
    total_sections: int,
    total_chains: int,
) -> str:
    lines: list[str] = [
        ":navigation: header",
        ":order: 1",
        ":nav_title: Golden Constructions",
        ":layout: book",
        ":book_title: Catalog of Golden Ratio Constructions",
        ":book_subtitle: Seven Geometric Families in Exact Symbolic Algebra",
        ":author: Alexander Bogomolny, Euclid & Contemporary Geometers",
        ":year: 2024",
        "",
        _rst_heading("Catalog of Golden Ratio Constructions", "="),
        "",
        ".. rubric:: Seven Geometric Families in Exact Symbolic Algebra",
        "",
        ".. container:: title-page",
        "",
        "   | **Alexander Bogomolny, Euclid & Contemporary Geometers**",
        "   | *Curated from Cut-the-Knot & Classical Treatises*",
        "   |",
        "   | *Source*: Cut-the-Knot (1996–2018) & Classical Treatises",
        "   | *GEOMETOR Digital Edition*: 45 Exact Symbolic Constructions in Seven Geometric Families",
        "",
        (f"A machine-verified symbolic catalog of **{total_constructions} geometric constructions and theorems** "
        f"across **7 geometric families**, certifying **{total_sections} exact golden sections** and "
        f"**{total_chains} connected golden chains** in 100% exact SymPy algebra."),
        "",
        _rst_heading("Cataloging Ethos & Scholarly Provenance", "-"),
        "",
        ("Mathematical theorems, geometric incidences, and algebraic proportions are universal facts of "
        "nature and logic. Over two decades on *Cut-the-Knot* (`Golden Ratio in Geometry "
        "<https://www.cut-the-knot.org/do_you_know/GoldenRatio.shtml>`_, © 1996–2018 "
        ":person:`Alexander Bogomolny <alexander-bogomolny>`), Bogomolny curated an extraordinary "
        "constellation of classical and modern Golden Ratio constructions contributed by geometers "
        "around the world—spanning :person:`Euclid <euclid>`, :person:`Claudius Ptolemy <claudius-ptolemy>`, "
        ":person:`Johannes Kepler <johannes-kepler>`, :person:`Émile Lemoine <emile-lemoine>`, "
        ":person:`H. E. Huntley <h-e-huntley>`, :person:`George Odom <george-odom>`, "
        ":person:`Kurt Hofstetter <kurt-hofstetter>`, :person:`Michel Bataille <michel-bataille>`, "
        ":person:`Tran Quang Hung <tran-quang-hung>`, :person:`Bùi Quang Tuân <bui-quang-tuan>`, "
        ":person:`Jerzy Kocik <jerzy-kocik>`, and many others."),
        "",
        ("In the GEOMETOR Digital Scriptorium tradition—alongside the companion Ron Knott Golden Ratio "
        "Catalog (``geometor/knott``, cataloging :person:`Ron Knott <ron-knott>`'s "
        ":cite:`Fibonacci Numbers and the Golden Section <knott-golden-section>`)—this codex **catalogs** "
        "each universal geometric fact in GEOMETOR's canonical symbolic format:"),
        "",
        ("1. **100% Exact Symbolic Modeling**: Every construction is built from scratch in :mod:`geometor.model` "
        "with zero floating-point approximations over :math:`\\mathbb{Q}(\\phi)`, :math:`\\mathbb{Q}(\\sqrt{2}, \\phi)`, "
        ":math:`\\mathbb{Q}(\\sqrt{3}, \\phi)`, :math:`\\mathbb{Q}(\\sqrt{\\phi})`, and cyclotomic pentagonal extensions."),
        ("2. **Rational Trigonometry Certification**: Primary ratios are certified via exact :term:`quadrance <quadrance>` "
        "identities :math:`Q_{\\text{long}} / Q_{\\text{short}} = \\phi + 1 = \\phi^2` and Lemoine "
        ":term:`Géométrographie <geometrographie>` locus metrics."),
        ("3. **Automated Divine Discovery**: Every model is scanned by :mod:`geometor.divine.golden` to "
        "uncover secondary golden sections and connected :term:`golden chains <golden-chain>`."),
        ("4. **Original Prose & Interactive Vector Plates**: All expositions, proofs, and theme-adaptive "
        "``.euclid-graphic`` SVGs are newly authored for GEOMETOR with bidirectional ``:g:`` hover "
        "highlighting and full bibliographic attribution."),
        "",
        _rst_heading("Table of Contents", "-"),
        "",
        ".. collection::",
        "   :type: family",
        "   :sort: order",
        "",
        _rst_heading("Scholarly Apparatus", "-"),
        "",
        "- :doc:`comparative_table` — Complete metrics across all 45 constructions (number fields, elementary loci, Lemoine simplicity, and detected golden chains).",
        "- :doc:`bibliography` — Primary treatises, journal articles, and *Cut-the-Knot* archival citations.",
        "- :doc:`persons` — Biographical index of classical and contemporary geometers.",
        "- :doc:`glossary` — Technical glossary of constructive and Rational Trigonometry invariants.",
        "",
        ".. toctree::",
        "   :hidden:",
        "",
        "   comparative_table",
        "   bibliography",
        "   persons",
        "   glossary",
        "",
    ]
    return "\n".join(lines)


def _render_comparative_table_rst(
    certified_rows: list[tuple[ConstructionSpec, GoldenCertificate]],
) -> str:
    lines: list[str] = [
        _rst_heading("Comparative Table of All 45 Constructions", "="),
        "",
        ("Side-by-side comparison of algebraic number fields, Euclidean locus counts, "
        ":term:`Lemoine Géométrographie <geometrographie>` simplicity (:math:`S`), and exact "
        "collinear golden sections and chains discovered automatically by :mod:`geometor.divine.golden`."),
        "",
        ".. list-table::",
        "   :widths: 11 31 19 8 13 6 6 6",
        "   :header-rows: 1",
        "",
        "   * - Code",
        "     - Construction",
        "     - Discoverer(s)",
        "     - Year",
        "     - Field",
        "     - Loci",
        "     - :math:`S`",
        "     - Sec / Chn",
    ]

    for spec, cert in certified_rows:
        doc_path = f"{spec.family_slug}/{spec.slug}/index"
        disc_names = ", ".join(
            PERSONS[d]["name"].split()[-1] if d in PERSONS else d
            for d in spec.discoverers
        )
        lines.extend(
            [
                f"   * - ``{spec.catalog_code}``",
                f"     - :doc:`{spec.short_title} <{doc_path}>`",
                f"     - {disc_names}",
                f"     - {spec.year}",
                f"     - :math:`{spec.number_field}`",
                f"     - {cert.stats.elementary_loci}",
                f"     - {cert.stats.lemoine_simplicity}",
                f"     - {len(cert.detected_sections)} / {len(cert.detected_chains)}",
            ]
        )

    lines.append("")
    return "\n".join(lines)


def _render_bibliography_rst(
    cite_usage: dict[str, list[ConstructionSpec]],
) -> str:
    lines: list[str] = [
        ":navigation: header",
        ":order: 6",
        ":nav_title: Bibliography",
        "",
        _rst_heading("Bibliography", "="),
        "",
        ".. rubric:: Primary Treatises, Journal Articles & Cut-the-Knot Archival Sources",
        "",
        ("Primary mathematical treatises, peer-reviewed journal articles, and curated archival pages "
        "from :person:`Alexander Bogomolny <alexander-bogomolny>`'s *Interactive Mathematics Miscellany "
        "and Puzzles* (*Cut-the-Knot*, © 1996–2018)."),
        "",
    ]

    for slug, entry in CITATIONS.items():
        lines.extend(
            [
                f".. _cite-{slug}:",
                "",
                f"**{entry['work']}** ({entry['year']})",
                f"   *{entry['author']}* — {entry['locus']}. {entry['note']}",
            ]
        )
        if entry.get("url"):
            lines.append(f"   URL: `{entry['url']} <{entry['url']}>`_")
        used_in = cite_usage.get(slug, [])
        if used_in:
            refs = ", ".join(
                f":doc:`{s.catalog_code} <{s.family_slug}/{s.slug}/index>`" for s in used_in
            )
            lines.append(f"   *Cataloged in*: {refs}")
        lines.append("")

    return "\n".join(lines)


def _render_persons_rst(
    person_usage: dict[str, list[ConstructionSpec]],
) -> str:
    primary_authors = ["alexander-bogomolny", "euclid", "luca-pacioli", "claudius-ptolemy"]
    lines: list[str] = [
        ":navigation: header",
        ":order: 5",
        ":nav_title: People",
        "",
        _rst_heading("People", "="),
        "",
        ".. rubric:: Curators, Classical Authors & Contemporary Geometers",
        "",
        ("Biographical registry of classical, modern, and contemporary geometers whose theorems, "
        "constructions, and archival curations are represented in this catalog."),
        "",
        _rst_heading("Authors, Translators & Editors", "-"),
        "",
    ]

    for slug in primary_authors:
        if slug in PERSONS:
            entry = PERSONS[slug]
            lines.extend(
                [
                    f".. _person-{slug}:",
                    "",
                    f"**{entry['name']}** ({entry['dates']}) — *{entry['role']}*",
                    f"   {entry['bio']}",
                ]
            )
            used_in = person_usage.get(slug, [])
            if used_in:
                refs = ", ".join(
                    f":doc:`{s.catalog_code} <{s.family_slug}/{s.slug}/index>`" for s in used_in
                )
                lines.append(f"   *Cataloged constructions*: {refs}")
            lines.append("")

    lines.extend(
        [
            _rst_heading("Cited Geometers, Philosophers & Scholars", "-"),
            "",
        ]
    )

    for slug, entry in PERSONS.items():
        if slug in primary_authors:
            continue
        lines.extend(
            [
                f".. _person-{slug}:",
                "",
                f"**{entry['name']}** ({entry['dates']}) — *{entry['role']}*",
                f"   {entry['bio']}",
            ]
        )
        used_in = person_usage.get(slug, [])
        if used_in:
            refs = ", ".join(
                f":doc:`{s.catalog_code} <{s.family_slug}/{s.slug}/index>`" for s in used_in
            )
            lines.append(f"   *Cataloged constructions*: {refs}")
        lines.append("")

    return "\n".join(lines)


def _render_glossary_rst(
    term_usage: dict[str, list[ConstructionSpec]],
) -> str:
    lines: list[str] = [
        ":navigation: footer",
        ":order: 93",
        ":nav_title: Glossary",
        "",
        _rst_heading("Glossary", "="),
        "",
        ".. rubric:: Classical Euclidean, Projective & Rational Trigonometry Invariants",
        "",
        ("Definitions of classical Euclidean, projective, and Rational Trigonometry concepts "
        "used throughout the catalog."),
        "",
    ]

    for slug, entry in GLOSSARY.items():
        safe_def = entry["definition"].replace("|", r"\|")
        lines.extend(
            [
                f".. _term-{slug}:",
                "",
                f"**{entry['headword']}** (*{entry['translation']}*)",
                f"   {safe_def}",
            ]
        )
        used_in = term_usage.get(slug, [])
        if used_in:
            refs = ", ".join(
                f":doc:`{s.catalog_code} <{s.family_slug}/{s.slug}/index>`" for s in used_in[:12]
            )
            more = f" (+{len(used_in) - 12} more)" if len(used_in) > 12 else ""
            lines.append(f"   *Appears in*: {refs}{more}")
        lines.append("")

    return "\n".join(lines)


def generate_all(repo_root: Path | None = None) -> dict[str, Any]:
    """Generate all JSON apparatus files, SVGs, and Book Codex RST pages."""
    if repo_root is None:
        repo_root = Path(__file__).resolve().parents[4]

    resources_dir = repo_root / "resources"
    codex_dir = repo_root / "docsrc" / "constructions"
    resources_dir.mkdir(parents=True, exist_ok=True)
    codex_dir.mkdir(parents=True, exist_ok=True)

    # 1. Write apparatus JSON files
    (resources_dir / "persons.json").write_text(
        json.dumps(PERSONS, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (resources_dir / "citations.json").write_text(
        json.dumps(CITATIONS, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (resources_dir / "glossary.json").write_text(
        json.dumps(GLOSSARY, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    families_by_slug = {f.slug: f for f in FAMILIES}
    specs_by_family: dict[str, list[ConstructionSpec]] = {f.slug: [] for f in FAMILIES}
    certified_rows: list[tuple[ConstructionSpec, GoldenCertificate]] = []

    cite_usage: dict[str, list[ConstructionSpec]] = {}
    person_usage: dict[str, list[ConstructionSpec]] = {}
    term_usage: dict[str, list[ConstructionSpec]] = {}
    manifest_entries: list[dict[str, Any]] = []

    total_sections = 0
    total_chains = 0

    # 2. Build, certify, export SVG, and emit index.rst + code.rst for each construction
    for spec in CATALOG:
        fam = families_by_slug[spec.family_slug]
        specs_by_family[fam.slug].append(spec)

        model, cert = certify_construction(spec)
        certified_rows.append((spec, cert))
        total_sections += len(cert.detected_sections)
        total_chains += len(cert.detected_chains)

        for d in spec.discoverers:
            person_usage.setdefault(d, []).append(spec)
        for c in spec.citations:
            cite_usage.setdefault(c, []).append(spec)
        for t in spec.terms:
            term_usage.setdefault(t, []).append(spec)

        entry_dir = codex_dir / fam.slug / spec.slug
        entry_dir.mkdir(parents=True, exist_ok=True)

        svg_path = entry_dir / f"{spec.slug}.svg"
        export_catalog_svg(
            model,
            svg_path,
            cert=cert,
            graphic_id=spec.slug,
            title=f"{spec.catalog_code} — {spec.title}",
            bbox=spec.svg_bbox,
        )

        (entry_dir / "index.rst").write_text(
            _render_construction_index_rst(spec, fam, cert),
            encoding="utf-8",
        )
        (entry_dir / "code.rst").write_text(
            _render_construction_code_rst(spec, model, cert),
            encoding="utf-8",
        )

        manifest_entries.append(
            {
                "catalog_code": spec.catalog_code,
                "slug": spec.slug,
                "family_slug": spec.family_slug,
                "title": spec.title,
                "short_title": spec.short_title,
                "discoverers": list(spec.discoverers),
                "year": spec.year,
                "ctk_url": spec.ctk_url,
                "ctk_title": spec.ctk_title,
                "number_field": spec.number_field,
                "number_field_text": spec.number_field_text,
                "primary_long": list(cert.primary_long),
                "primary_short": list(cert.primary_short),
                "primary_collinear": list(cert.primary_collinear),
                "length_long": str(cert.length_long),
                "length_short": str(cert.length_short),
                "ratio_expr": str(cert.ratio_expr),
                "q_long": str(cert.q_long),
                "q_short": str(cert.q_short),
                "quadrance_ratio": str(cert.quadrance_ratio),
                "elementary_loci": cert.stats.elementary_loci,
                "lemoine_simplicity": cert.stats.lemoine_simplicity,
                "detected_section_count": len(cert.detected_sections),
                "detected_chain_count": len(cert.detected_chains),
                "svg_path": f"docsrc/constructions/{fam.slug}/{spec.slug}/{spec.slug}.svg",
            }
        )

    # 3. Emit family index.rst pages
    for fam in FAMILIES:
        fam_dir = codex_dir / fam.slug
        fam_dir.mkdir(parents=True, exist_ok=True)
        (fam_dir / "index.rst").write_text(
            _render_family_index_rst(fam, specs_by_family[fam.slug]),
            encoding="utf-8",
        )

    # 4. Emit Book Codex root index, comparative table, and apparatus pages
    (codex_dir / "index.rst").write_text(
        _render_book_index_rst(len(CATALOG), total_sections, total_chains),
        encoding="utf-8",
    )
    (codex_dir / "comparative_table.rst").write_text(
        _render_comparative_table_rst(certified_rows),
        encoding="utf-8",
    )
    (codex_dir / "bibliography.rst").write_text(
        _render_bibliography_rst(cite_usage),
        encoding="utf-8",
    )
    (codex_dir / "persons.rst").write_text(
        _render_persons_rst(person_usage),
        encoding="utf-8",
    )
    (codex_dir / "glossary.rst").write_text(
        _render_glossary_rst(term_usage),
        encoding="utf-8",
    )

    # 5. Write master catalog_manifest.json
    manifest = {
        "title": "GEOMETOR Catalog of Golden Ratio Constructions",
        "attribution": (
            "Catalogs universal mathematical constructions and theorems curated in Alexander "
            "Bogomolny's Cut-the-Knot archive (© 1996–2018 Alexander Bogomolny) and peer-reviewed "
            "geometric literature, modeled from scratch in 100% exact SymPy symbolic algebra."
        ),
        "family_count": len(FAMILIES),
        "construction_count": len(CATALOG),
        "total_detected_sections": total_sections,
        "total_detected_chains": total_chains,
        "families": [
            {
                "slug": f.slug,
                "code_prefix": f.code_prefix,
                "order": f.order,
                "title": f.title,
                "count": len(specs_by_family[f.slug]),
            }
            for f in FAMILIES
        ],
        "constructions": manifest_entries,
    }
    (resources_dir / "catalog_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return manifest


if __name__ == "__main__":
    summary = generate_all()
    print(
        f"Generated {summary['construction_count']} constructions across "
        f"{summary['family_count']} families "
        f"({summary['total_detected_sections']} golden sections, "
        f"{summary['total_detected_chains']} chains)."
    )
