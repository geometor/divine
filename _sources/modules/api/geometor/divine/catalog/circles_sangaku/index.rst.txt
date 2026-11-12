geometor.divine.catalog.circles_sangaku
=======================================

.. py:module:: geometor.divine.catalog.circles_sangaku

.. autoapi-nested-parse::

   Family 06: Circles, Tangent Packings, Yin-Yang & Sangaku Configurations.

   Catalogs Bùi Quang Tuân's infinite chord families and four-circle chain,
   Elliot McGucken & Thanos Kalogerakis's equal tangent circles, Tran Quang Hung's
   three mutually tangent circles, Jerzy Kocik's Golden Window, John Arioni's
   Yin-Yang secant, and three congruent circles in a semicircle.



Attributes
----------

.. autoapisummary::

   geometor.divine.catalog.circles_sangaku.CIRCLES_SANGAKU_SPECS


Functions
---------

.. autoapisummary::

   geometor.divine.catalog.circles_sangaku.build_bui_circle_droves
   geometor.divine.catalog.circles_sangaku.build_mcgucken_kalogerakis_equal_circles
   geometor.divine.catalog.circles_sangaku.build_bui_four_golden_circles
   geometor.divine.catalog.circles_sangaku.build_tran_mcgucken_three_tangent_circles
   geometor.divine.catalog.circles_sangaku.build_kocik_golden_window
   geometor.divine.catalog.circles_sangaku.build_arioni_yin_yang
   geometor.divine.catalog.circles_sangaku.build_three_circles_in_semicircle


Module Contents
---------------

.. py:function:: build_bui_circle_droves() -> geometor.divine.catalog.schema.ConstructionResult

   Bùi Quang Tuân's infinite rational secant family dividing a radius in phi.


.. py:function:: build_mcgucken_kalogerakis_equal_circles() -> geometor.divine.catalog.schema.ConstructionResult

   Elliot McGucken & Thanos Kalogerakis's two externally tangent equal circles.


.. py:function:: build_bui_four_golden_circles() -> geometor.divine.catalog.schema.ConstructionResult

   Bùi Quang Tuân's four congruent circles generating a vertical golden chain.


.. py:function:: build_tran_mcgucken_three_tangent_circles() -> geometor.divine.catalog.schema.ConstructionResult

   Tran Quang Hung & Elliot McGucken's three mutually tangent equal circles.


.. py:function:: build_kocik_golden_window() -> geometor.divine.catalog.schema.ConstructionResult

   Jerzy Kocik's six-circle Golden Window Apollonian configuration (2010).


.. py:function:: build_arioni_yin_yang() -> geometor.divine.catalog.schema.ConstructionResult

   John Arioni's Golden Ratio secant in the Yin-Yang twin-circle figure.


.. py:function:: build_three_circles_in_semicircle() -> geometor.divine.catalog.schema.ConstructionResult

   Three tangent unit circles inscribed in a semicircle of radius 2*phi.


.. py:data:: CIRCLES_SANGAKU_SPECS
   :type:  tuple[geometor.divine.catalog.schema.ConstructionSpec, ...]

