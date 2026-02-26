# Dynamic Titles

## Description
Creates report titles that automatically update based on slicers and filters.

## DAX
```DAX
Dynamic Title =
"Sales Report for " &
IF (
    ISFILTERED ( Regions[Region] ),
    CONCATENATEX ( VALUES ( Regions[Region] ), Regions[Region], ", " ),
    "All Regions"
)
```

## Notes
- Use `CONCATENATEX` to list multiple selected values.
- Great for improving report clarity.
