"""
cleaner.py

Handles data cleaning using NumPy techniques:
- Boolean masking
- Filtering
"""

import numpy as np

def remove_negatives(data):
    """
    Remove all negative values
    """
    return data[data >= 0]


def remove_outliers(data, threshold=100):
    """
    Remove values greater than threshold
    """
    return data[data <= threshold]


def clean_data(data):
    """
    Full cleaning pipeline
    """
    data = remove_negatives(data)
    data = remove_outliers(data)

    return data