GC-03.06 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-03.06``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-03.06")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_suppa_square_inradii() -> ConstructionResult:
       """Ercole Suppa's square midpoint inradii ratio (2015)."""
       m = new_catalog_model("suppa-square-inradii")
       D = m.set_point(0, 0, classes=["given"], ID="D")
       C = m.set_point(2, 0, classes=["given"], ID="C")
       B = m.set_point(2, 2, ID="B")
       A = m.set_point(0, 2, ID="A")
       M = m.set_point(0, 1, ID="M")

       m.construct_polygon([A, B, C, D], ID="ABCD")
       ln_cm = m.construct_line(C, M, ID="CM")
       m.construct_segment(B, M, ID="BM")

       # Incenter E of isosceles BCM (inradius R = 1/phi, tangent to BC at H=(2,1))
       ex = (5 - sp.sqrt(5)) / 2
       E = m.set_point(ex, 1, classes=["golden"], ID="E")
       H = m.set_point(2, 1, ID="H")
       m.construct_circle(E, H, classes=["golden"], ID="cEH")

       # Incenter F of right CDM (inradius r = 1/phi^2, tangent to CD at P=((3-sqrt(5))/2, 0))
       fx = (3 - sp.sqrt(5)) / 2
       F = m.set_point(fx, fx, classes=["golden"], ID="F")
       P = m.set_point(fx, 0, ID="P")
       m.construct_circle(F, P, classes=["compass"], ID="cFP")

       ln_ef = m.construct_line(E, F, classes=["golden"], ID="EF")
       m.intersect(ln_ef, ln_cm, classes=["golden"], ID="K")

       return make_result(m, ("E", "K"), ("K", "F"), ("E", "K", "F"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``suppa-square-inradii`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\phi)`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``D``
     - :math:`0`
     - :math:`0`
   * - ``C``
     - :math:`2`
     - :math:`0`
   * - ``B``
     - :math:`2`
     - :math:`2`
   * - ``A``
     - :math:`0`
     - :math:`2`
   * - ``M``
     - :math:`0`
     - :math:`1`
   * - ``E``
     - :math:`\frac{5}{2} - \frac{\sqrt{5}}{2}`
     - :math:`1`
   * - ``H``
     - :math:`2`
     - :math:`1`
   * - ``F``
     - :math:`\frac{3}{2} - \frac{\sqrt{5}}{2}`
     - :math:`\frac{3}{2} - \frac{\sqrt{5}}{2}`
   * - ``P``
     - :math:`\frac{3}{2} - \frac{\sqrt{5}}{2}`
     - :math:`0`
   * - ``K``
     - :math:`3 - \sqrt{5}`
     - :math:`- \frac{1}{2} + \frac{\sqrt{5}}{2}`

**Certified Golden Ratio**: ``EK`` / ``KF`` = ``GoldenRatio``.
