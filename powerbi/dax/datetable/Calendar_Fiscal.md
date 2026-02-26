# Fiscal Calendar Table

## Description
A calendar table with fiscal year logic. This example uses a fiscal year starting in July (FY begins on July 1). Adjust the start month as needed.

## DAX
```DAX
Calendar Fiscal =
VAR StartMonth = 7   -- Fiscal year starts in July
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
    "Fiscal Year",
        YEAR ( EDATE ( [Date], 12 - StartMonth ) ),
    "Fiscal Quarter",
        "Q" &
        FORMAT ( ROUNDUP ( ( MONTH ( [Date] ) - StartMonth + 12 ) / 3, 0 ), "0" )
)
```

## Notes
- Change `StartMonth` to match your organization’s fiscal year.
- Fiscal year logic uses EDATE to shift the calendar.
