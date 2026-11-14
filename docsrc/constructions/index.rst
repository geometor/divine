:navigation: header
:order: 1
:nav_title: Golden Constructions
:layout: book
:book_title: Catalog of Golden Ratio Constructions
:book_subtitle: Seven Geometric Families in Exact Symbolic Algebra
:author: Alexander Bogomolny, Euclid & Contemporary Geometers
:year: 2024

Catalog of Golden Ratio Constructions
=====================================

.. rubric:: Seven Geometric Families in Exact Symbolic Algebra

.. container:: title-page

   | **Alexander Bogomolny, Euclid & Contemporary Geometers**
   | *Curated from Cut-the-Knot & Classical Treatises*
   |
   | *Source*: Cut-the-Knot (1996–2018) & Classical Treatises
   | *GEOMETOR Digital Edition*: 45 Exact Symbolic Constructions in Seven Geometric Families

A machine-verified symbolic catalog of **45 geometric constructions and theorems** across **7 geometric families**, certifying **129 exact golden sections** and **33 connected golden chains** in 100% exact SymPy algebra.

Cataloging Ethos & Scholarly Provenance
---------------------------------------

Mathematical theorems, geometric incidences, and algebraic proportions are universal facts of nature and logic. Over two decades on *Cut-the-Knot* (`Golden Ratio in Geometry <https://www.cut-the-knot.org/do_you_know/GoldenRatio.shtml>`_, © 1996–2018 :person:`Alexander Bogomolny <alexander-bogomolny>`), Bogomolny curated an extraordinary constellation of classical and modern Golden Ratio constructions contributed by geometers around the world—spanning :person:`Euclid <euclid>`, :person:`Claudius Ptolemy <claudius-ptolemy>`, :person:`Johannes Kepler <johannes-kepler>`, :person:`Émile Lemoine <emile-lemoine>`, :person:`H. E. Huntley <h-e-huntley>`, :person:`George Odom <george-odom>`, :person:`Kurt Hofstetter <kurt-hofstetter>`, :person:`Michel Bataille <michel-bataille>`, :person:`Tran Quang Hung <tran-quang-hung>`, :person:`Bùi Quang Tuân <bui-quang-tuan>`, :person:`Jerzy Kocik <jerzy-kocik>`, and many others.

In the GEOMETOR Digital Scriptorium tradition—alongside the companion Ron Knott Golden Ratio Catalog (``geometor/knott``, cataloging :person:`Ron Knott <ron-knott>`'s :cite:`Fibonacci Numbers and the Golden Section <knott-golden-section>`)—this codex **catalogs** each universal geometric fact in GEOMETOR's canonical symbolic format:

1. **100% Exact Symbolic Modeling**: Every construction is built from scratch in :mod:`geometor.model` with zero floating-point approximations over :math:`\mathbb{Q}(\phi)`, :math:`\mathbb{Q}(\sqrt{2}, \phi)`, :math:`\mathbb{Q}(\sqrt{3}, \phi)`, :math:`\mathbb{Q}(\sqrt{\phi})`, and cyclotomic pentagonal extensions.
2. **Rational Trigonometry Certification**: Primary ratios are certified via exact :term:`quadrance <quadrance>` identities :math:`Q_{\text{long}} / Q_{\text{short}} = \phi + 1 = \phi^2` and Lemoine :term:`Géométrographie <geometrographie>` locus metrics.
3. **Automated Divine Discovery**: Every model is scanned by :mod:`geometor.divine.golden` to uncover secondary golden sections and connected :term:`golden chains <golden-chain>`.
4. **Original Prose & Interactive Vector Plates**: All expositions, proofs, and theme-adaptive ``.euclid-graphic`` SVGs are newly authored for GEOMETOR with bidirectional ``:g:`` hover highlighting and full bibliographic attribution.

Table of Contents
-----------------

.. collection::
   :type: family
   :sort: order

Scholarly Apparatus
-------------------

- :doc:`comparative_table` — Complete metrics across all 45 constructions (number fields, elementary loci, Lemoine simplicity, and detected golden chains).
- :doc:`bibliography` — Primary treatises, journal articles, and *Cut-the-Knot* archival citations.
- :doc:`persons` — Biographical index of classical and contemporary geometers.
- :doc:`glossary` — Technical glossary of constructive and Rational Trigonometry invariants.

.. toctree::
   :hidden:

   comparative_table
   bibliography
   persons
   glossary
