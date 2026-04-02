"""
main.py

Full pipeline:
Load → Explore → Clean → Filter → Output
"""

from loader import load_data
from cleaner import clean_data
from explorer import explore_data
from utils import print_preview, print_filtered


def main():
    print("=== Pandas Data Cleaning Lab ===")

    # Step 1: Load data
    df = load_data("data/sales_data.csv")

    if df is None:
        return

    print_preview(df, "Raw Data")

    # Step 2: Explore
    explore_data(df)

    # Step 3: Clean
    df = clean_data(df)

    print_preview(df, "Cleaned Data")

    # Step 4: Filtering
    high_sales = df[df["sales"] > 500]

    # Sort by sales descending
    sorted_df = df.sort_values(by="sales", ascending=False)

    print_filtered(high_sales, "High Sales (>500)")
    print_filtered(sorted_df, "Sorted by Sales (Descending)")


if __name__ == "__main__":
    main()