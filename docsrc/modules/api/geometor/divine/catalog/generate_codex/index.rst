geometor.divine.catalog.generate_codex
======================================

.. py:module:: geometor.divine.catalog.generate_codex

.. autoapi-nested-parse::

   Deterministic generator for the Golden Ratio Catalog Book Codex & JSON resources.

   Builds and certifies all 45 symbolic constructions in :data:`~geometor.divine.catalog.CATALOG`,
   exports publication-grade interactive ``.euclid-graphic`` SVGs, writes machine-readable
   registries under ``resources/``, and emits the complete multi-track Sphinx Book Codex
   under ``docsrc/constructions/``.



Attributes
----------

.. autoapisummary::

   geometor.divine.catalog.generate_codex.summary


Functions
---------

.. autoapisummary::

   geometor.divine.catalog.generate_codex.generate_all


Module Contents
---------------

.. py:function:: generate_all(repo_root: pathlib.Path | None = None) -> dict[str, Any]

   Generate all JSON apparatus files, SVGs, and Book Codex RST pages.


.. py:data:: summary

