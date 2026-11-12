:type: construction
:order: 5
:excerpt: Place two unit-diameter circles cC1, cC2 tangent at O and two flanking congruent circles cC3, cC4 inside outer circle cO. Requiring symmetric upper and lower circles cU1, cU2 to be simultaneously tangent to all five circles uniquely forces the flanking circles to have exact radius φ, outer radius φ^3, and OC4/C4A4 = φ.
:categories: 06-circles-sangaku
:tags: field-q-phi, golden-chain, jerzy-kocik

GC-06.05 · Jerzy Kocik's Six-Circle Apollonian Golden Window (2010)
===================================================================

**Discoverer(s)**: :person:`Jerzy Kocik <jerzy-kocik>` | **Date**: 2010 | **Field**: :math:`\mathbb{Q}(\phi)` | **Loci**: 8 (:term:`Lemoine <geometrographie>` :math:`S = 24`)

.. enunciation::

   Place two unit-diameter circles :g:`cC1`, :g:`cC2` tangent at :g:`O` and two flanking congruent circles :g:`cC3`, :g:`cC4` inside outer circle :g:`cO`. Requiring symmetric upper and lower circles :g:`cU1`, :g:`cU2` to be simultaneously tangent to all five circles uniquely forces the flanking circles to have exact radius :math:`\phi`, outer radius :math:`\phi^3`, and :math:`|OC4|/|C4A4| = \phi`.

.. picture:: 05-kocik-golden-window.svg
   :alt: GC-06.05 — Jerzy Kocik's Six-Circle Apollonian Golden Window (2010)

Given & Constructive Steps
--------------------------

**Given**: Origin :g:`O` :math:`= (0,0)` and tangency point :g:`P2` :math:`= (1,0)` defining central unit-diameter circles :g:`cC1` and :g:`cC2`.

.. step::

   Construct central circles :g:`cC1` and :g:`cC2` of radius :math:`\tfrac{1}{2}` touching at :g:`O` and reaching :g:`P1`, :g:`P2` :math:`= (\pm 1, 0)`.

.. step::

   Construct flanking circles :g:`cC3` and :g:`cC4` of radius :math:`\phi` centered at :g:`C3`, :g:`C4` :math:`= (\pm \phi^2, 0)` inside outer circle :g:`cO` of radius :math:`\phi^3`.

.. step::

   Inscribe symmetric circles :g:`cU1` and :g:`cU2` of radius :math:`\phi^3/\sqrt{5}` centered at :math:`(0, \pm 2\phi^2/\sqrt{5})`, tangent to all five circles.

Exact Symbolic Proof & Certificate
----------------------------------

