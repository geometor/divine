"""Tests for incremental GoldenFieldTracker point-birth golden impact."""

from __future__ import annotations

from itertools import combinations

import sympy as sp
from geometor.model import Model

from geometor.divine.golden import (
    GoldenFieldTracker,
    find_golden_sections_in_model,
)


def _fundamental(model: Model, p1: sp.Point2D, p2: sp.Point2D) -> None:
    model.construct_line(p1, p2)
    model.construct_circle(p1, p2)
    model.construct_circle(p2, p1)


def test_tracker_matches_batch_on_level_2() -> None:
    """GoldenFieldTracker finds the exact same explicit-line sections as batch scan."""
    model = Model("level-2-tracked", use_point_subscript=True, enable_logging=False)
    tracker = GoldenFieldTracker(tag_model=True).attach(model)

    a = model.set_point(sp.Rational(-1, 2), 0, classes=["given"])
    b = model.set_point(sp.Rational(1, 2), 0, classes=["given"])
    _fundamental(model, a, b)
    for p1, p2 in combinations(model.points, 2):
        _fundamental(model, p1, p2)
    tracker.sync(model)

    batch_sections, _ = find_golden_sections_in_model(model, include_collinear=False)

    tracked_keys = {tuple(s.points) for s in tracker.sections}
    batch_keys = {tuple(s.points) for s in batch_sections}
    assert tracked_keys == batch_keys
    assert sum(len(v) for v in tracker.impact_by_point.values()) == len(tracker.sections)
