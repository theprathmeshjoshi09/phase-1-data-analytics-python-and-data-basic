"""
plots.py

Contains all visualization functions using matplotlib
"""

import matplotlib.pyplot as plt


def plot_sales_trend(df):
    """
    Line plot → sales over time
    """
    plt.figure()

    plt.plot(df["date"], df["sales"], marker='o')

    plt.title("Sales Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Sales")

    plt.xticks(rotation=45)
    plt.grid()

    plt.tight_layout()


def plot_sales_by_category(df):
    """
    Bar chart → total sales by category
    """
    category_sales = df.groupby("category")["sales"].sum()

    plt.figure()

    plt.bar(category_sales.index, category_sales.values)

    plt.title("Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Sales")

    plt.grid(axis='y')


def plot_sales_distribution(df):
    """
    Histogram → distribution of sales values
    """
    plt.figure()

    plt.hist(df["sales"], bins=10)

    plt.title("Sales Distribution")
    plt.xlabel("Sales Value")
    plt.ylabel("Frequency")

    plt.grid()