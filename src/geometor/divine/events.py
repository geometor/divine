"""
Event listeners for divine analysis.
"""
import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, Element
from geometor.model.sections import Section

from geometor.model.utils import sort_points

def point_added_listener(model: Model, pt: spg.Point):
    """
    Logs the creation of a point and then analyzes it to find all
    possible line sections.
    """
    # Log the creation of the point first.
    model.log(f"    [bold]{model[pt].ID}[/bold] : {{ {pt.x}, {pt.y} }}")

    # Use a local log function for indented analysis messages.
    def log_analysis(message):
        model.log(f"        {message}")

    log_analysis(f"divine analysis")

    parent_lines = [p for p in model[pt].parents if isinstance(p, spg.Line)]
    if not parent_lines:
        log_analysis("no parent lines found")
        return

    line_IDs = ", ".join([f"[bold]{model[l].ID}[/bold]" for l in parent_lines])
    # log_analysis(f"found {len(parent_lines)} parent line(s): {line_IDs}")

    for i, line in enumerate(parent_lines):
        log_analysis(f"line {i+1} of {len(parent_lines)} : [bold]{model[line].ID}[/bold]")
        points_on_line = [p for p in model.points if line.contains(p) and not model[p].guide]

        if len(points_on_line) < 3:
            log_analysis(f"  line has fewer than 3 points")
            continue

        sorted_pts = sort_points(points_on_line)
        from itertools import combinations
        section_candidates = list(combinations(sorted_pts, 3))

        relevant_sections = [s for s in section_candidates if pt in s]
        log_analysis(f"  {len(relevant_sections)} sections with [bold]{model[pt].ID}[/bold]")

        for section_pts in relevant_sections:
            section = Section(section_pts)
            s_IDs = [model[p].ID for p in section_pts]
            if section.is_golden:
                section_IDs_str = " ".join([f"[bold]{_id}[/bold]" for _id in s_IDs])
                log_analysis(f"    / {section_IDs_str} /")
                model.set_section(section.points, classes=["golden"])
