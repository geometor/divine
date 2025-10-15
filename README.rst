

**GEOMETOR • divine** is a Python library for analyzing `geometor.model` constructions to identify golden sections, harmonic ranges, and other geometric relationships.

Overview
--------

The `divine` library is a key component of the GEOMETOR ecosystem. It provides the analytical engine for discovering significant geometric properties within a model created using the `geometor.model` library. The results of this analysis are then displayed in the `geometor.explorer` web UI.

The primary focus of the library is the identification of the golden ratio (phi) in its various forms.

Key Features
------------

- **Golden Section Analysis:** Identifies points that divide segments into the golden ratio.
- **Harmonic Range Analysis:** Analyzes harmonic ranges within lines.
- **Chain and Group Analysis:** Finds chains of connected golden sections and groups them by various criteria.

Usage
-----

The `divine` library is typically used in conjunction with `geometor.model` and `geometor.explorer`. The `explorer` application automatically calls the `divine` analysis functions when a model is updated.
