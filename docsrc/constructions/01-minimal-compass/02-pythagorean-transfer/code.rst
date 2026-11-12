GC-01.02 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-01.02``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-01.02")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_pythagorean_transfer() -> ConstructionResult:
       """Heron-Ptolemy right-triangle hypotenuse transfer on a 1:2 right triangle."""
       m = new_catalog_model("pythagorean-transfer")
       A = m.set_point(0, 0, classes=["given"], ID="A")
       B = m.set_point(2, 0, classes=["given"], ID="B")
       M = m.set_point(1, 0, ID="M")
       C = m.set_point(2, 1, ID="C")

       seg_ab = m.construct_segment(A, B, ID="AB")
       m.construct_segment(B, C, ID="BC")
       ln_ac = m.construct_line(A, C, classes=["auxiliary"], ID="AC")
       m.construct_polygon([A, B, C], ID="ABC")

       c_bm = m.construct_circle(B, M, classes=["auxiliary"], ID="cBM")
       _ = c_bm
       c_cb = m.construct_circle(C, B, classes=["compass"], ID="cCB")
       D = m.intersect(c_cb, ln_ac, between=(A, C), ID="D")
       E = m.intersect(c_cb, ln_ac, beyond=(A, C), ID="E")

       c_ad = m.construct_circle(A, D, classes=["golden"], ID="cAD")
       m.intersect(c_ad, seg_ab, between=(A, B), classes=["golden"], ID="G")
       _ = E

       return make_result(m, ("A", "G"), ("G", "B"), ("A", "G", "B"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``pythagorean-transfer`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\phi)`:

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
     - :math:`2`
     - :math:`0`
   * - ``M``
     - :math:`1`
     - :math:`0`
   * - ``C``
     - :math:`2`
     - :math:`1`
   * - ``D``
     - :math:`2 - \frac{2 \sqrt{5}}{5}`
     - :math:`1 - \frac{\sqrt{5}}{5}`
   * - ``E``
     - :math:`\frac{2 \sqrt{5}}{5} + 2`
     - :math:`\frac{\sqrt{5}}{5} + 1`
   * - ``G``
     - :math:`-1 + \sqrt{5}`
     - :math:`0`

**Certified Golden Ratio**: ``AG`` / ``GB`` = ``GoldenRatio``.
