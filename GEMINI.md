# GEOMETOR Divine

A Python library for analyzing geometor.model constructions.

## Overview

The `divine` library provides tools to identify golden sections, harmonic ranges, and other geometric relationships within a `geometor.model` construction. It is used by the Explorer to provide real-time analysis.

## Key Concepts

-   **Golden Section**: A division of a segment into two parts such that the ratio of the whole to the larger part is equal to the ratio of the larger part to the smaller part ($\phi$).
-   **Harmonic Legend**: The study of ranges of points on a line fundamental to projective geometry.
-   **Flow**: The idea that geometry grows effectively like a biological organism, from parents to children.

## Index

-   `divine.py`: Main module containing the core analysis functions.
-   `golden/`: A sub-package for finding and analyzing golden sections.
-   `events.py`: Manages the analysis hook for analysis updates.
-   `chains.py`:  Logic for connecting individual sections into linked chains.
-   `groups.py`:  Aggregating findings into meaningful groups.

## Getting Started

### Installation

```bash
git clone https://github.com/geometor/divine
cd divine
pip install -e .
```

### Running Tests

```bash
pytest
```

### Key Tasks for Contributors

-   **Performance Optimization**: Analysis can be computationally intensive. Look for ways to optimize detection algorithms in `golden/`.
-   **New Patterns**: Implement detection for other geometric ratios or patterns.
