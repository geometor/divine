:type: construction
:order: 1
:excerpt: Given a straight segment AB, erect the square ABCD, bisect side AD at M, and transfer MB along ray DA beyond A to E. Swinging AE onto AB at G cuts AB in extreme and mean ratio, so that AB/AG = AG/GB = φ.
:categories: 01-minimal-compass
:tags: field-q-phi, euclid

GC-01.01 · Euclid's Classical Golden Section (Elements II.11 & VI.30)
=====================================================================

**Discoverer(s)**: :person:`Euclid of Alexandria <euclid>` | **Date**: c. 300 BCE | **Field**: :math:`\mathbb{Q}(\phi)` | **Loci**: 3 (:term:`Lemoine <geometrographie>` :math:`S = 9`)

.. enunciation::

   Given a straight segment :g:`AB`, erect the square :g:`ABCD`, bisect side :g:`AD` at :g:`M`, and transfer :g:`MB` along ray :g:`DA` beyond :g:`A` to :g:`E`. Swinging :g:`AE` onto :g:`AB` at :g:`G` cuts :g:`AB` in :term:`extreme and mean ratio <extreme-and-mean-ratio>`, so that :math:`|AB|/|AG| = |AG|/|GB| = \phi`.

.. picture:: 01-euclid-ii-11.svg
   :alt: GC-01.01 — Euclid's Classical Golden Section (Elements II.11 & VI.30)

Given & Constructive Steps
--------------------------

**Given**: Endpoints :g:`A` at :math:`(0, 0)` and :g:`B` at :math:`(2, 0)` defining a base segment :g:`AB` of length :math:`2`.

.. step::

   Erect square :g:`ABCD` on base :g:`AB` with :g:`D` at :math:`(0, 2)` and :g:`C` at :math:`(2, 2)`.

.. step::

   Bisect vertical side :g:`AD` at midpoint :g:`M` :math:`= (0, 1)` and join diagonal-radius :g:`MB` of length :math:`\sqrt{5}`.

.. step::

   Draw compass circle :g:`cMB` centered at :g:`M` through :g:`B`, cutting line :g:`AD` extended below :g:`A` at :g:`E` :math:`= (0, 1 - \sqrt{5})`.

.. step::

   Draw circle :g:`cAE` centered at :g:`A` through :g:`E`, cutting :g:`AB` internally at :g:`G` :math:`= (\sqrt{5} - 1, 0)` and completing the golden square :g:`AGFE`.

Exact Symbolic Proof & Certificate
----------------------------------

In right triangle :math:`\triangle MAB`, :math:`Q(M, A) = 1` and :math:`Q(A, B) = 4`, so :term:`quadrance <quadrance>` :math:`Q(M, B) = 5` and :math:`|ME| = |MB| = \sqrt{5}`. Subtracting :math:`|MA| = 1` gives :math:`|AG| = |AE| = \sqrt{5} - 1 = 2/\phi`, while the remainder on :g:`AB` has length :math:`|GB| = 2 - (\sqrt{5} - 1) = 3 - \sqrt{5} = 2/\phi^2`. Hence :math:`Q(A, G) = 6 - 2\sqrt{5}` and :math:`Q(G, B) = 14 - 6\sqrt{5}`, satisfying :math:`Q(A, G) = (\phi + 1)\,Q(G, B)` and :math:`|AG|/|GB| = \phi`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`AG` :math:`/` :g:`GB` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`A`, :g:`G`, :g:`B`)
   * - Exact Segment Lengths
     - :math:`|AG| = -1 + \sqrt{5}`, :math:`|GB| = 3 - \sqrt{5}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(A, G) = 6 - 2 \sqrt{5}`, :math:`Q(G, B) = 14 - 6 \sqrt{5}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 1 lines · 2 circles · 2 polygons (elementary loci :math:`= 3`, Lemoine :math:`S = 9`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **2** exact collinear golden section(s) and **0** connected golden chain(s) in this model:

- Section (:g:`E`, :g:`A`, :g:`D`): long :math:`|AD|^2 = 4` vs. short :math:`|EA|^2 = 6 - 2 \sqrt{5}`
- Section (:g:`A`, :g:`G`, :g:`B`): long :math:`|AG|^2 = 6 - 2 \sqrt{5}` vs. short :math:`|GB|^2 = 14 - 6 \sqrt{5}`

Historical Commentary & Attribution
-----------------------------------

In Book II Proposition 11 of the *Elements*, :person:`Euclid <euclid>` formulates this construction purely in the language of geometric algebra—requiring that rectangle :math:`AB \cdot GB` equal square :g:`AGFE`—and returns to it in Book VI Proposition 30 using theory of proportions (:cite:`Euclid <euclid-elements>`). In :person:`Alexander Bogomolny <alexander-bogomolny>`'s survey (:cite:`Cut-the-Knot <bogomolny-golden-ratio>`), this construction anchors all subsequent minimal-step refinements.

- **Scholarly Citations**: :cite:`Elements (Heath Edition) <euclid-elements>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`, :cite:`The Divine Proportion: A Study in Mathematical Beauty <huntley-1970>`
- **Curated Reference**: `Golden Ratio in Geometry <https://www.cut-the-knot.org/do_you_know/GoldenRatio.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Extreme and Mean Ratio <extreme-and-mean-ratio>` · :term:`Golden Section <golden-section>` · :term:`Quadrance <quadrance>`

.. toctree::
   :hidden:

   code
