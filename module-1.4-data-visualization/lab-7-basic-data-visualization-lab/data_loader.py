"""
data_loader.py

Loads dataset using pandas
"""

import pandas as pd


def load_data(path):
    """
    Load CSV and convert date column
    """
    try:
        df = pd.read_csv(path)

        # Convert date column to datetime
        df["date"] = pd.to_datetime(df["date"])

        return df

    except FileNotFoundError:
        print("File not found.")
        return None