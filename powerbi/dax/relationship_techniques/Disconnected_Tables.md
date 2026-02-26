# Disconnected Tables Pattern

## Description
Uses a disconnected table (no relationship in the model) to drive dynamic calculations.  
Common for parameter tables, TopN selectors, scenario analysis, and custom grouping.

## DAX (Example: Dynamic TopN)
```DAX
TopN Sales =
VAR NValue =
    SELECTEDVALUE ( TopNSelector[N] )
RETURN
CALCULATE (
    [Total Sales],
    TOPN (
        NValue,
        ALL ( Products ),
        [Total Sales],
        DESC
    )
)
```

## Notes
- Disconnected tables are powerful for user‑controlled logic.
- Use `SELECTEDVALUE` to read the user’s selection.
- Combine with slicers for dynamic behavior.
