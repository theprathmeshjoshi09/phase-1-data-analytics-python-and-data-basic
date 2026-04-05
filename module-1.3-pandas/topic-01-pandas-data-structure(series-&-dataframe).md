# 🚀 Module 1.3 — Pandas 

## Topic 01: Data Structures (Series & DataFrame)

---

# 🔥 Real-World Perspective

Pandas is the **most used tool in data analysis**

👉 Every dataset you work with:

* CSV
* Excel
* Database

👉 Will eventually become a **DataFrame**

---

## 🧠 Real Insight

👉 If NumPy = engine
👉 Pandas = interface for real-world data

---

# 🔹 1. Data Structures in Pandas 

In Pandas, data is stored using two main structures:

1. **Series (1D)**
2. **DataFrame (2D)**

👉 These are the **core building blocks of all analytics**

---

## 📊 Data Analyst Perspective

In real projects:

* Series → single column
* DataFrame → full dataset

---

# 🔸 1.1 What is a Series 

A **Series** is a **one-dimensional labeled array**

---

## 📊 Real Use Case

```python
import pandas as pd

sales = pd.Series([100, 200, 300, 400])
print(sales)
```

👉 Example:

* daily sales
* customer scores

---

## 🔥 Key Characteristics 

* One column only
* Has **index + values**
* Supports multiple data types

---

## 📊 Custom Index Example

```python
data = pd.Series([10, 20, 30], index=['A', 'B', 'C'])
```

👉 Real-world:

* Product IDs
* Customer IDs

---

## 💡 Real Insight

👉 Series = single column in Excel
👉 But with **powerful operations**

---

# 🔍 Interview Thinking

* What is Series?
  👉 1D labeled array

---

# 🔸 1.2 What is a DataFrame 

A **DataFrame** is a **2D tabular structure**

---

## 📊 Real Use Case

```python
data = {
    "Name": ["A", "B", "C"],
    "Age": [21, 22, 23]
}

df = pd.DataFrame(data)
print(df)
```

---

## 📊 Real Applications

👉 Used for:

* customer data
* sales data
* financial data

---

## 🔥 Key Characteristics 

* Multiple columns
* Each column = Series
* Table-like structure

---

## 💡 Real Insight

👉 DataFrame = Excel sheet + Python power

---

# 🔍 Interview Thinking

* What is DataFrame?
  👉 2D labeled data structure

---

# 🔸 1.3 Series vs DataFrame (Thinking)

| Feature   | Series         | DataFrame      |
| --------- | -------------- | -------------- |
| Dimension | 1D             | 2D             |
| Use       | Single feature | Full dataset   |
| Example   | Age column     | Customer table |

---

## 📊 Real Insight

👉 In real work:

* You rarely use Series alone
* Mostly work with DataFrames

---

# 🔹 2. Index & Columns 

---

## 🔸 2.1 What is Index 

Index = **row labels**

```python
print(df.index)
```

---

## 📊 Real Use Case

👉 Index represents:

* record ID
* timestamp
* row identifier

---

## 🔥 Insight

👉 Index is not just numbering
👉 It is **data alignment system**

---

# 🔍 Interview Thinking

* What is index?
  👉 row labels

---

## 🔸 2.2 What are Columns 

Columns = **features / variables**

```python
print(df.columns)
```

---

## 📊 Real Use Case

👉 Columns represent:

* age
* revenue
* product

---

## 🔥 Insight

👉 Each column is a **Series**

---

# 🔹 3. Data Types (dtypes) 

---

## 🔸 3.1 What are Data Types

Defines type of data stored

---

## 📊 Common Types 

| Type     | Real Example |
| -------- | ------------ |
| int64    | quantity     |
| float64  | price        |
| object   | names        |
| bool     | status       |
| datetime | timestamps   |

---

## 🔥 Real Insight

👉 Wrong dtype = wrong analysis

---

# 🔍 Interview Thinking

* Why dtype important?
  👉 correctness + performance

---

## 🔸 3.2 Why Data Types Matter 

* Performance
* Memory
* Accuracy

---

## 📊 Example

```python
df["Age"] = df["Age"].astype(float)
```

---

## 🔸 3.3 Checking Data Types

```python
df.info()
```

---

## 🔥 Real Insight

👉 `.info()` is one of the **most used functions**

---

# 🧠 Real Mini Case Study

## Problem: Customer Dataset

```python
data = {
    "Name": ["A", "B", "C"],
    "Sales": [1000, 2000, 3000]
}

df = pd.DataFrame(data)

print(df["Sales"].mean())
```

👉 Real-world:

* analyzing customer sales

---

# 🔍 Interview Thinking (Added Layer)

* Series vs DataFrame?
  👉 1D vs 2D

* Why Pandas used?
  👉 real-world data handling

---

# ⚠️ Common Mistakes

* Confusing Series and DataFrame ❌
* Ignoring index ❌
* Wrong data types ❌

---

# 💡 Key Takeaways

✔ Series = 1D
✔ DataFrame = 2D
✔ Index = row labels
✔ Columns = features
✔ dtypes affect performance

---

# 🎯 Final Insight

👉 Pandas is the **heart of data analytics**

If you master this:
👉 You can handle real datasets

---

# Summary 

In this lesson I learned:

* Series and DataFrame
* Index and columns
* Data types
* Real-world dataset structure

---
