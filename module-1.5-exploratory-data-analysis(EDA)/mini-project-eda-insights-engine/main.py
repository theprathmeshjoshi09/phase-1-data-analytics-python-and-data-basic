# main.py

import matplotlib.pyplot as plt

from loader import load_data
from cleaner import clean_data
from analyzer import (
    basic_info,
    missing_values,
    summary_stats,
    correlation,
    top_category,
    detect_outliers
)
from visualizer import (
    heatmap_corr,
    distribution_plot,
    boxplot_outliers,
    scatter_plot,
    count_plot
)
from report import generate_report
from utils import create_folders


def main():
    print("\n🚀 EDA Insights Engine\n")

    # Setup folders
    create_folders()

    # Load & clean
    df = load_data("dataset.csv")
    df = clean_data(df)

    # Analysis
    info = basic_info(df)
    missing = missing_values(df)
    stats = summary_stats(df)
    corr = correlation(df)
    top_cat = top_category(df)
    outliers = detect_outliers(df)

    # Print key insights
    print(f"Rows: {info['rows']}")
    print(f"Top Category: {top_cat}")
    print(f"Outliers: {outliers}")

    # Visualization
    heatmap_corr(corr)
    distribution_plot(df)
    boxplot_outliers(df)
    scatter_plot(df)
    count_plot(df)

    # Report
    generate_report(info, missing, stats, top_cat, outliers)

    print("\n✅ EDA Completed! Check 'outputs/' folder")

    plt.show()


if __name__ == "__main__":
    main()