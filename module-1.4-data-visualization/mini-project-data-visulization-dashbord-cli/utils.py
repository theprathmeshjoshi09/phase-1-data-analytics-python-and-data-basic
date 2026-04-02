# utils.py

import os

def create_output_folder():
    """
    Ensures outputs folder exists
    """
    if not os.path.exists("outputs"):
        os.makedirs("outputs")