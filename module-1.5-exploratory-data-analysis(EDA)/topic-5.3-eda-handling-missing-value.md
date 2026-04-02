# 🚀 Module 1.5 — Exploratory Data Analysis (EDA)

## Topic 5.3: Handle Missing Values

---

# 🔥 Real-World Perspective

In real-world datasets:

👉 Missing values are everywhere

* incomplete forms
* system errors
* data collection issues

---

## 🧠 Real Insight

👉 Missing data is not just a problem
👉 It is also a **signal**

---

# What is this step?

Handling missing values is a crucial step in data analysis.

👉 Missing data can distort results and lead to incorrect conclusions if ignored

---

# 📊 Data Analyst Perspective

Used for:

* improving data quality
* avoiding bias
* ensuring accurate analysis

---

# 🔹 Types of Missing Data

---

## 1. Null / NaN

* Standard missing values
* Represented as NaN

---

## 2. Empty Strings

* Stored as ""
* Common in categorical data

---

## 📊 Real Insight

👉 Missing data is not always obvious
👉 You must detect it carefully

---

# 🔹 Methods to Handle Missing Values

---

## 1. Remove Missing Data

```python id="mv1"
df.dropna()
```

* Removes rows with missing values

👉 Use when missing data is minimal

---

## 📊 Real Insight

👉 Removing too much data = loss of information

---

## 2. Fill Missing Values

```python id="mv2"
df.fillna()
```

### Numerical Data:

* Mean
* Median

### Categorical Data:

* Mode

---

## 📊 Real Insight

👉 Median is safer when data has outliers

---

## 🔥 Interview Thinking

* Why not always use mean?
  👉 sensitive to outliers

---

## 3. Forward / Backward Fill

* Forward Fill → use previous value
* Backward Fill → use next value

👉 Useful in time-series data

---

## 📊 Real Insight

👉 Works only when order matters (time-based data)

---

# 🔹 When to Use What?

* Small missing → Remove
* Large missing → Fill
* Time-based data → Forward/Backward fill

---

## 📊 Real Insight

👉 No single correct method
👉 Depends on data + problem

---

# 🔹 Real Workflow Example

```python id="mv3"
df.isnull().sum()

df["age"] = df["age"].fillna(df["age"].median())

df = df.dropna(subset=["important_column"])
```

---

👉 Identify → decide → handle

---

# 🔹 Analyst Thinking

Ask:

* Why is data missing?
* Is it random or systematic?
* Will this affect my analysis?

👉 "Why is this data missing?"

---

# 🧠 Real Mini Case Study

## Problem: Customer Dataset

```text id="mv4"
Issue:
- Missing income values  

Solution:
- Fill with median  

Reason:
- income data is skewed  
```

---

👉 Better accuracy

---

# ⚠️ Common Mistakes

❌ Ignoring missing values
❌ Blindly filling data
❌ Removing too many rows
❌ Using wrong method

---

# 💡 Key Takeaways

✔ Always detect missing values
✔ Choose method carefully
✔ Understand why data is missing
✔ Avoid blind assumptions

---

# 🎯 Final Insight

👉 Missing data is not just empty
👉 It carries meaning

---

# Summary

In this lesson I learned:

* Types of missing data
* Methods to handle missing values
* When to use each method
* Real-world decision-making

---
