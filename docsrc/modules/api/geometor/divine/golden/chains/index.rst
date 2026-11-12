geometor.divine.golden.chains
=============================

.. py:module:: geometor.divine.golden.chains

.. autoapi-nested-parse::

   Golden Chain Analyzer: Harmonic Range Identification in Golden Sections.

   This module analyzes and explores chains of connected golden sections,
   unraveling proportional progressions within exact symbolic geometric models.

   Features:

   - ``find_chains_in_sections``: Identifies maximal chains within a collection of
     golden sections, returning a hierarchical tree of connected sections.
   - ``unpack_chains``: Unpacks the chain tree into individual :class:`Chain`
     objects ready for symbolic inspection.



Functions
---------

.. autoapisummary::

   geometor.divine.golden.chains.find_chains_in_sections
   geometor.divine.golden.chains.unpack_chains


Module Contents
---------------

.. py:function:: find_chains_in_sections(sections: list[geometor.model.sections.Section]) -> dict[geometor.model.sections.Section, dict]

   Identify maximal chains of connected golden sections.

   Two ordered sections ``(A, B, C)`` and ``(B, C, D)`` connect when the
   trailing segment ``(B, C)`` of the first equals the leading segment
   ``(B, C)`` of the second.

   :param sections: A list of :class:`Section` objects to analyze.

   :returns: Tree structure mapping root :class:`Section` nodes to nested
             dictionaries of connected successor :class:`Section` nodes.
   :rtype: dict


.. py:function:: unpack_chains(tree: dict[geometor.model.sections.Section, dict]) -> list[geometor.model.chains.Chain]

   Unpack a chain tree into a list of individual :class:`Chain` objects.

   :param tree: Tree structure returned by :func:`find_chains_in_sections`.

   :returns: Connected golden-section chains.
   :rtype: list[Chain]


