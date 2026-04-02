# main.py

# Import all functions from utils.py
# This file only handles USER INTERACTION (CLI)
from utils import *


# Path to the file where expenses are stored
FILE_PATH = "data.txt"


def main():
    """
    Main function that runs the CLI-based Expense Tracker.
    
    Responsibilities:
    - Load existing data
    - Show menu
    - Take user input
    - Call appropriate functions
    - Save data when needed
    """

    # Load existing expenses from file
    # If file is empty → returns empty list []
    expenses = load_data(FILE_PATH)

    # Infinite loop to keep program running until user exits
    while True:

        # Display menu options
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spending")
        print("4. Category-wise Spending")
        print("5. Exit")

        # Take user input (always comes as string)
        choice = input("Enter your choice: ")

        # -------------------------------
        # Handle user choice
        # -------------------------------

        # Option 1 → Add new expense
        if choice == "1":
            # Call function from utils.py
            add_expense(expenses)

            # Save updated data to file
            save_data(FILE_PATH, expenses)

        # Option 2 → View all expenses
        elif choice == "2":
            view_expenses(expenses)

        # Option 3 → Calculate total spending
        elif choice == "3":
            total_spending(expenses)

        # Option 4 → Show category-wise spending
        elif choice == "4":
            category_spending(expenses)

        # Option 5 → Exit program
        elif choice == "5":
            # Save data before exiting (IMPORTANT)
            save_data(FILE_PATH, expenses)

            print("👋 Exiting... Data saved!")
            break  # Exit the loop → program ends

        # If user enters invalid option
        else:
            print("❌ Invalid choice. Please try again.")


# ---------------------------------------
# Entry Point of the Program
# ---------------------------------------

# This ensures:
# - main() runs ONLY when this file is executed directly
# - NOT when imported in another file
if __name__ == "__main__":
    main()