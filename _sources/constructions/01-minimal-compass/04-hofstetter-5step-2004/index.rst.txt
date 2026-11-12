:type: construction
:order: 4
:excerpt: Given points A and B, draw line AB and unit circles cAB, cBA meeting at C and D, with cAB meeting ray BA beyond A at E. Circle cEB cuts cBA above AB at F, and secant DF divides AB at G in the golden ratio AG/GB = φ in exactly five Euclidean loci.
:categories: 01-minimal-compass
:tags: field-q-sqrt3-phi, golden-chain, kurt-hofstetter

GC-01.04 · Hofstetter's 2004 Five-Step Secant Division
======================================================

**Discoverer(s)**: :person:`Kurt Hofstetter <kurt-hofstetter>` | **Date**: 2004 | **Field**: :math:`\mathbb{Q}(\sqrt{3}, \phi)` | **Loci**: 5 (:term:`Lemoine <geometrographie>` :math:`S = 15`)

.. enunciation::

   Given points :g:`A` and :g:`B`, draw line :g:`AB` and unit circles :g:`cAB`, :g:`cBA` meeting at :g:`C` and :g:`D`, with :g:`cAB` meeting ray :g:`BA` beyond :g:`A` at :g:`E`. Circle :g:`cEB` cuts :g:`cBA` above :g:`AB` at :g:`F`, and secant :g:`DF` divides :g:`AB` at :g:`G` in the golden ratio :math:`|AG|/|GB| = \phi` in exactly five Euclidean loci.

.. picture:: 04-hofstetter-5step-2004.svg
   :alt: GC-01.04 — Hofstetter's 2004 Five-Step Secant Division

Given & Constructive Steps
--------------------------

**Given**: Points :g:`A` :math:`= (0, 0)` and :g:`B` :math:`= (1, 0)` in the Euclidean plane.

.. step::

   Draw carrier line :g:`AB` (Locus 1).

.. step::

   Draw circle :g:`cAB` centered at :g:`A` through :g:`B` (Locus 2), meeting line :g:`AB` beyond :g:`A` at :g:`E` :math:`= (-1, 0)`.

.. step::

   Draw circle :g:`cBA` centered at :g:`B` through :g:`A` (Locus 3), intersecting :g:`cAB` at :g:`C` and :g:`D` :math:`= (\tfrac{1}{2}, -\tfrac{\sqrt{3}}{2})`.

.. step::

   Draw circle :g:`cEB` centered at :g:`E` through :g:`B` of radius :math:`2` (Locus 4), meeting :g:`cBA` above :g:`AB` at :g:`F` :math:`= (\tfrac{3}{4}, \tfrac{\sqrt{15}}{4})`.

.. step::

   Draw line :g:`DF` (Locus 5), cutting :g:`AB` at :g:`G` :math:`= (1/\phi, 0)`.

Exact Symbolic Proof & Certificate
----------------------------------

Subtracting :math:`(x - 1)^2 + y^2 = 1` from :math:`(x + 1)^2 + y^2 = 4` gives :math:`4x = 3`, so :g:`F` has exact coordinates :math:`(\tfrac{3}{4}, \tfrac{\sqrt{15}}{4})`. Along secant :g:`DF` joining :math:`(\tfrac{1}{2}, -\tfrac{\sqrt{3}}{2})` to :math:`(\tfrac{3}{4}, \tfrac{\sqrt{15}}{4})`, the :math:`x`-intercept :g:`G` is :math:`x_G = \tfrac{1}{2} + \tfrac{1}{4} \cdot \frac{\sqrt{3}/2}{\sqrt{3}/2 + \sqrt{15}/4} = \tfrac{1}{2} + \frac{1}{2(\sqrt{5} + 2)} = \frac{\sqrt{5} - 1}{2} = \frac{1}{\phi}`. Therefore :math:`|AG| = 1/\phi`, :math:`|GB| = 1/\phi^2`, and :math:`|AG|/|GB| = \phi`.

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
     - 2 given points · 2 lines · 3 circles · 0 polygons (elementary loci :math:`= 5`, Lemoine :math:`S = 15`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **2** exact collinear golden section(s) and **1** connected golden chain(s) in this model:

- Section (:g:`E`, :g:`A`, :g:`G`): long :math:`|EA|^2 = 1` vs. short :math:`|AG|^2 = \frac{3}{2} - \frac{\sqrt{5}}{2}`
- Section (:g:`A`, :g:`G`, :g:`B`): long :math:`|AG|^2 = \frac{3}{2} - \frac{\sqrt{5}}{2}` vs. short :math:`|GB|^2 = \frac{7}{2} - \frac{3 \sqrt{5}}{2}`

**Connected Golden Chains**:

- Chain (:g:`E` — :g:`A` — :g:`G` — :g:`B`) spanning 2 overlapping golden sections (progression ``> >``)

Historical Commentary & Attribution
-----------------------------------

Published in *Forum Geometricorum* (:cite:`Hofstetter 2004 <hofstetter-2004>`), this construction requires only **two lines and three circles** even when the line through :g:`A` and :g:`B` is not drawn in advance. Notice that its abscissae :math:`x_D = \tfrac{1}{2}` and :math:`x_F = \tfrac{3}{4}` (or under reflection :math:`\tfrac{1}{4}, \tfrac{1}{2}`) are a special case of :person:`Bùi Quang Tuân <bui-quang-tuan>`'s general bilinear circle theorem (:cite:`Cut-the-Knot <ctk-hofstetter3>`).

- **Scholarly Citations**: :cite:`Another 5-Step Division of a Segment in the Golden Section <hofstetter-2004>`, :cite:`Cut-the-Knot: Kurt Hofstetter's 5-Step Construction of the Golden Section <ctk-hofstetter3>`
- **Curated Reference**: `5-Step Construction of the Golden Ratio, One of Many <https://www.cut-the-knot.org/do_you_know/Hofstetter3.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Géométrographie <geometrographie>` · :term:`Golden Section <golden-section>` · :term:`Vesica Piscis <vesica-piscis>`

.. toctree::
   :hidden:

   code
