# visualizer.py

import matplotlib.pyplot as plt
import seaborn as sns
import os


def save_plot(name):
    """
    Save plot in outputs/plots
    """
    os.makedirs("outputs/plots", exist_ok=True)
    plt.savefig(f"outputs/plots/{name}.png")


def heatmap_corr(corr):
    plt.figure()
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    save_plot("heatmap")
    plt.show(block=False)


def distribution_plot(df):
    plt.figure()
    sns.histplot(df["Sales"], kde=True)
    plt.title("Sales Distribution")
    save_plot("distribution")
    plt.show(block=False)


def boxplot_outliers(df):
    plt.figure()
    sns.boxplot(x=df["Sales"])
    plt.title("Outliers Detection")
    save_plot("boxplot")
    plt.show(block=False)


def scatter_plot(df):
    plt.figure()
    sns.scatterplot(x="Quantity", y="Sales", data=df)
    plt.title("Sales vs Quantity")
    save_plot("scatter")
    plt.show(block=False)


def count_plot(df):
    plt.figure()
    sns.countplot(x="Category", data=df)
    plt.title("Category Distribution")
    save_plot("countplot")
    plt.show(block=False)