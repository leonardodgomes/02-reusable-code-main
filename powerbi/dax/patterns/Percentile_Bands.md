# Percentile Bands

## Description
Assigns percentile-based groups (e.g., Top 10%, Bottom 25%). Useful for HR analytics, sales performance, and distribution analysis.

## DAX
```DAX
Percentile Band =
VAR Pct =
    PERCENTILEX.INC (
        ALL ( Customers ),
        [Total Sales],
        0.9
    )
RETURN
SWITCH (
    TRUE (),
    [Total Sales] >= Pct, "Top 10%",
    [Total Sales] >= Pct * 0.75, "Top 25%",
    [Total Sales] >= Pct * 0.5, "Top 50%",
    "Bottom 50%"
)
```

## Notes
- Adjust percentile thresholds as needed.
- Works best with large datasets.
