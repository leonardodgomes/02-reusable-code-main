# TopN With "Others" Group

## Description
Shows the top N items and groups the remaining ones into an “Others” category. Ideal for pie charts and bar charts.

## DAX
```DAX
Category Group =
VAR TopNValue = 5
VAR TopCustomers =
    TOPN ( TopNValue, SUMMARIZE ( Customers, Customers[Customer Name], "Sales", [Total Sales] ), [Sales], DESC )
RETURN
IF (
    Customers[Customer Name] IN TopCustomers,
    Customers[Customer Name],
    "Others"
)
```

## Notes
- Change `TopNValue` to any number.
- Works best when used in a calculated column or disconnected table.
