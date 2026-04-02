# 🧪 LAB 2 — Relationship & Correlation Analysis

## 🚀 Overview

This project performs **Exploratory Data Analysis (EDA)** focused on identifying relationships between variables.

It helps answer key analytical questions:

👉 **What variables are related?**
👉 **Which features influence others?**

---

## 🎯 Objective

* Analyze relationships between numerical variables
* Identify correlations
* Compare categories visually
* Explore multi-variable interactions

---

## 🧠 Concepts Used

* Correlation Matrix (`df.corr()`)
* Seaborn Heatmap
* Scatter Plot (relationship analysis)
* Pairplot (multi-variable visualization)
* Boxplot (categorical comparison)

---

## 📂 Project Structure

```id="c3y7zq"
lab_eda_relationships/
│
├── main.py              # Runs full workflow
├── loader.py            # Loads dataset
├── analyzer.py          # Correlation & grouping logic
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

```bash id="u9n3wp"
git clone https://github.com/your-username/lab_eda_relationships.git
cd lab_eda_relationships
```

---

### 2️⃣ Create Virtual Environment

```bash id="y1k8fz"
python -m venv venv
```

---

### 3️⃣ Activate Environment

#### ▶ Windows:

```bash id="r2m6ht"
venv\Scripts\activate
```

#### ▶ Mac/Linux:

```bash id="l7c4dp"
source venv/bin/activate
```

---

### 4️⃣ Install Dependencies

```bash id="x5v2aq"
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash id="g8p1zo"
python main.py
```

---

## 📊 Features

### 🔹 Correlation Analysis

* Computes correlation matrix for numerical features
* Helps identify relationships between variables

### 🔹 Category Analysis

* Groups data by category
* Calculates average Sales and Quantity

---

## 📈 Visualizations

The project generates:

* 📊 Heatmap → Correlation between variables
* 🔵 Scatter Plot → Sales vs Quantity
* 📉 Pairplot → Multi-variable relationships
* 📦 Boxplot → Sales distribution by category

---

## 📸 Execution Proof (Screenshots)

> Add screenshots after running the project

![Screenshot](screenshots/Screenshot%20(1310).png)

---

 Correlation Heatmap

![Heatmap](screenshots/Screenshot%20(1311).png)

---

 Scatter Plot (Sales vs Quantity)

![Scatter](screenshots/Screenshot%20(1312).png)

---

### 📌 Pairplot (Relationships)

![Pairplot](screenshots/Screenshot%20(1313).png)

---

### 📌 Boxplot (Category Comparison)

![Boxplot](screenshots/Screenshot%20(1314).png)

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

* Sales and Quantity may show **positive correlation**
* Certain categories may have **higher variability in sales**
* Outliers can indicate unusual business events
* Pairplots reveal hidden multi-variable patterns

---

## 💥 Skills Demonstrated

* Relationship analysis using EDA
* Correlation interpretation
* Data visualization with Seaborn
* Analytical thinking & pattern recognition
* Structured project development

---

## ⚠️ Future Improvements

* Add statistical tests (correlation significance)
* Use larger real-world datasets
* Add interactive visualizations
* Integrate with dashboard tools

---

## 🙌 Author

**Prathmesh Joshi**

---

## ⭐ Support

If this lab helped and you liked it, give it a ⭐ and keep building!

---
