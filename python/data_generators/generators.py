"""
generators.py
Utility functions for generating synthetic datasets.

Includes:
- generate_random_numbers()
- generate_fake_people()
- generate_sales_data()
- generate_time_series()
"""

import random
import datetime
import pandas as pd
from faker import Faker

fake = Faker()


def generate_random_numbers(n, min_val=0, max_val=100):
    """
    Generate a list of random integers.
    """
    return [random.randint(min_val, max_val) for _ in range(n)]


def generate_fake_people(n):
    """
    Generate a list of fake people with name, email, address, and birthdate.
    """
    people = []
    for _ in range(n):
        people.append({
            "name": fake.name(),
            "email": fake.email(),
            "address": fake.address().replace("\n", ", "),
            "birthdate": fake.date_of_birth().isoformat()
        })
    return people


def generate_sales_data(n):
    """
    Generate synthetic sales records.
    """
    products = ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"]
    sales = []

    for _ in range(n):
        sales.append({
            "date": fake.date_between(start_date="-1y", end_date="today").isoformat(),
            "product": random.choice(products),
            "quantity": random.randint(1, 10),
            "price": round(random.uniform(50, 2000), 2)
        })

    return sales


def generate_time_series(n, start_value=100, volatility=2):
    """
    Generate a synthetic time series using a random walk.
    """
    values = [start_value]

    for _ in range(n - 1):
        change = random.uniform(-volatility, volatility)
        values.append(values[-1] + change)

    dates = [
        (datetime.date.today() - datetime.timedelta(days=i)).isoformat()
        for i in range(n)
    ]
    dates.reverse()

    return pd.DataFrame({"date": dates, "value": values})
