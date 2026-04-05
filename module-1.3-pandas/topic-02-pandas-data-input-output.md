# 🚀 Module 1.3 — Pandas 

## Topic 02: Data Input / Output (I/O)

---

# 🔥 Real-World Perspective

In real-world data analytics:

👉 You NEVER create data manually
👉 You always **load data from external sources**

Examples:

* CSV files
* Excel sheets
* APIs (JSON)
* Databases

---

## 🧠 Real Insight

👉 Data I/O = **entry + exit point of data pipeline**

Without this:
❌ no dataset
❌ no analysis

---

# 🔹 1. Data Input / Output 

Data I/O means:
👉 reading data
👉 writing data

---

## 📊 Data Analyst Perspective

Typical workflow:

1. Load dataset
2. Clean & analyze
3. Export results

---

# 🔹 2. Reading Data 

---

## 🔸 2.1 read_csv() 

Used to read CSV files

---

## 📊 Real Use Case

```python id="io1"
import pandas as pd

df = pd.read_csv("sales.csv")
print(df.head())
```

---

## 📊 Real Applications

👉 Used for:

* sales datasets
* logs
* reports

---

## 🔥 Key Parameters (Thinking)

* filepath → where file is
* sep → delimiter
* header → column names

---

## 💡 Real Insight

👉 CSV is the **most common format in industry**

---

# 🔍 Interview Thinking

* Why CSV widely used?
  👉 simple + universal

---

# 🔸 2.2 read_excel() 

---

## 📊 Real Use Case

```python id="io2"
df = pd.read_excel("data.xlsx")
```

---

## 📊 Applications

👉 Used in:

* business reports
* finance data

---

## 🔥 Insight

👉 Excel = most used business format

---

# 🔍 Interview Thinking

* Difference CSV vs Excel?
  👉 CSV simple, Excel structured

---

# 🔸 2.3 read_json() 

---

## 📊 Real Use Case

```python id="io3"
df = pd.read_json("data.json")
```

---

## 📊 Applications

👉 Used in:

* APIs
* web data

---

## 🔥 Insight

👉 JSON = common in modern systems

---

# 🔹 3. Writing Data 

---

## 🔸 3.1 to_csv() 

```python id="io4"
df.to_csv("output.csv", index=False)
```

---

## 📊 Applications

* exporting reports
* saving processed data

---

## 🔥 Insight

👉 `index=False` avoids extra column

---

# 🔸 3.2 to_excel() (Enhanced)

```python id="io5"
df.to_excel("output.xlsx", index=False)
```

---

## 📊 Real Use Case

👉 sending reports to business teams

---

# 🔸 3.3 to_json() 

```python id="io6"
df.to_json("output.json")
```

---

## 📊 Real Use Case

👉 APIs / data exchange

---

# 🔹 4. Complete Workflow 

---

## 📊 Real Pipeline Example

```python id="io7"
import pandas as pd

# Step 1: Load data
df = pd.read_csv("sales.csv")

# Step 2: Process
df["Total"] = df["Quantity"] * df["Price"]

# Step 3: Save
df.to_csv("processed_sales.csv", index=False)
```

---

## 🔥 Real Insight

👉 This is EXACTLY how real projects work

---

# 🧠 Real Mini Case Study

## Problem: Sales Report Generation

```python id="io8"
df = pd.read_csv("sales.csv")

df["Revenue"] = df["Price"] * df["Quantity"]

df.to_excel("report.xlsx", index=False)
```

👉 Business reporting workflow

---

# 🔍 Interview Thinking (Added Layer)

* What is Data I/O?
  👉 reading and writing data

* Most used function?
  👉 read_csv()

---

# ⚠️ Common Mistakes

* Wrong file path ❌
* Forgetting index=False ❌
* Incorrect separator ❌

---

# 💡 Key Takeaways

✔ read_csv → most used
✔ read_excel → business data
✔ read_json → API data
✔ to_csv / to_excel → export

---

# 🎯 Final Insight

👉 Data I/O is not optional
👉 It is the **starting point of every analysis**

---

# Summary 

In this lesson I learned:

* Reading data (CSV, Excel, JSON)
* Writing data (CSV, Excel, JSON)
* Real-world data workflow
* Data pipeline basics

---
