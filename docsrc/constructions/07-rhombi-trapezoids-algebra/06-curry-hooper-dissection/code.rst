GC-07.06 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-07.06``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-07.06")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_curry_hooper_dissection() -> ConstructionResult:
       """Exact phi-limit resolution of the Hooper (1794) / Curry Fibonacci dissection."""
       m = new_catalog_model("curry-hooper-dissection")
       phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
       inv_phi = phi - 1
       phi2 = phi + 1
       phi3 = 2 * phi + 1

       # Golden rectangle ABCD of width phi^3 and height phi (area = phi^4 = (phi^2)^2, zero gap!)
       A = m.set_point(0, 0, classes=["given"], ID="A")
       B = m.set_point(phi3, 0, classes=["given"], ID="B")
       C = m.set_point(phi3, phi, ID="C")
       D = m.set_point(0, phi, ID="D")
       m.construct_polygon([A, B, C, D], ID="ABCD")

       # Four-piece exact dissection cuts: E=(phi^2, 0), F=(phi, phi), P=(phi^2, 1), Q=(phi, 1/phi)
       E = m.set_point(phi2, 0, ID="E")
       F = m.set_point(phi, phi, ID="F")
       P = m.set_point(phi2, 1, classes=["golden"], ID="P")
       Q = m.set_point(phi, inv_phi, classes=["golden"], ID="Q")

       m.construct_line(A, C, classes=["golden"], ID="AC")
       m.construct_segment(E, P, classes=["auxiliary"], ID="EP")
       m.construct_segment(F, Q, classes=["auxiliary"], ID="FQ")
       m.construct_polygon([A, E, P], classes=["auxiliary"], ID="AEP")
       m.construct_polygon([C, F, Q], classes=["auxiliary"], ID="CFQ")

       return make_result(m, ("A", "Q"), ("Q", "P"), ("A", "Q", "P"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``curry-hooper-dissection`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\phi)`:

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
     - :math:`2 + \sqrt{5}`
     - :math:`0`
   * - ``C``
     - :math:`2 + \sqrt{5}`
     - :math:`\frac{1}{2} + \frac{\sqrt{5}}{2}`
   * - ``D``
     - :math:`0`
     - :math:`\frac{1}{2} + \frac{\sqrt{5}}{2}`
   * - ``E``
     - :math:`\frac{\sqrt{5}}{2} + \frac{3}{2}`
     - :math:`0`
   * - ``F``
     - :math:`\frac{1}{2} + \frac{\sqrt{5}}{2}`
     - :math:`\frac{1}{2} + \frac{\sqrt{5}}{2}`
   * - ``P``
     - :math:`\frac{\sqrt{5}}{2} + \frac{3}{2}`
     - :math:`1`
   * - ``Q``
     - :math:`\frac{1}{2} + \frac{\sqrt{5}}{2}`
     - :math:`- \frac{1}{2} + \frac{\sqrt{5}}{2}`

**Certified Golden Ratio**: ``AQ`` / ``QP`` = ``GoldenRatio``.
