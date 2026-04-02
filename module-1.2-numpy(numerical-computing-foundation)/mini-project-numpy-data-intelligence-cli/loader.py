"""
loader.py

Handles:
- Manual input
- File input
- Converts to NumPy array
"""

import numpy as np


def load_manual():
    raw = input("Enter numbers (comma-separated): ")

    values = []
    for item in raw.split(","):
        try:
            values.append(float(item.strip()))
        except ValueError:
            print(f"Invalid skipped: {item}")

    return np.array(values)


def load_file(path):
    values = []

    try:
        with open(path, "r") as file:
            lines = file.readlines()

            if not lines:
                print("⚠️ File is empty.")
                return np.array([])

            for line in lines:
                value = line.strip()

                if not value:
                    continue

                try:
                    num = float(value)
                    values.append(num)
                except ValueError:
                    print(f"Invalid skipped: {value}")

    except FileNotFoundError:
        print("File not found.")
        return np.array([])

    print(f"✅ Loaded {len(values)} valid values")

    return np.array(values)