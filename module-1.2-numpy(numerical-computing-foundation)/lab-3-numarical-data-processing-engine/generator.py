"""
generator.py

Responsible for generating raw numerical data
with noise (negative values + outliers)
"""

import numpy as np

def generate_data(size=80):
    """
    Generate random dataset

    Includes:
    - Normal values (0–100)
    - Negative values
    - Extreme outliers
    """

    # Normal values
    normal_data = np.random.randint(0, 100, size)

    # Negative values (noise)
    negative_data = np.random.randint(-50, 0, size // 5)

    # Outliers (very high values)
    outliers = np.random.randint(150, 300, size // 10)

    # Combine all
    data = np.concatenate([normal_data, negative_data, outliers])

    # Shuffle to mix values
    np.random.shuffle(data)

    return data