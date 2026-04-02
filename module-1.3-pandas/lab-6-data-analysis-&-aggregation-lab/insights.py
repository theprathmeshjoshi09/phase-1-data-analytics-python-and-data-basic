"""
insights.py

Generates business insights
"""

def best_category(category_sales):
    return category_sales.idxmax(), category_sales.max()


def weakest_region(region_sales):
    return region_sales.idxmin(), region_sales.min()


def high_value_customers(df):
    return df.groupby("customer")["sales"].sum().sort_values(ascending=False)