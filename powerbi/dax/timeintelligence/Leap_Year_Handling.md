# Handling Leap Years in DAX

## Description
Leap years introduce an extra day (February 29), which can affect time‑intelligence calculations such as YTD, rolling windows, and comparisons with previous years.  
This file provides reusable DAX patterns to correctly detect and handle leap years.

---

## 1. Detect if a Year Is a Leap Year

```DAX
Is Leap Year =
VAR YearNumber = YEAR ( 'Calendar'[Date] )
RETURN
IF (
    MOD ( YearNumber, 400 ) = 0
        || ( MOD ( YearNumber, 4 ) = 0 && MOD ( YearNumber, 100 ) <> 0 ),
    TRUE,
    FALSE
)
```

### Notes
- This follows the official Gregorian calendar rules.
- You can store this as a calculated column in your Date table.

---

## 2. Flag February 29

```DAX
Is Feb 29 =
IF (
    MONTH ( 'Calendar'[Date] ) = 2
        && DAY ( 'Calendar'[Date] ) = 29,
    TRUE,
    FALSE
)
```

### Notes
- Useful when you want to exclude Feb 29 from comparisons.
- Some businesses prefer to map Feb 29 to Feb 28 for YoY analysis.

---

## 3. Adjust Same Period Last Year (SPLY) for Leap Years

```DAX
Sales SPLY (Leap Safe) =
VAR CurrentDate = MAX ( 'Calendar'[Date] )
VAR PriorYearDate =
    DATE ( YEAR ( CurrentDate ) - 1, MONTH ( CurrentDate ), DAY ( CurrentDate ) )
VAR Adjust