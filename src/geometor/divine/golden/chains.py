"""Golden Chain Analyzer: Harmonic Range Identification in Golden Sections.

This module analyzes and explores chains of connected golden sections,
unraveling proportional progressions within exact symbolic geometric models.

Features:

- ``find_chains_in_sections``: Identifies maximal chains within a collection of
  golden sections, returning a hierarchical tree of connected sections.
- ``unpack_chains``: Unpacks the chain tree into individual :class:`Chain`
  objects ready for symbolic inspection.
"""

from __future__ import annotations

from geometor.model.chains import Chain
from geometor.model.sections import Section


def _endpoint_pair(points: list | tuple, start: bool) -> tuple:
    pts = tuple(points)
    return pts[:2] if start else pts[1:]


def find_chains_in_sections(sections: list[Section]) -> dict[Section, dict]:
    """Identify maximal chains of connected golden sections.

    Two ordered sections ``(A, B, C)`` and ``(B, C, D)`` connect when the
    trailing segment ``(B, C)`` of the first equals the leading segment
    ``(B, C)`` of the second.

    Args:
        sections: A list of :class:`Section` objects to analyze.

    Returns:
        dict: Tree structure mapping root :class:`Section` nodes to nested
        dictionaries of connected successor :class:`Section` nodes.
    """
    unique_sections: list[Section] = []
    seen_keys: set[tuple] = set()
    for sec in sections:
        pts_key = tuple(sec.points)
        if pts_key not in seen_keys:
            seen_keys.add(pts_key)
            unique_sections.append(
                sec if isinstance(sec.points, list) else Section(list(sec.points))
            )

    by_start: dict[tuple, list[Section]] = {}
    has_predecessor: set[Section] = set()
    for sec in unique_sections:
        start_key = _endpoint_pair(sec.points, start=True)
        by_start.setdefault(start_key, []).append(sec)

    for sec in unique_sections:
        end_key = _endpoint_pair(sec.points, start=False)
        for nxt in by_start.get(end_key, ()):
            if nxt != sec:
                has_predecessor.add(nxt)

    def build_subtree(current: Section, visited: frozenset[Section]) -> dict[Section, dict]:
        end_key = _endpoint_pair(current.points, start=False)
        subtree: dict[Section, dict] = {}
        for nxt in by_start.get(end_key, ()):
            if nxt not in visited:
                subtree[nxt] = build_subtree(nxt, visited | {nxt})
        return subtree

    chain_tree: dict[Section, dict] = {}
    roots = [sec for sec in unique_sections if sec not in has_predecessor]
    # Fallback in case of synthetic cyclic test fixtures
    if not roots and unique_sections:
        roots = list(unique_sections)

    for root in roots:
        children = build_subtree(root, frozenset({root}))
        if children:
            chain_tree[root] = children

    return chain_tree


def unpack_chains(tree: dict[Section, dict]) -> list[Chain]:
    """Unpack a chain tree into a list of individual :class:`Chain` objects.

    Args:
        tree: Tree structure returned by :func:`find_chains_in_sections`.

    Returns:
        list[Chain]: Connected golden-section chains.
    """

    def dfs(node: dict[Section, dict], path: list[Section], chains: list[Chain]) -> None:
        if not node:
            chains.append(Chain(path))
            return
        for child, subtree in node.items():
            dfs(subtree, path + [child], chains)

    chains: list[Chain] = []
    for root, subtree in tree.items():
        if not subtree:
            chains.append(Chain([root]))
        else:
            dfs(subtree, [root], chains)

    return chains
