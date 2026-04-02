# visualizer.py

import matplotlib.pyplot as plt
import seaborn as sns


def distribution_plot(df):
    """
    Histogram using Seaborn
    """
    plt.figure()

    sns.histplot(df["Sales"], kde=True)

    plt.title("Sales Distribution")
    plt.xlabel("Sales")
    plt.ylabel("Frequency")

    plt.show(block=False)


def boxplot_outliers(df):
    """
    Boxplot to detect outliers
    """
    plt.figure()

    sns.boxplot(x=df["Sales"])

    plt.title("Sales Outliers Detection")

    plt.show(block=False)