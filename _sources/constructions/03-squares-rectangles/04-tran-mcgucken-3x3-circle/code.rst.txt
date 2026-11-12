GC-03.04 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-03.04``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-03.04")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_tran_mcgucken_3x3_circle() -> ConstructionResult:
       """Tran Quang Hung & Elliot McGucken's 3x3 grid diagonal circle division."""
       m = new_catalog_model("tran-mcgucken-3x3-circle")
       S1 = m.set_point(-3, 3, ID="S1")
       A = m.set_point(3, 3, classes=["given"], ID="A")
       S3 = m.set_point(3, -3, ID="S3")
       S4 = m.set_point(-3, -3, ID="S4")

       C1 = m.set_point(-1, 1, ID="C1")
       C = m.set_point(1, 1, ID="C")
       C3 = m.set_point(1, -1, ID="C3")
       C4 = m.set_point(-1, -1, ID="C4")

       O = m.set_point(0, 0, classes=["given"], ID="O")
       T = m.set_point(1, 3, ID="T")

       m.construct_polygon([S1, A, S3, S4], ID="S1AS3S4")
       m.construct_polygon([C1, C, C3, C4], classes=["auxiliary"], ID="C1CC3C4")

       # Internal 3x3 grid lines
       G1 = m.set_point(-1, 3, guide=True, ID="G1")
       G2 = m.set_point(-1, -3, guide=True, ID="G2")
       G3 = m.set_point(1, -3, guide=True, ID="G3")
       G4 = m.set_point(-3, 1, guide=True, ID="G4")
       G5 = m.set_point(3, 1, guide=True, ID="G5")
       G6 = m.set_point(-3, -1, guide=True, ID="G6")
       G7 = m.set_point(3, -1, guide=True, ID="G7")
       m.construct_segment(G1, G2, classes=["auxiliary"], ID="gV1")
       m.construct_segment(T, G3, classes=["auxiliary"], ID="gV2")
       m.construct_segment(G4, G5, classes=["auxiliary"], ID="gH1")
       m.construct_segment(G6, G7, classes=["auxiliary"], ID="gH2")
       m.construct_segment(O, T, classes=["auxiliary"], ID="OT")

       ln_oa = m.construct_line(O, A, classes=["golden"], ID="OA")
       c_ot = m.construct_circle(O, T, classes=["golden"], ID="cOT")
       m.intersect(c_ot, ln_oa, between=(C, A), classes=["golden"], ID="B")

       return make_result(m, ("C", "B"), ("B", "A"), ("C", "B", "A"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``tran-mcgucken-3x3-circle`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\sqrt{2}, \phi)`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``S1``
     - :math:`-3`
     - :math:`3`
   * - ``A``
     - :math:`3`
     - :math:`3`
   * - ``S3``
     - :math:`3`
     - :math:`-3`
   * - ``S4``
     - :math:`-3`
     - :math:`-3`
   * - ``C1``
     - :math:`-1`
     - :math:`1`
   * - ``C``
     - :math:`1`
     - :math:`1`
   * - ``C3``
     - :math:`1`
     - :math:`-1`
   * - ``C4``
     - :math:`-1`
     - :math:`-1`
   * - ``O``
     - :math:`0`
     - :math:`0`
   * - ``T``
     - :math:`1`
     - :math:`3`
   * - ``B``
     - :math:`\sqrt{5}`
     - :math:`\sqrt{5}`

**Certified Golden Ratio**: ``CB`` / ``BA`` = ``GoldenRatio``.
