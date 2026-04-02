# main.py

# 🔥 Force proper backend (fixes window issues on Windows)
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

from data_loader import load_data
from analyzer import (
    sales_trend_by_region,
    region_performance
)
from plots import (
    scatter_plot,
    subplot_region_comparison,
    multiline_sales_trend,
    bar_region_performance
)


def main():
    # Step 1: Load data
    df = load_data("data/ecommerce.csv")

    # Step 2: Generate all plots (non-blocking)
    scatter_plot(df)
    subplot_region_comparison(df)

    pivot = sales_trend_by_region(df)
    multiline_sales_trend(pivot)

    region_sales = region_performance(df)
    bar_region_performance(region_sales)

    # Step 3: Insight
    best_region = region_sales.idxmax()
    print(f"\n🔥 Best performing region: {best_region}")

    print("\n📊 All plots opened in separate windows!")

    # 🔥 Keep all windows open
    plt.show()


if __name__ == "__main__":
    main()