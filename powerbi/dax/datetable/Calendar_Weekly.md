# Weekly Calendar Table

## Description
A calendar table focused on weekly reporting. Includes ISO week number and ISO year, which are essential for correct weekly time intelligence.

## DAX
```DAX
Calendar Weekly =
VAR MinDate =
    CALCULATE ( MIN ( 'Sales'[OrderDate] ), REMOVEFILTERS ( 'Sales' ) )
VAR MaxDate =
    CALCULATE ( MAX ( 'Sales'[OrderDate] ), REMOVEFILTERS ( 'Sales' ) )
RETURN
ADDCOLUMNS (
    CALENDAR ( MinDate, MaxDate ),
    "ISO Year", YEAR ( [Date] - WEEKDAY ( [Date], 2 ) + 4 ),
    "ISO Week", WEEKNUM ( [Date], 2 ),
    "Week Start", [Date] - WEEKDAY ( [Date], 2 ) + 1,
    "Week End", [Date] - WEEKDAY ( [Date], 2 ) + 7
)
```

## Notes
- ISO week logic ensures correct week grouping across year boundaries.
- Useful for operational dashboards and weekly KPIs.
