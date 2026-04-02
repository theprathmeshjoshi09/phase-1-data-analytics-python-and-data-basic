"""
main.py

Controls full flow:
Create → Operate → Transform → Analyze → Output
"""

from data_creator import create_marks
from operations import (
    total_per_student,
    average_per_subject,
    find_topper,
    find_lowest
)
from analyzer import (
    normalize_marks,
    add_bonus,
    hardest_subject,
    most_consistent_student
)
from utils import print_matrix, print_array


def main():
    print("=== Matrix Analysis Lab (NumPy) ===")

    # Step 1: Create Data
    marks = create_marks()

    print_matrix(marks, "Student Marks Matrix")

    # Step 2: Operations
    totals = total_per_student(marks)
    avg_subject = average_per_subject(marks)

    print_array(totals, "Total Marks per Student")
    print_array(avg_subject, "Average Marks per Subject")

    topper = find_topper(marks)
    lowest = find_lowest(marks)

    print(f"\nTopper: Student {topper[0]} with score {topper[1]}")
    print(f"Lowest: Student {lowest[0]} with score {lowest[1]}")

    # Step 3: Transformations
    normalized = normalize_marks(marks)
    bonus_marks = add_bonus(marks)

    print_matrix(normalized, "Normalized Marks (0–1)")
    print_matrix(bonus_marks, "Marks After Bonus")

    # Step 4: Insights
    hard_sub = hardest_subject(marks)
    consistent = most_consistent_student(marks)

    print(f"\nHardest Subject: Subject {hard_sub[0]} (avg={hard_sub[1]:.2f})")
    print(f"Most Consistent Student: Student {consistent[0]} (std={consistent[1]:.2f})")


if __name__ == "__main__":
    main()