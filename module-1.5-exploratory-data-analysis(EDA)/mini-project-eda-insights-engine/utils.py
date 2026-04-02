# utils.py

import os

def create_folders():
    """
    Create required folders
    """
    os.makedirs("outputs", exist_ok=True)
    os.makedirs("outputs/plots", exist_ok=True)