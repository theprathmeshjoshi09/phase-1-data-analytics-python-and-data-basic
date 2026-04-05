# 🧪 LAB 10 — Data Profiling & Summary Analysis

## 🚀 Overview

This project performs **Exploratory Data Analysis (EDA)** on a dataset to understand its structure, quality, and statistical properties.

It helps answer a critical question:

👉 **“What is inside the data?”**

---

## 🎯 Objective

* Analyze dataset structure
* Identify missing values
* Generate summary statistics
* Understand data distribution
* Detect outliers

---

## 🧠 Concepts Used

* Pandas (`.info()`, `.describe()`)
* Missing value analysis
* Value counts
* Seaborn visualization
* Histogram & Boxplot
* Data profiling techniques

---

## 📂 Project Structure

```id="q2h6bt"
lab_eda_profiling/
│
├── main.py              # Runs full workflow
├── loader.py            # Loads dataset
├── profiler.py          # Data analysis logic
├── visualizer.py        # Visualization logic
│
├── data/
│   └── dataset.csv      # Input dataset
│
└── requirements.txt
```

---

## ⚙️ Environment Setup

### 1️⃣ Clone Repository

```bash id="p2j0sm"
git clone https://github.com/your-username/lab_eda_profiling.git
cd lab_eda_profiling
```

---

### 2️⃣ Create Virtual Environment

```bash id="qz9m1e"
python -m venv venv
```

---

### 3️⃣ Activate Environment

#### ▶ Windows:

```bash id="c7i1e3"
venv\Scripts\activate
```

#### ▶ Mac/Linux:

```bash id="l0p4d9"
source venv/bin/activate
```

---

### 4️⃣ Install Dependencies

```bash id="t8n2f6"
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash id="r3k7h1"
python main.py
```

---

## 📊 Features

### 🔹 Dataset Profiling

* Shape of dataset
* Column names
* Data types

### 🔹 Missing Values Analysis

* Count of null values
* Percentage of missing data

### 🔹 Summary Statistics

* Mean
* Median
* Standard deviation
* Min / Max values

### 🔹 Category Analysis

* Value counts for categorical data

---

## 📈 Visualizations

The project generates:

* 📊 Histogram → Sales distribution
* 📦 Boxplot → Outlier detection

---

## 📸 Execution Proof (Screenshots)

> Add screenshots after running the project

![screenshots](screenshots/Screenshot%20(1306).png)
![screenshots](screenshots/Screenshot%20(1307).png)

### 📌 Sales Distribution (Histogram)

![Histogram](screenshots/Screenshot%20(1308).png)

---

### 📌 Outlier Detection (Boxplot)

![Boxplot](screenshots/Screenshot%20(1309).png)

---

## 🧪 Dataset Description

| Column   | Description          |
| -------- | -------------------- |
| Date     | Transaction date     |
| Category | Product category     |
| Sales    | Revenue generated    |
| Quantity | Number of items sold |

---

## 🔍 Key Insights (Example)

* Data distribution may be **skewed or normal**
* Outliers can indicate **extreme sales events**
* Missing values affect data quality
* Category frequency shows **dominant segments**

---

## 💥 Skills Demonstrated

* Exploratory Data Analysis (EDA)
* Data cleaning awareness
* Statistical understanding
* Visualization using Seaborn
* Structured project design

---

## ⚠️ Future Improvements

* Handle missing values more intelligently
* Add correlation analysis
* Generate automated EDA reports
* Use real-world large datasets

---

## 🙌 Author

**Prathmesh Joshi**

---

## ⭐ Support

If you liked it, give it a ⭐ and keep building!


