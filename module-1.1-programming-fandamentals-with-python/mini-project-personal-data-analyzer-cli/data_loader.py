# data_loader.py

def manual_input():
    """
    Take user input as comma-separated numbers
    Example: 10,20,30
    """

    user_input = input("Enter numbers separated by comma: ")

    try:
        # Convert input string → list of numbers
        data = [float(x.strip()) for x in user_input.split(",")]
        return data
    except:
        print("❌ Invalid input!")
        return []


def load_from_file(file_path):
    """
    Load data from file (one number per line)
    """

    try:
        with open(file_path, "r") as file:
            data = [float(line.strip()) for line in file]
        return data
    except:
        print("❌ Error reading file!")
        return []