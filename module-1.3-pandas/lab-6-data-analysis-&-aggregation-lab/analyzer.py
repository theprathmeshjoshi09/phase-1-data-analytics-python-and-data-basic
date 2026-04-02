"""
analyzer.py

Performs aggregation using Pandas
"""

def total_sales_per_category(df):
    return df.groupby("category")["sales"].sum()


def average_order_value(df):
    # Now safe because sales is numeric
    return df["sales"].mean()


def most_sold_product(df):
    return df["product"].value_counts().idxmax()


def region_wise_sales(df):
    return df.groupby("region")["sales"].sum()


def multi_group_analysis(df):
    return df.groupby(["region", "category"])["sales"].sum()