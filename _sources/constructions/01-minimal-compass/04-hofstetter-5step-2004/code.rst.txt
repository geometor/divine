GC-01.04 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-01.04``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-01.04")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_hofstetter_5step_2004() -> ConstructionResult:
       """Kurt Hofstetter's 2004 5-step straightedge-and-compass division."""
       m = new_catalog_model("hofstetter-5step-2004")
       A = m.set_point(0, 0, classes=["given"], ID="A")
       B = m.set_point(1, 0, classes=["given"], ID="B")

       # 5 elementary Euclidean steps: line AB, circles A(B), B(A), E(B), line DF
       ln_ab = m.construct_line(A, B, ID="AB")
       c_ab = m.construct_circle(A, B, classes=["compass"], ID="cAB")
       E = m.intersect(c_ab, ln_ab, beyond=(B, A), ID="E")
       c_ba = m.construct_circle(B, A, classes=["compass"], ID="cBA")
       C = m.intersect(c_ab, c_ba, side_of=(A, B, 1), ID="C")
       D = m.intersect(c_ab, c_ba, side_of=(A, B, -1), ID="D")
       _ = C

       c_eb = m.construct_circle(E, B, classes=["compass"], ID="cEB")
       F = m.intersect(c_eb, c_ba, side_of=(A, B, 1), ID="F")
       ln_df = m.construct_line(D, F, classes=["golden"], ID="DF")
       m.intersect(ln_df, ln_ab, classes=["golden"], ID="G")

       return make_result(m, ("A", "G"), ("G", "B"), ("A", "G", "B"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``hofstetter-5step-2004`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\sqrt{3}, \phi)`:

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
     - :math:`1`
     - :math:`0`
   * - ``E``
     - :math:`-1`
     - :math:`0`
   * - ``C``
     - :math:`\frac{1}{2}`
     - :math:`\frac{\sqrt{3}}{2}`
   * - ``D``
     - :math:`\frac{1}{2}`
     - :math:`- \frac{\sqrt{3}}{2}`
   * - ``F``
     - :math:`\frac{3}{4}`
     - :math:`\frac{\sqrt{15}}{4}`
   * - ``G``
     - :math:`- \frac{1}{2} + \frac{\sqrt{5}}{2}`
     - :math:`0`

**Certified Golden Ratio**: ``AG`` / ``GB`` = ``GoldenRatio``.
