"""Event listeners for divine analysis.

This module contains listeners that trigger analysis when elements are added to the model.
"""

from __future__ import annotations

from itertools import combinations

import sympy.geometry as spg
from geometor.model import Model
from geometor.model.sections import Section

from .golden import is_section_golden, points_on_line


def point_added_listener(model: Model, pt: spg.Point) -> None:
    """Log the creation of a point and analyze incident lines for golden sections.

    Args:
        model: The model containing the point.
        pt: The point that was added.
    """

    def log_analysis(message: str) -> None:
        model.log(f"        {message}")

    log_analysis("divine analysis")

    parent_lines = [p for p in model[pt].parents if isinstance(p, spg.Line)]
    if not parent_lines:
        log_analysis("no parent lines found")
        return

    for i, line in enumerate(parent_lines):
        log_analysis(
            f"line {i + 1} of {len(parent_lines)} : [bold]{model[line].ID}[/bold]"
        )
        line_pts = points_on_line(model, line, include_guides=False)

        if len(line_pts) < 3:
            log_analysis("  line has fewer than 3 points")
            continue

        section_candidates = [
            list(combo) for combo in combinations(line_pts, 3) if pt in combo
        ]
        log_analysis(
            f"  {len(section_candidates)} sections with [bold]{model[pt].ID}[/bold]"
        )

        for section_pts in section_candidates:
            if is_section_golden(section_pts):
                section = Section(section_pts)
                s_ids = [model[p].ID for p in section_pts]
                section_ids_str = " ".join([f"[bold]{_id}[/bold]" for _id in s_ids])
                log_analysis(f"    / {section_ids_str} /")
                model.set_section(section.points, classes=["golden"])
