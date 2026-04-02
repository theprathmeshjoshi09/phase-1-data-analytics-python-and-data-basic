# 📊 Pandas Data Analysis & Aggregation Lab

## 🚀 Project Overview

This project is a **Pandas-based data analysis system** focused on extracting **business insights from e-commerce data**.

It performs:

* Data loading from CSV
* Aggregation using `groupby()`
* Multi-level analysis
* Business insight generation

Built using **Pandas (Module 3 concepts only)**.

---

## 🎯 Objectives

* Master `groupby()` operations
* Perform data aggregation (`sum`, `mean`, `count`)
* Analyze structured datasets
* Generate meaningful business insights
* Build strong analytical thinking

---

## 🧠 Features

### 1. Data Loading

* Load e-commerce dataset using `pandas.read_csv()`

---

### 2. Data Analysis

* Total sales per category
* Average order value
* Most sold product
* Region-wise sales

---

### 3. Aggregations

* Single-column grouping
* Multi-column grouping
* Value counts

---

### 4. Business Insights

* Best performing category
* Weakest region
* High-value customers

---

## 📂 Project Structure

```bash id="struct_pa1"
lab_pandas_analysis/
│
├── main.py          # Entry point (controls workflow)
├── loader.py        # Loads dataset
├── analyzer.py      # Aggregation logic
├── insights.py      # Business insights
├── utils.py         # Helper functions
├── data/
│   └── ecommerce.csv
├── requirements.txt # Dependencies
└── README.md        # Documentation
```

---

## ⚙️ Requirements

* Python 3.x
* Pandas

---

## 🛠️ Environment Setup

### Step 1: Clone Repository

```bash id="clone_pa1"
git clone <your-repo-link>
cd lab_pandas_analysis
```

---

### Step 2: Create Virtual Environment (Recommended)

#### 🔹 Windows

```bash id="venv_pa1"
python -m venv venv
venv\Scripts\activate
```

#### 🔹 Mac/Linux

```bash id="venv_pa2"
python3 -m venv venv
source venv/bin/activate
```

---

### Step 3: Install Dependencies

```bash id="install_pa1"
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash id="run_pa1"
python main.py
```

---

## 💻 Sample Output (Example)

```bash id="output_pa1"
=== Pandas Data Analysis Lab ===

=== Total Sales per Category ===
Electronics    7450
Furniture      3000

Average Order Value: 650.0

Most Sold Product: Laptop

=== Region-wise Sales ===
North    2650
South    3000
East     3150
West     1650

Best Category: Electronics (Sales=7450)
Weakest Region: West (Sales=1650)

=== High Value Customers ===
Amit    2650
Riya    3000
John    3150
Sara    1650
```

---

## 📸 Execution Proof (Screenshots)

> Added real screenshots after running project

 🔹 Dataset Loaded
 🔹 Aggregation Results
 🔹 Region-wise Sales Output
 🔹 Insights Output

 ![Screenshot](./screenshots/Screenshot%20(1288).png)

---

## 🧠 Learning Outcomes

* Mastery of `groupby()` operations
* Data aggregation and summarization
* Multi-level data analysis
* Extracting business insights from data
* Structured data pipeline thinking

---

## ⚠️ Important Note

This project is about **thinking, not just coding**.

👉 Don’t just run it
👉 Ask questions about the data
👉 Try to explain the results

That’s what real analysts do.

---

## 🚀 Future Improvements

* Add revenue column (`sales * quantity`)
* Create pivot tables
* Add visualization (Matplotlib / Seaborn)
* Export insights to file

---

## 👨‍💻 Author

**Prathmesh Joshi**

---

## ⭐ Support

If this lab helped and you like it, give it a ⭐ and keep building! 
