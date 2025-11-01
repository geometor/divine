
from collections import defaultdict

from geometor.model import *
from geometor.model.utils import *
from geometor.render import *

def check_range(r):
    ad = spg.Segment(r[0], r[3]).length
    cd = spg.Segment(r[2], r[3]).length
    ac = spg.Segment(r[0], r[2]).length
    bc = spg.Segment(r[1], r[2]).length
    return sp.simplify((ad / cd) - (ac / bc))


def analyze_harmonics(line):
    line_pts = sort_points(line.pts)
    #  for pt in line_pts:
    #  print(pt.x, pt.x.evalf(), pt.y, pt.y.evalf())
    ranges = list(combinations(line_pts, 4))
    harmonics = []
    for i, r in enumerate(ranges):
        chk = check_range(r)
        #  if chk == 1 or chk == -1:
        #  if chk == 0 or chk == -1:
        if chk == 0:
            #  print(i, chk)
            #  print(f'    {r}')
            harmonics.append(r)
    return harmonics


def analyze_harmonics_by_segment(sections_by_line):
    harmonics_by_segment = {}
    for line, line_sections in sections_by_line.items():
        #  print(line)
        group_by_segments = defaultdict(list)
        for line_section in line_sections:
            group_by_segments[line_section[0]].append(line_section)
            group_by_segments[line_section[1]].append(line_section)
        harmonics_by_segment[line] = group_by_segments

    return harmonics_by_segment

