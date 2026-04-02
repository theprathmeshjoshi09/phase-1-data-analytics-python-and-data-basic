"""
cleaner.py

Handles:
- Data type fixing
- Missing values
- Duplicates
"""

import pandas as pd


def clean_data(df):
    print("\n--- Cleaning Started ---")

    # Convert numeric columns
    df["sales"] = pd.to_numeric(df["sales"], errors="coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

    # Handle missing values
    df["sales"] = df["sales"].fillna(df["sales"].median())
    df["quantity"] = df["quantity"].fillna(1)
    df["region"] = df["region"].fillna("Unknown")

    # Remove invalid rows
    df = df[df["sales"] >= 0]

    # Remove duplicates
    df = df.drop_duplicates()

    # Convert date
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    print("--- Cleaning Completed ---")
    print(f"Dataset size: {df.shape}")

    return df