# Virtual Tables

## Description
Example of using virtual tables for advanced calculations without creating physical tables.

## DAX
```DAX
Top Product Sales =
VAR vTable =
    TOPN (
        1,
        SUMMARIZE ( Products, Products[Product Name], "Sales", [Total Sales] ),
        [Sales],
        DESC
    )
RETURN
MAXX ( vTable, [Sales] )
```

## Notes
- Virtual tables exist only during calculation.
- Useful for complex aggregations and filtering logic.
