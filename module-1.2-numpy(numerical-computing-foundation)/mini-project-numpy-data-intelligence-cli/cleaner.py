"""
cleaner.py

Handles:
- NaN removal
- Outlier removal using Z-score
"""

import numpy as np


def remove_nan(data):
    return data[~np.isnan(data)]


def remove_outliers_zscore(data, threshold=3):
    """
    Remove values beyond Z-score threshold
    """
    mean = np.mean(data)
    std = np.std(data)

    if std == 0:
        return data

    z_scores = (data - mean) / std

    filtered = data[np.abs(z_scores) < threshold]

    # 🚨 Safety check
    if len(filtered) == 0:
        print("⚠️ All data removed as outliers. Skipping outlier removal.")
        return data

    return filtered


def clean_data(data):
    print(f"Before cleaning: {len(data)}")

    data = remove_nan(data)

    print(f"After NaN removal: {len(data)}")

    data = remove_outliers_zscore(data)

    print(f"After outlier removal: {len(data)}")

    return data