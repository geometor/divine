"""Comprehensive test suite for the GEOMETOR Catalog of Golden Ratio Constructions."""

from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest
import sympy as sp
from geometor.model import Model, zero_test

from geometor.divine import (
    CATALOG,
    FAMILIES,
    build_construction,
    get_construction,
)
from geometor.divine.catalog import CATALOG_BY_CODE, CATALOG_BY_SLUG
from geometor.divine.golden import (
    find_chains_in_model,
    find_chains_in_sections,
    find_golden_sections_in_model,
    unpack_chains,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCSRC_CONSTRUCTIONS = REPO_ROOT / "docsrc" / "constructions"
RESOURCES_DIR = REPO_ROOT / "resources"


def _collect_svg_refs(svg_path: Path) -> set[str]:
    tree = ET.parse(svg_path)
    root = tree.getroot()
    tokens: set[str] = set()
    for el in root.iter():
        el_id = el.attrib.get("id")
        if el_id:
            tokens.add(el_id.strip())
        dref = el.attrib.get("data-ref")
        if dref:
            tokens.add(dref.strip())
        aliases = el.attrib.get("data-aliases", "")
        for part in aliases.split("|"):
            tok = part.strip()
            if tok:
                tokens.add(tok)
    return tokens


def test_chains_order_independence_and_implicit_collinear_triples() -> None:
    """Verify the chains.py pruning bug fix and implicit collinear golden scanning."""
    m = Model("golden_chain_regression", auto_intersect=False)
    # 4-point symmetric golden chain along y = x (no explicit construct_line!)
    p0 = m.set_point(0, 0, ID="P0")
    p1 = m.set_point(1, 1, ID="P1")
    p2 = m.set_point(sp.GoldenRatio, sp.GoldenRatio, ID="P2")
    p3 = m.set_point(sp.GoldenRatio + 1, sp.GoldenRatio + 1, ID="P3")
    assert (p0, p1, p2, p3) is not None

    sections, _ = find_golden_sections_in_model(m, include_collinear=True)
    assert len(sections) >= 2

    # Forward and reversed section orderings must both find the connected 4-point chain
    chains_fwd = unpack_chains(find_chains_in_sections(list(sections)))
    chains_rev = unpack_chains(find_chains_in_sections(list(reversed(sections))))
    assert any(len(ch.sections) >= 2 for ch in chains_fwd)
    assert any(len(ch.sections) >= 2 for ch in chains_rev)

    _, model_chains = find_chains_in_model(m, include_collinear=True)
    assert any(len(ch.sections) >= 2 for ch in model_chains)


def test_catalog_registry_integrity() -> None:
    """Verify 7 families, 45 unique constructions, and flexible lookup keys."""
    assert len(FAMILIES) == 7
    assert len(CATALOG) == 45
    assert len(CATALOG_BY_CODE) == 45
    assert len(CATALOG_BY_SLUG) == 45

    counts_by_family = {
        fam.slug: sum(1 for spec in CATALOG if spec.family_slug == fam.slug)
        for fam in FAMILIES
    }
    assert counts_by_family == {
        "01-minimal-compass": 7,
        "02-equilateral-hexagon": 7,
        "03-squares-rectangles": 8,
        "04-right-and-345": 4,
        "05-pentagons-polygons": 6,
        "06-circles-sangaku": 7,
        "07-rhombi-trapezoids-algebra": 6,
    }

    # Lookup by code, family/slug, and short slug
    s1 = get_construction("GC-01.01")
    s2 = get_construction("01-minimal-compass/01-euclid-ii-11")
    s3 = get_construction("01-euclid-ii-11")
    assert s1 is s2 is s3

    with pytest.raises(KeyError):
        get_construction("GC-99.99")


@pytest.mark.parametrize(
    "code",
    [spec.catalog_code for spec in CATALOG],
)
def test_symbolic_construction_and_certificate(code: str) -> None:
    """Every catalog construction must be 100% exact symbolic and certified GoldenRatio."""
    model, cert = build_construction(code)

    assert len(model.points) >= 3
    for pt in model.points:
        assert not pt.x.atoms(sp.Float), f"{code} point {model[pt].ID} has Float x={pt.x}"
        assert not pt.y.atoms(sp.Float), f"{code} point {model[pt].ID} has Float y={pt.y}"
        pt_id = model[pt].ID
        if not model[pt].guide:
            assert pt_id.isalnum(), f"{code} visible point ID {pt_id!r} must be alphanumeric"

    assert cert.ratio_expr == sp.GoldenRatio
    assert zero_test(cert.q_long - (sp.GoldenRatio + 1) * cert.q_short)
    assert zero_test(cert.quadrance_ratio - (sp.GoldenRatio + 1))
    assert len(cert.detected_sections) >= 1


def test_compass_only_rusty_compass_and_golden_chains() -> None:
    """Verify compass-only, rusty-compass, 5-step locus counts, and golden chain discoveries."""
    # Hofstetter 5-step compass-only construction uses 0 lines and 5 circles
    _, cert_compass5 = build_construction("GC-01.05")
    assert cert_compass5.stats.constructed_lines == 0
    assert cert_compass5.stats.constructed_circles == 5
    assert cert_compass5.stats.elementary_loci == 5
    assert len(cert_compass5.detected_chains) >= 1

    # Hofstetter 2004 and Bui 2014 5-step divisions each use 5 elementary loci (2 lines + 3 circles)
    for code_5step in ("GC-01.04", "GC-01.07"):
        _, cert_5 = build_construction(code_5step)
        assert cert_5.stats.constructed_lines == 2
        assert cert_5.stats.constructed_circles == 3
        assert cert_5.stats.elementary_loci == 5

    # Hofstetter rusty compass uses 3 circles of identical unit radius 1
    m_rusty, cert_rusty = build_construction("GC-01.06")
    assert cert_rusty.stats.constructed_circles == 3
    for cir in m_rusty.circles:
        if not m_rusty[cir].guide:
            assert zero_test(cir.radius - 1)

    # Symmetric / projective constructions yield multi-link golden chains
    for chain_code in (
        "GC-03.07",  # Bui Greek Cross & Square
        "GC-05.05",  # Star of Six Pentagons
        "GC-06.05",  # Kocik Golden Window
        "GC-07.05",  # Tran Mixtilinear Circles
    ):
        _, cert = build_construction(chain_code)
        assert len(cert.detected_chains) >= 1, (
            f"{chain_code} expected >= 1 golden chain"
        )


def test_codex_resources_and_svg_g_role_parity() -> None:
    """Verify resources JSON integrity, .euclid-graphic XML structure, and 100% :g: parity."""
    persons = json.loads((RESOURCES_DIR / "persons.json").read_text(encoding="utf-8"))
    citations = json.loads((RESOURCES_DIR / "citations.json").read_text(encoding="utf-8"))
    glossary = json.loads((RESOURCES_DIR / "glossary.json").read_text(encoding="utf-8"))
    manifest = json.loads(
        (RESOURCES_DIR / "catalog_manifest.json").read_text(encoding="utf-8")
    )

    assert manifest["construction_count"] == 45
    assert manifest["family_count"] == 7

    g_role_re = re.compile(r":g:`([^`]+)`")
    person_re = re.compile(r":person:`(?:[^`<]*<([^`>]+)>|([^`]+))`")
    cite_re = re.compile(r":cite:`(?:[^`<]*<([^`>]+)>|([^`]+))`")
    term_re = re.compile(r":term:`(?:[^`<]*<([^`>]+)>|([^`]+))`")

    for spec in CATALOG:
        entry_dir = DOCSRC_CONSTRUCTIONS / spec.family_slug / spec.slug
        svg_path = entry_dir / f"{spec.slug}.svg"
        idx_path = entry_dir / "index.rst"
        code_path = entry_dir / "code.rst"

        assert svg_path.is_file(), f"Missing SVG for {spec.catalog_code}: {svg_path}"
        assert idx_path.is_file(), f"Missing index.rst for {spec.catalog_code}: {idx_path}"
        assert code_path.is_file(), f"Missing code.rst for {spec.catalog_code}: {code_path}"

        tree = ET.parse(svg_path)
        root = tree.getroot()
        assert "euclid-graphic" in root.attrib.get("class", "")

        marker_ids = {
            el.attrib.get("id")
            for el in root.iter()
            if el.tag.endswith("marker")
        }
        assert {"geom-tick-1", "geom-tick-2", "geom-tick-3"}.issubset(marker_ids)
        for el in root.iter():
            if el.tag.endswith("marker"):
                assert el.attrib.get("markerUnits") == "userSpaceOnUse"

        # 3-vertex midpoint <path> segments exist
        seg_paths = [
            el
            for el in root.iter()
            if el.tag.endswith("path") and "geom-segment" in el.attrib.get("class", "")
        ]
        assert len(seg_paths) >= 2
        for sp_el in seg_paths:
            d_attr = sp_el.attrib.get("d", "")
            assert d_attr.count(" L ") == 2, (
                f"{spec.catalog_code} segment path must have 3 vertices: {d_attr}"
            )

        # Every :g: token in index.rst (handling both :g:`X` and :g:`label <X>`) resolves to SVG
        svg_tokens = _collect_svg_refs(svg_path)
        rst_text = idx_path.read_text(encoding="utf-8")
        for g_raw in g_role_re.findall(rst_text):
            m_target = re.search(r"<([^>]+)>", g_raw)
            tok = m_target.group(1).strip() if m_target else g_raw.strip()
            assert tok in svg_tokens, (
                f"{spec.catalog_code} unmatched :g:`{g_raw}` (target {tok!r}) in {idx_path}"
            )

        # Every :person:, :cite:, and :term: reference exists in resources/*.json
        for m in person_re.finditer(rst_text):
            slug = (m.group(1) or m.group(2)).strip()
            assert slug in persons, f"{spec.catalog_code} unknown person {slug!r}"
        for m in cite_re.finditer(rst_text):
            slug = (m.group(1) or m.group(2)).strip()
            assert slug in citations, f"{spec.catalog_code} unknown citation {slug!r}"
        for m in term_re.finditer(rst_text):
            slug = (m.group(1) or m.group(2)).strip()
            assert slug in glossary, f"{spec.catalog_code} unknown glossary term {slug!r}"
