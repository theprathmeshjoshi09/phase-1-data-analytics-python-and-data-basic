# 🧪 LAB 8 — Advanced Visualization & Comparison

## 🎯 Objective

This lab focuses on building **advanced data visualization skills** using Python.
The goal is to analyze **Sales, Quantity, and Region** data and extract meaningful insights using multiple types of plots.

---

## 🧠 Concepts Covered

* Scatter Plot (relationship between variables)
* Subplots (multi-view comparison)
* Multi-line Chart (time-based trends)
* Bar Chart (categorical comparison)
* Legends & Grid Styling
* Data Aggregation using Pandas

---

## 📊 Problem Statement

Analyze an e-commerce dataset to:

* Compare **Sales vs Quantity**
* Understand **regional performance**
* Identify **sales trends over time**
* Determine **best-performing region**

---

## 📂 Project Structure

```
lab_visualization_advanced/
│
├── main.py              # Runs the full pipeline
├── data_loader.py       # Loads dataset
├── analyzer.py          # Data processing & aggregation
├── plots.py             # Visualization logic
├── data/
│   └── ecommerce.csv    # Dataset
└── requirements.txt
```

---

## ⚙️ Environment Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/lab_visualization_advanced.git
cd lab_visualization_advanced
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

### 3️⃣ Activate Environment

#### ▶ Windows:

```bash
venv\Scripts\activate
```

#### ▶ Mac/Linux:

```bash
source venv/bin/activate
```

---

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
python main.py
```

---

## 📈 Expected Output

The program will generate the following visualizations:

* 📌 Scatter Plot → Sales vs Quantity
* 📌 Subplots → Region-wise comparison
* 📌 Multi-line Chart → Sales trend over time
* 📌 Bar Chart → Total sales per region

Additionally, it will print:

```
🔥 Best performing region: <Region Name>
```

---

## 📸 Execution Proof (Screenshots)

> Added real screenshots below after running the project

 🔹Scatter Plot

![Scatter Plot](screenshots/Screenshot%20(1297).png)

---

 🔹Subplots (Region Comparison)

![Subplots](screenshots/Screenshot%20(1298).png)

---

 🔹Sales Trend (Multi-line Chart)

![Sales Trend](screenshots/Screenshot%20(1299).png)

---

 🔹Region Performance (Bar Chart)

![Bar Chart](screenshots/Screenshot%20(1300).png)

---

## 🧪 Dataset Description

| Column   | Description                    |
| -------- | ------------------------------ |
| Date     | Transaction date               |
| Region   | Sales region (North/South/etc) |
| Sales    | Revenue generated              |
| Quantity | Number of items sold           |

---

## 🔍 Key Insights (Example)

* Some regions generate higher sales with fewer quantities → **high-value transactions**
* Certain regions show consistent growth over time
* Best-performing region identified based on total sales

---

## 🚀 Skills Gained

* Multi-variable data analysis
* Visual storytelling
* Comparative analytics
* Structuring real-world data projects

---

## ⚠️ Future Improvements

* Add Seaborn for advanced styling
* Export plots as image files automatically
* Build interactive dashboard (Streamlit)
* Add larger real-world dataset

---

## 🙌 Author

**Prathmesh Joshi**

---

## ⭐ If you found this useful

If you liked it, give it a ⭐ and keep building!


