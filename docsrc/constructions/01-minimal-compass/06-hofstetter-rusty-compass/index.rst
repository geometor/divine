:type: construction
:order: 6
:excerpt: With a rusty compass locked permanently to aperture r = AB, circles cAB and cBA determine midpoint M via CD; a third unit circle cM centered at M meets cBA above AB at F, and line DF cuts AB at G in the golden ratio AG/GB = φ.
:categories: 01-minimal-compass
:tags: field-q-sqrt3-phi, kurt-hofstetter

GC-01.06 · Hofstetter's Fixed-Aperture Rusty-Compass Division
=============================================================

**Discoverer(s)**: :person:`Kurt Hofstetter <kurt-hofstetter>` | **Date**: 2005 | **Field**: :math:`\mathbb{Q}(\sqrt{3}, \phi)` | **Loci**: 6 (:term:`Lemoine <geometrographie>` :math:`S = 18`)

.. enunciation::

   With a **rusty compass** locked permanently to aperture :math:`r = |AB|`, circles :g:`cAB` and :g:`cBA` determine midpoint :g:`M` via :g:`CD`; a third unit circle :g:`cM` centered at :g:`M` meets :g:`cBA` above :g:`AB` at :g:`F`, and line :g:`DF` cuts :g:`AB` at :g:`G` in the golden ratio :math:`|AG|/|GB| = \phi`.

.. picture:: 06-hofstetter-rusty-compass.svg
   :alt: GC-01.06 — Hofstetter's Fixed-Aperture Rusty-Compass Division

Given & Constructive Steps
--------------------------

**Given**: Unit segment endpoints :g:`A` :math:`= (0, 0)` and :g:`B` :math:`= (1, 0)` and a fixed compass radius :math:`r = 1`.

.. step::

   Draw line :g:`AB` and unit circles :g:`cAB`, :g:`cBA` meeting at :g:`C` and :g:`D`.

.. step::

   Join :g:`CD` to bisect :g:`AB` at :g:`M` :math:`= (\tfrac{1}{2}, 0)`.

.. step::

   With the unchanged compass opening :math:`r = 1`, draw circle :g:`cM` centered at :g:`M`, meeting :g:`cBA` farthest from :g:`D` at :g:`F` :math:`= (\tfrac{3}{4}, \tfrac{\sqrt{15}}{4})`.

.. step::

   Join :g:`DF` to intersect :g:`AB` at :g:`G` :math:`= (1/\phi, 0)`.

Exact Symbolic Proof & Certificate
----------------------------------

Unit circles :g:`cM` :math:`((x - \tfrac{1}{2})^2 + y^2 = 1)` and :g:`cBA` :math:`((x - 1)^2 + y^2 = 1)` intersect along their radical axis :math:`x = \tfrac{3}{4}`, giving :g:`F` :math:`= (\tfrac{3}{4}, \tfrac{\sqrt{15}}{4})`—the exact same upper intersection point achieved by radius-:math:`2` circle :math:`E(B)` in Hofstetter's 2004 construction! Hence line :g:`DF` meets :g:`AB` at :g:`G` :math:`= (1/\phi, 0)`, so :math:`|AG|/|GB| = \phi`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`AG` :math:`/` :g:`GB` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`A`, :g:`G`, :g:`B`)
   * - Exact Segment Lengths
     - :math:`|AG| = - \frac{1}{2} + \frac{\sqrt{5}}{2}`, :math:`|GB| = \frac{3}{2} - \frac{\sqrt{5}}{2}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(A, G) = \frac{3}{2} - \frac{\sqrt{5}}{2}`, :math:`Q(G, B) = \frac{7}{2} - \frac{3 \sqrt{5}}{2}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\sqrt{3}, \phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 3 lines · 3 circles · 0 polygons (elementary loci :math:`= 6`, Lemoine :math:`S = 18`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **1** exact collinear golden section(s) and **0** connected golden chain(s) in this model:

- Section (:g:`A`, :g:`G`, :g:`B`): long :math:`|AG|^2 = \frac{3}{2} - \frac{\sqrt{5}}{2}` vs. short :math:`|GB|^2 = \frac{7}{2} - \frac{3 \sqrt{5}}{2}`

Historical Commentary & Attribution
-----------------------------------

Poncelet–Steiner and Abū al-Wafāʾ tradition prizes constructions executed with a single fixed compass opening (*compas rouillé*). :person:`Kurt Hofstetter <kurt-hofstetter>` (:cite:`Hofstetter 2005 <hofstetter-2005>`, :cite:`Cut-the-Knot <ctk-rusty-compass>`) requires only **three unit circles** and **three lines**.

- **Scholarly Citations**: :cite:`Division of a Segment in the Golden Section with Ruler and Rusty Compass <hofstetter-2005>`, :cite:`Cut-the-Knot: Golden Ratio with a Rusty Compass <ctk-rusty-compass>`
- **Curated Reference**: `Golden Ratio with a Rusty Compass <https://www.cut-the-knot.org/do_you_know/GoldenRatioByRustyCompass.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Rusty Compass <rusty-compass>` · :term:`Golden Section <golden-section>` · :term:`Vesica Piscis <vesica-piscis>`

.. toctree::
   :hidden:

   code
