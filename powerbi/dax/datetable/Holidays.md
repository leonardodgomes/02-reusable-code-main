# Holiday Table (Dynamic)

## Description
Generates a holiday table for a given date range. Includes fixed-date holidays and dynamic ones (e.g., Easter). You can customize for your country.

## DAX
```DAX
Holidays =
VAR MinDate =
    CALCULATE ( MIN ( 'Calendar'[Date] ), REMOVEFILTERS ( 'Calendar' ) )
VAR MaxDate =
    CALCULATE ( MAX ( 'Calendar'[Date] ), REMOVEFILTERS ( 'Calendar' ) )
VAR BaseCalendar =
    CALENDAR ( MinDate, MaxDate )
RETURN
FILTER (
    ADDCOLUMNS (
        BaseCalendar,
        "Holiday Name",
            SWITCH (
                TRUE (),
                FORMAT ( [Date], "MM-DD" ) = "01-01", "New Year's Day",
                FORMAT ( [Date], "MM-DD" ) = "12-25", "Christmas",
                FORMAT ( [Date], "MM-DD" ) = "04-25", "Freedom Day (PT)",
                FORMAT ( [Date], "MM-DD" ) = "06-10", "Portugal Day",
                BLANK ()
            )
    ),
    NOT ISBLANK ( [Holiday Name] )
)
```

## Notes
- Add or remove holidays depending on your country.
- You can join this table to your Calendar table using the Date column.
