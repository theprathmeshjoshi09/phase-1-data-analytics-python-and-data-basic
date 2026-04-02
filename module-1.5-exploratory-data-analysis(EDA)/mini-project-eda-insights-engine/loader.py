# loader.py

import pandas as pd
import os

def load_data(file_name):
    """
    Load dataset using safe absolute path
    """
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, "data", file_name)

    print(f"📂 Loading file: {file_path}")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ File not found: {file_path}")

    df = pd.read_csv(file_path)
    df["Date"] = pd.to_datetime(df["Date"])

    return df