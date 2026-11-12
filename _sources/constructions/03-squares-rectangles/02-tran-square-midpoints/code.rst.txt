GC-03.02 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-03.02``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-03.02")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_tran_square_midpoints() -> ConstructionResult:
       """Tran Quang Hung's square midpoint circle construction (Buratino 1)."""
       m = new_catalog_model("tran-square-midpoints")
       A = m.set_point(-2, 2, classes=["given"], ID="A")
       B = m.set_point(2, 2, classes=["given"], ID="B")
       C = m.set_point(2, -2, ID="C")
       D = m.set_point(-2, -2, ID="D")
       F = m.set_point(0, 0, ID="F")

       M = m.set_point(0, 2, ID="M")
       N = m.set_point(2, 0, ID="N")
       P = m.set_point(0, -2, ID="P")
       Q = m.set_point(-2, 0, ID="Q")

       m.construct_polygon([A, B, C, D], ID="ABCD")
       ln_qn = m.construct_line(Q, N, classes=["golden"], ID="QN")
       ln_mp = m.construct_line(M, P, classes=["auxiliary"], ID="MP")
       m.construct_segment(A, P, classes=["auxiliary"], ID="AP")

       K = m.set_point(-1, 0, ID="K")
       c_ka = m.construct_circle(K, A, classes=["compass"], ID="cKA")
       X = m.intersect(c_ka, ln_qn, between=(F, N), classes=["golden"], ID="X")

       ln_ax = m.construct_line(A, X, classes=["auxiliary"], ID="AX")
       Z = m.intersect(ln_ax, ln_mp, classes=["golden"], ID="Z")
       _ = Z

       return make_result(m, ("F", "X"), ("X", "N"), ("F", "X", "N"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``tran-square-midpoints`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\phi)`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``A``
     - :math:`-2`
     - :math:`2`
   * - ``B``
     - :math:`2`
     - :math:`2`
   * - ``C``
     - :math:`2`
     - :math:`-2`
   * - ``D``
     - :math:`-2`
     - :math:`-2`
   * - ``F``
     - :math:`0`
     - :math:`0`
   * - ``M``
     - :math:`0`
     - :math:`2`
   * - ``N``
     - :math:`2`
     - :math:`0`
   * - ``P``
     - :math:`0`
     - :math:`-2`
   * - ``Q``
     - :math:`-2`
     - :math:`0`
   * - ``K``
     - :math:`-1`
     - :math:`0`
   * - ``X``
     - :math:`-1 + \sqrt{5}`
     - :math:`0`
   * - ``Z``
     - :math:`0`
     - :math:`3 - \sqrt{5}`

**Certified Golden Ratio**: ``FX`` / ``XN`` = ``GoldenRatio``.
