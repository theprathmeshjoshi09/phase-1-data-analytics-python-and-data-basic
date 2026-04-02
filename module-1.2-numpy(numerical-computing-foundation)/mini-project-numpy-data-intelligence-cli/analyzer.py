"""
analyzer.py

Performs statistical analysis using NumPy
"""

import numpy as np


def basic_stats(data):
    return {
        "mean": np.mean(data),
        "median": np.median(data),
        "std": np.std(data),
        "variance": np.var(data)
    }


def percentiles(data):
    return {
        "25th": np.percentile(data, 25),
        "50th": np.percentile(data, 50),
        "75th": np.percentile(data, 75)
    }


def correlation(data):
    """
    If data is 2D → compute correlation matrix
    """
    if data.ndim == 2:
        return np.corrcoef(data, rowvar=False)
    return None