# profiler.py

def dataset_overview(df):
    """
    Prints basic dataset information
    """
    print("\n📊 Dataset Overview")
    print("-" * 40)

    print(f"Shape: {df.shape}")
    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)


def missing_values(df):
    """
    Calculates missing values count and percentage
    """
    print("\n❗ Missing Values Analysis")
    print("-" * 40)

    missing_count = df.isnull().sum()
    missing_percent = (missing_count / len(df)) * 100

    print("Count:\n", missing_count)
    print("\nPercentage:\n", missing_percent)


def summary_statistics(df):
    """
    Prints summary statistics
    """
    print("\n📈 Summary Statistics")
    print("-" * 40)

    print(df.describe())


def value_counts(df):
    """
    Category frequency
    """
    print("\n📦 Category Counts")
    print("-" * 40)

    print(df["Category"].value_counts())