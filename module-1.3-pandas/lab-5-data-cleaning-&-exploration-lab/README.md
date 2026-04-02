# 🧪 Pandas Data Cleaning & Exploration Lab

## 🚀 Project Overview

This project is a **Pandas-based data cleaning and exploration system** designed to simulate real-world messy datasets.

It performs:

* Data loading from CSV
* Data exploration (EDA basics)
* Data cleaning (missing values, duplicates, type fixing)
* Filtering and sorting
* Preparing dataset for analysis

Built using **Pandas (Module 3 concepts only)**.

---

## 🎯 Objectives

* Handle messy real-world datasets
* Perform data exploration using Pandas
* Clean and preprocess data efficiently
* Apply filtering and sorting operations
* Build strong foundation for data analysis

---

## 🧠 Features

### 1. Data Loading

* Load CSV dataset using `pandas.read_csv()`

---

### 2. Data Exploration

* Dataset shape
* Column information
* Summary statistics
* Missing value detection

---

### 3. Data Cleaning

* Remove duplicate rows
* Handle missing values (`fillna`, `dropna`)
* Fix incorrect data types (`to_numeric`)

---

### 4. Data Processing

* Filter high sales records
* Sort dataset based on sales

---

### 5. Output

* Preview raw and cleaned data
* Display summary insights

---

## 📂 Project Structure

```bash id="struct_pd1"
lab_pandas_cleaning/
│
├── main.py          # Entry point (workflow controller)
├── loader.py        # Loads CSV data
├── cleaner.py       # Data cleaning logic
├── explorer.py      # Data exploration (EDA)
├── utils.py         # Helper functions
├── data/
│   └── sales_data.csv
├── requirements.txt # Dependencies
└── README.md        # Documentation
```

---

## ⚙️ Requirements

* Python 3.x
* Pandas

---

## 🛠️ Environment Setup

### Step 1: Clone the Repository

```bash id="clone_pd1"
git clone <your-repo-link>
cd lab_pandas_cleaning
```

---

### Step 2: Create Virtual Environment (Recommended)

#### 🔹 Windows

```bash id="venv_pd1"
python -m venv venv
venv\Scripts\activate
```

#### 🔹 Mac/Linux

```bash id="venv_pd2"
python3 -m venv venv
source venv/bin/activate
```

---

### Step 3: Install Dependencies

```bash id="install_pd1"
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash id="run_pd1"
python main.py
```

---

## 💻 Sample Output (Example)

```bash id="output_pd1"
=== Pandas Data Cleaning Lab ===

=== Raw Data ===
   order_id product     category  sales  quantity region        date
0         1  Laptop  Electronics  1200.0       2.0  North  2024-01-01
...

=== Cleaning Completed ===

=== Cleaned Data ===
   order_id product     category  sales  quantity   region        date
0         1  Laptop  Electronics  1200.0       2.0    North  2024-01-01
...

=== High Sales (>500) ===
...

=== Sorted by Sales (Descending) ===
...
```

---

## 📸 Execution Proof (Screenshots)

> Added real screenshots after running the project

 🔹 Raw Dataset Preview
 🔹 Cleaned Dataset Output
 🔹 High Sales Filter Output
 🔹 Sorted Data Output

![Screenshot](./screenshots/Screenshot%20(1283).png)
![Screenshot](./screenshots/Screenshot%20(1284).png)
![Screenshot](./screenshots/Screenshot%20(1285).png)
![Screenshot](./screenshots/Screenshot%20(1286).png)
![Screenshot](./screenshots/Screenshot%20(1287).png)

---

## 🧠 Learning Outcomes

* Real-world data cleaning using Pandas
* Handling missing and inconsistent data
* Data exploration using `.info()` and `.describe()`
* Filtering and sorting datasets
* Building structured data pipelines

---

## ⚠️ Important Note

This project is about **understanding data**, not just code.

👉 Don’t just run it
👉 Modify cleaning logic
👉 Test with messy datasets

That’s how you grow.

---

## 🚀 Future Improvements

* Add revenue column (`sales * quantity`)
* Perform groupby analysis
* Add visualization (Matplotlib / Seaborn)
* Export cleaned dataset

---

## 👨‍💻 Author

**Prathmesh Joshi**

---

## ⭐ Support

If this lab helped and you liked it , give it a ⭐ and keep building!
