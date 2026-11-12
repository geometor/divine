geometor.divine.catalog.squares_rectangles
==========================================

.. py:module:: geometor.divine.catalog.squares_rectangles

.. autoapi-nested-parse::

   Family 03: Squares, Grids & Golden Rectangles.

   Catalogs exact symbolic Golden Ratio constructions arising from squares,
   $2 \times 2$ and $3 \times 3$ lattice grids, inscribed incircles, the Greek cross,
   and rotated unit squares curated on Cut-the-Knot.



Attributes
----------

.. autoapisummary::

   geometor.divine.catalog.squares_rectangles.SQUARES_RECTANGLES_SPECS


Functions
---------

.. autoapisummary::

   geometor.divine.catalog.squares_rectangles.build_tran_square_inscribed_semicircle
   geometor.divine.catalog.squares_rectangles.build_tran_square_midpoints
   geometor.divine.catalog.squares_rectangles.build_nguyen_2x2_square
   geometor.divine.catalog.squares_rectangles.build_tran_mcgucken_3x3_circle
   geometor.divine.catalog.squares_rectangles.build_tran_3x3_incenter
   geometor.divine.catalog.squares_rectangles.build_suppa_square_inradii
   geometor.divine.catalog.squares_rectangles.build_bui_cross_and_square
   geometor.divine.catalog.squares_rectangles.build_arioni_rotating_square


Module Contents
---------------

.. py:function:: build_tran_square_inscribed_semicircle() -> geometor.divine.catalog.schema.ConstructionResult

   Square inscribed in a right isosceles triangle inside a circle (Tran Quang Hung).


.. py:function:: build_tran_square_midpoints() -> geometor.divine.catalog.schema.ConstructionResult

   Tran Quang Hung's square midpoint circle construction (Buratino 1).


.. py:function:: build_nguyen_2x2_square() -> geometor.divine.catalog.schema.ConstructionResult

   Nguyen Thanh Dung's 2x2 square grid compass arc construction.


.. py:function:: build_tran_mcgucken_3x3_circle() -> geometor.divine.catalog.schema.ConstructionResult

   Tran Quang Hung & Elliot McGucken's 3x3 grid diagonal circle division.


.. py:function:: build_tran_3x3_incenter() -> geometor.divine.catalog.schema.ConstructionResult

   Tran Quang Hung's 3x3 grid isosceles triangle incenter theorem.


.. py:function:: build_suppa_square_inradii() -> geometor.divine.catalog.schema.ConstructionResult

   Ercole Suppa's square midpoint inradii ratio (2015).


.. py:function:: build_bui_cross_and_square() -> geometor.divine.catalog.schema.ConstructionResult

   Bùi Quang Tuân & Alexandre Borovik's Greek cross and square in a circle.


.. py:function:: build_arioni_rotating_square() -> geometor.divine.catalog.schema.ConstructionResult

   John Arioni's 30-degree rotated unit square and diagonal circle.


.. py:data:: SQUARES_RECTANGLES_SPECS
   :type:  tuple[geometor.divine.catalog.schema.ConstructionSpec, ...]

