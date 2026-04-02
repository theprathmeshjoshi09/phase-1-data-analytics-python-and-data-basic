# data_loader.py

import pandas as pd

def load_data(file_path):
    """
    Loads CSV data into a pandas DataFrame

    Args:
        file_path (str): Path to dataset

    Returns:
        df (DataFrame): Loaded dataset
    """
    df = pd.read_csv(file_path)

    # Convert Date column to datetime for time-based plots
    df['Date'] = pd.to_datetime(df['Date'])

    return df