# Month‑to‑Date (MTD)

## Description
Calculates cumulative values from the start of the month up to the selected date.

## DAX
```DAX
Total Sales MTD =
CALCULATE (
    [Total Sales],
    DATESMTD ( 'Calendar'[Date] )
)
```

## Notes
- Works best with daily granularity.
- Automatically resets each month.
