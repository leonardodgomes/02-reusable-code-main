"""
financial_generator.py
Synthetic financial data generators for testing and simulation.

Includes:
- generate_stock_prices()
- generate_crypto_prices()
- generate_transactions()
- generate_portfolio()
- generate_credit_card_purchases()
- generate_invoices()
"""

import random
import datetime
import pandas as pd
from faker import Faker

fake = Faker()


def generate_stock_prices(days=30, start_price=100, volatility=2):
    """
    Generate a synthetic stock price time series using a random walk.
    """
    prices = [start_price]

    for _ in range(days - 1):
        change = random.uniform(-volatility, volatility)
        prices.append(max(1, prices[-1] + change))

    dates = [
        (datetime.date.today() - datetime.timedelta(days=i)).isoformat()
        for i in range(days)
    ]
    dates.reverse()

    return pd.DataFrame({"date": dates, "price": prices})


def generate_crypto_prices(hours=48, start_price=20000, volatility=150):
    """
    Generate synthetic crypto price data with higher volatility.
    """
    prices = [start_price]

    for _ in range(hours - 1):
        change = random.uniform(-volatility, volatility)
        prices.append(max(1, prices[-1] + change))

    timestamps = [
        (datetime.datetime.now() - datetime.timedelta(hours=i)).isoformat()
        for i in range(hours)
    ]
    timestamps.reverse()

    return pd.DataFrame({"timestamp": timestamps, "price": prices})


def generate_transactions(n=50):
    """
    Generate synthetic bank transactions.
    """
    transactions = []

    for _ in range(n):
        amount = round(random.uniform(-500, 2000), 2)
        transactions.append({
            "date": fake.date_between(start_date="-3m", end_date="today").isoformat(),
            "description": fake.company(),
            "amount": amount,
            "type": "credit" if amount > 0 else "debit",
            "balance_after": round(random.uniform(1000, 5000), 2)
        })

    return transactions


def generate_portfolio(n=5):
    """
    Generate a synthetic investment portfolio.
    """
    assets = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NVDA"]
    portfolio = []

    for _ in range(n):
        ticker = random.choice(assets)
        portfolio.append({
            "ticker": ticker,
            "shares": random.randint(1, 100),
            "avg_price": round(random.uniform(50, 3000), 2),
            "current_price": round(random.uniform(50, 3000), 2)
        })

    return portfolio


def generate_credit_card_purchases(n=30):
    """
    Generate synthetic credit card purchase records.
    """
    purchases = []

    for _ in range(n):
        amount = round(random.uniform(5, 500), 2)
        purchases.append({
            "timestamp": fake.date_time_between(start_date="-2m", end_date="now").isoformat(),
            "merchant": fake.company(),
            "category": random.choice(["Food", "Travel", "Electronics", "Clothing", "Online"]),
            "amount": amount,
            "currency": "USD"
        })

    return purchases


def generate_invoices(n=20):
    """
    Generate synthetic invoices for business testing.
    """
    invoices = []

    for _ in range(n):
        invoices.append({
            "invoice_id": fake.uuid4(),
            "client": fake.company(),
            "issue_date": fake.date_between(start_date="-6m", end_date="today").isoformat(),
            "due_date": fake.date_between(start_date="today", end_date="+2m").isoformat(),
            "amount": round(random.uniform(100, 5000), 2),
            "status": random.choice(["Paid", "Pending", "Overdue"])
        })

    return invoices
