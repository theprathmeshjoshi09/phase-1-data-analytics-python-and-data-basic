# plots.py

import matplotlib.pyplot as plt


def scatter_plot(df):
    plt.figure()
    plt.scatter(df['Quantity'], df['Sales'])

    plt.title("Sales vs Quantity")
    plt.xlabel("Quantity")
    plt.ylabel("Sales")

    plt.grid()

    plt.show(block=False)   # 🔥 NON-BLOCKING


def subplot_region_comparison(df):
    regions = df['Region'].unique()

    plt.figure(figsize=(10, 6))

    for i, region in enumerate(regions, 1):
        plt.subplot(2, 2, i)

        region_data = df[df['Region'] == region]

        plt.scatter(region_data['Quantity'], region_data['Sales'])

        plt.title(region)
        plt.xlabel("Quantity")
        plt.ylabel("Sales")

    plt.tight_layout()
    plt.show(block=False)   # 🔥 NON-BLOCKING


def multiline_sales_trend(pivot_data):
    plt.figure()

    for column in pivot_data.columns:
        plt.plot(pivot_data.index, pivot_data[column], label=column)

    plt.title("Sales Trend by Region")
    plt.xlabel("Date")
    plt.ylabel("Sales")

    plt.legend()
    plt.grid()

    plt.show(block=False)   # 🔥 NON-BLOCKING


def bar_region_performance(region_sales):
    plt.figure()

    region_sales.plot(kind='bar')

    plt.title("Total Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Total Sales")

    plt.grid()

    plt.show(block=False)   # 🔥 NON-BLOCKING

    