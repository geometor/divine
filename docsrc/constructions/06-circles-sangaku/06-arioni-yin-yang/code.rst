GC-06.06 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-06.06``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-06.06")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_arioni_yin_yang() -> ConstructionResult:
       """John Arioni's Golden Ratio secant in the Yin-Yang twin-circle figure."""
       m = new_catalog_model("arioni-yin-yang")
       O = m.set_point(0, 0, classes=["given"], ID="O")
       B = m.set_point(0, 1, classes=["given"], ID="B")
       PL = m.set_point(-1, 0, ID="PL")
       PR = m.set_point(1, 0, ID="PR")
       A = m.set_point(-sp.Rational(1, 2), 0, ID="A")
       C = m.set_point(sp.Rational(1, 2), 0, ID="C")

       m.construct_circle(O, B, classes=["primary"], ID="cO")
       c_a = m.construct_circle(A, O, classes=["golden"], ID="cA")
       m.construct_circle(C, O, classes=["compass"], ID="cC")
       m.construct_segment(PL, PR, classes=["auxiliary"], ID="PLPR")
       m.construct_segment(O, B, classes=["auxiliary"], ID="OB")

       ln_ba = m.construct_line(B, A, classes=["golden"], ID="BA")
       m.intersect(c_a, ln_ba, between=(B, A), classes=["golden"], ID="H")
       m.intersect(c_a, ln_ba, beyond=(B, A), classes=["golden"], ID="I")

       return make_result(m, ("H", "I"), ("B", "H"), ("B", "H", "I"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``arioni-yin-yang`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\phi)`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``O``
     - :math:`0`
     - :math:`0`
   * - ``B``
     - :math:`0`
     - :math:`1`
   * - ``PL``
     - :math:`-1`
     - :math:`0`
   * - ``PR``
     - :math:`1`
     - :math:`0`
   * - ``A``
     - :math:`- \frac{1}{2}`
     - :math:`0`
   * - ``C``
     - :math:`\frac{1}{2}`
     - :math:`0`
   * - ``H``
     - :math:`- \frac{1}{2} + \frac{\sqrt{5}}{10}`
     - :math:`\frac{\sqrt{5}}{5}`
   * - ``I``
     - :math:`- \frac{1}{2} - \frac{\sqrt{5}}{10}`
     - :math:`- \frac{\sqrt{5}}{5}`

**Certified Golden Ratio**: ``HI`` / ``BH`` = ``GoldenRatio``.
