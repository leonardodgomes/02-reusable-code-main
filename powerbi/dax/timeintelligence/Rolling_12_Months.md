# Rolling 12 Months

## Description
Calculates the total for the last 12 months from the selected date.

## DAX
```DAX
Total Sales Rolling 12M =
CALCULATE (
    [Total Sales],
    DATESINPERIOD (
        'Calendar'[Date],
        MAX ( 'Calendar'[Date] ),
        -12,
        MONTH
    )
)
```

## Notes
- Uses `DATESINPERIOD` for flexible rolling windows.
- Works even when months have different day counts.
