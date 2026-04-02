"""
analyzer.py

Performs statistical operations using NumPy
"""

import numpy as np

def basic_stats(data):
    """
    Compute basic statistics
    """
    return {
        "mean": np.mean(data),
        "median": np.median(data),
        "std_dev": np.std(data),
        "min": np.min(data),
        "max": np.max(data)
    }


def count_above_average(data):
    """
    Count how many values are above average
    """
    avg = np.mean(data)

    # Boolean masking
    count = np.sum(data > avg)

    return count


def normalize_data(data):
    """
    Normalize data using Min-Max scaling (0–1)
    """
    min_val = np.min(data)
    max_val = np.max(data)

    # Avoid division by zero
    if max_val == min_val:
        return data

    normalized = (data - min_val) / (max_val - min_val)

    return normalized