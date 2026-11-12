GC-06.07 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-06.07``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-06.07")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_three_circles_in_semicircle() -> ConstructionResult:
       """Three tangent unit circles inscribed in a semicircle of radius 2*phi."""
       m = new_catalog_model("three-circles-in-semicircle")
       phi = sp.Rational(1, 2) + sp.sqrt(5) / 2

       O = m.set_point(0, 0, classes=["given"], ID="O")
       T1 = m.set_point(-2, 0, ID="T1")
       T2 = m.set_point(2, 0, classes=["given"], ID="T2")
       C1 = m.set_point(-2, 1, ID="C1")
       C0 = m.set_point(0, 1, ID="C0")
       C2 = m.set_point(2, 1, ID="C2")

       A = m.set_point(-2 * phi, 0, ID="A")
       B = m.set_point(2 * phi, 0, classes=["golden"], ID="B")

       c_o = m.construct_circle(O, B, classes=["primary"], ID="cO")
       m.construct_line(A, B, classes=["golden"], ID="AB")
       m.construct_circle(C1, T1, classes=["compass"], ID="cC1")
       m.construct_circle(C0, O, classes=["compass"], ID="cC0")
       c_c2 = m.construct_circle(C2, T2, classes=["golden"], ID="cC2")

       ln_oc2 = m.construct_line(O, C2, classes=["auxiliary"], ID="OC2")
       S = m.intersect(c_c2, ln_oc2, between=(O, C2), classes=["golden"], ID="S")
       K = m.intersect(c_o, ln_oc2, side_of=(B, A, 1), classes=["golden"], ID="K")
       _ = (S, K)

       return make_result(m, ("O", "T2"), ("T2", "B"), ("O", "T2", "B"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``three-circles-in-semicircle`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\phi)`:

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
     - :math:`-2`
     - :math:`0`
   * - ``T2``
     - :math:`2`
     - :math:`0`
   * - ``C1``
     - :math:`-2`
     - :math:`1`
   * - ``C0``
     - :math:`0`
     - :math:`1`
   * - ``C2``
     - :math:`2`
     - :math:`1`
   * - ``A``
     - :math:`- \sqrt{5} - 1`
     - :math:`0`
   * - ``B``
     - :math:`1 + \sqrt{5}`
     - :math:`0`
   * - ``S``
     - :math:`2 - \frac{2 \sqrt{5}}{5}`
     - :math:`1 - \frac{\sqrt{5}}{5}`
   * - ``K``
     - :math:`-2 - \frac{2 \sqrt{5}}{5}`
     - :math:`-1 - \frac{\sqrt{5}}{5}`

**Certified Golden Ratio**: ``OT2`` / ``T2B`` = ``GoldenRatio``.
