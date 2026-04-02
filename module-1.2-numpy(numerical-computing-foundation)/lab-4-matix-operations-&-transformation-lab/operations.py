"""
operations.py

Handles matrix-based calculations using NumPy
Focus: axis operations (VERY IMPORTANT)
"""

import numpy as np

def total_per_student(marks):
    """
    Sum across subjects (row-wise)
    axis=1 → rows
    """
    return np.sum(marks, axis=1)


def average_per_subject(marks):
    """
    Mean across students (column-wise)
    axis=0 → columns
    """
    return np.mean(marks, axis=0)


def find_topper(marks):
    """
    Student with highest total marks
    """
    totals = total_per_student(marks)

    topper_index = np.argmax(totals)
    topper_score = totals[topper_index]

    return topper_index, topper_score


def find_lowest(marks):
    """
    Student with lowest total marks
    """
    totals = total_per_student(marks)

    lowest_index = np.argmin(totals)
    lowest_score = totals[lowest_index]

    return lowest_index, lowest_score