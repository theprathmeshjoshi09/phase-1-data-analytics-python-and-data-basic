# report.py

def generate_report(info, missing, stats, top_cat, outliers):
    """
    Create text report
    """
    with open("outputs/report.txt", "w", encoding="utf-8") as f:

        f.write("📊 EDA REPORT\n")
        f.write("="*40 + "\n\n")

        f.write(f"Total Rows: {info['rows']}\n")
        f.write(f"Columns: {info['columns']}\n\n")

        f.write("Missing Values:\n")
        f.write(str(missing) + "\n\n")

        f.write("Summary Statistics:\n")
        f.write(str(stats) + "\n\n")

        f.write(f"Top Category: {top_cat}\n")
        f.write(f"Outliers Detected: {outliers}\n")