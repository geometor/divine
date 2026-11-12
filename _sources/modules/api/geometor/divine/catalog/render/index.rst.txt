geometor.divine.catalog.render
==============================

.. py:module:: geometor.divine.catalog.render

.. autoapi-nested-parse::

   Publication-grade interactive ``.euclid-graphic`` SVG renderer for the Golden Ratio Catalog.

   Generates crisp, theme-adaptive SVGs directly from exact symbolic
   :class:`~geometor.model.Model` instances and :class:`~geometor.divine.catalog.schema.GoldenCertificate`
   certificates. Conforms simultaneously to:

   1. **Standalone SVG viewing** (embedded ``<style>`` with ``prefers-color-scheme``
      dark/light palettes, ``<defs>`` tick markers ``#geom-tick-1..3``, and luminous
      gold highlighting), and
   2. **PHOTON Publish Book Codex interactive figures** (``svg.euclid-graphic``,
      ``#elements``, ``#graphics``, ``#highlights``, ``#points``, ``#labels``,
      3-vertex ``<path>`` segments, ``data-ref``, and ``data-aliases`` consumed by
      ``geometor_interactive.js``).



Attributes
----------

.. autoapisummary::

   geometor.divine.catalog.render.EMBEDDED_SVG_STYLE


Functions
---------

.. autoapisummary::

   geometor.divine.catalog.render.render_catalog_svg
   geometor.divine.catalog.render.export_catalog_svg


Module Contents
---------------

.. py:data:: EMBEDDED_SVG_STYLE
   :type:  str
   :value: ''


.. py:function:: render_catalog_svg(model: geometor.model.Model, cert: geometor.divine.catalog.schema.GoldenCertificate | None = None, *, graphic_id: str = 'g1', title: str = 'Golden Ratio Construction', width: int = 680, height: int = 480, margin: float = 42.0, bbox: tuple[float, float, float, float] | None = None, include_guides: bool = False) -> str

   Render ``model`` and optional ``cert`` into an interactive ``.euclid-graphic`` SVG.


.. py:function:: export_catalog_svg(model: geometor.model.Model, output_path: str | pathlib.Path, cert: geometor.divine.catalog.schema.GoldenCertificate | None = None, *, graphic_id: str = 'g1', title: str = 'Golden Ratio Construction', width: int = 680, height: int = 480, margin: float = 42.0, bbox: tuple[float, float, float, float] | None = None, include_guides: bool = False) -> pathlib.Path

   Write an interactive ``.euclid-graphic`` SVG for ``model`` to ``output_path``.


