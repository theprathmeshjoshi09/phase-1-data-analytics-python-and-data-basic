"""
cleaner.py

Handles:
- Type conversion
- Missing values
- Invalid data
"""

import pandas as pd


def clean_data(df):
    print("\n--- Cleaning Started ---")

    # 1. Convert sales to numeric (fix main issue)
    df["sales"] = pd.to_numeric(df["sales"], errors="coerce")

    # 2. Convert quantity to numeric
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

    # 3. Handle missing values
    df["sales"] = df["sales"].fillna(df["sales"].median())
    df["quantity"] = df["quantity"].fillna(1)

    # 4. Remove negative sales (invalid business data)
    df = df[df["sales"] >= 0]

    # 5. Remove duplicates
    df = df.drop_duplicates()

    # 6. Fill missing region
    df["region"] = df["region"].fillna("Unknown")

    print("--- Cleaning Completed ---")
    print(f"Final dataset size: {df.shape}")

    return df