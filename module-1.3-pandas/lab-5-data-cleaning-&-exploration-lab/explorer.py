"""
explorer.py

Performs basic data exploration
"""

def explore_data(df):
    print("\n=== Dataset Overview ===")

    print("\nShape of data:")
    print(df.shape)

    print("\nColumn Info:")
    print(df.info())

    print("\nSummary Statistics:")
    print(df.describe())

    print("\nMissing Values:")
    print(df.isnull().sum())