"""
utils.py

Helper functions for printing
"""

def print_preview(df, title):
    print(f"\n=== {title} ===")
    print(df.head())


def print_filtered(df, title):
    print(f"\n=== {title} ===")
    print(df)