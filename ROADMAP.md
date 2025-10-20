# GEOMETOR Divine: Development Roadmap

## Core Objective: Real-Time Geometric Analysis

The primary goal is to shift `divine` from a batch-processing tool that analyzes a complete model to a real-time analysis engine. The analysis should be triggered automatically whenever a new point is added to the model, providing immediate feedback on the geometric relationships it creates.

## Key Initiatives

### 1. Event-Driven Analysis Hook (Ready for Implementation)

-   **Status:** The `geometor.model` library now includes a `point_added` event trigger.
-   **Next Step:** The `divine` library needs to implement a listener function that can be registered with the `model`'s event system. This function will trigger the incremental analysis logic.

### 2. Storing and Surfacing Results

-   The analysis results (e.g., a list of golden sections, harmonic ranges) need to be stored in a structured way, likely associated with the `model` instance.
-   The results should be easily serializable so they can be sent to the `explorer` frontend via the API.

### 3. API for Explorer Integration

-   The existing `/api/model` endpoint in `explorer` should be updated.
-   When the model is requested, the JSON response should include not only the geometric elements but also the latest analysis results from `divine`. This ensures that every construction action that creates a point also returns the immediate analysis of that point's impact.