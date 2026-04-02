# visualizer.py

import matplotlib.pyplot as plt
import seaborn as sns


def heatmap_corr(corr_matrix):
    """
    Heatmap to visualize correlation
    """
    plt.figure()

    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")

    plt.title("Correlation Heatmap")

    plt.show(block=False)


def scatter_sales_quantity(df):
    """
    Scatter plot → Sales vs Quantity
    """
    plt.figure()

    sns.scatterplot(x="Quantity", y="Sales", data=df)

    plt.title("Sales vs Quantity")

    plt.show(block=False)


def pairplot_relationships(df):
    """
    Pairplot for multi-variable relationships
    """
    sns.pairplot(df.select_dtypes(include="number"))

    plt.show(block=False)


def boxplot_category(df):
    """
    Boxplot → Sales by Category
    """
    plt.figure()

    sns.boxplot(x="Category", y="Sales", data=df)

    plt.title("Sales Distribution by Category")

    plt.show(block=False)