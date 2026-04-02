"""
utils.py

Helper functions
"""

def print_array(data, title):
    print(f"\n=== {title} ===")
    print(data)


def print_dict(data, title):
    print(f"\n=== {title} ===")
    for k, v in data.items():
        print(f"{k}: {v:.2f}")