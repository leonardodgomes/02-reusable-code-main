"""
time_series.py
A collection of time-series analysis utilities.

These functions are commonly used in finance, forecasting,
monitoring systems, and data analytics.
"""

import math


def moving_average(data, window):
    """
    Calculate the simple moving average (SMA).

    Explanation:
    SMA smooths short-term fluctuations by averaging the last N values.
    Formula:
        SMA_t = (x_{t-N+1} + ... + x_t) / N

    Example:
        moving_average([1,2,3,4,5], 3) → [None, None, 2.0, 3.0, 4.0]
    """
    result = []
    for i in range(len(data)):
        if i < window - 1:
            result.append(None)
        else:
            window_slice = data[i - window + 1 : i + 1]
            result.append(sum(window_slice) / window)
    return result


def exponential_moving_average(data, alpha):
    """
    Calculate the exponential moving average (EMA).

    Explanation:
    EMA gives more weight to recent values.
    Formula:
        EMA_t = alpha * x_t + (1 - alpha) * EMA_{t-1}

    Example:
        exponential_moving_average([1,2,3,4], 0.5)
    """
    ema = []
    prev = data[0]
    ema.append(prev)

    for x in data[1:]:
        prev = alpha * x + (1 - alpha) * prev
        ema.append(prev)

    return ema


def rate_of_change(data, periods=1):
    """
    Calculate the Rate of Change (ROC).

    Explanation:
    ROC measures the percentage change over N periods.
    Formula:
        ROC_t = (x_t - x_{t-N}) / x_{t-N}

    Example:
        rate_of_change([10, 12, 15], 1) → [None, 0.2, 0.25]
    """
    result = []
    for i in range(len(data)):
        if i < periods:
            result.append(None)
        else:
            result.append((data[i] - data[i - periods]) / data[i - periods])
    return result


def cumulative_sum(data):
    """
    Calculate the cumulative sum (CUSUM).

    Explanation:
    CUSUM is used to track accumulated totals over time.

    Example:
        cumulative_sum([1,2,3]) → [1, 3, 6]
    """
    total = 0
    result = []
    for x in data:
        total += x
        result.append(total)
    return result


def rolling_volatility(data, window):
    """
    Calculate rolling volatility (rolling standard deviation).

    Explanation:
    Used in finance and monitoring to measure short-term risk.

    Example:
        rolling_volatility([1,2,3,4,5], 3)
    """
    result = []
    for i in range(len(data)):
        if i < window - 1:
            result.append(None)
        else:
            window_slice = data[i - window + 1 : i + 1]
            mean_val = sum(window_slice) / window
            squared = [(x - mean_val) ** 2 for x in window_slice]
            result.append(math.sqrt(sum(squared) / window))
    return result
