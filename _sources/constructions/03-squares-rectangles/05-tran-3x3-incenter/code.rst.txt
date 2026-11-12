GC-03.05 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-03.05``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-03.05")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_tran_3x3_incenter() -> ConstructionResult:
       """Tran Quang Hung's 3x3 grid isosceles triangle incenter theorem."""
       m = new_catalog_model("tran-3x3-incenter")
       A = m.set_point(0, 0, classes=["given"], ID="A")
       Q1 = m.set_point(3, 0, classes=["given"], ID="Q1")
       Q2 = m.set_point(3, 3, ID="Q2")
       Q3 = m.set_point(0, 3, ID="Q3")

       S = m.set_point(1, 1, ID="S")
       K1 = m.set_point(2, 1, ID="K1")
       T = m.set_point(2, 2, ID="T")
       K2 = m.set_point(1, 2, ID="K2")

       U = m.set_point(3, 1, ID="U")
       V = m.set_point(1, 3, ID="V")

       m.construct_polygon([A, Q1, Q2, Q3], ID="AQ1Q2Q3")
       m.construct_polygon([S, K1, T, K2], classes=["auxiliary"], ID="SK1TK2")
       m.construct_polygon([A, U, V], ID="AUV")

       # Exact incenter P = ((5 - sqrt(5))/2, (5 - sqrt(5))/2) of AUV; tangent to UV at T=(2,2)
       px = (5 - sp.sqrt(5)) / 2
       P = m.set_point(px, px, classes=["golden"], ID="P")
       m.construct_line(A, Q2, classes=["golden"], ID="AT")
       m.construct_circle(P, T, classes=["golden"], ID="cPT")

       return make_result(m, ("P", "T"), ("S", "P"), ("S", "P", "T"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``tran-3x3-incenter`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\sqrt{2}, \phi)`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``A``
     - :math:`0`
     - :math:`0`
   * - ``Q1``
     - :math:`3`
     - :math:`0`
   * - ``Q2``
     - :math:`3`
     - :math:`3`
   * - ``Q3``
     - :math:`0`
     - :math:`3`
   * - ``S``
     - :math:`1`
     - :math:`1`
   * - ``K1``
     - :math:`2`
     - :math:`1`
   * - ``T``
     - :math:`2`
     - :math:`2`
   * - ``K2``
     - :math:`1`
     - :math:`2`
   * - ``U``
     - :math:`3`
     - :math:`1`
   * - ``V``
     - :math:`1`
     - :math:`3`
   * - ``P``
     - :math:`\frac{5}{2} - \frac{\sqrt{5}}{2}`
     - :math:`\frac{5}{2} - \frac{\sqrt{5}}{2}`

**Certified Golden Ratio**: ``PT`` / ``SP`` = ``GoldenRatio``.
