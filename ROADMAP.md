# GEOMETOR Divine: Development Roadmap

## Core Objective: Real-Time Geometric Analysis

The primary goal is to shift `divine` from a batch-processing tool that analyzes a complete model to a real-time analysis engine. The analysis should be triggered automatically whenever a new point is added to the model, providing immediate feedback on the geometric relationships it creates.

## Key Initiatives

### 1. Event-Driven Analysis Hook (Ready for Implementation)

-   **Status:** The `geometor.model` library now includes a `point_added` event trigger.
-   **Next Step:** The `divine` library needs to implement a listener function that can be registered with the `model`'s event system. This function will trigger the incremental analysis logic.

### 2. Analysis Visualization in UI

-   **Objective:** Integrate the existing grouping, chaining, and range-finding logic into the event-driven workflow and visualize these relationships in the `explorer` UI.
-   **Strategy:** Create a central analysis orchestrator that runs after a new golden section is found. The results will be pushed to the frontend via a new SSE event and displayed in new, interactive tables that allow for highlighting elements in the SVG.
-   **Plan:** See the detailed implementation plan in `ANALYSIS_VISUALIZATION.md`.

### 3. Incremental Analysis Logic

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

### 4. Storing and Surfacing Results

-   The analysis results (e.g., a list of golden sections, harmonic ranges) need to be stored in a structured way, likely associated with the `model` instance.
-   The results should be easily serializable so they can be sent to the `explorer` frontend via the API.

### 5. API for Explorer Integration

-   The existing `/api/model` endpoint in `explorer` should be updated.
-   When the model is requested, the JSON response should include not only the geometric elements but also the latest analysis results from `divine`. This ensures that every construction action that creates a point also returns the immediate analysis of that point's impact.
