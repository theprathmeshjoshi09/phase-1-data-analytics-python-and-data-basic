"""
utils.py

Helper functions
"""

def print_preview(df):
    print("\n=== Data Preview ===")
    print(df.head())


def print_info(df):
    print("\n=== Data Info ===")
    print(df.info())