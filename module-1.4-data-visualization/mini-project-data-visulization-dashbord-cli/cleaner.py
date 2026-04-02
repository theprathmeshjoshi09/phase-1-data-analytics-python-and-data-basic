# cleaner.py

def clean_data(df):
    """
    Basic data cleaning
    """
    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values (simple approach)
    df = df.dropna()

    return df