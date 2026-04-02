# analyzer.py

def total_sales(df):
    """
    Total revenue
    """
    return df["Sales"].sum()


def sales_by_category(df):
    """
    Sales grouped by category
    """
    return df.groupby("Category")["Sales"].sum()


def sales_trend(df):
    """
    Sales over time
    """
    return df.groupby("Date")["Sales"].sum()


def distribution(df):
    """
    Sales distribution
    """
    return df["Sales"]