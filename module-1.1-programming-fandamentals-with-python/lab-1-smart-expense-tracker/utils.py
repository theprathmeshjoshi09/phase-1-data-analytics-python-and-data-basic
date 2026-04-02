# utils.py

# Import json module
# Used to store and retrieve structured data from file
import json


# ---------------------------------------------------
# FUNCTION: load_data
# ---------------------------------------------------
def load_data(file_path):
    """
    Load expense data from a file.

    Parameters:
        file_path (str): Path to the data file

    Returns:
        list: List of expense dictionaries

    Logic:
    - Try reading file
    - Convert JSON → Python list
    - If file doesn't exist or is empty → return empty list
    """

    try:
        # Open file in read mode
        with open(file_path, "r") as file:
            return json.load(file)  # Convert JSON data → Python object

    except:
        # If file not found or empty → return empty list
        return []


# ---------------------------------------------------
# FUNCTION: save_data
# ---------------------------------------------------
def save_data(file_path, data):
    """
    Save expense data to a file.

    Parameters:
        file_path (str): Path to save file
        data (list): List of expense dictionaries

    Logic:
    - Open file in write mode
    - Convert Python list → JSON format
    - Store in file
    """

    # Open file in write mode (overwrites old data)
    with open(file_path, "w") as file:
        # Dump data into file in readable format
        json.dump(data, file, indent=4)


# ---------------------------------------------------
# FUNCTION: add_expense
# ---------------------------------------------------
def add_expense(expenses):
    """
    Add a new expense to the list.

    Parameters:
        expenses (list): Existing list of expenses

    Logic:
    - Take user input
    - Convert amount to float
    - Store as dictionary
    - Append to list
    """

    try:
        # Take amount input and convert to float
        amount = float(input("Enter amount: "))

        # Take category input (string)
        category = input("Enter category: ")

        # Create dictionary (structured data)
        expense = {
            "amount": amount,
            "category": category
        }

        # Add expense to list
        expenses.append(expense)

        print("✅ Expense added successfully!")

    except:
        # If user enters invalid amount (like text instead of number)
        print("❌ Invalid input! Please enter correct data.")


# ---------------------------------------------------
# FUNCTION: view_expenses
# ---------------------------------------------------
def view_expenses(expenses):
    """
    Display all expenses.

    Parameters:
        expenses (list): List of expense dictionaries

    Logic:
    - Loop through list
    - Print each expense
    """

    # If no data available
    if not expenses:
        print("No expenses found.")
        return

    print("\n--- All Expenses ---")

    # Loop through expenses with index
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. Amount: {exp['amount']} | Category: {exp['category']}")


# ---------------------------------------------------
# FUNCTION: total_spending
# ---------------------------------------------------
def total_spending(expenses):
    """
    Calculate and display total spending.

    Parameters:
        expenses (list)

    Logic:
    - Sum all 'amount' values using generator expression
    """

    # Sum all amounts
    total = sum(exp["amount"] for exp in expenses)

    print(f"\n💰 Total Spending: {total}")


# ---------------------------------------------------
# FUNCTION: category_spending
# ---------------------------------------------------
def category_spending(expenses):
    """
    Calculate spending per category.

    Parameters:
        expenses (list)

    Logic:
    - Use dictionary to accumulate category totals
    - Loop through expenses
    - Add values category-wise
    """

    # Dictionary to store category totals
    result = {}

    for exp in expenses:
        category = exp["category"]
        amount = exp["amount"]

        # If category exists → add amount
        # Else → initialize with amount
        result[category] = result.get(category, 0) + amount

    print("\n--- Category-wise Spending ---")

    # Print category totals
    for cat, amt in result.items():
        print(f"{cat}: {amt}")