# 📊 Data Visualization Dashboard CLI

## 🚀 Overview

This project is a **Command-Line Data Visualization Dashboard** built using Python.

It allows users to:

* Load a dataset
* Clean and process data
* Perform analysis
* Generate multiple visual insights
* Save plots as images

👉 This project demonstrates **data storytelling using visualizations**, a critical skill for data analysts.

---

## 🎯 Objective

Build a system that:

* Processes raw data
* Extracts insights
* Communicates results visually

---

## 🧠 Concepts Used

* Pandas (data handling)
* Matplotlib (visualization)
* Data cleaning (duplicates, null values)
* GroupBy operations
* CLI-based execution

---

## 📂 Project Structure

```id="r9c6w3"
visual_dashboard_cli/
│
├── main.py              # Entry point
├── loader.py            # Load dataset
├── cleaner.py           # Clean data
├── analyzer.py          # Analyze data
├── visualizer.py        # Create plots
├── utils.py             # Utility functions
│
├── data/
│   └── dataset.csv      # Input data
│
├── outputs/             # Saved plots (auto-generated)
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Environment Setup

### 1️⃣ Clone the Repository

```bash id="u8eh8f"
git clone https://github.com/your-username/visual_dashboard_cli.git
cd visual_dashboard_cli
```

---

### 2️⃣ Create Virtual Environment

```bash id="3m0p1q"
python -m venv venv
```

---

### 3️⃣ Activate Environment

#### ▶ Windows:

```bash id="e9v2ah"
venv\Scripts\activate
```

#### ▶ Mac/Linux:

```bash id="2d1a4k"
source venv/bin/activate
```

---

### 4️⃣ Install Dependencies

```bash id="lf5n6g"
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash id="m4k2l1"
python main.py
```

---

## 📊 Features

### 🔹 Data Handling

* Load dataset from CSV
* Clean missing values and duplicates

### 🔹 Analysis

* Total revenue calculation
* Category-wise performance
* Time-based trends

### 🔹 Visualization

The system generates:

* 📈 Line Chart → Sales Trend
* 📊 Bar Chart → Category Performance
* 📉 Histogram → Sales Distribution
* 🔵 Scatter Plot → Sales vs Quantity

---

## 💾 Output

All plots are automatically saved in:

```id="9w2j3k"
outputs/
```

Files generated:

* `line_chart.png`
* `bar_chart.png`
* `histogram.png`
* `scatter.png`

---

## 📸 Execution Proof (Screenshots)

> Add your screenshots here after running the project

![Screenshots](./screenshots/Screenshot%20(1300).png)

 🔹 Line Chart (Sales Trend)

![Line Chart](./screenshots/Screenshot%20(1301).png)

---

 🔹 Bar Chart (Category Performance)

![Bar Chart](./screenshots/Screenshot%20(1302).png)

---

 🔹 Histogram (Distribution)

![Histogram](./screenshots/Screenshot%20(1303).png)

---

 🔹 Scatter Plot (Sales vs Quantity)

![Scatter Plot](./screenshots/Screenshot%20(1304).png)

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

* Identifies top-performing product category
* Shows whether business is growing over time
* Highlights distribution patterns in sales
* Reveals relationship between quantity and sales

---

## 💥 Skills Demonstrated

* Data analysis using Python
* Data visualization & storytelling
* Project structuring (modular code)
* CLI-based application design

---

## ⚠️ Future Improvements

* Add Seaborn for advanced visuals
* Add interactive dashboard (Streamlit)
* Use real-world large dataset
* Add filtering options (date/category)

---

## 🙌 Author

**Prathmesh Joshi**

---

## ⭐ Support

If you liked it, give it a ⭐ and keep building!

---
