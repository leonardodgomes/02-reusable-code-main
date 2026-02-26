# CROSSFILTER Pattern

## Description
Overrides the default relationship direction between two tables.  
Useful when you need to force single‑direction or bi‑directional filtering for a specific measure.

## DAX
```DAX
Sales with Single Direction =
CALCULATE (
    [Total Sales],
    CROSSFILTER ( Customers[CustomerID], Sales[CustomerID], ONEWAY )
)
```

## Notes
- Options: `BOTH`, `ONEWAY`, `NONE`.
- Use carefully — can change filter propagation.
- Great for debugging ambiguous relationships.
