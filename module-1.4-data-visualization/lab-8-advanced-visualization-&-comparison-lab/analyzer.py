# analyzer.py

def group_by_region(df):
    """
    Groups data by region

    Returns:
        grouped DataFrame
    """
    return df.groupby('Region')


def sales_trend_by_region(df):
    """
    Prepares data for multi-line chart (sales over time)

    Returns:
        pivot table
    """
    pivot = df.pivot_table(
        values='Sales',
        index='Date',
        columns='Region',
        aggfunc='sum'
    )
    return pivot


def region_performance(df):
    """
    Calculates total sales per region

    Returns:
        Series (region vs total sales)
    """
    return df.groupby('Region')['Sales'].sum()