GC-03.01 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-03.01``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-03.01")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_tran_square_inscribed_semicircle() -> ConstructionResult:
       """Square inscribed in a right isosceles triangle inside a circle (Tran Quang Hung)."""
       m = new_catalog_model("tran-square-inscribed-semicircle")
       O = m.set_point(0, 0, classes=["given"], ID="O")
       A = m.set_point(-3, 0, classes=["given"], ID="A")
       B = m.set_point(3, 0, classes=["given"], ID="B")
       C = m.set_point(0, 3, ID="C")

       c_o = m.construct_circle(O, B, classes=["primary"], ID="cO")
       m.construct_polygon([A, B, C], ID="ABC")
       m.construct_line(A, B, ID="AB")

       # Inscribed square DEGF with F=(-1,0), G=(1,0) on AB and D=(-1,2) on AC, E=(1,2) on BC
       D = m.set_point(-1, 2, ID="D")
       E = m.set_point(1, 2, ID="E")
       G = m.set_point(1, 0, ID="G")
       F = m.set_point(-1, 0, ID="F")
       m.construct_polygon([D, E, G, F], classes=["golden"], ID="DEGF")

       ln_de = m.construct_line(D, E, classes=["golden"], ID="DE")
       Q = m.intersect(ln_de, c_o, beyond=(E, D), classes=["golden"], ID="Q")
       m.intersect(ln_de, c_o, beyond=(D, E), classes=["golden"], ID="P")
       _ = Q

       return make_result(m, ("D", "E"), ("E", "P"), ("D", "E", "P"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``tran-square-inscribed-semicircle`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\phi)`:

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
     - :math:`-3`
     - :math:`0`
   * - ``B``
     - :math:`3`
     - :math:`0`
   * - ``C``
     - :math:`0`
     - :math:`3`
   * - ``D``
     - :math:`-1`
     - :math:`2`
   * - ``E``
     - :math:`1`
     - :math:`2`
   * - ``G``
     - :math:`1`
     - :math:`0`
   * - ``F``
     - :math:`-1`
     - :math:`0`
   * - ``Q``
     - :math:`- \sqrt{5}`
     - :math:`2`
   * - ``P``
     - :math:`\sqrt{5}`
     - :math:`2`

**Certified Golden Ratio**: ``DE`` / ``EP`` = ``GoldenRatio``.
