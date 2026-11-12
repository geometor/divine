GC-02.02 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-02.02``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-02.02")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_bataille_triangle_square() -> ConstructionResult:
       """Michel Bataille's 2011 equilateral triangle and external square sweep."""
       m = new_catalog_model("bataille-triangle-square")
       s3 = sp.sqrt(3)
       B = m.set_point(0, 0, classes=["given"], ID="B")
       C = m.set_point(2, 0, classes=["given"], ID="C")
       A = m.set_point(1, s3, ID="A")
       D = m.set_point(2, -2, ID="D")
       E = m.set_point(0, -2, ID="E")

       m.construct_polygon([A, B, C], ID="ABC")
       m.construct_polygon([B, C, D, E], ID="BCDE")
       ln_ab = m.construct_line(A, B, ID="AB")
       m.construct_segment(C, E, classes=["auxiliary"], ID="CE")

       c_ce = m.construct_circle(C, E, classes=["golden"], ID="cCE")
       m.intersect(c_ce, ln_ab, beyond=(A, B), classes=["golden"], ID="F")

       return make_result(m, ("A", "B"), ("B", "F"), ("A", "B", "F"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``bataille-triangle-square`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\sqrt{3}, \phi)`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``B``
     - :math:`0`
     - :math:`0`
   * - ``C``
     - :math:`2`
     - :math:`0`
   * - ``A``
     - :math:`1`
     - :math:`\sqrt{3}`
   * - ``D``
     - :math:`2`
     - :math:`-2`
   * - ``E``
     - :math:`0`
     - :math:`-2`
   * - ``F``
     - :math:`\frac{1}{2} - \frac{\sqrt{5}}{2}`
     - :math:`\frac{- \sqrt{15} + \sqrt{3}}{2}`

**Certified Golden Ratio**: ``AB`` / ``BF`` = ``GoldenRatio``.
