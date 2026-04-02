# cleaner.py

def clean_data(df):
    """
    Clean dataset
    """
    # Remove duplicates
    df = df.drop_duplicates()

    # Drop missing values
    df = df.dropna()

    return df