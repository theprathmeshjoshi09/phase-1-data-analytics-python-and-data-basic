# 🚀 NumPy Data Intelligence CLI

## 📊 Project Overview

The **NumPy Data Intelligence CLI** is a command-line based data analysis engine built using **NumPy (Module 2 concepts only)**.

It allows users to:

* Input numerical data (manual or file)
* Clean and preprocess data
* Perform advanced statistical analysis
* Transform data (normalize, standardize, reshape)
* Generate meaningful insights

This project simulates a **real-world data processing pipeline** using efficient NumPy operations.

---

## 🎯 Objectives

* Build an end-to-end NumPy data pipeline
* Apply vectorized operations for performance
* Perform statistical and distribution analysis
* Generate insights from raw data
* Strengthen analytical thinking

---

## 🧠 Features

### 1. Data Input

* Manual input (comma-separated values)
* File input (line-by-line values)

---

### 2. Data Cleaning

* Remove missing values (`NaN`)
* Remove outliers using **Z-score method**

---

### 3. Statistical Analysis

* Mean, Median, Standard Deviation
* Variance
* Percentiles (25th, 50th, 75th)
* Correlation (for 2D data)

---

### 4. Data Transformation

* Normalization (Min-Max scaling)
* Standardization (Z-score scaling)
* Reshaping (1D → 2D if possible)

---

### 5. Insights Generation

* Detect data stability (stable vs volatile)
* Identify extreme values
* Detect skewness (left/right)
* Analyze data spread

---

## 📂 Project Structure

```bash id="struc1"
numpy_data_analyzer/
│
├── main.py          # Entry point (controls full workflow)
├── loader.py        # Input handling (manual/file)
├── cleaner.py       # Data cleaning logic
├── analyzer.py      # Statistical analysis
├── transformer.py   # Data transformations
├── insights.py      # Insight generation
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

### Step 1: Clone the Repository

```bash id="clone1"
git clone <your-repo-link>
cd numpy_data_analyzer
```

---

### Step 2: Create Virtual Environment (Recommended)

#### 🔹 Windows

```bash id="win1"
python -m venv venv
venv\Scripts\activate
```

#### 🔹 Mac/Linux

```bash id="mac1"
python3 -m venv venv
source venv/bin/activate
```

---

### Step 3: Install Dependencies

```bash id="install1"
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash id="run1"
python main.py
```

---

## 💻 Example Usage

### Manual Input:

```bash id="man1"
Enter numbers (comma-separated): 10, 20, 30, 1000, 50
```

### File Input:

```bash id="file1"
Enter file path: data.txt
```

---

## 📈 Sample Output (Example)

```bash id="output1"
=== NumPy Data Intelligence CLI ===

=== Cleaned Data ===
[10. 20. 30. 50.]

=== Basic Stats ===
mean: 27.50
median: 25.00
std: 14.79
variance: 218.75

=== Percentiles ===
25th: 17.50
50th: 25.00
75th: 40.00

=== Normalized Data ===
[0.   0.25 0.5  1.  ]

=== Standardized Data ===
[-1.17 -0.51  0.17  1.51]

=== Insights ===
- Data is relatively stable.
- Wide spread detected in data.
- Data is right-skewed.
```

---

## 📸 Execution Proof (Screenshots)

> Added real screenshots after running the project

### 1: Manual Input 
 🔹 Input & Cleaned Data
 
 🔹 Statistical Analysis Output
 
 🔹 Transformations Output
 
 🔹 Insights Output

![Screenshot](./screenshots/Screenshot%20(1278).png)
![Screenshot](./screenshots/Screenshot%20(1279).png)

### 2: File Input 
 🔹 Input & Cleaned Data
 
 🔹 Statistical Analysis Output
 
 🔹 Transformations Output
 
 🔹 Insights Output

![Screenshot](./screenshots/Screenshot%20(1280).png)
![Screenshot](./screenshots/Screenshot%20(1281).png)
![Screenshot](./screenshots/Screenshot%20(1282).png)

---

## 🧠 Learning Outcomes

* Advanced NumPy usage (vectorization, masking)
* Real-world data cleaning techniques
* Statistical and distribution analysis
* Data transformation techniques
* Insight-driven thinking

---

## ⚠️ Important Note

This is not just a coding project.

👉 This is **data thinking training**

Don’t just run it:

* Modify logic
* Add new insights
* Test with different datasets

---

## 🚀 Future Improvements

* Add visualization (Matplotlib / Seaborn)
* Improve outlier detection methods
* Add support for CSV datasets
* Enhance insight generation logic

---

## 👨‍💻 Author

**Prathmesh Joshi** 

---

## ⭐ Support

If this project helped and you liked it, give it a ⭐ and keep building!
