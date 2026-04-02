# analyzer.py

def basic_info(df):
    return {
        "rows": len(df),
        "columns": list(df.columns)
    }


def missing_values(df):
    return df.isnull().sum()


def summary_stats(df):
    return df.describe()


def correlation(df):
    return df.corr(numeric_only=True)


def top_category(df):
    return df["Category"].value_counts().idxmax()


def detect_outliers(df):
    """
    Simple outlier detection using IQR
    """
    Q1 = df["Sales"].quantile(0.25)
    Q3 = df["Sales"].quantile(0.75)
    IQR = Q3 - Q1

    outliers = df[(df["Sales"] < Q1 - 1.5 * IQR) | 
                  (df["Sales"] > Q3 + 1.5 * IQR)]

    return len(outliers)