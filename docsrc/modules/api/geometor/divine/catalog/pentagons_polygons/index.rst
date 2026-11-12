geometor.divine.catalog.pentagons_polygons
==========================================

.. py:module:: geometor.divine.catalog.pentagons_polygons

.. autoapi-nested-parse::

   Family 05: Regular Pentagons, Pentagrams, Irregular Pentagons & Polygonal Stars.

   Catalogs Claudius Ptolemy's *Almagest* pentagon and pentagram, Dao Thanh Oai's
   regular pentagon perpendicular, V. V. Prasolov & Bùi Quang Tuân's equi-area
   irregular pentagon, and Tran Quang Hung's pentagon-hexagon, six-pentagon star,
   and fivefold *Wu Xing* equilateral star theorems.



Attributes
----------

.. autoapisummary::

   geometor.divine.catalog.pentagons_polygons.PENTAGONS_POLYGONS_SPECS


Functions
---------

.. autoapisummary::

   geometor.divine.catalog.pentagons_polygons.build_ptolemy_pentagon_pentagram
   geometor.divine.catalog.pentagons_polygons.build_dao_tran_pentagon_bisector_incircle
   geometor.divine.catalog.pentagons_polygons.build_prasolov_bui_irregular_pentagon
   geometor.divine.catalog.pentagons_polygons.build_tran_pentagon_hexagon
   geometor.divine.catalog.pentagons_polygons.build_tran_star_six_pentagons
   geometor.divine.catalog.pentagons_polygons.build_tran_wu_xing_equilaterals


Module Contents
---------------

.. py:function:: build_ptolemy_pentagon_pentagram() -> geometor.divine.catalog.schema.ConstructionResult

   Claudius Ptolemy's Almagest I.10 regular pentagon & pentagram construction.


.. py:function:: build_dao_tran_pentagon_bisector_incircle() -> geometor.divine.catalog.schema.ConstructionResult

   Dao Thanh Oai's perpendicular at a vertex of a regular pentagon.


.. py:function:: build_prasolov_bui_irregular_pentagon() -> geometor.divine.catalog.schema.ConstructionResult

   V. V. Prasolov & Bùi Quang Tuân's equi-area irregular pentagon.


.. py:function:: build_tran_pentagon_hexagon() -> geometor.divine.catalog.schema.ConstructionResult

   Tran Quang Hung's regular pentagon inscribed on the base of a regular hexagon.


.. py:function:: build_tran_star_six_pentagons() -> geometor.divine.catalog.schema.ConstructionResult

   Tran Quang Hung's star formed by reflecting a regular pentagon across its five sides.


.. py:function:: build_tran_wu_xing_equilaterals() -> geometor.divine.catalog.schema.ConstructionResult

   Tran Quang Hung's fivefold Wu Xing congruent equilateral triangles & pentagram.


.. py:data:: PENTAGONS_POLYGONS_SPECS
   :type:  tuple[geometor.divine.catalog.schema.ConstructionSpec, ...]

