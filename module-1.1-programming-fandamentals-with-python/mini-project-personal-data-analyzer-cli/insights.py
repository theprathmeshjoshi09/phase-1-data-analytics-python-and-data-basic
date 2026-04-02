# insights.py

# This file converts numbers → meaning
# Responsibility: Generate human-readable insights


def generate_insights(data, avg, max_val, min_val):
    """
    Generate insights based on analysis

    This is where DATA → DECISION happens
    """

    print("\n===== Insights =====")

    # Insight 1: Average level
    if avg > 50:
        print("📈 Data has high average values")
    else:
        print("📉 Data has low average values")

    # Insight 2: Range
    print(f"🔺 Maximum value: {max_val}")
    print(f"🔻 Minimum value: {min_val}")

    # Insight 3: Detect anomalies
    # Rule: value > 2x average → unusual
    for val in data:
        if val > avg * 2:
            print(f"⚠️ Possible anomaly detected: {val}")