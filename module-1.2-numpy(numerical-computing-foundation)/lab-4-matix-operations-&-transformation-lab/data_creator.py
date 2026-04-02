"""
data_creator.py

Responsible for creating student marks matrix

Rows = Students
Columns = Subjects
"""

import numpy as np

def create_marks(num_students=6, num_subjects=4):
    """
    Generate random marks between 0–100
    """

    # Create 2D array
    marks = np.random.randint(0, 101, size=(num_students, num_subjects))

    return marks