"""
Event listeners for divine analysis.
"""
import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, Element
from geometor.model.sections import Section

from geometor.model.utils import sort_points

def point_added_listener(model: Model, pt: spg.Point, logger=None):
    """
    Logs the creation of a point and then analyzes it to find all
    possible line sections.
    """
    if not logger:
        return

    # Log the creation of the point first.
    logger.info(f"    {model[pt].ID} : {{ {pt.x}, {pt.y} }}")

    # Use a local log function for indented analysis messages.
    def log_analysis(message):
        logger.info(f"        {message}")

    log_analysis(f"divine analysis")

    parent_lines = [p for p in model[pt].parents if isinstance(p, spg.Line)]
    if not parent_lines:
        log_analysis("no parent lines found")
        return

    log_analysis(f"found {len(parent_lines)} parent line(s): {[model[l].ID for l in parent_lines]}")

    for i, line in enumerate(parent_lines):
        log_analysis(f"line {i+1} of {len(parent_lines)} : {model[line].ID}")
        points_on_line = [p for p in model.points if line.contains(p)]

        if len(points_on_line) < 3:
            log_analysis(f"  line has fewer than 3 points")
            continue

        sorted_pts = sort_points(points_on_line)
        from itertools import combinations
        section_candidates = list(combinations(sorted_pts, 3))

        relevant_sections = [s for s in section_candidates if pt in s]
        log_analysis(f"  {len(relevant_sections)} sections with {model[pt].ID}")

        for section_pts in relevant_sections:
            section = Section(section_pts)
            s_IDs = [model[p].ID for p in section_pts]
            if section.is_golden:
                log_analysis(f"    / {' '.join(s_IDs)} /")
                model.set_section(section.points, classes=["golden"])
