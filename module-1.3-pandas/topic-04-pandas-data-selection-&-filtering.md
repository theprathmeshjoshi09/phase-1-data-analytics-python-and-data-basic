# 🚀 Module 1.3 — Pandas 

## Topic 04: Data Selection & Filtering

---

# 🔥 Real-World Perspective

This is where real analysis starts.

👉 You rarely use the full dataset
👉 You always:

* filter rows
* select columns
* extract relevant data

---

## 🧠 Real Insight

👉 70–80% of data work = filtering + selecting

If you master this:
👉 you can handle any dataset

---

# 🔹 1. Introduction 

Data Selection & Filtering allows you to:
👉 extract specific data
👉 focus on relevant information

---

## 📊 Data Analyst Perspective

Used for:

* selecting columns
* filtering customers
* segmenting data
* preparing datasets

---

# 🔹 2. Label-Based Selection 

## 🔸 2.1 .loc[] (Enhanced)

Used to select data using **labels**

---

## 📊 Real Use Case

```python id="sel1"
import pandas as pd

df = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Age": [21, 22, 23]
})

print(df.loc[0])            # row
print(df.loc[:, "Name"])    # column
```

---

## 📊 Advanced Example

```python id="sel2"
df.loc[df["Age"] > 21, ["Name", "Age"]]
```

👉 Filter + select columns together

---

## 🔥 Key Insights

✔ Uses labels
✔ Includes end index
✔ Most flexible method

---

# 🔍 Interview Thinking

* When to use .loc?
  👉 label-based selection

---

# 🔹 3. Position-Based Selection 

## 🔸 3.1 .iloc[] 

Used for **integer position-based selection**

---

## 📊 Real Use Case

```python id="sel3"
print(df.iloc[0])       # first row
print(df.iloc[:, 0])    # first column
```

---

## 📊 Advanced Example

```python id="sel4"
df.iloc[0:2, 0:2]
```

---

## 🔥 Key Insights

✔ Uses positions
✔ Faster for numeric indexing
✔ Does NOT include end index

---

# 🔍 Interview Thinking

* loc vs iloc?
  👉 label vs position

---

# 🔹 4. Conditional Filtering (VERY IMPORTANT 🔥)

---

## 📊 Real Use Case

```python id="sel5"
filtered = df[df["Age"] > 21]
print(filtered)
```

---

## 📊 Business Example

👉 Find:

* customers above age 25
* high-value sales
* active users

---

## 🔥 Insight

👉 This is used in **every project**

---

# 🔍 Interview Thinking

* How filtering works?
  👉 boolean conditions

---

# 🔹 5. isin() 

---

## 📊 Real Use Case

```python id="sel6"
df[df["Name"].isin(["A", "C"])]
```

---

## 📊 Applications

* selecting multiple categories
* filtering groups

---

## 🔥 Insight

👉 Cleaner than multiple OR conditions

---

# 🔹 6. query() 

---

## 📊 Real Use Case

```python id="sel7"
df.query("Age > 21")
```

---

## 📊 Real Insight

👉 Similar to SQL

---

## 🔥 When to Use

👉 complex filtering

---

# 🔍 Interview Thinking

* Why use query?
  👉 readable filtering

---

# 🔹 7. Multiple Conditions 

---

## 📊 Real Use Case

```python id="sel8"
df[(df["Age"] > 21) & (df["Name"] == "C")]
```

---

## 📊 Key Operators

* `&` → AND
* `|` → OR

---

## ⚠️ Important

👉 Always use parentheses

---

# 🔹 8. Workflow Example 

---

## 📊 Real Pipeline

```python id="sel9"
import pandas as pd

df = pd.read_csv("data.csv")

# Select column
names = df["Name"]

# Filter rows
filtered = df[df["Age"] > 25]

print(filtered)
```

---

## 🔥 Real Insight

👉 This is real-world analysis flow

---

# 🧠 Real Mini Case Study

## Problem: High Value Customers

```python id="sel10"
df = pd.read_csv("customers.csv")

high_value = df[(df["Spending"] > 5000) & (df["Age"] > 25)]

print(high_value)
```

---

👉 Real-world segmentation

---

# 🔍 Interview Thinking (Added Layer)

* Most used operation in Pandas?
  👉 filtering

* Difference loc vs iloc?
  👉 labels vs positions

---

# ⚠️ Common Mistakes

* Missing parentheses in conditions ❌
* Confusing loc and iloc ❌
* Using loops instead of filtering ❌

---

# 💡 Key Takeaways

✔ .loc → label-based
✔ .iloc → position-based
✔ filtering → core operation
✔ isin/query → advanced filtering

---

# 🎯 Final Insight

👉 If you master filtering…
👉 you can extract insights from any dataset

---

# Summary 

In this lesson I learned:

* .loc and .iloc
* Conditional filtering
* isin() and query()
* Multiple condition filtering
* Real-world data extraction

---
