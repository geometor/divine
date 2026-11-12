GC-06.05 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-06.05``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-06.05")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_kocik_golden_window() -> ConstructionResult:
       """Jerzy Kocik's six-circle Golden Window Apollonian configuration (2010)."""
       m = new_catalog_model("kocik-golden-window")
       s5 = sp.sqrt(5)
       phi = sp.Rational(1, 2) + s5 / 2
       phi2 = phi + 1
       phi3 = 2 * phi + 1

       O = m.set_point(0, 0, classes=["given"], ID="O")
       P1 = m.set_point(-1, 0, ID="P1")
       P2 = m.set_point(1, 0, classes=["given"], ID="P2")
       C1 = m.set_point(-sp.Rational(1, 2), 0, guide=True, ID="C1")
       C2 = m.set_point(sp.Rational(1, 2), 0, guide=True, ID="C2")

       # Central unit-diameter circles
       m.construct_circle(C1, O, classes=["compass"], ID="cC1")
       m.construct_circle(C2, O, classes=["compass"], ID="cC2")

       # Flanking golden circles of radius phi centered at +-phi^2
       C3 = m.set_point(-phi2, 0, ID="C3")
       C4 = m.set_point(phi2, 0, classes=["golden"], ID="C4")
       A3 = m.set_point(-phi3, 0, ID="A3")
       A4 = m.set_point(phi3, 0, classes=["golden"], ID="A4")
       m.construct_circle(C3, P1, classes=["golden"], ID="cC3")
       m.construct_circle(C4, P2, classes=["golden"], ID="cC4")

       # Outer window circle of radius phi^3 = 2*phi + 1
       m.construct_circle(O, A4, classes=["primary"], ID="cO")
       m.construct_line(A3, A4, classes=["golden"], ID="A3A4")

       # Upper & lower circles tangent to all five circles: center (0, +-2*phi^2/sqrt(5)), top (0, +-phi^3)
       hu = (2 * phi2) / s5
       U1 = m.set_point(0, hu, ID="U1")
       U2 = m.set_point(0, -hu, ID="U2")
       T_top = m.set_point(0, phi3, ID="T1")
       T_bot = m.set_point(0, -phi3, ID="T2")
       m.construct_circle(U1, T_top, classes=["auxiliary"], ID="cU1")
       m.construct_circle(U2, T_bot, classes=["auxiliary"], ID="cU2")

       return make_result(m, ("O", "C4"), ("C4", "A4"), ("O", "C4", "A4"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``kocik-golden-window`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\phi)`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``O``
     - :math:`0`
     - :math:`0`
   * - ``P1``
     - :math:`-1`
     - :math:`0`
   * - ``P2``
     - :math:`1`
     - :math:`0`
   * - ``C3``
     - :math:`- \frac{3}{2} - \frac{\sqrt{5}}{2}`
     - :math:`0`
   * - ``C4``
     - :math:`\frac{\sqrt{5}}{2} + \frac{3}{2}`
     - :math:`0`
   * - ``A3``
     - :math:`- \sqrt{5} - 2`
     - :math:`0`
   * - ``A4``
     - :math:`2 + \sqrt{5}`
     - :math:`0`
   * - ``U1``
     - :math:`0`
     - :math:`1 + \frac{3 \sqrt{5}}{5}`
   * - ``U2``
     - :math:`0`
     - :math:`- \frac{3 \sqrt{5}}{5} - 1`
   * - ``T1``
     - :math:`0`
     - :math:`2 + \sqrt{5}`
   * - ``T2``
     - :math:`0`
     - :math:`- \sqrt{5} - 2`

**Certified Golden Ratio**: ``OC4`` / ``C4A4`` = ``GoldenRatio``.
