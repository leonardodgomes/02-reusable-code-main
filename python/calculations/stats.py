"""
stats.py
A small collection of statistical helper functions.

Each function includes a clear explanation of the underlying math,
so the module is easy to understand and maintain.
"""

import math


def mean(data):
    """
    Calculate the arithmetic mean (average) of a list of numbers.

    Explanation:
    The mean is the sum of all values divided by the number of values.
    Formula:
        mean = (x1 + x2 + ... + xn) / n

    Example:
        mean([1, 2, 3]) → 2.0
    """
    return sum(data) / len(data)


def median(data):
    """
    Calculate the median of a list of numbers.

    Explanation:
    The median is the middle value when the data is sorted.
    - If the list has an odd number of elements → return the middle one.
    - If it has an even number → return the average of the two middle values.

    Example:
        median([10, 20, 30, 40]) → (20 + 30) / 2 = 25.0
    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2

    if n % 2 == 1:
        return sorted_data[mid]
    else:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2


def variance(data):
    """
    Calculate the variance of a list of numbers.

    Explanation:
    Variance measures how spread out the numbers are.
    It is the average of the squared differences from the mean.

    Formula:
        variance = Σ (xi - mean)^2 / n

    Example:
        variance([10, 20, 30, 40])
    """
    m = mean(data)
    squared_diffs = [(x - m) ** 2 for x in data]
    return sum(squared_diffs) / len(data)


def std_dev(data):
    """
    Calculate the standard deviation of a list of numbers.

    Explanation:
    Standard deviation is the square root of the variance.
    It tells you how much the values typically deviate from the mean.

    Formula:
        std_dev = sqrt(variance)

    Example:
        std_dev([10, 20, 30, 40])
    """
    return math.sqrt(variance(data))


def percentile(data, p):
    """
    Calculate the p-th percentile of a list of numbers.

    Explanation:
    The percentile tells you the value below which p% of the data falls.
    We use linear interpolation between data points.

    Steps:
    1. Sort the data.
    2. Compute the index: i = p/100 * (n - 1)
    3. If i is an integer → return that element.
    4. Otherwise → interpolate between floor(i) and ceil(i).

    Example:
        percentile([10, 20, 30, 40], 50) → 25.0
    """
    sorted_data = sorted(data)
    n = len(sorted_data)

    index = p / 100 * (n - 1)
    lower = int(math.floor(index))
    upper = int(math.ceil(index))

    if lower == upper:
        return sorted_data[lower]

    # Linear interpolation
    weight = index - lower
    return sorted_data[lower] * (1 - weight) + sorted_data[upper] * weight
