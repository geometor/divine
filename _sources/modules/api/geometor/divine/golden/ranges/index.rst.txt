geometor.divine.golden.ranges
=============================

.. py:module:: geometor.divine.golden.ranges


Functions
---------

.. autoapisummary::

   geometor.divine.golden.ranges.check_range
   geometor.divine.golden.ranges.analyze_harmonics
   geometor.divine.golden.ranges.analyze_harmonics_by_segment


Module Contents
---------------

.. py:function:: check_range(r)

   Check if a range of 4 points forms a harmonic range.

   :param r: A tuple of 4 points.

   :returns: The cross ratio value (0 if harmonic).
   :rtype: sp.Expr


.. py:function:: analyze_harmonics(line)

   Analyze a line for harmonic ranges.

   :param line: The line to analyze.

   :returns: A list of harmonic ranges (tuples of 4 points).
   :rtype: list


.. py:function:: analyze_harmonics_by_segment(sections_by_line)

   Group harmonic ranges by segment.

   :param sections_by_line: Dictionary of sections by line.

   :returns: Nested dictionary mapping lines to segments to harmonic ranges.
   :rtype: dict


