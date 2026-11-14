:navigation: header
:order: 20
:nav_title: Usage

==================
Using This Edition
==================

.. rubric:: Reader's Guide to the Catalog of Golden Ratio Constructions & Symbolic Discovery Engine

Welcome to the GEOMETOR edition of the **Catalog of Golden Ratio Constructions** and the ``geometor.divine`` symbolic discovery engine. This edition unites 45 certified ruler-and-compass constructions across 7 geometric families with automated golden section discovery and exact SymPy modeling.

----

1. Synchronized Reading Tracks
------------------------------

Every construction in the catalog (:doc:`/constructions/index`) is organized across two synchronized companion tracks:

* **Synthesis Track** (``index.rst``): The mathematical enunciation, historical background, Euclidean proof, and certified algebraic metrics (number field, Lemoine simplicity, and discovered golden chains).
* **Code Track** (``code.rst``): The complete, executable Python script using :mod:`geometor.model` that builds the construction, accompanied by exact symbolic coordinates for every point, line, and circle.

Switch seamlessly between the Synthesis and Code views using the track switcher in the chapter header bar.

----

2. Interactive Vector Plates & Deductive Links
----------------------------------------------

Each construction is accompanied by a publication-grade interactive ``.euclid-graphic`` SVG plate:

* **Bidirectional Highlighting**: Hovering over or clicking diagram labels (*A*, *B*, *C*, *G*, segments, or circles) highlights the element on the plate and cross-references its role in the geometric proof.
* **Golden Section Markers**: Color-coded tick marks (single, double, triple ticks) identify collinear segments in extreme and mean ratio :math:`Q_{\text{long}} / Q_{\text{short}} = \phi + 1 = \phi^2`.
* **Theme Adaptability**: Diagrams render crisply with high-contrast geometry optimized for both dark and parchment themes.

----

3. Full-Text Search with In-Page Highlighting
---------------------------------------------

Search across the entire catalog and API documentation:

* Enter terms into the search bar in the left navigation sidebar.
* Search results highlight matched keywords directly within chapter enunciations and proofs using URL ``?highlight=`` parameters.
* Locate constructions by discoverer (e.g. *Odom*, *Kepler*, *Tran*), theorem type (*sangaku*, *pentagon*), or algebraic field.

----

4. Categories, Tags, Document Types & Collection Views
------------------------------------------------------

Navigate the 45 constructions using rich taxonomy facets:

* **Taxonomy Facets**: Browse by algebraic number field (:math:`\mathbb{Q}(\phi)`, :math:`\mathbb{Q}(\sqrt{2}, \phi)`, :math:`\mathbb{Q}(\sqrt{3}, \phi)`, :math:`\mathbb{Q}(\sqrt{\phi})`), construction type (*compass-only*, *golden-chain*), or discoverer.
* **Collection View Toggles**: Index pages support instant toggling between **Cards**, **Banners**, and **List** layouts to suit your research workflow.

----

5. People, Bibliography & Glossary Tooltips
-------------------------------------------

Rich contextual apparatus is integrated directly into the reading experience:

* **People Tooltips**: Hovering over :person:`Alexander Bogomolny <alexander-bogomolny>`, :person:`Euclid <euclid>`, or contemporary geometers reveals biographical sketches and links to their full profile in :doc:`/constructions/persons`.
* **Citations**: Citations (e.g. :cite:`euclid-elements`) show primary treatise loci and Cut-the-Knot source URLs on hover, linking to :doc:`/constructions/bibliography`.
* **Glossary Terms**: Technical terms like :term:`quadrance <quadrance>`, :term:`golden chain <golden-chain>`, and :term:`Géométrographie <geometrographie>` display definition cards via :doc:`/constructions/glossary`.
* **Master Comparative Table**: Inspect all 45 constructions side-by-side in the :doc:`/constructions/comparative_table`.

----

6. Installation & Setup
-----------------------

Install ``geometor.divine`` from PyPI or editable source:

.. code-block:: bash

   pip install geometor-divine

Or clone and install in development mode:

.. code-block:: bash

   git clone https://github.com/geometor/divine
   cd divine
   pip install -e .

----

7. Python API & Automated Discovery
-----------------------------------

Scan arbitrary geometric models constructed with :mod:`geometor.model` for hidden golden sections and multi-point chains:

.. code-block:: python

   from geometor.model import Model
   from geometor.divine.golden import find_golden_sections_in_model, find_chains_in_model

   # Create or import an exact symbolic model
   model = Model("golden_exploration")
   # ... perform geometric constructions ...

   # Discover all collinear golden sections
   sections = find_golden_sections_in_model(model)
   print(f"Discovered {len(sections)} golden sections")

   # Assemble connected golden chains
   chains = find_chains_in_model(model)
   print(f"Found {len(chains)} maximal golden chains")

----

8. Additional Guides
--------------------

.. toctree::
   :maxdepth: 1

   installation
   getting_started
   analysis/index
