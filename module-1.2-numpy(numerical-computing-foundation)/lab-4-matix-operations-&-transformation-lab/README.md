# 🧪 Matrix Operations & Transformation Lab (NumPy)

## 🚀 Project Overview

This project is a **NumPy-based matrix analysis system** that simulates real-world student performance data.

It works with **2D arrays (matrices)** where:

* Rows → Students
* Columns → Subjects

The system performs:

* Matrix operations (totals, averages)
* Axis-based computations
* Data transformations (normalization, bonus addition)
* Insight generation

Built using **NumPy (Module 2 concepts only)**.

---

## 🎯 Objectives

* Understand multi-dimensional arrays
* Master axis-based operations (`axis=0`, `axis=1`)
* Apply broadcasting in real scenarios
* Perform matrix-level analysis
* Build analytical thinking using NumPy

---

## 🧠 Features

### 1. Data Creation

* Generates student marks matrix
* Random values between 0–100
* Configurable students & subjects

---

### 2. Matrix Operations

* Total marks per student (row-wise)
* Average marks per subject (column-wise)
* Identify topper and lowest scorer

---

### 3. Transformations

* Normalize marks (0–1 scaling)
* Add bonus marks using broadcasting

---

### 4. Insights

* Hardest subject (lowest average)
* Most consistent student (lowest variation)

---

## 📂 Project Structure

```bash id="5p5b3r"
lab_matrix_analysis/
│
├── main.py          # Entry point (controls workflow)
├── data_creator.py  # Generates matrix data
├── operations.py    # Core matrix operations
├── analyzer.py      # Transformations & insights
├── utils.py         # Helper functions
├── requirements.txt # Dependencies
└── README.md        # Documentation
```

---

## ⚙️ Requirements

* Python 3.x
* NumPy

---

## 🛠️ Environment Setup

### Step 1: Clone Repository

```bash id="y2kxoz"
git clone <your-repo-link>
cd lab_matrix_analysis
```

---

### Step 2: Create Virtual Environment (Recommended)

#### 🔹 Windows

```bash id="6n5o9q"
python -m venv venv
venv\Scripts\activate
```

#### 🔹 Mac/Linux

```bash id="b1e8yz"
python3 -m venv venv
source venv/bin/activate
```

---

### Step 3: Install Dependencies

```bash id="z0u9o6"
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash id="5yapd4"
python main.py
```

---

## 💻 Sample Output (Example)

```bash id="g0q5l3"
=== Matrix Analysis Lab (NumPy) ===

=== Student Marks Matrix ===
[[78 65 89 90]
 [56 70 60 75]
 [90 88 92 95]
 ...]

Total Marks per Student
[322 261 365 ...]

Average Marks per Subject
[74.5 72.3 80.1 85.6]

Topper: Student 2 with score 365
Lowest: Student 1 with score 261

=== Normalized Marks (0–1) ===
[[0.78 0.65 0.89 ...]]

=== Marks After Bonus ===
[[83 70 94 95] ...]

Hardest Subject: Subject 1 (avg=72.3)
Most Consistent Student: Student 0 (std=8.21)
```

---

## 📸 Execution Proof (Screenshots)

> Added real screenshots after running  project

 🔹 Student Marks Matrix
 🔹 Operations Output (Totals & Averages)
 🔹 Transformations (Normalized + Bonus)
 🔹 Insights Output

![Screenshot](./screenshots/Screenshot%20(1277).png)

---

## 🧠 Learning Outcomes

* Mastery of 2D NumPy arrays
* Understanding of axis-based computations
* Real-world matrix data simulation
* Efficient vectorized operations
* Analytical thinking with structured data

---

## ⚠️ Important Concept (Must Understand)

* `axis=0` → Column-wise (Subjects)
* `axis=1` → Row-wise (Students)

👉 This is critical for real-world data analysis.

---

## 🚀 Future Improvements

* Add ranking system for students
* Add subject-wise grading
* Visualize data (Matplotlib)
* Export results to file

---

## 👨‍💻 Author

**Prathmesh Joshi**

---

## ⭐ Support

If this lab helped and you liked it, give it a ⭐ and keep building!
