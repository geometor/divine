GC-05.04 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-05.04``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-05.04")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_tran_pentagon_hexagon() -> ConstructionResult:
       """Tran Quang Hung's regular pentagon inscribed on the base of a regular hexagon."""
       m = new_catalog_model("tran-pentagon-hexagon")
       phi, s36, _c36, _s72, _c72 = _pentagon_radicals()
       phi2 = phi + 1
       s3 = sp.sqrt(3)

       A = m.set_point(-1, 0, classes=["given"], ID="A")
       F = m.set_point(1, 0, classes=["given"], ID="F")
       E = m.set_point(2, s3, ID="E")
       D = m.set_point(1, 2 * s3, ID="D")
       C = m.set_point(-1, 2 * s3, ID="C")
       B = m.set_point(-2, s3, ID="B")
       m.construct_polygon([A, B, C, D, E, F], ID="ABCDEF")

       M = m.set_point(-phi, 2 * phi * s36, ID="M")
       N = m.set_point(0, 2 * phi2 * s36, ID="N")
       P = m.set_point(phi, 2 * phi * s36, ID="P")
       m.construct_polygon([A, M, N, P, F], classes=["golden"], ID="AMNPF")
       m.construct_segment(M, P, classes=["auxiliary"], ID="MP")

       ln_bc = m.construct_line(B, C, classes=["golden"], ID="BC")
       ln_de = m.construct_line(D, E, classes=["auxiliary"], ID="DE")

       # Perpendiculars to horizontal diagonal MP at M and P
       GM = m.set_point(-phi, 2 * phi * s36 + 1, guide=True, ID="GM")
       GP = m.set_point(phi, 2 * phi * s36 + 1, guide=True, ID="GP")
       ln_mq = m.construct_line(M, GM, classes=["golden"], ID="MQ")
       ln_pr = m.construct_line(P, GP, classes=["auxiliary"], ID="PR")

       m.intersect(ln_mq, ln_bc, classes=["golden"], ID="Q")
       R = m.intersect(ln_pr, ln_de, classes=["golden"], ID="R")
       _ = R

       return make_result(m, ("C", "Q"), ("Q", "B"), ("C", "Q", "B"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``tran-pentagon-hexagon`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\sqrt{3}, \phi, \sqrt{10 - 2\sqrt{5}})`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``A``
     - :math:`-1`
     - :math:`0`
   * - ``F``
     - :math:`1`
     - :math:`0`
   * - ``E``
     - :math:`2`
     - :math:`\sqrt{3}`
   * - ``D``
     - :math:`1`
     - :math:`2 \sqrt{3}`
   * - ``C``
     - :math:`-1`
     - :math:`2 \sqrt{3}`
   * - ``B``
     - :math:`-2`
     - :math:`\sqrt{3}`
   * - ``M``
     - :math:`- \frac{\sqrt{5}}{2} - \frac{1}{2}`
     - :math:`\frac{\sqrt{2} \sqrt{5 - \sqrt{5}} + \sqrt{10} \sqrt{5 - \sqrt{5}}}{4}`
   * - ``N``
     - :math:`0`
     - :math:`\frac{\sqrt{10} \sqrt{5 - \sqrt{5}} + 3 \sqrt{2} \sqrt{5 - \sqrt{5}}}{4}`
   * - ``P``
     - :math:`\frac{1}{2} + \frac{\sqrt{5}}{2}`
     - :math:`\frac{\sqrt{2} \sqrt{5 - \sqrt{5}} + \sqrt{10} \sqrt{5 - \sqrt{5}}}{4}`
   * - ``Q``
     - :math:`- \frac{\sqrt{5}}{2} - \frac{1}{2}`
     - :math:`\frac{- \sqrt{15} + 5 \sqrt{3}}{2}`
   * - ``R``
     - :math:`\frac{1}{2} + \frac{\sqrt{5}}{2}`
     - :math:`\frac{- \sqrt{15} + 5 \sqrt{3}}{2}`

**Certified Golden Ratio**: ``CQ`` / ``QB`` = ``GoldenRatio``.
