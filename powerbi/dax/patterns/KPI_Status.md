# KPI Status Logic

## Description
Generates a KPI status label based on performance vs. target.

## DAX
```DAX
KPI Status =
SWITCH (
    TRUE (),
    [Actual] >= [Target], "On Track",
    [Actual] >= [Target] * 0.9, "At Risk",
    "Off Track"
)
```

## Notes
- Adjust thresholds depending on business rules.
- Can be paired with icons or conditional formatting.
