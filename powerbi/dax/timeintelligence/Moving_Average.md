# Moving Average (7‑Day Example)

## Description
Calculates a moving average over a rolling window. This example uses 7 days, but you can adjust the window size.

## DAX
```DAX
Sales Moving Average 7D =
VAR Window = 7
RETURN
AVERAGEX (
    DATESINPERIOD (
        'Calendar'[Date],
        MAX ( 'Calendar'[Date] ),
        -Window,
        DAY
    ),
    [Total Sales]
)
```

## Notes
- Change `Window` to 30 for a 30‑day average, etc.
- Smooths out volatility in daily data.
