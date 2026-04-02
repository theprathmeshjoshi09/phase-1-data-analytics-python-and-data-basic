"""
loader.py

Loads dataset using pandas
"""

import pandas as pd


def load_data(path):
    """
    Load CSV into DataFrame
    """
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        print("File not found.")
        return None