# Full Calendar Table

## Description
A complete, reusable calendar table that automatically expands based on the minimum and maximum dates in your fact table. Includes year, quarter, month, week, and day attributes.

## DAX
```DAX
Calendar =
VAR MinDate =
    CALCULATE ( MIN ( 'Sales'[OrderDate] ), REMOVEFILTERS ( 'Sales' ) )
VAR MaxDate =
    CALCULATE ( MAX ( 'Sales'[OrderDate] ), REMOVEFILTERS ( 'Sales' ) )
RETURN
ADDCOLUMNS (
    CALENDAR ( MinDate, MaxDate ),
    "Year", YEAR ( [Date] ),
    "Month Number", MONTH ( [Date] ),
    "Month Name", FORMAT ( [Date], "MMMM" ),
    "Month Short", FORMAT ( [Date], "MMM" ),
    "Quarter", "Q" & FORMAT ( [Date], "Q" ),
    "Week Number", WEEKNUM ( [Date], 2 ),
    "Day", DAY ( [Date] ),
    "Day Name", FORMAT ( [Date], "DDDD" ),
    "Day Short", FORMAT ( [Date], "DDD" )
)
```

## Notes
- Uses ISO week numbering (WEEKNUM with return type 2).
- Works with any fact table — just replace `'Sales'[OrderDate]`.
- Add fiscal logic if needed.
