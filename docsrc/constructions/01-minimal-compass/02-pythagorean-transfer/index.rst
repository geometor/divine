:type: construction
:order: 2
:excerpt: On segment AB of length 2, erect perpendicular leg BC of length 1 = tfrac{1}{2}AB. Circle cCB cuts hypotenuse AC at D (and ray AC at E), and circle cAD transfers AD onto AB at G, dividing AB in the golden ratio AG/GB = φ.
:categories: 01-minimal-compass
:tags: field-q-phi, euclid

GC-01.02 · Right-Triangle Hypotenuse Transfer (1 : 2 : √5)
==========================================================

**Discoverer(s)**: :person:`Euclid of Alexandria <euclid>` | **Date**: Classical | **Field**: :math:`\mathbb{Q}(\phi)` | **Loci**: 4 (:term:`Lemoine <geometrographie>` :math:`S = 12`)

.. enunciation::

   On segment :g:`AB` of length :math:`2`, erect perpendicular leg :g:`BC` of length :math:`1 = \tfrac{1}{2}|AB|`. Circle :g:`cCB` cuts hypotenuse :g:`AC` at :g:`D` (and ray :g:`AC` at :g:`E`), and circle :g:`cAD` transfers :g:`AD` onto :g:`AB` at :g:`G`, dividing :g:`AB` in the golden ratio :math:`|AG|/|GB| = \phi`.

.. picture:: 02-pythagorean-transfer.svg
   :alt: GC-01.02 — Right-Triangle Hypotenuse Transfer (1 : 2 : √5)

Given & Constructive Steps
--------------------------

**Given**: Segment :g:`AB` from :g:`A` :math:`= (0, 0)` to :g:`B` :math:`= (2, 0)` with midpoint :g:`M` :math:`= (1, 0)` and perpendicular leg endpoint :g:`C` :math:`= (2, 1)`.

.. step::

   Form the :math:`1 : 2 : \sqrt{5}` right triangle :g:`ABC` with right angle at :g:`B` and line :g:`AC`.

.. step::

   Draw circle :g:`cCB` centered at :g:`C` through :g:`B` (radius :math:`1`), intersecting :g:`AC` internally at :g:`D` and externally at :g:`E`.

.. step::

   Draw circle :g:`cAD` centered at :g:`A` through :g:`D`, meeting segment :g:`AB` at :g:`G`.

Exact Symbolic Proof & Certificate
----------------------------------

Since :math:`|AB| = 2` and :math:`|BC| = 1`, hypotenuse :g:`AC` has length :math:`\sqrt{5}`. Circle :g:`cCB` subtracts and adds unit radius :math:`1` along line :g:`AC`, yielding :math:`|AD| = \sqrt{5} - 1 = 2/\phi` and :math:`|AE| = \sqrt{5} + 1 = 2\phi`. Along :g:`AC`, :math:`|AE|/|DE| = (2\phi)/2 = \phi`, while transferring :math:`|AD|` to :g:`AG` on :g:`AB` produces :math:`|AG|/|GB| = (\sqrt{5} - 1)/(3 - \sqrt{5}) = \phi`.

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
     - 2 given points · 1 lines · 3 circles · 1 polygons (elementary loci :math:`= 4`, Lemoine :math:`S = 12`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **2** exact collinear golden section(s) and **0** connected golden chain(s) in this model:

- Section (:g:`A`, :g:`D`, :g:`E`): long :math:`|DE|^2 = 4` vs. short :math:`|AD|^2 = 6 - 2 \sqrt{5}`
- Section (:g:`A`, :g:`G`, :g:`B`): long :math:`|AG|^2 = 6 - 2 \sqrt{5}` vs. short :math:`|GB|^2 = 14 - 6 \sqrt{5}`

Historical Commentary & Attribution
-----------------------------------

Cataloged at the opening of :cite:`Bogomolny's Golden Ratio overview <bogomolny-golden-ratio>` and popularized by :person:`H. E. Huntley <h-e-huntley>` (:cite:`Huntley 1970 <huntley-1970>`), this streamlined distillation of Euclid II.11 simultaneously exhibits both :math:`2/\phi` (at :g:`D`) and :math:`2\phi` (at :g:`E`) along a single secant line :g:`AC`.

- **Scholarly Citations**: :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`, :cite:`The Divine Proportion: A Study in Mathematical Beauty <huntley-1970>`
- **Curated Reference**: `Golden Ratio in Geometry — Classical Right-Triangle Division <https://www.cut-the-knot.org/do_you_know/GoldenRatio.shtml#construct>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Section <golden-section>` · :term:`Quadrance <quadrance>` · :term:`Golden Chain <golden-chain>`

.. toctree::
   :hidden:

   code
