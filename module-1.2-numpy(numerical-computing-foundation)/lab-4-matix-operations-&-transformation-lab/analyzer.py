"""
analyzer.py

Performs transformations + generates insights
"""

import numpy as np

def normalize_marks(marks):
    """
    Normalize marks between 0–1
    """
    min_val = np.min(marks)
    max_val = np.max(marks)

    if max_val == min_val:
        return marks

    return (marks - min_val) / (max_val - min_val)


def add_bonus(marks, bonus=5):
    """
    Add bonus marks using broadcasting
    """
    return marks + bonus


def hardest_subject(marks):
    """
    Subject with lowest average marks
    """
    avg = np.mean(marks, axis=0)

    subject_index = np.argmin(avg)

    return subject_index, avg[subject_index]


def most_consistent_student(marks):
    """
    Student with lowest standard deviation
    (least variation in marks)
    """
    std_dev = np.std(marks, axis=1)

    student_index = np.argmin(std_dev)

    return student_index, std_dev[student_index]