GC-05.01 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-05.01``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-05.01")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_ptolemy_pentagon_pentagram() -> ConstructionResult:
       """Claudius Ptolemy's Almagest I.10 regular pentagon & pentagram construction."""
       m = new_catalog_model("ptolemy-pentagon-pentagram")
       _phi, s36, c36, s72, c72 = _pentagon_radicals()

       O = m.set_point(0, 0, classes=["given"], ID="O")
       B = m.set_point(1, 0, classes=["given"], ID="B")
       A = m.set_point(-1, 0, ID="A")
       C = m.set_point(0, 1, ID="C")
       M = m.set_point(sp.Rational(1, 2), 0, ID="M")

       c_o = m.construct_circle(O, B, classes=["primary"], ID="cO")
       _ = c_o
       ln_ab = m.construct_line(A, B, classes=["auxiliary"], ID="AB")
       m.construct_segment(O, C, classes=["auxiliary"], ID="OC")

       c_mc = m.construct_circle(M, C, classes=["compass"], ID="cMC")
       E = m.intersect(c_mc, ln_ab, between=(A, O), classes=["golden"], ID="E")
       m.construct_segment(C, E, classes=["auxiliary"], ID="CE")

       # Inscribed regular pentagon C P1 P2 P3 P4 of side |CE| = 2 * s36
       P1 = m.set_point(-s72, c72, ID="P1")
       P2 = m.set_point(-s36, -c36, ID="P2")
       P3 = m.set_point(s36, -c36, ID="P3")
       P4 = m.set_point(s72, c72, ID="P4")
       m.construct_polygon([C, P1, P2, P3, P4], ID="CP1P2P3P4")

       # Inscribed regular pentagram diagonals
       ln_p1p4 = m.construct_line(P1, P4, classes=["golden"], ID="P1P4")
       ln_cp2 = m.construct_line(C, P2, classes=["auxiliary"], ID="CP2")
       ln_cp3 = m.construct_line(C, P3, classes=["auxiliary"], ID="CP3")
       m.construct_segment(P1, P3, classes=["auxiliary"], ID="P1P3")
       m.construct_segment(P2, P4, classes=["auxiliary"], ID="P2P4")

       K1 = m.intersect(ln_p1p4, ln_cp2, classes=["golden"], ID="K1")
       m.intersect(ln_p1p4, ln_cp3, classes=["golden"], ID="K2")
       _ = K1

       return make_result(m, ("P1", "K2"), ("K2", "P4"), ("P1", "K2", "P4"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``ptolemy-pentagon-pentagram`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\phi, \sqrt{10 - 2\sqrt{5}})`:

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
     - :math:`1`
     - :math:`0`
   * - ``A``
     - :math:`-1`
     - :math:`0`
   * - ``C``
     - :math:`0`
     - :math:`1`
   * - ``M``
     - :math:`\frac{1}{2}`
     - :math:`0`
   * - ``E``
     - :math:`\frac{1}{2} - \frac{\sqrt{5}}{2}`
     - :math:`0`
   * - ``P1``
     - :math:`\frac{- \sqrt{10} \sqrt{5 - \sqrt{5}} - \sqrt{2} \sqrt{5 - \sqrt{5}}}{8}`
     - :math:`- \frac{1}{4} + \frac{\sqrt{5}}{4}`
   * - ``P2``
     - :math:`- \frac{\sqrt{2} \sqrt{5 - \sqrt{5}}}{4}`
     - :math:`- \frac{\sqrt{5}}{4} - \frac{1}{4}`
   * - ``P3``
     - :math:`\frac{\sqrt{2} \sqrt{5 - \sqrt{5}}}{4}`
     - :math:`- \frac{\sqrt{5}}{4} - \frac{1}{4}`
   * - ``P4``
     - :math:`\frac{\sqrt{2} \sqrt{5 - \sqrt{5}} + \sqrt{10} \sqrt{5 - \sqrt{5}}}{8}`
     - :math:`- \frac{1}{4} + \frac{\sqrt{5}}{4}`
   * - ``K1``
     - :math:`\frac{- 3 \sqrt{2} \sqrt{5 - \sqrt{5}} + \sqrt{10} \sqrt{5 - \sqrt{5}}}{8}`
     - :math:`- \frac{1}{4} + \frac{\sqrt{5}}{4}`
   * - ``K2``
     - :math:`\frac{- \sqrt{10} \sqrt{5 - \sqrt{5}} + 3 \sqrt{2} \sqrt{5 - \sqrt{5}}}{8}`
     - :math:`- \frac{1}{4} + \frac{\sqrt{5}}{4}`

**Certified Golden Ratio**: ``P1K2`` / ``K2P4`` = ``GoldenRatio``.
