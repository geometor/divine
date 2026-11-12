:type: construction
:order: 7
:excerpt: Let I be the midpoint of radius OJ of circle cO, XT the chord perpendicular to OJ through I, and ICD an equilateral triangle symmetric about OJ with C and D on cO. If rays CI and DI meet cO again at A and B, then chords BC and AD cut XT at Y and Z with YZ/ZT = YT/YZ = YZ/XY = φ.
:categories: 02-equilateral-hexagon
:tags: field-q-sqrt3-phi, golden-chain, nguyen-thanh-dung

GC-02.07 · Butterfly Chords Astride an Equilateral Triangle
===========================================================

**Discoverer(s)**: :person:`Nguyen Thanh Dung <nguyen-thanh-dung>` | **Date**: 2016 | **Field**: :math:`\mathbb{Q}(\sqrt{3}, \phi)` | **Loci**: 6 (:term:`Lemoine <geometrographie>` :math:`S = 18`)

.. enunciation::

   Let :g:`I` be the midpoint of radius :g:`OJ` of circle :g:`cO`, :g:`XT` the chord perpendicular to :g:`OJ` through :g:`I`, and :g:`ICD` an equilateral triangle symmetric about :g:`OJ` with :g:`C` and :g:`D` on :g:`cO`. If rays :g:`CI` and :g:`DI` meet :g:`cO` again at :g:`A` and :g:`B`, then chords :g:`BC` and :g:`AD` cut :g:`XT` at :g:`Y` and :g:`Z` with :math:`|YZ|/|ZT| = |YT|/|YZ| = |YZ|/|XY| = \phi`.

.. picture:: 07-nguyen-butterfly-equilateral.svg
   :alt: GC-02.07 — Butterfly Chords Astride an Equilateral Triangle

Given & Constructive Steps
--------------------------

**Given**: Circle :g:`cO` centered at :g:`O` :math:`= (0, 0)` through :g:`J` :math:`= (0, 2)` with radius midpoint :g:`I` :math:`= (0, 1)`.

.. step::

   Draw chord :g:`XT` through :g:`I` perpendicular to :g:`OJ`, meeting :g:`cO` at :g:`X` :math:`= (-\sqrt{3}, 1)` and :g:`T` :math:`= (\sqrt{3}, 1)`.

.. step::

   Inscribe equilateral triangle :g:`ICD` with apex :g:`I` and base vertices :g:`C`, :g:`D` on :g:`cO`.

.. step::

   Extend :g:`CI` and :g:`DI` to meet :g:`cO` at :g:`A` and :g:`B`, then draw butterfly chords :g:`BC` and :g:`AD` cutting :g:`XT` at :g:`Y` and :g:`Z`.

Exact Symbolic Proof & Certificate
----------------------------------

For :g:`C` and :g:`D` on :math:`x^2 + y^2 = 4` forming equilateral :g:`ICD` of side :math:`s` below :g:`I` :math:`= (0, 1)`, :math:`(s/2)^2 + (1 - s\sqrt{3}/2)^2 = 4 \implies s^2 - \sqrt{3}\,s - 3 = 0`, giving :math:`s = \sqrt{3}\,\phi` directly. By the Butterfly Theorem and symmetry across :g:`OJ`, :math:`|IY| = |IZ| = \sqrt{3}/(2\phi)`, while :math:`|IT| = \sqrt{3}`. Hence :math:`|YZ| = \sqrt{3}/\phi` and :math:`|ZT| = \sqrt{3}(1 - 1/(2\phi))`—moreover :math:`|YZ|/|ZT| = |YT|/|YZ| = |YZ|/|XY| = \phi`, forming the 4-point golden chain :math:`(X, Y, Z, T)`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`YZ` :math:`/` :g:`ZT` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`Y`, :g:`Z`, :g:`T`)
   * - Exact Segment Lengths
     - :math:`|YZ| = \frac{\sqrt{30} \sqrt{- 5 \sqrt{2} \sqrt{\sqrt{5} + 3} - \sqrt{10} \sqrt{\sqrt{5} + 3} + 6 \sqrt{5} + 18}}{10}`, :math:`|ZT| = \frac{\sqrt{15} \sqrt{- 10 \sqrt{2} \sqrt{\sqrt{5} + 3} - \sqrt{5} + 19 + 3 \sqrt{10} \sqrt{\sqrt{5} + 3}}}{10}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(Y, Z) = \frac{- 15 \sqrt{2} \sqrt{\sqrt{5} + 3} - 3 \sqrt{10} \sqrt{\sqrt{5} + 3} + 18 \sqrt{5}}{10} + \frac{27}{5}`, :math:`Q(Z, T) = \frac{- 30 \sqrt{2} \sqrt{\sqrt{5} + 3} - 3 \sqrt{5} + 9 \sqrt{10} \sqrt{\sqrt{5} + 3}}{20} + \frac{57}{20}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\sqrt{3}, \phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 5 lines · 1 circles · 1 polygons (elementary loci :math:`= 6`, Lemoine :math:`S = 18`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **2** exact collinear golden section(s) and **1** connected golden chain(s) in this model:

- Section (:g:`X`, :g:`Y`, :g:`Z`): long :math:`|YZ|^2 = \frac{- 15 \sqrt{2} \sqrt{\sqrt{5} + 3} - 3 \sqrt{10} \sqrt{\sqrt{5} + 3} + 18 \sqrt{5}}{10} + \frac{27}{5}` vs. short :math:`|XY|^2 = \frac{- 30 \sqrt{2} \sqrt{\sqrt{5} + 3} - 3 \sqrt{5} + 9 \sqrt{10} \sqrt{\sqrt{5} + 3}}{20} + \frac{57}{20}`
- Section (:g:`Y`, :g:`Z`, :g:`T`): long :math:`|YZ|^2 = \frac{- 15 \sqrt{2} \sqrt{\sqrt{5} + 3} - 3 \sqrt{10} \sqrt{\sqrt{5} + 3} + 18 \sqrt{5}}{10} + \frac{27}{5}` vs. short :math:`|ZT|^2 = \frac{- 30 \sqrt{2} \sqrt{\sqrt{5} + 3} - 3 \sqrt{5} + 9 \sqrt{10} \sqrt{\sqrt{5} + 3}}{20} + \frac{57}{20}`

**Connected Golden Chains**:

- Chain (:g:`X` — :g:`Y` — :g:`Z` — :g:`T`) spanning 2 overlapping golden sections (progression ``< >``)

Historical Commentary & Attribution
-----------------------------------

Discovered by :person:`Nguyen Thanh Dung <nguyen-thanh-dung>` (:cite:`Cut-the-Knot <ctk-butterfly-equilateral>`), this synthesis of Odom's equilateral chord and the classical **Butterfly Theorem** creates four collinear points :math:`(X, Y, Z, T)` with three overlapping golden sections on :g:`XT`.

- **Scholarly Citations**: :cite:`Cut-the-Knot: Golden Ratio Astride Equilateral Triangle <ctk-butterfly-equilateral>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Golden Ratio in a Butterfly Astride an Equilateral Triangle <https://www.cut-the-knot.org/do_you_know/GoldenRatioAstrideEquilateralTriangle.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Butterfly Configuration <butterfly-theorem>` · :term:`Golden Chain <golden-chain>` · :term:`Golden Section <golden-section>`

.. toctree::
   :hidden:

   code
