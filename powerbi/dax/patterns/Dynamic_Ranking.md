# Dynamic Ranking

## Description
Creates a ranking that responds to slicers and filters. Useful for ranking customers, products, employees, or any entity dynamically.

## DAX
```DAX
Rank Customer =
RANKX (
    ALLSELECTED ( Customers[Customer Name] ),
    [Total Sales],
    ,
    DESC,
    DENSE
)
```

## Notes
- Uses `ALLSELECTED` so ranking respects slicers.
- Replace `[Total Sales]` with any measure.
- Use `DENSE` to avoid gaps in ranking.
