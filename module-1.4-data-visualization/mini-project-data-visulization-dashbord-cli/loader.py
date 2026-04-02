# loader.py

import pandas as pd

def load_data(file_path):
    """
    Loads dataset into pandas DataFrame
    """
    df = pd.read_csv(file_path)

    # Convert Date column to datetime
    df["Date"] = pd.to_datetime(df["Date"])

    return df