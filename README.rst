GEOMETOR • divine
==================

.. image:: https://img.shields.io/pypi/v/geometor-divine.svg
   :target: https://pypi.python.org/pypi/geometor-divine
.. image:: https://img.shields.io/github/license/geometor/divine.svg
   :target: https://github.com/geometor/divine/blob/main/LICENSE

**Seeking harmony in the noise.**

Overview
--------

``geometor.divine`` is the analytical engine of the GEOMETOR ecosystem. While ``geometor.model`` builds the geometry, ``divine`` observes it, searching for hidden patterns, proportions, and relationships.

Its primary mission is to identify instances of the **Divine Proportion** (the Golden Ratio, $\phi \approx 1.618$) and other harmonic structures that emerge from simple constructions.

Key Features
------------

- **Golden Section Analysis**: Automatically detects segments cut in the golden ratio.
- **Harmonic Ranges**: Identifies sets of collinear points that form harmonic ranges.
- **Pattern Recognition**: Groups related elements into chains and families, revealing the organic growth of the construction.
- **Integration**: Designed to plug directly into ``geometor.model`` and stream results to ``geometor.explorer``.

Installation
------------

.. code-block:: bash

    pip install geometor-divine

Usage
-----

``divine`` works by analyzing a ``Model`` instance.

.. code-block:: python

    from geometor.model import Model
    from geometor.divine import analyze_model

    # Load or create a model
    model = Model("pentagon")
    # ... (construction logic) ...
    
    # Run analysis
    analysis = analyze_model(model)

    # Inspect results
    print(f"Golden Sections found: {len(analysis.golden_sections)}")
    for section in analysis.golden_sections:
        print(section)

Resources
---------

- **Source Code**: https://github.com/geometor/divine
- **Issues**: https://github.com/geometor/divine/issues

Related Projects
----------------

- `GEOMETOR Model <https://github.com/geometor/model>`_: The symbolic engine being analyzed.
- `GEOMETOR Explorer <https://github.com/geometor/explorer>`_: The interface for viewing the analysis.
