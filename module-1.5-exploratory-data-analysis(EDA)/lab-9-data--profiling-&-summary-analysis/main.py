# main.py

import matplotlib.pyplot as plt

from loader import load_data
from profiler import (
    dataset_overview,
    missing_values,
    summary_statistics,
    value_counts
)
from visualizer import (
    distribution_plot,
    boxplot_outliers
)


def main():
    print("\n🧪 LAB 1 — Data Profiling & Summary Analysis\n")

    # Step 1: Load data
    df = load_data("dataset.csv")

    # Step 2: Profiling
    dataset_overview(df)
    missing_values(df)
    summary_statistics(df)
    value_counts(df)

    # Step 3: Visualization
    distribution_plot(df)
    boxplot_outliers(df)

    print("\n✅ EDA Profiling Completed!")

    # Keep plots open
    plt.show()


if __name__ == "__main__":
    main()