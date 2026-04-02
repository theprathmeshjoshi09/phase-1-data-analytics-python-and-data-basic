"""
main.py

Workflow:
Load → Preview → Plot → Show All
"""

from data_loader import load_data
from plots import (
    plot_sales_trend,
    plot_sales_by_category,
    plot_sales_distribution
)
from utils import print_preview, print_info
import matplotlib.pyplot as plt


def main():
    print("=== Basic Data Visualization Lab ===")

    # Step 1: Load data
    df = load_data("data/sales.csv")

    if df is None:
        return

    # Step 2: Preview
    print_preview(df)
    print_info(df)

    # Step 3: Generate all plots (NO show here)
    plot_sales_trend(df)
    plot_sales_by_category(df)
    plot_sales_distribution(df)

    # 🚀 Step 4: Show ALL plots together
    plt.show()


if __name__ == "__main__":
    main()