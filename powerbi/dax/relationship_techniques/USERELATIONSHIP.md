# USERELATIONSHIP Pattern

## Description
Activates an inactive relationship in the data model for a specific calculation.  
Useful when you have multiple date fields (Order Date, Ship Date, Due Date) or multiple relationship paths.

## DAX
```DAX
Total Sales by Ship Date =
CALCULATE (
    [Total Sales],
    USERELATIONSHIP ( 'Calendar'[Date], Sales[ShipDate] )
)
```

## Notes
- Does NOT change the model — only affects this calculation.
- Perfect for scenarios with multiple date roles.
- You can activate only **one** inactive relationship per