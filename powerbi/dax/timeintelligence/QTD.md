# Quarter‑to‑Date (QTD)

## Description
Calculates cumulative values from the start of the quarter up to the selected date.

## DAX
```DAX
Total Sales QTD =
CALCULATE (
    [Total Sales],
    DATESQTD ( 'Calendar'[Date] )
)
```

## Notes
- Quarter definitions come from your Date table.
- Works with fiscal calendars if your Date table includes fiscal quarters.
