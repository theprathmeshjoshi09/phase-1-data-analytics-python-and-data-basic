# cleaner.py

# This file handles data cleaning operations
# Responsibility: Clean raw data before analysis


def remove_duplicates(data):
    """
    Remove duplicate values

    Example:
        [10, 20, 20, 30] → [10, 20, 30]
    """

    # Convert list → set → list
    # Set automatically removes duplicates
    return list(set(data))


def validate_data(data):
    """
    Ensure all values are numbers

    Filters out invalid entries
    """

    clean_data = []

    for value in data:
        # Check if value is int or float
        if isinstance(value, (int, float)):
            clean_data.append(value)

    return clean_data