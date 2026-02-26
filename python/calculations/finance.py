"""
finance.py
A collection of financial calculation utilities.

Each function includes a clear explanation of the underlying formula
and real-world use cases.
"""

import math


def compound_interest(principal, rate, periods):
    """
    Calculate compound interest.

    Explanation:
    Compound interest grows the principal by applying interest repeatedly.
    Formula:
        A = P * (1 + r)^n

    Parameters:
        principal (float): Initial amount of money.
        rate (float): Interest rate per period (e.g., 0.05 for 5%).
        periods (int): Number of compounding periods.

    Returns:
        float: Final amount after compounding.

    Example:
        compound_interest(1000, 0.05, 10) → 1628.89
    """
    return principal * (1 + rate) ** periods


def present_value(future_value, rate, periods):
    """
    Calculate the present value of a future amount.

    Explanation:
    Present value tells you how much a future amount is worth today.
    Formula:
        PV = FV / (1 + r)^n

    Example:
        present_value(1000, 0.05, 10)
    """
    return future_value / ((1 + rate) ** periods)


def net_present_value(rate, cashflows):
    """
    Calculate Net Present Value (NPV).

    Explanation:
    NPV discounts each cashflow back to today and sums them.
    Formula:
        NPV = Σ (Ct / (1 + r)^t)

    Parameters:
        rate (float): Discount rate.
        cashflows (list): Cashflows where index = time period.

    Example:
        net_present_value(0.1, [-1000, 300, 400, 500])
    """
    return sum(cf / ((1 + rate) ** t) for t, cf in enumerate(cashflows))


def internal_rate_of_return(cashflows, guess=0.1, tolerance=1e-6, max_iter=1000):
    """
    Calculate Internal Rate of Return (IRR) using Newton's method.

    Explanation:
    IRR is the discount rate that makes NPV = 0.
    There is no closed-form formula, so we solve it iteratively.

    Example:
        internal_rate_of_return([-1000, 300, 400, 500])
    """
    rate = guess

    for _ in range(max_iter):
        npv = sum(cf / ((1 + rate) ** t) for t, cf in enumerate(cashflows))
        d_npv = sum(-t * cf / ((1 + rate) ** (t + 1)) for t, cf in enumerate(cashflows))

        if abs(npv) < tolerance:
            return rate

        rate -= npv / d_npv

    return rate  # best estimate


def return_rate(initial, final):
    """
    Calculate the simple return rate.

    Explanation:
    Measures percentage growth from initial to final value.
    Formula:
        return = (final - initial) / initial

    Example:
        return_rate(100, 120) → 0.20 (20%)
    """
    return (final - initial) / initial


def annualized_return(initial, final, years):
    """
    Calculate annualized return (CAGR).

    Explanation:
    CAGR shows the average yearly growth rate.
    Formula:
        CAGR = (final / initial)^(1/years) - 1

    Example:
        annualized_return(1000, 2000, 5)
    """
    return (final / initial) ** (1 / years) - 1


def volatility(returns):
    """
    Calculate volatility (standard deviation of returns).

    Explanation:
    Volatility measures how much returns fluctuate.
    Used heavily in finance and risk management.

    Example:
        volatility([0.01, -0.02, 0.03])
    """
    mean_r = sum(returns) / len(returns)
    squared_diffs = [(r - mean_r) ** 2 for r in returns]
    return math.sqrt(sum(squared_diffs) / len(returns))


def sharpe_ratio(returns, risk_free_rate):
    """
    Calculate the Sharpe Ratio.

    Explanation:
    Measures risk-adjusted return.
    Formula:
        Sharpe = (mean(returns) - risk_free_rate) / volatility

    Example:
        sharpe_ratio([0.01, 0.02, 0.015], 0.005)
    """
    mean_r = sum(returns) / len(returns)
    vol = volatility(returns)
    return (mean_r - risk_free_rate) / vol if vol != 0 else float("inf")
