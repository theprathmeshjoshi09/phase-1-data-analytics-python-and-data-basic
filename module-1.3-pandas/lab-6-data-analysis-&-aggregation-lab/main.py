"""
main.py

Workflow:
Load → Clean → Analyze → Insights → Output
"""

from loader import load_data
from cleaner import clean_data
from analyzer import (
    total_sales_per_category,
    average_order_value,
    most_sold_product,
    region_wise_sales,
    multi_group_analysis
)
from insights import (
    best_category,
    weakest_region,
    high_value_customers
)
from utils import print_series, print_value


def main():
    print("=== Pandas Data Analysis Lab ===")

    # Step 1: Load data
    df = load_data("data/ecommerce.csv")

    if df is None:
        return

    # Debug: check raw types
    print("\nRaw Data Types:")
    print(df.dtypes)

    # Step 2: Clean data (IMPORTANT)
    df = clean_data(df)

    # Debug: check cleaned types
    print("\nCleaned Data Types:")
    print(df.dtypes)

    # Step 3: Analysis
    category_sales = total_sales_per_category(df)
    avg_order = average_order_value(df)
    top_product = most_sold_product(df)
    region_sales = region_wise_sales(df)
    multi_group = multi_group_analysis(df)

    print_series(category_sales, "Total Sales per Category")
    print_value(round(avg_order, 2), "Average Order Value")
    print_value(top_product, "Most Sold Product")
    print_series(region_sales, "Region-wise Sales")
    print_series(multi_group, "Multi-level Group Analysis")

    # Step 4: Insights
    best_cat = best_category(category_sales)
    weak_reg = weakest_region(region_sales)
    customers = high_value_customers(df)

    print(f"\nBest Category: {best_cat[0]} (Sales={best_cat[1]})")
    print(f"Weakest Region: {weak_reg[0]} (Sales={weak_reg[1]})")

    print_series(customers, "High Value Customers")


if __name__ == "__main__":
    main()