:type: construction
:order: 2
:excerpt: Let ABCD be a square with center F and side midpoints M, N, P, Q. The circle cKA on diameter AP intersects midline QN at X between F and N such that FX/XN = φ, while chord AX cuts MP at Z with MZ/ZF = φ.
:categories: 03-squares-rectangles
:tags: field-q-phi, golden-chain, tran-quang-hung

GC-03.02 · Tran Quang Hung's Square Midpoint Circle Division
============================================================

**Discoverer(s)**: :person:`Tran Quang Hung <tran-quang-hung>` | **Date**: 2015 | **Field**: :math:`\mathbb{Q}(\phi)` | **Loci**: 4 (:term:`Lemoine <geometrographie>` :math:`S = 12`)

.. enunciation::

   Let :g:`ABCD` be a square with center :g:`F` and side midpoints :g:`M`, :g:`N`, :g:`P`, :g:`Q`. The circle :g:`cKA` on diameter :g:`AP` intersects midline :g:`QN` at :g:`X` between :g:`F` and :g:`N` such that :math:`|FX|/|XN| = \phi`, while chord :g:`AX` cuts :g:`MP` at :g:`Z` with :math:`|MZ|/|ZF| = \phi`.

.. picture:: 02-tran-square-midpoints.svg
   :alt: GC-03.02 — Tran Quang Hung's Square Midpoint Circle Division

Given & Constructive Steps
--------------------------

**Given**: Square :g:`ABCD` of side :math:`4` centered at :g:`F` :math:`= (0,0)` with vertices :math:`(\pm 2, \pm 2)`.

.. step::

   Mark side midpoints :g:`M` :math:`= (0,2)`, :g:`N` :math:`= (2,0)`, :g:`P` :math:`= (0,-2)`, :g:`Q` :math:`= (-2,0)` and center :g:`F` :math:`= (0,0)`.

.. step::

   Bisect :g:`AP` at :g:`K` :math:`= (-1,0)` and draw circle :g:`cKA` of radius :math:`\sqrt{5}` on diameter :g:`AP`.

.. step::

   Mark :g:`X` where :g:`cKA` crosses :g:`QN` between :g:`F` and :g:`N`, and :g:`Z` where :g:`AX` crosses :g:`MP`.

Exact Symbolic Proof & Certificate
----------------------------------

Circle :g:`cKA` has equation :math:`(x + 1)^2 + y^2 = 5`. Along :g:`QN` (:math:`y = 0`), the positive root is :math:`x_X = \sqrt{5} - 1 = 2/\phi`. Since :math:`x_N = 2`, :math:`|XN| = 3 - \sqrt{5} = 2/\phi^2`, whence :math:`|FX|/|XN| = (2/\phi)/(2/\phi^2) = \phi`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`FX` :math:`/` :g:`XN` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`F`, :g:`X`, :g:`N`)
   * - Exact Segment Lengths
     - :math:`|FX| = -1 + \sqrt{5}`, :math:`|XN| = 3 - \sqrt{5}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(F, X) = 6 - 2 \sqrt{5}`, :math:`Q(X, N) = 14 - 6 \sqrt{5}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 3 lines · 1 circles · 1 polygons (elementary loci :math:`= 4`, Lemoine :math:`S = 12`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **4** exact collinear golden section(s) and **1** connected golden chain(s) in this model:

- Section (:g:`Q`, :g:`F`, :g:`X`): long :math:`|QF|^2 = 4` vs. short :math:`|FX|^2 = 6 - 2 \sqrt{5}`
- Section (:g:`F`, :g:`X`, :g:`N`): long :math:`|FX|^2 = 6 - 2 \sqrt{5}` vs. short :math:`|XN|^2 = 14 - 6 \sqrt{5}`
- Section (:g:`F`, :g:`Z`, :g:`M`): long :math:`|ZM|^2 = 6 - 2 \sqrt{5}` vs. short :math:`|FZ|^2 = 14 - 6 \sqrt{5}`
- Section (:g:`A`, :g:`Z`, :g:`X`): long :math:`|AZ|^2 = 10 - 2 \sqrt{5}` vs. short :math:`|ZX|^2 = 20 - 8 \sqrt{5}`

**Connected Golden Chains**:

- Chain (:g:`Q` — :g:`F` — :g:`X` — :g:`N`) spanning 2 overlapping golden sections (progression ``> >``)

Historical Commentary & Attribution
-----------------------------------

Right angle :math:`\angle AXP = 90^\circ` (Thales' theorem on diameter :g:`AP`) also makes :math:`\triangle PFX \sim \triangle AFZ`, transferring the golden division from horizontal half-midline :g:`FN` directly onto vertical half-midline :g:`FM`.

- **Scholarly Citations**: :cite:`Cut-the-Knot: Golden Ratio in Square <bogomolny-buratino1>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Golden Ratio in Square via Midpoints <https://www.cut-the-knot.org/do_you_know/Buratino1.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Ratio (φ) <golden-ratio>` · :term:`Golden Section <golden-section>`

.. toctree::
   :hidden:

   code
