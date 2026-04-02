# visualizer.py

import matplotlib.pyplot as plt
import os


def line_chart(trend_data):
    """
    Line chart → Sales trend over time
    """
    plt.figure()

    plt.plot(trend_data.index, trend_data.values)

    plt.title("Sales Trend")
    plt.xlabel("Date")
    plt.ylabel("Sales")

    plt.grid()

    # Save plot
    plt.savefig("outputs/line_chart.png")

    plt.show(block=False)


def bar_chart(category_data):
    """
    Bar chart → Category performance
    """
    plt.figure()

    category_data.plot(kind="bar")

    plt.title("Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Sales")

    plt.grid()

    plt.savefig("outputs/bar_chart.png")

    plt.show(block=False)


def histogram(dist_data):
    """
    Histogram → Sales distribution
    """
    plt.figure()

    plt.hist(dist_data, bins=10)

    plt.title("Sales Distribution")
    plt.xlabel("Sales")
    plt.ylabel("Frequency")

    plt.grid()

    plt.savefig("outputs/histogram.png")

    plt.show(block=False)


def scatter_plot(df):
    """
    Scatter → Sales vs Quantity
    """
    plt.figure()

    plt.scatter(df["Quantity"], df["Sales"])

    plt.title("Sales vs Quantity")
    plt.xlabel("Quantity")
    plt.ylabel("Sales")

    plt.grid()

    plt.savefig("outputs/scatter.png")

    plt.show(block=False)