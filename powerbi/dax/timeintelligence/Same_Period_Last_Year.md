# Same Period Last Year (SPLY)

## Description
Compares the selected period with the same period in the previous year.

## DAX
```DAX
Total Sales SPLY =
CALCULATE (
    [Total Sales],
    SAMEPERIODLASTYEAR ( 'Calendar'[Date] )
)
```

## Notes
- Works for days, months, quarters, and years.
- Requires a continuous Date table with no gaps.
