# 🚀 Module 1.3 — Pandas 

## Topic 3.13: Pandas Categorical Data

---

# 🔥 Real-World Perspective

In real datasets, many columns are **categorical**:

* Gender
* City
* Product Category
* Status (Active/Inactive)

---

## 🧠 Real Insight

👉 Treating categorical data correctly:

* improves performance
* reduces memory usage
* enables better analysis

---

# 🔹 1. Introduction (Enhanced)

Categorical data represents:
👉 discrete values
👉 fixed set of categories

---

## 📊 Data Analyst Perspective

Used for:

* segmentation
* grouping
* classification

---

# 🔹 2. Creating Categorical Data

---

## 🔸 2.1 Convert to Category

```python id="cat1"
df["Category"] = df["Category"].astype("category")
```

---

## 📊 Real Use Case

👉 Convert:

* product types
* regions
* labels

---

## 🔥 Insight

👉 Reduces memory usage significantly

---

# 🔍 Interview Thinking

* Why use categorical type?
  👉 memory + performance

---

# 🔹 3. Category Properties 

---

## 📊 View Categories

```python id="cat2"
df["Category"].cat.categories
```

---

## 📊 View Codes

```python id="cat3"
df["Category"].cat.codes
```

---

## 🔥 Insight

👉 Internally stored as numbers → faster

---

# 🔹 4. Ordering Categories 

---

## 📊 Real Use Case

```python id="cat4"
df["Size"] = pd.Categorical(
    df["Size"],
    categories=["Small", "Medium", "Large"],
    ordered=True
)
```

---

## 📊 Applications

* ranking categories
* sorting data

---

## 🔥 Insight

👉 Enables meaningful comparisons

---

# 🔍 Interview Thinking

* Why ordered categories?
  👉 logical comparison

---

# 🔹 5. Adding / Removing Categories 

---

## 📊 Add Category

```python id="cat5"
df["Category"] = df["Category"].cat.add_categories(["New"])
```

---

## 📊 Remove Category

```python id="cat6"
df["Category"] = df["Category"].cat.remove_categories(["Old"])
```

---

## 📊 Remove Unused

```python id="cat7"
df["Category"] = df["Category"].cat.remove_unused_categories()
```

---

## 🔥 Insight

👉 Keeps data clean and optimized

---

# 🔹 6. Value Counts with Categories 

---

## 📊 Real Use Case

```python id="cat8"
df["Category"].value_counts()
```

---

## 📊 Applications

* frequency analysis
* category distribution

---

# 🔹 7. Workflow Example 

---

## 📊 Real Pipeline

```python id="cat9"
import pandas as pd

df = pd.read_csv("data.csv")

df["City"] = df["City"].astype("category")

print(df["City"].value_counts())
```

---

👉 Efficient category handling

---

# 🧠 Real Mini Case Study

## Problem: Customer Segmentation

```python id="cat10"
df = pd.read_csv("customers.csv")

df["Segment"] = df["Segment"].astype("category")

print(df.groupby("Segment")["Revenue"].mean())
```

---

👉 Business insight:

* which segment generates more revenue

---

# 🔍 Interview Thinking (Added Layer)

* What is categorical data?
  👉 discrete values

* Why important?
  👉 memory + speed

---

# ⚠️ Common Mistakes

* Treating categorical as string ❌
* Not ordering categories ❌
* Ignoring memory optimization ❌

---

# 💡 Key Takeaways

✔ categorical → optimized storage
✔ .cat → category operations
✔ ordering → meaningful analysis
✔ essential for segmentation

---

# 🎯 Final Insight

👉 Categorical data = **efficient + structured analysis**

---

# Summary 

In this lesson I learned:

* Categorical data concept
* Converting to category
* Category operations
* Ordering categories
* Real-world applications

---
