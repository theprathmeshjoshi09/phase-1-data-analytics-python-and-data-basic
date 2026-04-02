"""
analyzer.py

Performs analysis using Pandas
"""

def add_revenue(df):
    """
    Create revenue column
    """
    df["revenue"] = df["sales"] * df["quantity"]
    return df


def summary_stats(df):
    """
    Basic statistics
    """
    return df.describe()


def category_analysis(df):
    return df.groupby("category")["revenue"].sum()


def region_analysis(df):
    return df.groupby("region")["revenue"].sum()


def trend_analysis(df):
    """
    Sales trend over time
    """
    return df.groupby("date")["revenue"].sum()