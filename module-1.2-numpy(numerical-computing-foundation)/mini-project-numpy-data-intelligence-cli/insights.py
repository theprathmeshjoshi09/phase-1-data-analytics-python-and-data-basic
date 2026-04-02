"""
insights.py

Converts numbers → meaning
"""

import numpy as np


def generate_insights(data):
    insights = []

    mean = np.mean(data)
    std = np.std(data)
    min_val = np.min(data)
    max_val = np.max(data)

    # Stability check
    if std < mean * 0.5:
        insights.append("Data is relatively stable.")
    else:
        insights.append("Data is highly variable (volatile).")

    # Range insight
    if max_val - min_val > mean:
        insights.append("Wide spread detected in data.")

    # Outlier-like detection
    for val in data:
        if val > mean * 2:
            insights.append(f"Extreme high value detected: {val}")
            break

    # Skew detection (simple)
    median = np.median(data)
    if mean > median:
        insights.append("Data is right-skewed.")
    elif mean < median:
        insights.append("Data is left-skewed.")

    return insights