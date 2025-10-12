"""
Event listeners for divine analysis.
"""
import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, Element 
from geometor.model.sections import Section

def point_added_listener(model: Model, pt: spg.Point):
    """
    Analyzes a new point to find all possible line sections.
    """
    print(f"point_added_listener triggered for point: {pt}")
    
    # 1. Get parent lines of the new point
    parent_lines = [p for p in model[pt].parents if isinstance(p, spg.Line)]

    for line in parent_lines:
        # 2. Get all points on the line
        points_on_line = [p for p in model.points if line.contains(p)]
        
        # 3. Find combinations of 2 points from the other points
        from itertools import combinations
        
        other_points = [p for p in points_on_line if p != pt]
        if len(other_points) < 2:
            continue

        for pt1, pt2 in combinations(other_points, 2):
            # 4. Check for golden sections and add them to the model
            section1 = Section([pt, pt1, pt2])
            if section1.is_golden:
                model.set_section(section1.points, classes=["golden"])

            section2 = Section([pt1, pt, pt2])
            if section2.is_golden:
                model.set_section(section2.points, classes=["golden"])

            section3 = Section([pt1, pt2, pt])
            if section3.is_golden:
                model.set_section(section3.points, classes=["golden"])

