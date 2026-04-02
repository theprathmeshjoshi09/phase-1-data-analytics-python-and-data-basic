# 🚀 Pandas Business Intelligence CLI

## 📊 Project Overview

The **Pandas Business Intelligence CLI** is a command-line data analysis system built using **Pandas (Module 3 concepts)**.

It simulates a real-world data pipeline that:

* Loads raw business data
* Cleans and preprocesses it
* Performs analysis using Pandas
* Generates meaningful business insights

This project represents a **complete data analysis workflow** used in real-world analytics.

---

## 🎯 Objectives

* Build an end-to-end data analysis pipeline
* Apply data cleaning techniques on messy datasets
* Perform aggregation and trend analysis
* Generate actionable business insights
* Strengthen analytical thinking

---

## 🧠 Features

### 1. Data Loading

* Load dataset from CSV using `pandas.read_csv()`

---

### 2. Data Cleaning

* Convert data types (`to_numeric`, `to_datetime`)
* Handle missing values (`fillna`)
* Remove duplicates
* Filter invalid values

---

### 3. Data Analysis

* Summary statistics (`describe`)
* Revenue calculation (`sales × quantity`)
* Category-wise analysis
* Region-wise analysis
* Time-based trend analysis

---

### 4. Insights Generation

* Best performing category
* Worst performing category
* Best performing region
* Detection of anomalies (unusual sales)

---

## 📂 Project Structure

```bash id="struct_pbi"
pandas_data_analyzer/
│
├── main.py          # Entry point (workflow controller)
├── loader.py        # Loads dataset
├── cleaner.py       # Data cleaning logic
├── analyzer.py      # Analysis logic
├── insights.py      # Business insights
├── utils.py         # Helper functions
├── data/
│   └── dataset.csv
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

```bash id="clone_pbi"
git clone <your-repo-link>
cd pandas_data_analyzer
```

---

### Step 2: Create Virtual Environment (Recommended)

#### 🔹 Windows

```bash id="venv_pbi1"
python -m venv venv
venv\Scripts\activate
```

#### 🔹 Mac/Linux

```bash id="venv_pbi2"
python3 -m venv venv
source venv/bin/activate
```

---

### Step 3: Install Dependencies

```bash id="install_pbi"
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash id="run_pbi"
python main.py
```

---

## 💻 Example Usage

```bash id="usage_pbi"
=== Pandas Business Intelligence CLI ===

--- Cleaning Completed ---
Dataset size: (12, 8)

=== Revenue by Category ===
Electronics    8500
Furniture      3000

=== Revenue by Region ===
North    4000
South    3500
East     3000
West     1000

Best Category: Electronics (8500)
Worst Category: Furniture (3000)
Best Region: North (4000)

=== Anomalies Detected ===
(order with unusually high sales)
```

---

## 📸 Execution Proof (Screenshots)

> Add real screenshots after running your project

 🔹 Raw Dataset / Input
 🔹 Cleaned Data Output
 🔹 Analysis Results (Category & Region)
 🔹 Insights Output
 🔹 Anomaly Detection

 ![Screenshot](./screenshots/Screenshot%20(1290).png)
 ![Screenshot](./screenshots/Screenshot%20(1291).png)

---

## 🧠 Learning Outcomes

* Real-world data cleaning using Pandas
* Handling inconsistent and messy datasets
* Performing aggregation and trend analysis
* Building insight-driven systems
* Understanding business data patterns

---

## ⚠️ Important Note

This project is about **thinking like an analyst**, not just writing code.

👉 Don’t just run it
👉 Analyze results
👉 Ask: *What does this data mean?*

---

## 🚀 Future Improvements

* Monthly and seasonal trend analysis
* Data visualization (Matplotlib / Seaborn)
* Export insights to CSV or reports
* Build dashboard (Streamlit / Power BI)

---

## 👨‍💻 Author

**Prathmesh Joshi**

---

## ⭐ Support

If this project helped and you liked it, give it a ⭐ and keep building!
