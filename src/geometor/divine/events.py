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
    Analyzes a new point to find all possible line sections.
    """
    print(f"\n[DIVINE] Listener triggered for point: {model[pt].ID} ({pt.x}, {pt.y})")
    
    parent_lines = [p for p in model[pt].parents if isinstance(p, spg.Line)]
    if not parent_lines:
        print("[DIVINE] No parent lines found.")
        return

    print(f"[DIVINE] Found {len(parent_lines)} parent line(s): {[model[l].ID for l in parent_lines]}")

    for line in parent_lines:
        points_on_line = [p for p in model.points if line.contains(p)]
        
        if len(points_on_line) < 3:
            print(f"  [DIVINE] Line {model[line].ID} has fewer than 3 points. Skipping.")
            continue

        # Sort the points to ensure correct section ordering
        sorted_pts = sort_points(points_on_line)
        print(f"  [DIVINE] Sorted points on line {model[line].ID}: {[model[p].ID for p in sorted_pts]}")

        from itertools import combinations
        
        section_candidates = list(combinations(sorted_pts, 3))
        print(f"  [DIVINE] Found {len(section_candidates)} total 3-point combinations.")

        # Filter for combinations that include the new point
        relevant_sections = [s for s in section_candidates if pt in s]
        print(f"  [DIVINE] Testing {len(relevant_sections)} section(s) containing point {model[pt].ID}...")

        for i, section_pts in enumerate(relevant_sections):
            section = Section(section_pts)
            s_IDs = [model[p].ID for p in section_pts]
            print(f"    [TEST {i+1}] Section: {s_IDs}, Ratio: {section.ratio.evalf():.4f}, Golden: {section.is_golden}")
            if section.is_golden:
                print(f"      [GOLDEN FOUND] Adding section {s_IDs}")
                model.set_section(section.points, classes=["golden"])

