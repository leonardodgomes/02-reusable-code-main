# Dynamic Segmentation

## Description
Creates dynamic performance segments (e.g., High, Medium, Low) based on measure values.

## DAX
```DAX
Sales Segment =
SWITCH (
    TRUE (),
    [Total Sales] >= 100000, "High",
    [Total Sales] >= 50000, "Medium",
    "Low"
)
```

## Notes
- Thresholds can be dynamic by replacing numbers with measures.
- Useful for customer tiers, product bands, or employee performance.
