# 🚀 Module 1.3 — Pandas 

## Topic 08: Merging & Combining Data

---

# 🔥 Real-World Perspective

In real-world analytics:

👉 Data comes from multiple sources
👉 You MUST combine them

Examples:

* Customers + Orders
* Sales + Products
* Users + Transactions

---

## 🧠 Real Insight

👉 This is basically **SQL JOIN inside Pandas**

---

# 🔹 1. Introduction 

Merging & Combining allows you to:
👉 join datasets
👉 enrich data
👉 perform relational operations

---

## 📊 Data Analyst Perspective

Used for:

* combining datasets
* building full reports
* data integration

---

# 🔹 2. merge() 

---

## 🔸 2.1 Basic Merge

```python id="merge1"
import pandas as pd

df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["A", "B", "C"]
})

df2 = pd.DataFrame({
    "ID": [1, 2, 4],
    "Salary": [50000, 60000, 70000]
})

merged = pd.merge(df1, df2, on="ID")
print(merged)
```

---

## 📊 Real Use Case

👉 Combine:

* customer info
* salary/order data

---

## 🔥 Insight

👉 Merge happens on **common key**

---

# 🔍 Interview Thinking

* What is merge?
  👉 join datasets

---

# 🔹 3. Join Types 

---

## 🔸 Inner Join (Default)

```python id="merge2"
pd.merge(df1, df2, on="ID", how="inner")
```

👉 Only matching rows

---

## 🔸 Left Join

```python id="merge3"
pd.merge(df1, df2, on="ID", how="left")
```

👉 All left + matches

---

## 🔸 Right Join

```python id="merge4"
pd.merge(df1, df2, on="ID", how="right")
```

👉 All right + matches

---

## 📊 Real Insight

| Join  | Meaning                |
| ----- | ---------------------- |
| Inner | common data            |
| Left  | keep main dataset      |
| Right | keep secondary dataset |

---

## 🔥 Pro Insight

👉 Left join is **most used in industry**

---

# 🔍 Interview Thinking

* Difference between joins?
  👉 data retention logic

---

# 🔹 4. concat() (Enhanced)

---

## 🔸 4.1 Row-wise

```python id="merge5"
pd.concat([df1, df2])
```

---

## 🔸 4.2 Column-wise

```python id="merge6"
pd.concat([df1, df2], axis=1)
```

---

## 📊 Applications

* stacking datasets
* combining features

---

## 🔥 Insight

👉 concat ≠ merge

---

# 🔍 Interview Thinking

* merge vs concat?
  👉 key vs axis

---

# 🔹 5. Workflow Example 

---

## 📊 Real Pipeline

```python id="merge7"
df1 = pd.read_csv("customers.csv")
df2 = pd.read_csv("orders.csv")

df = pd.merge(df1, df2, on="CustomerID", how="inner")

print(df.head())
```

---

👉 Real-world dataset integration

---

# 🧠 Real Mini Case Study

## Problem: Customer + Orders Analysis

```python id="merge8"
customers = pd.read_csv("customers.csv")
orders = pd.read_csv("orders.csv")

data = pd.merge(customers, orders, on="CustomerID", how="left")
```

---

👉 Insight:

* customer behavior
* purchase patterns

---

# 🔍 Interview Thinking (Added Layer)

* What is merge?
  👉 combining datasets

* Most used join?
  👉 left join

---

# ⚠️ Common Mistakes

* Wrong join key ❌
* Data duplication after merge ❌
* Confusing merge and concat ❌

---

# 💡 Key Takeaways

✔ merge → combine using key
✔ joins → control data
✔ concat → stack data
✔ essential for real datasets

---

# 🎯 Final Insight

👉 Real data is always split
👉 Your job = combine it correctly

---

# Summary 

In this lesson I learned:

* merge()
* join types
* concat()
* dataset integration
* real-world data combination

---
