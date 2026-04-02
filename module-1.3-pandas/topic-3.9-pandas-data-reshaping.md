# 🚀 Module 1.3 — Pandas 

## Topic 3.9: Reshaping Data

---

# 🔥 Real-World Perspective

In real-world analytics:

👉 Data rarely comes in the format you need
👉 You must reshape it

Examples:

* Convert raw data → report format
* Create pivot tables
* Prepare dashboards

---

## 🧠 Real Insight

👉 Reshaping = **changing structure without changing meaning**

---

# 🔹 1. Introduction 

Reshaping data means:
👉 changing layout
👉 restructuring format

---

## 📊 Data Analyst Perspective

Used for:

* reporting
* dashboards
* data transformation

---

# 🔹 2. pivot() (Enhanced)

---

## 🔸 2.1 Basic Pivot

```python id="reshape1"
import pandas as pd

df = pd.DataFrame({
    "Date": ["2024-01", "2024-01", "2024-02"],
    "Product": ["A", "B", "A"],
    "Sales": [100, 200, 150]
})

pivot_df = df.pivot(index="Date", columns="Product", values="Sales")
print(pivot_df)
```

---

## 📊 Real Use Case

👉 Create reports like:

| Date | Product A | Product B |
| ---- | --------- | --------- |

---

## 🔥 Insight

👉 pivot = reshape without aggregation

---

# 🔍 Interview Thinking

* What is pivot?
  👉 reshape data

---

# 🔹 3. pivot_table() (Enhanced)

---

## 📊 Real Use Case

```python id="reshape2"
df.pivot_table(index="Date", columns="Product", values="Sales", aggfunc="sum")
```

---

## 📊 Applications

* summarizing data
* handling duplicates

---

## 🔥 Insight

👉 pivot_table = pivot + aggregation

---

# 🔍 Interview Thinking

* pivot vs pivot_table?
  👉 aggregation support

---

# 🔹 4. melt() (Enhanced)

---

## 📊 Real Use Case

```python id="reshape3"
pd.melt(df, id_vars=["Date"], value_vars=["A", "B"])
```

---

## 📊 Applications

👉 Convert:

* wide → long format

---

## 🔥 Insight

👉 Required for:

* ML models
* visualization

---

# 🔍 Interview Thinking

* melt purpose?
  👉 reshape to long format

---

# 🔹 5. stack() and unstack() 

---

## 🔸 stack()

```python id="reshape4"
df.stack()
```

---

👉 columns → rows

---

## 🔸 unstack()

```python id="reshape5"
df.unstack()
```

---

👉 rows → columns

---

## 📊 Applications

* multi-level data
* advanced reshaping

---

# 🔹 6. Key Differences (Enhanced)

| Function    | Purpose             |
| ----------- | ------------------- |
| pivot       | reshape             |
| pivot_table | reshape + aggregate |
| melt        | wide → long         |
| stack       | columns → rows      |
| unstack     | rows → columns      |

---

# 🧠 Real Mini Case Study

## Problem: Sales Report Format

```python id="reshape6"
df = pd.read_csv("sales.csv")

pivot = df.pivot_table(index="Region", columns="Product", values="Sales", aggfunc="sum")

print(pivot)
```

---

👉 Used in:

* dashboards
* business reports

---

# 🔍 Interview Thinking (Added Layer)

* Why reshaping needed?
  👉 reporting + analysis

* Most used function?
  👉 pivot_table

---

# ⚠️ Common Mistakes

* Using pivot with duplicate data ❌
* Confusing melt and pivot ❌
* Not understanding data format ❌

---

# 💡 Key Takeaways

✔ pivot → reshape
✔ pivot_table → reshape + aggregate
✔ melt → long format
✔ stack/unstack → advanced reshape

---

# 🎯 Final Insight

👉 Reshaping is what makes data:

* readable
* presentable
* useful

---

# Summary 

In this lesson I learned:

* pivot()
* pivot_table()
* melt()
* stack/unstack()
* Real-world reshaping

---
