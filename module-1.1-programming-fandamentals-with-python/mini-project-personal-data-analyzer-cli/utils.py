# utils.py

# This file contains helper functions
# Responsibility: Output formatting and display


def print_data(data):
    """
    Display raw data
    """
    print("\n📊 Data:", data)


def print_summary(total, avg, max_val, min_val, above, below):
    """
    Print analysis summary in structured format
    """

    print("\n===== Summary =====")

    print(f"Total: {total}")
    print(f"Average: {avg:.2f}")
    print(f"Max: {max_val}")
    print(f"Min: {min_val}")

    print(f"Above Average: {above}")
    print(f"Below Average: {below}")