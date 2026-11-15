"""Tools and symbolic catalog for analyzing divine proportions in geometric models.

**Key Components**
- **Analysis Hook**: :func:`register_divine_hook` automatically analyzes points as they are added to a model.
- **Golden Sections & Chains**: Exact Rational Trigonometry discovery tools (:mod:`geometor.divine.golden`).
- **Catalog of Golden Ratio Constructions**: 45 exact symbolic constructions and theorems across 7 families (:mod:`geometor.divine.catalog`).
- **Events**: Listeners that trigger real-time analysis on model updates.

**Usage**
Register the divine hook with a :class:`~geometor.model.Model` instance or build a certified catalog construction via :func:`~geometor.divine.catalog.build_construction`.
"""

from __future__ import annotations

from .catalog import CATALOG, FAMILIES, build_construction, get_construction
from .divine import register_divine_hook

__all__ = [
    "CATALOG",
    "FAMILIES",
    "build_construction",
    "get_construction",
    "register_divine_hook",
]

__version__ = "0.4.4"