Let flanking circles have unknown radius :math:`R`, so outer circle :g:`cO` has radius :math:`1 + 2R`. For upper circle :g:`cU1` of radius :math:`r_u` at :math:`(0, 1 + 2R - r_u)`, tangency to :g:`cC2` gives :math:`(1/2)^2 + (1 + 2R - r_u)^2 = (r_u + 1/2)^2`, while tangency to :g:`cC4` gives :math:`(1 + R)^2 + (1 + 2R - r_u)^2 = (r_u + R)^2`. Eliminating :math:`r_u` yields :math:`R^2 - R - 1 = 0`, uniquely forcing :math:`R = \phi`!

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`OC4` :math:`/` :g:`C4A4` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`O`, :g:`C4`, :g:`A4`)
   * - Exact Segment Lengths
     - :math:`|OC4| = \frac{\sqrt{5}}{2} + \frac{3}{2}`, :math:`|C4A4| = \frac{1}{2} + \frac{\sqrt{5}}{2}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(O, C4) = \frac{3 \sqrt{5}}{2} + \frac{7}{2}`, :math:`Q(C4, A4) = \frac{\sqrt{5}}{2} + \frac{3}{2}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 1 lines · 7 circles · 0 polygons (elementary loci :math:`= 8`, Lemoine :math:`S = 24`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **10** exact collinear golden section(s) and **3** connected golden chain(s) in this model:

- Section (:g:`A3`, :g:`C3`, :g:`O`): long :math:`|C3O|^2 = \frac{3 \sqrt{5}}{2} + \frac{7}{2}` vs. short :math:`|A3C3|^2 = \frac{\sqrt{5}}{2} + \frac{3}{2}`
- Section (:g:`A3`, :g:`P1`, :g:`P2`): long :math:`|A3P1|^2 = 2 \sqrt{5} + 6` vs. short :math:`|P1P2|^2 = 4`
- Section (:g:`A3`, :g:`P1`, :g:`A4`): long :math:`|P1A4|^2 = 6 \sqrt{5} + 14` vs. short :math:`|A3P1|^2 = 2 \sqrt{5} + 6`
- Section (:g:`A3`, :g:`O`, :g:`C4`): long :math:`|A3O|^2 = 4 \sqrt{5} + 9` vs. short :math:`|OC4|^2 = \frac{3 \sqrt{5}}{2} + \frac{7}{2}`
- Section (:g:`A3`, :g:`P2`, :g:`A4`): long :math:`|A3P2|^2 = 6 \sqrt{5} + 14` vs. short :math:`|P2A4|^2 = 2 \sqrt{5} + 6`
- Section (:g:`C3`, :g:`P1`, :g:`O`): long :math:`|C3P1|^2 = \frac{\sqrt{5}}{2} + \frac{3}{2}` vs. short :math:`|P1O|^2 = 1`
- Section (:g:`C3`, :g:`O`, :g:`A4`): long :math:`|OA4|^2 = 4 \sqrt{5} + 9` vs. short :math:`|C3O|^2 = \frac{3 \sqrt{5}}{2} + \frac{7}{2}`
- Section (:g:`P1`, :g:`P2`, :g:`A4`): long :math:`|P2A4|^2 = 2 \sqrt{5} + 6` vs. short :math:`|P1P2|^2 = 4`
- Section (:g:`O`, :g:`P2`, :g:`C4`): long :math:`|P2C4|^2 = \frac{\sqrt{5}}{2} + \frac{3}{2}` vs. short :math:`|OP2|^2 = 1`
- Section (:g:`O`, :g:`C4`, :g:`A4`): long :math:`|OC4|^2 = \frac{3 \sqrt{5}}{2} + \frac{7}{2}` vs. short :math:`|C4A4|^2 = \frac{\sqrt{5}}{2} + \frac{3}{2}`

**Connected Golden Chains**:

- Chain (:g:`A3` — :g:`C3` — :g:`O` — :g:`A4`) spanning 2 overlapping golden sections (progression ``< <``)
- Chain (:g:`A3` — :g:`P1` — :g:`P2` — :g:`A4`) spanning 2 overlapping golden sections (progression ``> <``)
- Chain (:g:`A3` — :g:`O` — :g:`C4` — :g:`A4`) spanning 2 overlapping golden sections (progression ``> >``)

Historical Commentary & Attribution
-----------------------------------

Published by Jerzy Kocik in *Mathematics Magazine* (2010), the Golden Window embeds powers :math:`1, \phi, \phi^2, \phi^3`, golden rectangles, and Kepler's right triangle in a single rigid Apollonian circle gasket.

- **Scholarly Citations**: :cite:`Golden Window <kocik-2010>`, :cite:`Cut-the-Knot: Golden Window <bogomolny-golden-window>`
- **Curated Reference**: `Golden Window <https://www.cut-the-knot.org/do_you_know/GoldenWindow.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Ratio (φ) <golden-ratio>` · :term:`Golden Section <golden-section>` · :term:`Golden Chain <golden-chain>` · :term:`Kepler Triangle <kepler-triangle>` · :term:`Golden Rectangle <golden-rectangle>`

.. toctree::
   :hidden:

   code
