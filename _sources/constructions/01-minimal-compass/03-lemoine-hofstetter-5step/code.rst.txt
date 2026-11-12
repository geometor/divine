GC-01.03 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-01.03``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-01.03")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_lemoine_hofstetter_5step() -> ConstructionResult:
       """Lemoine (1902), Reusch (1904) & Hofstetter (2003) 5-step segment division."""
       m = new_catalog_model("lemoine-hofstetter-5step")
       A = m.set_point(0, 0, classes=["given"], ID="A")
       B = m.set_point(1, 0, classes=["given"], ID="B")

       ln_ab = m.construct_line(A, B, ID="AB")
       c_ab = m.construct_circle(A, B, classes=["compass"], ID="cAB")
       c_ba = m.construct_circle(B, A, classes=["compass"], ID="cBA")
       C = m.intersect(c_ab, c_ba, side_of=(A, B, 1), ID="C")
       D = m.intersect(c_ab, c_ba, side_of=(A, B, -1), ID="D")

       ln_cd = m.construct_line(C, D, classes=["auxiliary"], ID="CD")
       c_ca = m.construct_circle(C, A, classes=["compass"], ID="cCA")
       E = m.intersect(c_ca, c_ab, other_than=B, ID="E")
       F = m.intersect(c_ca, ln_cd, between=(C, D), ID="F")

       c_ef = m.construct_circle(E, F, classes=["golden"], ID="cEF")
       m.intersect(c_ef, ln_ab, between=(A, B), classes=["golden"], ID="G")
       G1 = m.intersect(c_ef, ln_ab, beyond=(B, A), ID="G1")
       _ = G1

       return make_result(m, ("A", "G"), ("G", "B"), ("A", "G", "B"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``lemoine-hofstetter-5step`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\sqrt{3}, \phi)`:

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
     - :math:`1`
     - :math:`0`
   * - ``C``
     - :math:`\frac{1}{2}`
     - :math:`\frac{\sqrt{3}}{2}`
   * - ``D``
     - :math:`\frac{1}{2}`
     - :math:`- \frac{\sqrt{3}}{2}`
   * - ``E``
     - :math:`- \frac{1}{2}`
     - :math:`\frac{\sqrt{3}}{2}`
   * - ``F``
     - :math:`\frac{1}{2}`
     - :math:`-1 + \frac{\sqrt{3}}{2}`
   * - ``G``
     - :math:`- \frac{1}{2} + \frac{\sqrt{5}}{2}`
     - :math:`0`
   * - ``G1``
     - :math:`- \frac{\sqrt{5}}{2} - \frac{1}{2}`
     - :math:`0`

**Certified Golden Ratio**: ``AG`` / ``GB`` = ``GoldenRatio``.
