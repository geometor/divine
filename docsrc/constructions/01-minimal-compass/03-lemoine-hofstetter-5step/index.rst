:type: construction
:order: 3
:excerpt: Given points A and B on line AB, let unit vesica circles cAB and cBA meet at C and D. Circle cCA cuts cAB at E and chord CD at F; then circle cEF cuts AB internally at G and externally at G_1 so that AG/GB = G_1A/AB = φ.
:categories: 01-minimal-compass
:tags: field-q-sqrt3-phi, emile-lemoine, kurt-hofstetter

GC-01.03 · Lemoine–Reusch–Hofstetter 5-Step Division
====================================================

**Discoverer(s)**: :person:`Émile Michel Hyacinthe Lemoine <emile-lemoine>`, :person:`Kurt Hofstetter <kurt-hofstetter>` | **Date**: 1902 / 2003 | **Field**: :math:`\mathbb{Q}(\sqrt{3}, \phi)` | **Loci**: 6 (:term:`Lemoine <geometrographie>` :math:`S = 18`)

.. enunciation::

   Given points :g:`A` and :g:`B` on line :g:`AB`, let unit vesica circles :g:`cAB` and :g:`cBA` meet at :g:`C` and :g:`D`. Circle :g:`cCA` cuts :g:`cAB` at :g:`E` and chord :g:`CD` at :g:`F`; then circle :g:`cEF` cuts :g:`AB` internally at :g:`G` and externally at :g:`G_1 <G1>` so that :math:`|AG|/|GB| = |G_1A|/|AB| = \phi`.

.. picture:: 03-lemoine-hofstetter-5step.svg
   :alt: GC-01.03 — Lemoine–Reusch–Hofstetter 5-Step Division

Given & Constructive Steps
--------------------------

**Given**: Unit base points :g:`A` :math:`= (0, 0)` and :g:`B` :math:`= (1, 0)` on carrier line :g:`AB`.

.. step::

   Draw circles :g:`cAB` and :g:`cBA` of unit radius, intersecting at :g:`C` :math:`= (\tfrac{1}{2}, \tfrac{\sqrt{3}}{2})` and :g:`D` :math:`= (\tfrac{1}{2}, -\tfrac{\sqrt{3}}{2})`.

.. step::

   Join perpendicular bisector line :g:`CD`.

.. step::

   Draw circle :g:`cCA` centered at :g:`C` through :g:`A`, intersecting :g:`cAB` at :g:`E` :math:`= (-\tfrac{1}{2}, \tfrac{\sqrt{3}}{2})` and segment :g:`CD` at :g:`F` :math:`= (\tfrac{1}{2}, \tfrac{\sqrt{3}}{2} - 1)`.

.. step::

   Draw circle :g:`cEF` centered at :g:`E` through :g:`F`, cutting :g:`AB` internally at :g:`G` and externally at :g:`G_1 <G1>`.

Exact Symbolic Proof & Certificate
----------------------------------

Because :g:`E` and :g:`C` share ordinate :math:`\tfrac{\sqrt{3}}{2}` at horizontal separation :math:`1`, while :g:`F` lies :math:`1` unit directly below :g:`C`, triangle :math:`\triangle ECF` is right isosceles with :math:`Q(E, F) = 1^2 + 1^2 = 2`. Circle :g:`cEF` therefore satisfies :math:`(x + \tfrac{1}{2})^2 + y^2 = 2`; setting :math:`y = 0` yields :math:`(x + \tfrac{1}{2})^2 = 2 - \tfrac{3}{4} = \tfrac{5}{4}`, giving :g:`G` :math:`= (1/\phi, 0)` and :g:`G_1 <G1>` :math:`= (-\phi, 0)`. Thus :math:`|AG|/|GB| = \phi` and :math:`(G_1, A, G, B)` forms a connected golden chain along :g:`AB`.

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
     - 2 given points · 2 lines · 4 circles · 0 polygons (elementary loci :math:`= 6`, Lemoine :math:`S = 18`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **2** exact collinear golden section(s) and **0** connected golden chain(s) in this model:

- Section (:g:`G1`, :g:`A`, :g:`B`): long :math:`|G1A|^2 = \frac{\sqrt{5}}{2} + \frac{3}{2}` vs. short :math:`|AB|^2 = 1`
- Section (:g:`A`, :g:`G`, :g:`B`): long :math:`|AG|^2 = \frac{3}{2} - \frac{\sqrt{5}}{2}` vs. short :math:`|GB|^2 = \frac{7}{2} - \frac{3 \sqrt{5}}{2}`

Historical Commentary & Attribution
-----------------------------------

Rediscovered independently by :person:`Kurt Hofstetter <kurt-hofstetter>` (:cite:`Hofstetter 2003 <hofstetter-2003>`), this five-locus division of a pre-drawn line segment had appeared a century earlier in :person:`Émile Lemoine <emile-lemoine>`'s *Géométrographie* (:cite:`Lemoine 1902 <lemoine-1902>`) and J. Reusch's *Planymetrische Konstruktionen in geometrographischer Ausführung* (1904).

- **Scholarly Citations**: :cite:`Géométrographie ou Art des constructions géométriques <lemoine-1902>`, :cite:`5-Step Division of a Segment in the Golden Section <hofstetter-2003>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Golden Ratio in Geometry — 5-Step Construction <https://www.cut-the-knot.org/do_you_know/GoldenRatio.shtml#5step>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Géométrographie <geometrographie>` · :term:`Golden Section <golden-section>` · :term:`Golden Chain <golden-chain>` · :term:`Vesica Piscis <vesica-piscis>`

.. toctree::
   :hidden:

   code
