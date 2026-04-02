# 🚀 Module 1.3 — Pandas 

## Topic 3.3: Data Inspection & Understanding

---

# 🔥 Real-World Perspective

Before doing ANY analysis:

👉 You must understand your data

If you skip this:
❌ wrong conclusions
❌ bad models
❌ incorrect insights

---

## 🧠 Real Insight

👉 Good analysts spend **more time understanding data than coding**

---

# 🔹 1. Data Inspection 

Data inspection is the process of:
👉 exploring dataset structure
👉 identifying issues
👉 getting initial insights

---

## 📊 Data Analyst Perspective

Used to:

* detect missing values
* understand data types
* find anomalies

---

# 🔹 2. Viewing Data 

---

## 🔸 2.1 .head() 

```python id="insp1"
df.head()
```

---

## 📊 Real Use Case

👉 Check:

* first rows
* column values
* data format

---

## 🔥 Insight

👉 Always first function to use

---

## 🔸 2.2 .tail() 

```python id="insp2"
df.tail()
```

---

## 📊 Real Use Case

👉 Check:

* last entries
* data completeness

---

# 🔍 Interview Thinking

* Why use head()?
  👉 quick preview

---

# 🔹 3. Data Information 

---

## 🔸 3.1 .info() (VERY IMPORTANT 🔥)

```python id="insp3"
df.info()
```

---

## 📊 What It Shows

* column names
* data types
* non-null counts

---

## 🔥 Real Insight

👉 This is used in **every project**

---

## 🔸 3.2 .describe() 

```python id="insp4"
df.describe()
```

---

## 📊 Shows

* mean
* std
* min/max
* quartiles

---

## 📊 Real Use Case

👉 Understand distribution

---

# 🔍 Interview Thinking

* What does describe() give?
  👉 statistical summary

---

# 🔹 4. Dataset Structure 

---

## 🔸 4.1 .shape

```python id="insp5"
df.shape
```

👉 (rows, columns)

---

## 🔸 4.2 .columns

```python id="insp6"
df.columns
```

👉 column names

---

## 🔸 4.3 .dtypes

```python id="insp7"
df.dtypes
```

👉 data types

---

## 🔥 Real Insight

👉 Structure understanding = foundation

---

# 🔍 Interview Thinking

* What does shape return?
  👉 rows and columns

---

# 🔹 5. Value Analysis 

---

## 🔸 5.1 value_counts() 

```python id="insp8"
df["column"].value_counts()
```

---

## 📊 Real Use Case

👉 frequency analysis

---

## 🔸 5.2 unique()

```python id="insp9"
df["column"].unique()
```

---

👉 unique values

---

## 🔸 5.3 nunique()

```python id="insp10"
df["column"].nunique()
```

---

👉 count of unique values

---

## 📊 Real Applications

* category analysis
* segmentation

---

# 🧠 Real Mini Case Study

## Problem: Customer Dataset Understanding

```python id="insp11"
df = pd.read_csv("customers.csv")

print(df.info())
print(df["City"].value_counts())
```

---

👉 Identify:

* missing values
* customer distribution

---

# 🔍 Interview Thinking (Added Layer)

* First step after loading data?
  👉 inspection

* Most important function?
  👉 df.info()

---

# ⚠️ Common Mistakes

* Skipping inspection ❌
* Ignoring missing values ❌
* Not checking data types ❌

---

# 💡 Key Takeaways

✔ head/tail → preview
✔ info → structure
✔ describe → statistics
✔ value_counts → distribution

---

# 🎯 Final Insight

👉 If you don’t understand your data…
👉 you cannot analyze it

---

# Summary 

In this lesson I learned:

* Viewing data
* Inspecting structure
* Understanding statistics
* Analyzing values
* Real-world dataset exploration

---
