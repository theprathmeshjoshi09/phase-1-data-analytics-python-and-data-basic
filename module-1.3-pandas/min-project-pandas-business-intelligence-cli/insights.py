"""
insights.py

Generates business insights
"""

def best_category(category_data):
    return category_data.idxmax(), category_data.max()


def worst_category(category_data):
    return category_data.idxmin(), category_data.min()


def best_region(region_data):
    return region_data.idxmax(), region_data.max()


def detect_anomalies(df):
    """
    Detect unusually high sales
    """
    threshold = df["sales"].mean() * 2
    return df[df["sales"] > threshold]