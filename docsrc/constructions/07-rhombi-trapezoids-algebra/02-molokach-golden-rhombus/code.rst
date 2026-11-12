GC-07.02 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-07.02``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-07.02")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_molokach_golden_rhombus() -> ConstructionResult:
       """John Molokach's golden rhombus from two shifted 1x3 rectangles and a unit circle."""
       m = new_catalog_model("molokach-golden-rhombus")
       phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
       inv_phi = phi - 1

       O = m.set_point(0, 0, classes=["given"], ID="O")
       T1 = m.set_point(0, 1, classes=["golden"], ID="T1")
       T2 = m.set_point(0, -1, ID="T2")
       _ = T2

       # Two shifted 3x1 rectangles [-2, 1] x [0, 1] and [-1, 2] x [-1, 0]
       R1 = m.set_point(-2, 1, ID="R1")
       K = m.set_point(1, 1, classes=["given"], ID="K")
       R2 = m.set_point(1, 0, guide=True, ID="R2")
       R3 = m.set_point(-2, 0, guide=True, ID="R3")
       m.construct_polygon([R1, K, R2, R3], classes=["auxiliary"], ID="RECT1")

       R4 = m.set_point(-1, 0, guide=True, ID="R4")
       R5 = m.set_point(2, 0, guide=True, ID="R5")
       R6 = m.set_point(2, -1, ID="R6")
       R7 = m.set_point(-1, -1, ID="R7")
       m.construct_polygon([R4, R5, R6, R7], classes=["auxiliary"], ID="RECT2")

       # Long diagonal R1 R6 and unit incircle cO
       m.construct_segment(R1, R6, classes=["auxiliary"], ID="R1R6")
       m.construct_circle(O, T1, classes=["primary"], ID="cO")

       # Golden rhombus ABCD circumscribed about cO via tangents at y=+-1 and 2x - y = +-sqrt(5)
       A = m.set_point(phi, 1, classes=["golden"], ID="A")
       B = m.set_point(-inv_phi, 1, classes=["golden"], ID="B")
       C = m.set_point(-phi, -1, ID="C")
       D = m.set_point(inv_phi, -1, ID="D")
       m.construct_polygon([A, B, C, D], classes=["golden"], ID="ABCD")
       m.construct_line(B, A, classes=["golden"], ID="BA")
       m.construct_segment(A, C, classes=["auxiliary"], ID="AC")
       m.construct_segment(B, D, classes=["auxiliary"], ID="BD")

       return make_result(m, ("T1", "K"), ("K", "A"), ("T1", "K", "A"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``molokach-golden-rhombus`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\phi)`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``O``
     - :math:`0`
     - :math:`0`
   * - ``T1``
     - :math:`0`
     - :math:`1`
   * - ``T2``
     - :math:`0`
     - :math:`-1`
   * - ``R1``
     - :math:`-2`
     - :math:`1`
   * - ``K``
     - :math:`1`
     - :math:`1`
   * - ``R6``
     - :math:`2`
     - :math:`-1`
   * - ``R7``
     - :math:`-1`
     - :math:`-1`
   * - ``A``
     - :math:`\frac{1}{2} + \frac{\sqrt{5}}{2}`
     - :math:`1`
   * - ``B``
     - :math:`\frac{1}{2} - \frac{\sqrt{5}}{2}`
     - :math:`1`
   * - ``C``
     - :math:`- \frac{\sqrt{5}}{2} - \frac{1}{2}`
     - :math:`-1`
   * - ``D``
     - :math:`- \frac{1}{2} + \frac{\sqrt{5}}{2}`
     - :math:`-1`

**Certified Golden Ratio**: ``T1K`` / ``KA`` = ``GoldenRatio``.
