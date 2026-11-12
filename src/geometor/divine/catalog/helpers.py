"""Shared exact symbolic construction helpers for :mod:`geometor.divine.catalog`."""

from __future__ import annotations

from geometor.model import Model

from .schema import ConstructionResult


def new_catalog_model(name: str) -> Model:
    """Create a deterministic, exact symbolic :class:`~geometor.model.Model`."""
    return Model(name, auto_intersect=False, enable_logging=False)


def make_result(
    model: Model,
    primary_long: tuple[str, str],
    primary_short: tuple[str, str],
    primary_collinear: tuple[str, str, str],
) -> ConstructionResult:
    """Register ``primary_collinear`` on ``model`` and bundle a :class:`ConstructionResult`."""
    pts = [model.get_element_by_ID(pid) for pid in primary_collinear]
    model.set_section(pts, classes=["golden"], by="Primary catalog golden section")
    model.conclude(
        pts[0],
        pts[1],
        pts[2],
        by=f"Exact golden ratio certified on {primary_long[0]}{primary_long[1]} : {primary_short[0]}{primary_short[1]}",
    )
    return ConstructionResult(
        model=model,
        primary_long=primary_long,
        primary_short=primary_short,
        primary_collinear=primary_collinear,
    )
