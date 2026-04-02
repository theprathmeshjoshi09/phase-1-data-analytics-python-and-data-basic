"""
cleaner.py

Handles data cleaning:
- Missing values
- Duplicates
- Data type fixes
"""

import pandas as pd


def clean_data(df):
    """
    Full cleaning pipeline
    """

    print("\n--- Cleaning Started ---")

    # 1. Remove duplicates
    df = df.drop_duplicates()

    # 2. Fix data types (sales should be numeric)
    df["sales"] = pd.to_numeric(df["sales"], errors="coerce")

    # 3. Handle missing values

    # Fill missing sales with median
    df["sales"] = df["sales"].fillna(df["sales"].median())

    # Fill missing quantity with 1
    df["quantity"] = df["quantity"].fillna(1)

    # Fill missing region with 'Unknown'
    df["region"] = df["region"].fillna("Unknown")

    # 4. Drop rows if critical fields missing
    df = df.dropna(subset=["product", "category"])

    print("--- Cleaning Completed ---")

    return df