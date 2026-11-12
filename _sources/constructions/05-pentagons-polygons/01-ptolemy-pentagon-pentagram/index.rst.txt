:type: construction
:order: 1
:excerpt: In unit circle cO with perpendicular radii OB and OC, let M bisect OB. Circle cMC cuts AB at E with OB/EO = φ and chord CE equal to the side of inscribed regular pentagon CP1P2P3P4, whose pentagram diagonals P1P4, CP2, CP3 cut one another in golden chains P1K2/K2P4 = φ.
:categories: 05-pentagons-polygons
:tags: field-pentagonal, golden-chain, claudius-ptolemy, euclid

GC-05.01 · Claudius Ptolemy's Regular Pentagon & Pentagram (Almagest I.10)
==========================================================================

**Discoverer(s)**: :person:`Claudius Ptolemy <claudius-ptolemy>`, :person:`Euclid of Alexandria <euclid>` | **Date**: c. 150 CE | **Field**: :math:`\mathbb{Q}(\phi, \sqrt{10 - 2\sqrt{5}})` | **Loci**: 6 (:term:`Lemoine <geometrographie>` :math:`S = 18`)

.. enunciation::

   In unit circle :g:`cO` with perpendicular radii :g:`OB` and :g:`OC`, let :g:`M` bisect :g:`OB`. Circle :g:`cMC` cuts :g:`AB` at :g:`E` with :math:`|OB|/|EO| = \phi` and chord :math:`|CE|` equal to the side of inscribed regular pentagon :g:`CP1P2P3P4`, whose pentagram diagonals :g:`P1P4`, :g:`CP2`, :g:`CP3` cut one another in golden chains :math:`|P1K2|/|K2P4| = \phi`.

.. picture:: 01-ptolemy-pentagon-pentagram.svg
   :alt: GC-05.01 — Claudius Ptolemy's Regular Pentagon & Pentagram (Almagest I.10)

Given & Constructive Steps
--------------------------

**Given**: Unit circle :g:`cO` centered at :g:`O` :math:`= (0,0)` through :g:`B` :math:`= (1,0)`, diameter :g:`AB`, and perpendicular apex :g:`C` :math:`= (0,1)`.

.. step::

   Bisect radius :g:`OB` at :g:`M` :math:`= (\tfrac{1}{2}, 0)` and swing circle :g:`cMC` to meet :g:`AB` at :g:`E` :math:`= (-1/\phi, 0)`.

.. step::

   Step off chord length :math:`|CE| = \sqrt{3 - \phi}` around :g:`cO` from :g:`C` to inscribe regular pentagon :g:`CP1P2P3P4`.

.. step::

   Draw pentagram diagonals :g:`P1P4`, :g:`CP2`, and :g:`CP3`, intersecting along :g:`P1P4` at :g:`K1` and :g:`K2`.

Exact Symbolic Proof & Certificate
----------------------------------

Right triangle :math:`\triangle MOC` has :math:`|MC| = \frac{\sqrt{5}}{2}`, so :math:`|OE| = \frac{\sqrt{5}-1}{2} = 1/\phi` (the regular decagon side, Euclid XIII.9–10) and :math:`|CE|^2 = 1 + 1/\phi^2 = 3 - \phi = 4\sin^2 36^\circ` (the regular pentagon side). By Euclid XIII.8, every pair of crossing pentagram diagonals cuts each other in extreme and mean ratio, forming the 4-point golden chain :math:`(P1, K1, K2, P4)`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`P1K2` :math:`/` :g:`K2P4` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`P1`, :g:`K2`, :g:`P4`)
   * - Exact Segment Lengths
     - :math:`|P1K2| = \frac{\sqrt{2} \sqrt{5 - \sqrt{5}}}{2}`, :math:`|K2P4| = \sqrt{5 - 2 \sqrt{5}}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(P1, K2) = \frac{5}{2} - \frac{\sqrt{5}}{2}`, :math:`Q(K2, P4) = 5 - 2 \sqrt{5}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\phi, \sqrt{10 - 2\sqrt{5}})`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 4 lines · 2 circles · 1 polygons (elementary loci :math:`= 6`, Lemoine :math:`S = 18`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **8** exact collinear golden section(s) and **2** connected golden chain(s) in this model:

- Section (:g:`A`, :g:`E`, :g:`O`): long :math:`|EO|^2 = \frac{3}{2} - \frac{\sqrt{5}}{2}` vs. short :math:`|AE|^2 = \frac{7}{2} - \frac{3 \sqrt{5}}{2}`
- Section (:g:`E`, :g:`O`, :g:`B`): long :math:`|OB|^2 = 1` vs. short :math:`|EO|^2 = \frac{3}{2} - \frac{\sqrt{5}}{2}`
- Section (:g:`P1`, :g:`K1`, :g:`K2`): long :math:`|P1K1|^2 = 5 - 2 \sqrt{5}` vs. short :math:`|K1K2|^2 = \frac{25}{2} - \frac{11 \sqrt{5}}{2}`
- Section (:g:`P1`, :g:`K1`, :g:`P4`): long :math:`|K1P4|^2 = \frac{5}{2} - \frac{\sqrt{5}}{2}` vs. short :math:`|P1K1|^2 = 5 - 2 \sqrt{5}`
- Section (:g:`P1`, :g:`K2`, :g:`P4`): long :math:`|P1K2|^2 = \frac{5}{2} - \frac{\sqrt{5}}{2}` vs. short :math:`|K2P4|^2 = 5 - 2 \sqrt{5}`
- Section (:g:`K1`, :g:`K2`, :g:`P4`): long :math:`|K2P4|^2 = 5 - 2 \sqrt{5}` vs. short :math:`|K1K2|^2 = \frac{25}{2} - \frac{11 \sqrt{5}}{2}`
- Section (:g:`P2`, :g:`K1`, :g:`C`): long :math:`|P2K1|^2 = \frac{5}{2} - \frac{\sqrt{5}}{2}` vs. short :math:`|K1C|^2 = 5 - 2 \sqrt{5}`
- Section (:g:`C`, :g:`K2`, :g:`P3`): long :math:`|K2P3|^2 = \frac{5}{2} - \frac{\sqrt{5}}{2}` vs. short :math:`|CK2|^2 = 5 - 2 \sqrt{5}`

**Connected Golden Chains**:

- Chain (:g:`A` — :g:`E` — :g:`O` — :g:`B`) spanning 2 overlapping golden sections (progression ``< <``)
- Chain (:g:`P1` — :g:`K1` — :g:`K2` — :g:`P4`) spanning 2 overlapping golden sections (progression ``> <``)

Historical Commentary & Attribution
-----------------------------------

Ptolemy introduced this streamlined circle-and-midpoint construction in *Almagest* I.10 to compute his chord table at :math:`36^\circ` and :math:`72^\circ`, dramatically simplifying Euclid's Book IV Proposition 11.

- **Scholarly Citations**: :cite:`Syntaxis Mathematica (Almagest) <ptolemy-almagest>`, :cite:`Elements (Heath Edition) <euclid-elements>`, :cite:`Cut-the-Knot: Regular Pentagon and Golden Ratio <bogomolny-pentagon>`
- **Curated Reference**: `Regular Pentagon and Golden Ratio <https://www.cut-the-knot.org/pythagoras/pentagon.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Ratio (φ) <golden-ratio>` · :term:`Golden Section <golden-section>` · :term:`Golden Chain <golden-chain>` · :term:`Extreme and Mean Ratio <extreme-and-mean-ratio>`

.. toctree::
   :hidden:

   code
