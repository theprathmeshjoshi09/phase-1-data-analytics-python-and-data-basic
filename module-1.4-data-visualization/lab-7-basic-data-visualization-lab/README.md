# 📊 Basic Data Visualization Lab (Matplotlib)

## 🚀 Project Overview

This project focuses on **visualizing sales data using Matplotlib** to extract meaningful insights.

It converts raw data into **clear visual representations** such as:

* Sales trends over time
* Category-wise comparisons
* Distribution of sales values

Built using:

* **Pandas** (data handling)
* **Matplotlib** (data visualization)

---

## 🎯 Objectives

* Understand how to visualize data effectively
* Learn different types of plots
* Interpret trends and patterns from graphs
* Build foundation for data storytelling

---

## 🧠 Features

### 1. Data Loading

* Load dataset using `pandas.read_csv()`
* Convert date column to datetime

---

### 2. Visualizations

#### 📈 Line Plot

* Shows **sales trend over time**

#### 📊 Bar Chart

* Compares **sales across categories**

#### 📉 Histogram

* Displays **distribution of sales values**

---

### 3. Output

* Visual plots displayed using Matplotlib
* Clear labels, titles, and formatting

---

## 📂 Project Structure

```bash id="struct_viz1"
lab_visualization_basic/
│
├── main.py          # Entry point (workflow controller)
├── data_loader.py   # Loads dataset
├── plots.py         # Visualization logic
├── utils.py         # Helper functions
├── data/
│   └── sales.csv
├── requirements.txt # Dependencies
└── README.md        # Documentation
```

---

## ⚙️ Requirements

* Python 3.x
* Pandas
* Matplotlib

---

## 🛠️ Environment Setup

### Step 1: Clone the Repository

```bash id="clone_viz1"
git clone <your-repo-link>
cd lab_visualization_basic
```

---

### Step 2: Create Virtual Environment (Recommended)

#### 🔹 Windows

```bash id="venv_viz1"
python -m venv venv
venv\Scripts\activate
```

#### 🔹 Mac/Linux

```bash id="venv_viz2"
python3 -m venv venv
source venv/bin/activate
```

---

### Step 3: Install Dependencies

```bash id="install_viz1"
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash id="run_viz1"
python main.py
```

---

## 💻 Sample Output (Example)

```bash id="output_viz1"
=== Basic Data Visualization Lab ===

=== Data Preview ===
        date     category  sales
0 2024-01-01  Electronics   1200
1 2024-01-02  Electronics    800
...

(Line plot, bar chart, and histogram windows will open)
```

---

## 📸 Execution Proof (Screenshots)

> Added real screenshots after running your project
  
  ![Screenshot](./screenshots/Screenshot%20(1291).png)

 🔹 Line Plot — Sales Trend
    
   ![Screenshot](./screenshots/Screenshot%20(1293).png)

 🔹 Bar Chart — Sales by Category
  
   ![Screenshot](./screenshots/Screenshot%20(1292).png)
 
 🔹 Histogram — Sales Distribution

   ![Screenshot](./screenshots/Screenshot%20(1294).png)

---

## 🧠 Learning Outcomes

* Understanding different types of plots
* Interpreting trends and patterns visually
* Comparing categories using charts
* Identifying data distribution and outliers
* Building foundation for data storytelling

---

## 🚀 Future Improvements

* Add multiple categories
* Add region-wise analysis
* Improve styling and aesthetics
* Save plots as images
* Add interactive dashboards

---

## 👨‍💻 Author

**Prathmesh Joshi**

---

## ⭐ Support

If you liked it, give it a ⭐ and keep building!
