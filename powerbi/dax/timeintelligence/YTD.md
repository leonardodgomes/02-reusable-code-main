# Year‑to‑Date (YTD)

## Description
Calculates cumulative values from the start of the year up to the selected date.

## DAX
```DAX
Total Sales YTD =
CALCULATE (
    [Total Sales],
    DATESYTD ( 'Calendar'[Date] )
)
```

## Notes
- Requires a proper, continuous Date table.
- Respects filters (e.g., region, product).
