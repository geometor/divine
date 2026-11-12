GC-05.06 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-05.06``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-05.06")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_tran_wu_xing_equilaterals() -> ConstructionResult:
       """Tran Quang Hung's fivefold Wu Xing congruent equilateral triangles & pentagram."""
       m = new_catalog_model("tran-wu-xing-equilaterals")
       _phi, s36, c36, s72, c72 = _pentagon_radicals()
       s3 = sp.sqrt(3)

       O = m.set_point(0, 0, classes=["given"], ID="O")
       v_coords = [
           (sp.Integer(0), sp.Integer(1)),
           (-s72, c72),
           (-s36, -c36),
           (s36, -c36),
           (s72, c72),
       ]

       v_pts = []
       w_pts = []
       for i, (vx, vy) in enumerate(v_coords, start=1):
           vp = m.set_point(vx, vy, classes=["given"] if i == 1 else [], ID=f"V{i}")
           wx = sp.expand(vx / 2 + (s3 * vy) / 2)
           wy = sp.expand(-(s3 * vx) / 2 + vy / 2)
           wp = m.set_point(wx, wy, ID=f"W{i}")
           v_pts.append(vp)
           w_pts.append(wp)
           m.construct_polygon([O, vp, wp], ID=f"OV{i}W{i}")

       # Pentagram star connecting V1..V5 skipping one vertex at a time
       ln_v2v5 = m.construct_line(v_pts[1], v_pts[4], classes=["golden"], ID="V2V5")
       for i in range(5):
           m.construct_segment(v_pts[i], v_pts[(i + 2) % 5], classes=["auxiliary"])

       ln_ow1 = m.construct_line(O, w_pts[0], classes=["golden"], ID="OW1")
       m.intersect(ln_v2v5, ln_ow1, classes=["golden"], ID="F")

       return make_result(m, ("O", "F"), ("F", "W1"), ("O", "F", "W1"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``tran-wu-xing-equilaterals`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\sqrt{3}, \phi, \sqrt{10 - 2\sqrt{5}})`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``O``
     - :math:`0`
     - :math:`0`
   * - ``V1``
     - :math:`0`
     - :math:`1`
   * - ``W1``
     - :math:`\frac{\sqrt{3}}{2}`
     - :math:`\frac{1}{2}`
   * - ``V2``
     - :math:`\frac{- \sqrt{10} \sqrt{5 - \sqrt{5}} - \sqrt{2} \sqrt{5 - \sqrt{5}}}{8}`
     - :math:`- \frac{1}{4} + \frac{\sqrt{5}}{4}`
   * - ``W2``
     - :math:`\frac{- \sqrt{10} \sqrt{5 - \sqrt{5}} - 2 \sqrt{3} - \sqrt{2} \sqrt{5 - \sqrt{5}} + 2 \sqrt{15}}{16}`
     - :math:`- \frac{1}{8} + \frac{\sqrt{6} \sqrt{5 - \sqrt{5}} + 2 \sqrt{5} + \sqrt{30} \sqrt{5 - \sqrt{5}}}{16}`
   * - ``V3``
     - :math:`- \frac{\sqrt{2} \sqrt{5 - \sqrt{5}}}{4}`
     - :math:`- \frac{\sqrt{5}}{4} - \frac{1}{4}`
   * - ``W3``
     - :math:`\frac{- \sqrt{15} - \sqrt{2} \sqrt{5 - \sqrt{5}} - \sqrt{3}}{8}`
     - :math:`- \frac{1}{8} + \frac{- \sqrt{5} + \sqrt{6} \sqrt{5 - \sqrt{5}}}{8}`
   * - ``V4``
     - :math:`\frac{\sqrt{2} \sqrt{5 - \sqrt{5}}}{4}`
     - :math:`- \frac{\sqrt{5}}{4} - \frac{1}{4}`
   * - ``W4``
     - :math:`\frac{- \sqrt{15} - \sqrt{3} + \sqrt{2} \sqrt{5 - \sqrt{5}}}{8}`
     - :math:`\frac{- \sqrt{6} \sqrt{5 - \sqrt{5}} - \sqrt{5}}{8} - \frac{1}{8}`
   * - ``V5``
     - :math:`\frac{\sqrt{2} \sqrt{5 - \sqrt{5}} + \sqrt{10} \sqrt{5 - \sqrt{5}}}{8}`
     - :math:`- \frac{1}{4} + \frac{\sqrt{5}}{4}`
   * - ``W5``
     - :math:`\frac{- 2 \sqrt{3} + \sqrt{2} \sqrt{5 - \sqrt{5}} + \sqrt{10} \sqrt{5 - \sqrt{5}} + 2 \sqrt{15}}{16}`
     - :math:`\frac{- \sqrt{30} \sqrt{5 - \sqrt{5}} - \sqrt{6} \sqrt{5 - \sqrt{5}} + 2 \sqrt{5}}{16} - \frac{1}{8}`
   * - ``F``
     - :math:`\frac{- \sqrt{3} + \sqrt{15}}{4}`
     - :math:`- \frac{1}{4} + \frac{\sqrt{5}}{4}`

**Certified Golden Ratio**: ``OF`` / ``FW1`` = ``GoldenRatio``.
