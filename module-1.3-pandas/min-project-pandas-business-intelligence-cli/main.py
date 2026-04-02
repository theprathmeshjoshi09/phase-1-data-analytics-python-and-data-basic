"""
main.py

Full pipeline:
Load → Clean → Analyze → Insights → Output
"""

from loader import load_data
from cleaner import clean_data
from analyzer import (
    add_revenue,
    summary_stats,
    category_analysis,
    region_analysis,
    trend_analysis
)
from insights import (
    best_category,
    worst_category,
    best_region,
    detect_anomalies
)
from utils import print_df, print_series


def main():
    print("=== Pandas Business Intelligence CLI ===")

    # Step 1: Load
    df = load_data("data/dataset.csv")

    if df is None:
        return

    # Step 2: Clean
    df = clean_data(df)

    # Step 3: Analysis
    df = add_revenue(df)

    stats = summary_stats(df)
    category_data = category_analysis(df)
    region_data = region_analysis(df)
    trends = trend_analysis(df)

    print_df(stats, "Summary Statistics")
    print_series(category_data, "Revenue by Category")
    print_series(region_data, "Revenue by Region")
    print_series(trends, "Revenue Trend")

    # Step 4: Insights
    best_cat = best_category(category_data)
    worst_cat = worst_category(category_data)
    best_reg = best_region(region_data)
    anomalies = detect_anomalies(df)

    print(f"\nBest Category: {best_cat[0]} ({best_cat[1]})")
    print(f"Worst Category: {worst_cat[0]} ({worst_cat[1]})")
    print(f"Best Region: {best_reg[0]} ({best_reg[1]})")

    print_df(anomalies, "Anomalies Detected")


if __name__ == "__main__":
    main()