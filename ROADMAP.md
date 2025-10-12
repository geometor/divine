# GEOMETOR Divine: Development Roadmap

## Core Objective: Real-Time Geometric Analysis

The primary goal is to shift `divine` from a batch-processing tool that analyzes a complete model to a real-time analysis engine. The analysis should be triggered automatically whenever a new point is added to the model, providing immediate feedback on the geometric relationships it creates.

## Key Initiatives

### 1. Event-Driven Analysis Hook

-   **Dependency:** This requires a mechanism in the `geometor.model` library to announce when a new element, particularly a point, is created.
-   **Implementation:** A callback or observer pattern should be implemented in the `model`. When a point is added (either directly or through intersection), the `model` will trigger a registered analysis function from `divine`.

### 2. Incremental Analysis Logic

When a new point `P_new` is created, the following analysis should occur instantly:

-   **Line Section Analysis:**
    1.  Identify all lines (`L1`, `L2`, ...) that `P_new` lies on.
    2.  For each line `L`, retrieve all other existing points on that line.
    3.  Generate all new three-point `Section` combinations that include `P_new`.
    4.  Run the golden section analysis on only these newly created sections.

-   **Harmonic Range Analysis:**
    1.  For each affected line `L`, re-calculate the four-point harmonic ranges.
    2.  This avoids re-calculating for lines not affected by the new point, ensuring efficiency.

-   **Circle Section Analysis:**
    1.  Similarly, identify all circles (`C1`, `C2`, ...) that `P_new` lies on.
    2.  Analyze the new arcs and chords formed by `P_new` in relation to other points on the circle.

### 3. Storing and Surfacing Results

-   The analysis results (e.g., a list of golden sections, harmonic ranges) need to be stored in a structured way, likely associated with the `model` instance.
-   The results should be easily serializable so they can be sent to the `explorer` frontend via the API.

### 4. API for Explorer Integration

-   The existing `/api/model` endpoint in `explorer` should be updated.
-   When the model is requested, the JSON response should include not only the geometric elements but also the latest analysis results from `divine`. This ensures that every construction action that creates a point also returns the immediate analysis of that point's impact.
