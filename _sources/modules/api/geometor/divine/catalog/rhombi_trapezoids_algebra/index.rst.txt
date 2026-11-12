geometor.divine.catalog.rhombi_trapezoids_algebra
=================================================

.. py:module:: geometor.divine.catalog.rhombi_trapezoids_algebra

.. autoapi-nested-parse::

   Family 07: Rhombi, Trapezoids, Mixtilinear Circles & Dissection Paradoxes.

   Catalogs Tran Quang Hung's 1:2 rhombus incircle, 60-degree isosceles trapezoid,
   and equilateral mixtilinear circle theorems, John Molokach's golden rhombus
   from shifted 1x3 rectangles, Jingcheng Tong's area-bisecting trapezoid chord,
   and the exact phi-limit resolution of the Hooper-Curry Fibonacci dissection.



Attributes
----------

.. autoapisummary::

   geometor.divine.catalog.rhombi_trapezoids_algebra.RHOMBI_TRAPEZOIDS_ALGEBRA_SPECS


Functions
---------

.. autoapisummary::

   geometor.divine.catalog.rhombi_trapezoids_algebra.build_tran_rhombus_incircle
   geometor.divine.catalog.rhombi_trapezoids_algebra.build_molokach_golden_rhombus
   geometor.divine.catalog.rhombi_trapezoids_algebra.build_tong_trapezoid_rms
   geometor.divine.catalog.rhombi_trapezoids_algebra.build_tran_isosceles_trapezoid_60
   geometor.divine.catalog.rhombi_trapezoids_algebra.build_tran_mixtilinear_equilateral
   geometor.divine.catalog.rhombi_trapezoids_algebra.build_curry_hooper_dissection


Module Contents
---------------

.. py:function:: build_tran_rhombus_incircle() -> geometor.divine.catalog.schema.ConstructionResult

   Tran Quang Hung's rhombus with diagonal ratio 2:1 and its incircle (Buratino 8).


.. py:function:: build_molokach_golden_rhombus() -> geometor.divine.catalog.schema.ConstructionResult

   John Molokach's golden rhombus from two shifted 1x3 rectangles and a unit circle.


.. py:function:: build_tong_trapezoid_rms() -> geometor.divine.catalog.schema.ConstructionResult

   Jingcheng Tong's area-bisecting chord in a trapezoid of base ratio 1:3.


.. py:function:: build_tran_isosceles_trapezoid_60() -> geometor.divine.catalog.schema.ConstructionResult

   Tran Quang Hung's 60-degree half-hexagon trapezoid & reflected compass arc.


.. py:function:: build_tran_mixtilinear_equilateral() -> geometor.divine.catalog.schema.ConstructionResult

   Tran Quang Hung's Golden Ratio in a mixtilinear circle of an equilateral triangle.


.. py:function:: build_curry_hooper_dissection() -> geometor.divine.catalog.schema.ConstructionResult

   Exact phi-limit resolution of the Hooper (1794) / Curry Fibonacci dissection.


.. py:data:: RHOMBI_TRAPEZOIDS_ALGEBRA_SPECS
   :type:  tuple[geometor.divine.catalog.schema.ConstructionSpec, ...]

