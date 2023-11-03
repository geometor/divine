"""
find and analyze golden sections
"""

from rich import print
from collections import defaultdict

from geometor.model import *
from geometor.model.utils import *
from geometor.render import *

from multiprocessing import Pool, cpu_count

from .chains import *
from .groups import *
from .ranges import *

Φ = sp.GoldenRatio
phi = sp.Rational(1, 2) + (sp.sqrt(5) / 2)


def find_golden_sections_in_model(
    model: Model,
) -> tuple[list[Section], dict[spg.Line, list[Section]]]:
    """
    analyze all lines in the model for golden sections
    """
    sections = []
    sections_by_line = {}

    # TODO: start the Pool here
    for i, line in enumerate(model.lines):
        # get points on the line
        line_pts = model[line].parents
        line_sections = find_golden_sections_in_points(line_pts)
        sections.extend(line_sections)
        sections_by_line[line] = line_sections

    return sections, sections_by_line


def find_golden_sections_in_points(pts) -> list[Section]:
    """
    find golden sections in combinations of 3 points in list
    returns a list of golden section pairs
    """
    goldens = []
    pts = sort_points(pts)

    # this will walk the combinations of three points down the line
    sections = list(combinations(pts, 3))

    with Pool(cpu_count()) as pool:
        results = pool.map(is_section_golden, sections)
        goldens = [Section(section) for i, section in enumerate(sections) if results[i]]

    return goldens


def is_section_golden(section_points) -> bool:
    section = Section(section_points)
    return section.is_golden


