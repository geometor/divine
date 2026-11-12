GC-07.01 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-07.01``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-07.01")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_tran_rhombus_incircle() -> ConstructionResult:
       """Tran Quang Hung's rhombus with diagonal ratio 2:1 and its incircle (Buratino 8)."""
       m = new_catalog_model("tran-rhombus-incircle")
       s5 = sp.sqrt(5)

       O = m.set_point(0, 0, classes=["given"], ID="O")
       A = m.set_point(0, s5, ID="A")
       C = m.set_point(0, -s5, ID="C")
       B = m.set_point(2 * s5, 0, classes=["given"], ID="B")
       D = m.set_point(-2 * s5, 0, ID="D")

       m.construct_polygon([A, B, C, D], ID="ABCD")
       m.construct_segment(A, C, classes=["auxiliary"], ID="AC")
       ln_bd = m.construct_line(D, B, classes=["golden"], ID="DB")

       # Inradius r = (2*sqrt(5) * sqrt(5)) / 5 = 2; tangency on AB at H = (2/sqrt(5), 4/sqrt(5))
       F = m.set_point(2, 0, classes=["golden"], ID="F")
       c_o = m.construct_circle(O, F, classes=["golden"], ID="cO")
       m.intersect(c_o, ln_bd, other_than=F, classes=["golden"], ID="E")

       return make_result(m, ("E", "F"), ("F", "B"), ("E", "F", "B"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``tran-rhombus-incircle`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\phi)`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``O``
     - :math:`0`
     - :math:`0`
   * - ``A``
     - :math:`0`
     - :math:`\sqrt{5}`
   * - ``C``
     - :math:`0`
     - :math:`- \sqrt{5}`
   * - ``B``
     - :math:`2 \sqrt{5}`
     - :math:`0`
   * - ``D``
     - :math:`- 2 \sqrt{5}`
     - :math:`0`
   * - ``F``
     - :math:`2`
     - :math:`0`
   * - ``E``
     - :math:`-2`
     - :math:`0`

**Certified Golden Ratio**: ``EF`` / ``FB`` = ``GoldenRatio``.
