def generate_quality_report(results: dict) -> str:
    """
    Converts validation results into a human-readable report.
    """
    lines = ["DATA QUALITY REPORT", "-" * 40]
    for check, result in results.items():
        status = "PASS" if result else "FAIL"
        lines.append(f"{check}: {status}")
    return "\n".join(lines)


