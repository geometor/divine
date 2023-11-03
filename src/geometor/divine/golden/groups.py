from rich import print
from collections import defaultdict

from geometor.model import *
from geometor.model.utils import *
from geometor.render import *


def group_sections_by_size(sections: list[Section]) -> dict[sp.Expr, list[Section]]:
    groups = defaultdict(list)
    for section in sections:
        key = section.min_length
        groups[key].append(section)

    sorted_groups = dict(
        sorted(groups.items(), key=lambda item: float(item[0].evalf()))
    )

    return sorted_groups


def group_sections_by_segments(
    sections: list[Section],
) -> dict[spg.Segment, list[Section]]:
    groups = defaultdict(list)
    for section in sections:
        for segment in section.segments:
            groups[segment].append(section)

    sorted_groups = dict(
        sorted(groups.items(), key=lambda item: float(item[0].length.evalf()))
    )

    return sorted_groups


def group_sections_by_points(sections: list[Section]) -> dict[spg.Point, list[Section]]:
    groups = defaultdict(list)
    for section in sections:
        for point in section.points:
            groups[point].append(section)

    sorted_groups = dict(
        sorted(groups.items(), key=lambda item: len(item[1]), reverse=True)
    )

    return sorted_groups
