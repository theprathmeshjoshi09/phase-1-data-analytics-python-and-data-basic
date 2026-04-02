"""
main.py

Controls full workflow:
Generate → Clean → Analyze → Output
"""

from generator import generate_data
from cleaner import clean_data
from analyzer import basic_stats, count_above_average, normalize_data
from utils import print_array_preview


def main():
    print("=== NumPy Data Processing Lab ===")

    # Step 1: Generate data
    raw_data = generate_data()

    print_array_preview(raw_data, "Raw Data (with noise)")

    # Step 2: Clean data
    clean = clean_data(raw_data)

    print_array_preview(clean, "Cleaned Data")

    # Step 3: Analysis
    stats = basic_stats(clean)

    print("\n=== Statistics ===")
    for key, value in stats.items():
        print(f"{key}: {value:.2f}")

    # Step 4: Advanced analysis
    above_avg = count_above_average(clean)
    normalized = normalize_data(clean)

    print(f"\nValues above average: {above_avg}")

    print_array_preview(normalized, "Normalized Data (0–1 scale)")


if __name__ == "__main__":
    main()