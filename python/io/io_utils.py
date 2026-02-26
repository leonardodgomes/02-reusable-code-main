"""
io_utils.py
Utility functions for reading and writing common data formats.

Includes:
- read_text()
- write_text()
- read_json()
- write_json()
- read_csv()
- write_csv()
- append_text()
"""

import json
import csv


def read_text(path):
    """
    Read a text file and return its contents as a string.
    """
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_text(path, content):
    """
    Write text content to a file (overwrites existing file).
    """
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def append_text(path, content):
    """
    Append text to an existing file.
    """
    with open(path, "a", encoding="utf-8") as f:
        f.write(content)


def read_json(path):
    """
    Read a JSON file and return a Python object.
    """
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path, data):
    """
    Write a Python object to a JSON file.
    """
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def read_csv(path):
    """
    Read a CSV file into a list of dictionaries.
    """
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def write_csv(path, rows, fieldnames):
    """
    Write a list of dictionaries to a CSV file.
    """
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
