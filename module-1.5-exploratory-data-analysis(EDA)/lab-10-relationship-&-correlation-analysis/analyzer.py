# analyzer.py

def correlation_matrix(df):
    """
    Returns correlation matrix for numerical columns
    """
    return df.corr(numeric_only=True)


def category_analysis(df):
    """
    Grouped statistics by category
    """
    return df.groupby("Category")[["Sales", "Quantity"]].mean()