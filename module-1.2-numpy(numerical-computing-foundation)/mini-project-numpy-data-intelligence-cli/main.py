"""
main.py

Full pipeline:
Input → Clean → Analyze → Transform → Insights → Output
"""

from loader import load_manual, load_file
from cleaner import clean_data
from analyzer import basic_stats, percentiles, correlation
from transformer import normalize, standardize, reshape_data
from insights import generate_insights
from utils import print_array, print_dict


def main():
    print("=== NumPy Data Intelligence CLI ===")

    choice = input("1: Manual Input | 2: File Input → ")

    if choice == "1":
        data = load_manual()
    elif choice == "2":
        path = input("Enter file path: ")
        data = load_file(path)
    else:
        print("Invalid choice.")
        return

    # Cleaning
    data = clean_data(data)

    print_array(data, "Cleaned Data")

    if len(data) == 0:
        print("❌ No data left after cleaning. Exiting.")
        return

    # Analysis
    stats = basic_stats(data)
    perc = percentiles(data)

    print_dict(stats, "Basic Stats")
    print_dict(perc, "Percentiles")

    # Transformation
    norm = normalize(data)
    std = standardize(data)
    reshaped = reshape_data(data)

    print_array(norm, "Normalized Data")
    print_array(std, "Standardized Data")
    print_array(reshaped, "Reshaped Data")

    # Correlation (if 2D)
    corr = correlation(reshaped)
    if corr is not None:
        print_array(corr, "Correlation Matrix")

    # Insights
    insights = generate_insights(data)

    print("\n=== Insights ===")
    for ins in insights:
        print("-", ins)


if __name__ == "__main__":
    main()