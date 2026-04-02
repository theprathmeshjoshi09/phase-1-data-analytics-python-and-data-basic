# main.py

import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

from loader import load_data
from cleaner import clean_data
from analyzer import (
    total_sales,
    sales_by_category,
    sales_trend,
    distribution
)
from visualizer import (
    line_chart,
    bar_chart,
    histogram,
    scatter_plot
)
from utils import create_output_folder


def main():
    print("\n🚀 Data Visualization Dashboard CLI\n")

    # Step 1: Setup
    create_output_folder()

    # Step 2: Load data
    df = load_data("data/dataset.csv")

    # Step 3: Clean data
    df = clean_data(df)

    # Step 4: Analysis
    total = total_sales(df)
    category_sales = sales_by_category(df)
    trend = sales_trend(df)
    dist = distribution(df)

    # Step 5: Print insights
    print(f"💰 Total Sales: {total}")
    print(f"🏆 Best Category: {category_sales.idxmax()}")

    # Step 6: Visualization
    line_chart(trend)
    bar_chart(category_sales)
    histogram(dist)
    scatter_plot(df)

    print("\n📊 All plots generated and saved in 'outputs/' folder!")

    # Keep windows open
    plt.show()


if __name__ == "__main__":
    main()