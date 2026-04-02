# loader.py

import pandas as pd
import os

def load_data(file_name):
    """
    Loads dataset safely using absolute path
    """

    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, "data", file_name)

    print(f"📂 Loading file from: {file_path}")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ File not found: {file_path}")

    df = pd.read_csv(file_path)

    # Convert Date column to datetime
    df["Date"] = pd.to_datetime(df["Date"])

    return df