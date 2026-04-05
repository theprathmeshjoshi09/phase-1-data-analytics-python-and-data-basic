# 🚀 Module 1.3 — Pandas 

## Topic 05: Data Cleaning (MOST IMPORTANT)

---

# 🔥 Real-World Perspective

Real-world data is ALWAYS messy:

* missing values
* duplicates
* wrong formats
* inconsistent text

---

## 🧠 Real Insight

👉 70–80% of real data work = cleaning

---

# 🔹 1. Introduction (Enhanced)

Data Cleaning ensures:
👉 accuracy
👉 consistency
👉 reliability

---

## 📊 Data Analyst Perspective

Used to:

* fix missing values
* remove duplicates
* correct formats
* clean text data

---

# 🔹 2. Missing Values 

---

## 🔸 2.1 Detect Missing Values

```python id="clean1"
df.isnull()
df.notnull()
```

---

## 📊 Real Use Case

👉 Identify incomplete data

---

## 🔸 2.2 Drop Missing Values

```python id="clean2"
df.dropna()
```

---

## 📊 When to Use

👉 If missing data is small

---

## 🔸 2.3 Fill Missing Values

```python id="clean3"
df.fillna(0)
df.fillna(method='ffill')
```

---

## 📊 Real Applications

* filling defaults
* forward filling time data

---

## 🔥 Insight

👉 Choice depends on business logic

---

# 🔍 Interview Thinking

* drop vs fill?
  👉 remove vs replace

---

# 🔹 3. Duplicates 

---

## 🔸 3.1 Detect Duplicates

```python id="clean4"
df.duplicated()
```

---

## 🔸 3.2 Remove Duplicates

```python id="clean5"
df.drop_duplicates()
```

---

## 📊 Real Use Case

👉 Remove repeated records

---

# 🔍 Interview Thinking

* Why remove duplicates?
  👉 avoid double counting

---

# 🔹 4. Data Type Fixing 

---

## 🔸 4.1 Change Data Types

```python id="clean6"
df["Age"] = df["Age"].astype(int)
```

---

## 📊 Real Use Case

👉 Fix incorrect formats

---

## 🔥 Insight

👉 Wrong dtype = wrong analysis

---

# 🔍 Interview Thinking

* Why dtype important?
  👉 accuracy

---

# 🔹 5. String Cleaning 

---

## 🔸 5.1 Convert Case

```python id="clean7"
df["Name"].str.lower()
df["Name"].str.upper()
```

---

## 🔸 5.2 Remove Spaces

```python id="clean8"
df["Name"].str.strip()
```

---

## 🔸 5.3 Replace Values

```python id="clean9"
df["Name"].str.replace("old", "new")
```

---

## 🔸 5.4 Extract Patterns

```python id="clean10"
df["Email"].str.extract(r"(\\w+)@")
```

---

## 📊 Real Applications

* cleaning names
* extracting usernames
* standardizing data

---

# 🔹 6. Outlier Handling 

---

## 🔸 6.1 IQR Method

```python id="clean11"
Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
```

---

## 🔸 6.2 Filter Outliers

```python id="clean12"
df = df[(df["Salary"] >= lower) & (df["Salary"] <= upper)]
```

---

## 📊 Real Use Case

👉 Remove extreme values

---

## 🔥 Insight

👉 Important for:

* ML models
* statistical analysis

---

# 🔍 Interview Thinking

* What is outlier?
  👉 extreme value

---

# 🔹 7. Workflow Example 

---

## 📊 Real Pipeline

```python id="clean13"
import pandas as pd

df = pd.read_csv("data.csv")

df = df.dropna()
df = df.drop_duplicates()
df["Name"] = df["Name"].str.strip()
```

---

👉 Real-world cleaning workflow

---

# 🧠 Real Mini Case Study

## Problem: Clean Customer Dataset

```python id="clean14"
df = pd.read_csv("customers.csv")

df = df.dropna()
df = df.drop_duplicates()
df["City"] = df["City"].str.lower()
```

---

👉 Clean + standardize data

---

# 🔍 Interview Thinking (Added Layer)

* Most important step in analysis?
  👉 data cleaning

* Why critical?
  👉 ensures accuracy

---

# ⚠️ Common Mistakes

* Blindly dropping data ❌
* Ignoring outliers ❌
* Not fixing data types ❌

---

# 💡 Key Takeaways

✔ Handle missing values
✔ Remove duplicates
✔ Fix data types
✔ Clean strings
✔ Handle outliers

---

# 🎯 Final Insight

👉 Clean data = correct insights

---

# Summary 

In this lesson I learned:

* Handling missing values
* Removing duplicates
* Fixing data types
* String cleaning
* Outlier handling
* Real-world data cleaning

---
