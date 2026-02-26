# Rolling 3 Months

## Description
Calculates the total for the last 3 months from the selected date.

## DAX
```DAX
Total Sales Rolling 3M =
CALCULATE (
    [Total Sales],
    DATESINPERIOD (
        'Calendar'[Date],
        MAX ( 'Calendar'[Date] ),
        -3,
        MONTH
    )
)
```

## Notes
- Ideal for short‑term trend analysis.
- Works with any measure.
