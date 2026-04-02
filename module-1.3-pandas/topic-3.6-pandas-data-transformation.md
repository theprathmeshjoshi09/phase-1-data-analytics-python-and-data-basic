# 🚀 Module 1.3 — Pandas 

## Topic 3.6: Data Transformation

---

# 🔥 Real-World Perspective

After cleaning data:

👉 You don’t directly analyze it
👉 You transform it into useful features

---

## 🧠 Real Insight

👉 Data transformation = **turning raw data into insights-ready data**

---

# 🔹 1. Introduction 

Data Transformation involves:
👉 modifying data
👉 creating new features
👉 preparing datasets

---

## 📊 Data Analyst Perspective

Used for:

* feature engineering
* business calculations
* data restructuring

---

# 🔹 2. Sorting Data 

---

## 🔸 2.1 sort_values()

```python id="trans1"
df.sort_values(by="Age")
```

---

## 📊 Descending

```python id="trans2"
df.sort_values(by="Age", ascending=False)
```

---

## 📊 Real Use Case

👉 Find:

* top customers
* highest sales

---

## 🔥 Insight

👉 Sorting helps identify extremes

---

# 🔍 Interview Thinking

* Why sorting important?
  👉 ranking analysis

---

# 🔹 3. Renaming Columns 

---

## 🔸 3.1 rename()

```python id="trans3"
df.rename(columns={"OldName": "NewName"}, inplace=True)
```

---

## 📊 Real Use Case

👉 Make column names:

* readable
* consistent

---

## 🔥 Insight

👉 Clean column names = clean code

---

# 🔍 Interview Thinking

* Why rename columns?
  👉 readability

---

# 🔹 4. Creating New Columns (Feature Engineering) 🔥

---

## 📊 Real Use Case

```python id="trans4"
df["Total"] = df["Quantity"] * df["Price"]
```

---

## 📊 Applications

* revenue calculation
* profit calculation
* KPI creation

---

## 🔥 Insight

👉 This is **core of analytics work**

---

# 🔍 Interview Thinking

* What is feature engineering?
  👉 creating new variables

---

# 🔹 5. apply() 

---

## 📊 Real Use Case

```python id="trans5"
df["Age"] = df["Age"].apply(lambda x: x + 1)
```

---

## 📊 Applications

* custom transformations
* complex logic

---

## 🔥 Insight

👉 Powerful but slower than vectorization

---

# 🔍 Interview Thinking

* When to use apply?
  👉 custom logic

---

# 🔹 6. map() (Enhanced)

---

## 📊 Real Use Case

```python id="trans6"
df["Status"] = df["Score"].map({
    90: "Excellent",
    80: "Good"
})
```

---

## 📊 Applications

* value mapping
* category labeling

---

## 🔥 Insight

👉 Cleaner than multiple conditions

---

# 🔍 Interview Thinking

* map vs apply?
  👉 mapping vs function

---

# 🔹 7. Workflow Example 

---

## 📊 Real Pipeline

```python id="trans7"
import pandas as pd

df = pd.read_csv("data.csv")

# Sort
df = df.sort_values(by="Age")

# Feature engineering
df["Total"] = df["Quantity"] * df["Price"]

# Transformation
df["Age"] = df["Age"].apply(lambda x: x + 1)
```

---

👉 Real-world transformation pipeline

---

# 🧠 Real Mini Case Study

## Problem: Sales Feature Engineering

```python id="trans8"
df = pd.read_csv("sales.csv")

df["Revenue"] = df["Price"] * df["Quantity"]
df["Category"] = df["Revenue"].apply(lambda x: "High" if x > 5000 else "Low")
```

---

👉 Business insights creation

---

# 🔍 Interview Thinking (Added Layer)

* What is transformation?
  👉 modifying data

* Most important use?
  👉 feature engineering

---

# ⚠️ Common Mistakes

* Overusing apply() ❌
* Not using vectorized operations ❌
* Creating unnecessary columns ❌

---

# 💡 Key Takeaways

✔ Sorting → ranking
✔ rename → clarity
✔ new columns → insights
✔ apply/map → transformations

---

# 🎯 Final Insight

👉 Transformation is where:
data → insight

---

# Summary 

In this lesson I learned:

* Sorting data
* Renaming columns
* Creating new features
* Using apply() and map()
* Real-world transformations

---
