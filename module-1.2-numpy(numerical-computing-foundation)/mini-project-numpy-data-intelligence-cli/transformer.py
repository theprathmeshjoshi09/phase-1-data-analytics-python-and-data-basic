"""
transformer.py

Handles:
- Normalization
- Standardization
- Reshaping
"""

import numpy as np


def normalize(data):
    min_val = np.min(data)
    max_val = np.max(data)

    if max_val == min_val:
        return data

    return (data - min_val) / (max_val - min_val)


def standardize(data):
    mean = np.mean(data)
    std = np.std(data)

    if std == 0:
        return data

    return (data - mean) / std


def reshape_data(data, rows=2):
    """
    Reshape into 2D (if possible)
    """
    size = data.size

    if size % rows != 0:
        return data  # cannot reshape cleanly

    return data.reshape(rows, -1)