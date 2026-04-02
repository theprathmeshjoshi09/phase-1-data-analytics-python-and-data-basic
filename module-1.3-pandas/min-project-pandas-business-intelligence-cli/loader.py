"""
loader.py

Loads dataset from CSV
"""

import pandas as pd


def load_data(path):
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        print("File not found.")
        return None