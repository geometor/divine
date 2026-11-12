GC-02.06 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-02.06``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-02.06")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_tran_hexagon_square() -> ConstructionResult:
       """Tran Quang Hung's regular hexagon & external square compass sweep."""
       m = new_catalog_model("tran-hexagon-square")
       s3 = sp.sqrt(3)
       A = m.set_point(0, 0, classes=["given"], ID="A")
       B = m.set_point(2, 0, classes=["given"], ID="B")
       C = m.set_point(3, s3, ID="C")
       D = m.set_point(2, 2 * s3, ID="D")
       E = m.set_point(0, 2 * s3, ID="E")
       F = m.set_point(-1, s3, ID="F")

       G = m.set_point(0, -2, ID="G")
       H = m.set_point(2, -2, ID="H")

       m.construct_polygon([A, B, C, D, E, F], ID="ABCDEF")
       m.construct_polygon([A, B, H, G], ID="ABHG")
       m.construct_segment(A, H, classes=["auxiliary"], ID="AH")

       ln_ef = m.construct_line(E, F, ID="EF")
       ln_bc = m.construct_line(B, C, ID="BC")
       c_ah = m.construct_circle(A, H, classes=["golden"], ID="cAH")

       m.intersect(c_ah, ln_ef, between=(E, F), classes=["golden"], ID="I")
       L = m.intersect(c_ah, ln_bc, between=(B, C), classes=["golden"], ID="L")
       _ = L

       return make_result(m, ("F", "I"), ("I", "E"), ("F", "I", "E"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``tran-hexagon-square`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\sqrt{3}, \phi)`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``A``
     - :math:`0`
     - :math:`0`
   * - ``B``
     - :math:`2`
     - :math:`0`
   * - ``C``
     - :math:`3`
     - :math:`\sqrt{3}`
   * - ``D``
     - :math:`2`
     - :math:`2 \sqrt{3}`
   * - ``E``
     - :math:`0`
     - :math:`2 \sqrt{3}`
   * - ``F``
     - :math:`-1`
     - :math:`\sqrt{3}`
   * - ``G``
     - :math:`0`
     - :math:`-2`
   * - ``H``
     - :math:`2`
     - :math:`-2`
   * - ``I``
     - :math:`- \frac{3}{2} + \frac{\sqrt{5}}{2}`
     - :math:`\frac{\sqrt{3} + \sqrt{15}}{2}`
   * - ``L``
     - :math:`\frac{\sqrt{5}}{2} + \frac{3}{2}`
     - :math:`\frac{- \sqrt{3} + \sqrt{15}}{2}`

**Certified Golden Ratio**: ``FI`` / ``IE`` = ``GoldenRatio``.
