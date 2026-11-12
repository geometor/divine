"""Exact Symbolic Catalog of Golden Ratio Constructions & Theorems.

Catalogs 45 geometric constructions and theorems across 7 families—curated from
classical antiquity, *Forum Geometricorum*, *Mathematics Magazine*, *American
Mathematical Monthly*, and Alexander Bogomolny's *Cut-the-Knot* archive—verified
with 100% exact SymPy symbolic algebra, Rational Trigonometry quadrances, and
automated :mod:`geometor.divine` golden-chain discovery.
"""

from __future__ import annotations

from .registry import (
    CATALOG,
    CATALOG_BY_CODE,
    CATALOG_BY_SHORT_SLUG,
    CATALOG_BY_SLUG,
    FAMILIES,
    FAMILIES_BY_SLUG,
    build_construction,
    get_construction,
    get_family,
    iter_catalog,
)
from .render import export_catalog_svg, render_catalog_svg
from .schema import (
    ConstructionResult,
    ConstructionSpec,
    DetectedChain,
    DetectedSection,
    FamilySpec,
    GeometrographieStats,
    GoldenCertificate,
    certify_construction,
    count_geometrographie,
)

__all__ = [
    "CATALOG",
    "CATALOG_BY_CODE",
    "CATALOG_BY_SHORT_SLUG",
    "CATALOG_BY_SLUG",
    "FAMILIES",
    "FAMILIES_BY_SLUG",
    "ConstructionResult",
    "ConstructionSpec",
    "DetectedChain",
    "DetectedSection",
    "FamilySpec",
    "GeometrographieStats",
    "GoldenCertificate",
    "build_construction",
    "certify_construction",
    "count_geometrographie",
    "export_catalog_svg",
    "get_construction",
    "get_family",
    "iter_catalog",
    "render_catalog_svg",
]
