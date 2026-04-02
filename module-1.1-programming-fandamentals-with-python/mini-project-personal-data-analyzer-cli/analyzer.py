# analyzer.py

# This file performs ALL calculations
# Responsibility: Convert data → numerical results


def calculate_total(data):
    """
    Calculate sum of all values
    """
    return sum(data)


def calculate_average(data):
    """
    Calculate average value

    Handles empty data safely
    """

    if len(data) == 0:
        return 0

    return sum(data) / len(data)


def find_max(data):
    """
    Find maximum value
    """
    return max(data) if data else None


def find_min(data):
    """
    Find minimum value
    """
    return min(data) if data else None


def detect_distribution(data):
    """
    Analyze how data is distributed around average

    Returns:
        count_above_avg, count_below_avg
    """

    avg = calculate_average(data)

    # Count values above average
    above = len([x for x in data if x > avg])

    # Count values below average
    below = len([x for x in data if x < avg])

    return above, below