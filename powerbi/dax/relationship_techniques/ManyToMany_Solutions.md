# Many‑to‑Many Relationship Solutions

## Description
Handles many‑to‑many scenarios using bridge tables or DAX logic.  
Useful when a fact table relates to multiple dimension values (e.g., customers with multiple segments).

## DAX (Bridge Table Pattern)
```DAX
Total Sales by Segment =
CALCULATE (
    [Total Sales],
    TREATAS ( VALUES ( SegmentBridge[Segment] ), Segments[Segment] )
)
```

## Notes
- `TREATAS` applies filter values from one table to another.
- Works even when no physical relationship exists.
- Ideal for multi‑select attributes (e.g., tags, categories).
