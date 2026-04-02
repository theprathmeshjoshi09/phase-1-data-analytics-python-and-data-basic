# main.py

# Import all analysis functions
from analysis import *


def main():
    """
    Main CLI function for Student Analyzer.

    Responsibilities:
    - Take user input
    - Store student data
    - Call analysis functions
    """

    # Dictionary to store student data
    students = {}

    while True:
        print("\n===== Student Analyzer =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Analyze Data")
        print("4. Exit")

        choice = input("Enter your choice: ")

        # -------------------------
        # Add Student
        # -------------------------
        if choice == "1":
            name = input("Enter student name: ")

            try:
                marks = float(input("Enter marks: "))

                # Store in dictionary
                students[name] = marks

                print("✅ Student added successfully!")

            except:
                print("❌ Invalid marks!")

        # -------------------------
        # View Students
        # -------------------------
        elif choice == "2":
            if not students:
                print("No student data found.")
            else:
                print("\n--- Student Records ---")
                for name, marks in students.items():
                    print(f"{name}: {marks}")

        # -------------------------
        # Analyze Data
        # -------------------------
        elif choice == "3":
            if not students:
                print("No data to analyze.")
            else:
                generate_summary(students)

        # -------------------------
        # Exit
        # -------------------------
        elif choice == "4":
            print("👋 Exiting program.")
            break

        else:
            print("❌ Invalid choice!")


# Entry point
if __name__ == "__main__":
    main()