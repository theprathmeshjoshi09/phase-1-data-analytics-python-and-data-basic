"""
utils.py

Helper functions for formatting output
"""

def print_array_preview(data, title):
    """
    Print first few elements of array
    """
    print(f"\n{title}")
    print(data[:10])  # show first 10 values
    print(f"Total elements: {len(data)}")