"""
converters.py
Utility functions for converting between common file formats.

Includes:
- excel_to_csv()
- csv_to_txt()
- csv_to_parquet()
- txt_to_csv()
- json_to_csv()
- csv_to_json()
"""

import csv
import json
import pandas as pd


def excel_to_csv(excel_path, csv_path):
    """
    Convert an Excel file (.xlsx or .xls) to CSV.
    """
    df = pd.read_excel(excel_path)
    df.to_csv(csv_path, index=False)
    print(f"Converted Excel → CSV: {csv_path}")


def csv_to_txt(csv_path, txt_path, delimiter=","):
    """
    Convert a CSV file to a TXT file with a chosen delimiter.
    """
    with open(csv_path, "r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        with open(txt_path, "w", encoding="utf-8") as txt_file:
            for row in reader:
                txt_file.write(delimiter.join(row) + "\n")
    print(f"Converted CSV → TXT: {txt_path}")


def csv_to_parquet(csv_path, parquet_path):
    """
    Convert a CSV file to Parquet format.
    """
    df = pd.read_csv(csv_path)
    df.to_parquet(parquet_path, index=False)
    print(f"Converted CSV → Parquet: {parquet_path}")


def txt_to_csv(txt_path, csv_path, delimiter=","):
    """
    Convert a TXT file to CSV using a chosen delimiter.
    """
    with open(txt_path, "r", encoding="utf-8") as txt_file:
        lines = txt_file.readlines()

    with open(csv_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        for line in lines:
            writer.writerow(line.strip().split(delimiter))

    print(f"Converted TXT → CSV: {csv_path}")


def json_to_csv(json_path, csv_path):
    """
    Convert a JSON file (list of objects) to CSV.
    """
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("JSON must contain a list of objects")

    keys = data[0].keys()

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

    print(f"Converted JSON → CSV: {csv_path}")


def csv_to_json(csv_path, json_path):
    """
    Convert a CSV file to JSON.
    """
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"Converted CSV → JSON: {json_path}")
