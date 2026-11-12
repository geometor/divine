geometor.divine.catalog.equilateral_hexagon
===========================================

.. py:module:: geometor.divine.catalog.equilateral_hexagon

.. autoapi-nested-parse::

   Family 02: Equilateral Triangles & Regular Hexagons — The Odom Lineage.

   Catalogs George Odom's celebrated 1983 equilateral midline construction and six
   modern descendants by Michel Bataille, Bùi Quang Tuân, Tran Quang Hung, and
   Nguyen Thanh Dung.



Attributes
----------

.. autoapisummary::

   geometor.divine.catalog.equilateral_hexagon.EQUILATERAL_HEXAGON_SPECS


Functions
---------

.. autoapisummary::

   geometor.divine.catalog.equilateral_hexagon.build_odom_equilateral
   geometor.divine.catalog.equilateral_hexagon.build_bataille_triangle_square
   geometor.divine.catalog.equilateral_hexagon.build_bui_two_equilaterals
   geometor.divine.catalog.equilateral_hexagon.build_tran_reflected_equilaterals
   geometor.divine.catalog.equilateral_hexagon.build_tran_incircle_equilateral
   geometor.divine.catalog.equilateral_hexagon.build_tran_hexagon_square
   geometor.divine.catalog.equilateral_hexagon.build_nguyen_butterfly_equilateral


Module Contents
---------------

.. py:function:: build_odom_equilateral() -> geometor.divine.catalog.schema.ConstructionResult

   George Odom's 1983 equilateral triangle midline & circumcircle secant.


.. py:function:: build_bataille_triangle_square() -> geometor.divine.catalog.schema.ConstructionResult

   Michel Bataille's 2011 equilateral triangle and external square sweep.


.. py:function:: build_bui_two_equilaterals() -> geometor.divine.catalog.schema.ConstructionResult

   Bùi Quang Tuân's coupled equilateral triangles on side and altitude.


.. py:function:: build_tran_reflected_equilaterals() -> geometor.divine.catalog.schema.ConstructionResult

   Tran Quang Hung's reflected equilateral triangles & midline secant.


.. py:function:: build_tran_incircle_equilateral() -> geometor.divine.catalog.schema.ConstructionResult

   Tran Quang Hung's nested equilateral triangles inscribed in the incircle.


.. py:function:: build_tran_hexagon_square() -> geometor.divine.catalog.schema.ConstructionResult

   Tran Quang Hung's regular hexagon & external square compass sweep.


.. py:function:: build_nguyen_butterfly_equilateral() -> geometor.divine.catalog.schema.ConstructionResult

   Nguyen Thanh Dung's butterfly chords astride an equilateral triangle.


.. py:data:: EQUILATERAL_HEXAGON_SPECS
   :type:  tuple[geometor.divine.catalog.schema.ConstructionSpec, ...]

