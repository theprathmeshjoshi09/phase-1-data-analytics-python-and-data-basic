# 🚀 Module 1.5 — Exploratory Data Analysis (EDA)

## Topic 02: Data Cleaning

---

# 🔥 Real-World Perspective

In real-world analytics:

👉 60–80% of time is spent on cleaning data

Why?

👉 Because real data is:

* messy
* inconsistent
* incomplete

---

## 🧠 Real Insight

👉 Clean data = correct insights
👉 Dirty data = wrong decisions

---

# What is this step?

Data Cleaning is the process of making raw data usable for analysis.

Raw data is messy. Always.

👉 Cleaning ensures your data is accurate, consistent, and reliable

---

# 📊 Data Analyst Perspective

Used for:

* improving data quality
* ensuring consistency
* preventing wrong conclusions

---

# What comes under cleaning

---

## 1. Remove Duplicates

* Duplicate rows can distort analysis
* Always check and remove them

---

## 📊 Real Insight

👉 Duplicates can:

* inflate metrics
* create bias

---

## 2. Fix Column Names

* Rename columns for clarity
* Use consistent naming format (lowercase, underscores)

---

## 📊 Real Insight

👉 Clean column names = easier analysis

---

## 3. Convert Data Types

* Ensure correct data types for each column

Examples:

* String → Integer
* Object → DateTime

---

## 🔥 Interview Thinking

* Why data types important?
  👉 accuracy + performance

---

## 4. Handle Inconsistent Values

Example:

* "Male", "male", "M" → should be standardized

---

## 📊 Real Insight

👉 Inconsistent data breaks grouping and analysis

---

# 🔹 Tools You Use (Pandas)

```python id="8z9m1v"
df.drop_duplicates()
df.rename()
df.astype()
```

---

# 🔹 Real Workflow Example

```python id="k3x7lm"
df = df.drop_duplicates()

df.columns = df.columns.str.lower()

df["date"] = pd.to_datetime(df["date"])
```

---

👉 Clean → structured → ready

---

# 🔹 Analyst Thinking

Ask:

* Is this data clean and consistent?
* Can I trust this dataset?
* Will errors affect my analysis?

👉 "Is this data reliable enough to trust?"

---

# 🧠 Real Mini Case Study

## Problem: Customer Dataset

```text id="p4m8xz"
Issues:
- duplicate customers  
- inconsistent gender values  

Solution:
- remove duplicates  
- standardize values  
```

---

👉 Improves accuracy

---

# ⚠️ Common Mistakes

❌ Ignoring duplicates
❌ Not fixing data types
❌ Leaving inconsistent values
❌ Messy column names

---

# 💡 Key Takeaways

✔ Remove duplicates
✔ Standardize data
✔ Fix data types
✔ Clean column names
✔ Ensure reliability

---

# 🎯 Final Insight

👉 Data cleaning is not optional
👉 It is the foundation of analysis

---

# Summary

In this lesson I learned:

* Data cleaning process
* Removing duplicates
* Fixing data types
* Handling inconsistencies
* Ensuring data reliability

---
