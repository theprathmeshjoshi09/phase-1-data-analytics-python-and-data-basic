# main.py

# This is the MAIN controller file
# It connects all modules together

from data_loader import *
from cleaner import *
from analyzer import *
from insights import *
from utils import *


def main():
    """
    Main pipeline:

    1. Take input
    2. Clean data
    3. Analyze data
    4. Generate insights
    5. Display output
    """

    print("===== Personal Data Analyzer =====")

    # --------------------------
    # STEP 1: INPUT
    # --------------------------
    print("1. Manual Input")
    print("2. Load from File")

    choice = input("Choose input method: ")

    if choice == "1":
        data = manual_input()

    elif choice == "2":
        file_path = input("Enter file path: ")
        data = load_from_file(file_path)

    else:
        print("❌ Invalid choice")
        return

    # If no data → stop
    if not data:
        print("❌ No data to process")
        return

    print_data(data)

    # --------------------------
    # STEP 2: CLEANING
    # --------------------------
    data = validate_data(data)
    data = remove_duplicates(data)

    print("\n🧹 Cleaned Data:", data)

    # --------------------------
    # STEP 3: ANALYSIS
    # --------------------------
    total = calculate_total(data)
    avg = calculate_average(data)
    max_val = find_max(data)
    min_val = find_min(data)
    above, below = detect_distribution(data)

    # --------------------------
    # STEP 4: OUTPUT
    # --------------------------
    print_summary(total, avg, max_val, min_val, above, below)

    # --------------------------
    # STEP 5: INSIGHTS
    # --------------------------
    generate_insights(data, avg, max_val, min_val)


# Entry point
if __name__ == "__main__":
    main()