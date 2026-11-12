geometor.divine.catalog.minimal_compass
=======================================

.. py:module:: geometor.divine.catalog.minimal_compass

.. autoapi-nested-parse::

   Family 01: Classical & Minimal-Step Compass-and-Straightedge Constructions.

   Catalogs Euclid's foundational *Elements* II.11 division, the right-triangle
   hypotenuse transfer, Émile Lemoine and Kurt Hofstetter's minimal 5-step
   constructions, Mascheroni 5-circle compass-only division, rusty-compass
   division, and Bùi Quang Tuân's 5-step circle secant construction.



Attributes
----------

.. autoapisummary::

   geometor.divine.catalog.minimal_compass.MINIMAL_COMPASS_SPECS


Functions
---------

.. autoapisummary::

   geometor.divine.catalog.minimal_compass.build_euclid_ii_11
   geometor.divine.catalog.minimal_compass.build_pythagorean_transfer
   geometor.divine.catalog.minimal_compass.build_lemoine_hofstetter_5step
   geometor.divine.catalog.minimal_compass.build_hofstetter_5step_2004
   geometor.divine.catalog.minimal_compass.build_hofstetter_compass_only
   geometor.divine.catalog.minimal_compass.build_hofstetter_rusty_compass
   geometor.divine.catalog.minimal_compass.build_bui_5step


Module Contents
---------------

.. py:function:: build_euclid_ii_11() -> geometor.divine.catalog.schema.ConstructionResult

   Euclid's Elements II.11 & VI.30 square-and-midpoint division of AB.


.. py:function:: build_pythagorean_transfer() -> geometor.divine.catalog.schema.ConstructionResult

   Heron-Ptolemy right-triangle hypotenuse transfer on a 1:2 right triangle.


.. py:function:: build_lemoine_hofstetter_5step() -> geometor.divine.catalog.schema.ConstructionResult

   Lemoine (1902), Reusch (1904) & Hofstetter (2003) 5-step segment division.


.. py:function:: build_hofstetter_5step_2004() -> geometor.divine.catalog.schema.ConstructionResult

   Kurt Hofstetter's 2004 5-step straightedge-and-compass division.


.. py:function:: build_hofstetter_compass_only() -> geometor.divine.catalog.schema.ConstructionResult

   Kurt Hofstetter's 2002 Mascheroni 5-circle compass-only construction.


.. py:function:: build_hofstetter_rusty_compass() -> geometor.divine.catalog.schema.ConstructionResult

   Kurt Hofstetter's 2005 fixed-opening rusty-compass golden division.


.. py:function:: build_bui_5step() -> geometor.divine.catalog.schema.ConstructionResult

   Bùi Quang Tuân's 5-step collinear three-circle secant construction.


.. py:data:: MINIMAL_COMPASS_SPECS
   :type:  tuple[geometor.divine.catalog.schema.ConstructionSpec, ...]

