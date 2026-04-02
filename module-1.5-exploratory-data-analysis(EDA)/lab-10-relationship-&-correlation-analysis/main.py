# main.py

import matplotlib.pyplot as plt

from loader import load_data
from analyzer import (
    correlation_matrix,
    category_analysis
)
from visualizer import (
    heatmap_corr,
    scatter_sales_quantity,
    pairplot_relationships,
    boxplot_category
)


def main():
    print("\n🧪 LAB 2 — Relationship & Correlation Analysis\n")

    # Step 1: Load data
    df = load_data("dataset.csv")

    # Step 2: Correlation
    corr = correlation_matrix(df)
    print("\n📊 Correlation Matrix:\n")
    print(corr)

    # Step 3: Category Analysis
    category_stats = category_analysis(df)
    print("\n📦 Category-wise Averages:\n")
    print(category_stats)

    # Step 4: Visualization
    heatmap_corr(corr)
    scatter_sales_quantity(df)
    pairplot_relationships(df)
    boxplot_category(df)

    print("\n✅ Relationship Analysis Completed!")

    # Keep all plots open
    plt.show()


if __name__ == "__main__":
    main()