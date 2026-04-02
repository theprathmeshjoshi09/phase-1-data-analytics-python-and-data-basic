# analysis.py

# ---------------------------------------------------
# FUNCTION: calculate_average
# ---------------------------------------------------
def calculate_average(students):
    """
    Calculate average marks of all students.

    Parameters:
        students (dict): {name: marks}

    Returns:
        float: average marks
    """

    # Get all marks (values from dictionary)
    marks = students.values()

    # Calculate average
    avg = sum(marks) / len(students)

    return avg


# ---------------------------------------------------
# FUNCTION: find_topper
# ---------------------------------------------------
def find_topper(students):
    """
    Find student with highest marks.

    Returns:
        (name, marks)
    """

    # max() finds highest based on marks
    topper = max(students, key=students.get)

    return topper, students[topper]


# ---------------------------------------------------
# FUNCTION: assign_grade
# ---------------------------------------------------
def assign_grade(mark):
    """
    Assign grade based on marks.

    Grading Logic:
        90+  → A
        75+  → B
        60+  → C
        <60  → D
    """

    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 60:
        return "C"
    else:
        return "D"


# ---------------------------------------------------
# FUNCTION: generate_summary
# ---------------------------------------------------
def generate_summary(students):
    """
    Generate full analysis summary.

    Includes:
    - Average marks
    - Topper
    - Grades for each student
    """

    print("\n===== Analysis Summary =====")

    # Average
    avg = calculate_average(students)
    print(f"📊 Average Marks: {avg:.2f}")

    # Topper
    topper, marks = find_topper(students)
    print(f"🏆 Topper: {topper} ({marks})")

    # Grades
    print("\n🎓 Grades:")
    for name, mark in students.items():
        grade = assign_grade(mark)
        print(f"{name}: {mark} → Grade {grade}")