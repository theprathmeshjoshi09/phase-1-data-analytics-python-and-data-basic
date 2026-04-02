 # 🚀 Module 1.3 — Pandas 

## Topic 3.12: Pandas Window Functions

---

# 🔥 Real-World Perspective

Window functions allow you to:
👉 analyze data **relative to neighboring rows**

---

## 🧠 Real Insight

👉 This is heavily used in:

* financial analysis
* trend detection
* time-based insights

---

# 🔹 1. Introduction 

Window functions perform calculations:
👉 over a subset (window) of data

---

## 📊 Data Analyst Perspective

Used for:

* moving averages
* cumulative metrics
* rolling statistics

---

# 🔹 2. Rolling Window 

---

## 🔸 2.1 rolling()

```python id="win1"
df["Sales"].rolling(window=3).mean()
```

---

## 📊 Real Use Case

👉 3-day moving average

---

## 📊 Applications

* trend smoothing
* noise reduction

---

## 🔥 Insight

👉 Helps identify patterns

---

# 🔍 Interview Thinking

* What is rolling?
  👉 moving window calculation

---

# 🔹 3. Expanding Window

---

## 🔸 3.1 expanding()

```python id="win2"
df["Sales"].expanding().mean()
```

---

## 📊 Real Use Case

👉 cumulative average

---

## 📊 Applications

* long-term trends
* progressive metrics

---

## 🔥 Insight

👉 window grows over time

---

# 🔍 Interview Thinking

* rolling vs expanding?
  👉 fixed vs growing window

---

# 🔹 4. Exponential Moving Window 

---

## 🔸 4.1 ewm()

```python id="win3"
df["Sales"].ewm(span=3).mean()
```

---

## 📊 Real Use Case

👉 weighted moving average

---

## 📊 Applications

* stock price analysis
* recent trend emphasis

---

## 🔥 Insight

👉 recent values get more weight

---

# 🔍 Interview Thinking

* What is ewm?
  👉 weighted moving average

---

# 🔹 5. Common Window Operations 

---

## 📊 Examples

```python id="win4"
df["Sales"].rolling(3).sum()
df["Sales"].rolling(3).max()
df["Sales"].rolling(3).std()
```

---

## 📊 Applications

* volatility analysis
* trend detection

---

# 🔹 6. Workflow Example 

---

## 📊 Real Pipeline

```python id="win5"
import pandas as pd

df = pd.read_csv("sales.csv")

df["Date"] = pd.to_datetime(df["Date"])
df = df.set_index("Date")

df["Moving_Avg"] = df["Sales"].rolling(3).mean()
```

---

👉 Real-world trend analysis

---

# 🧠 Real Mini Case Study

## Problem: Sales Trend Analysis

```python id="win6"
df = pd.read_csv("sales.csv")

df["Date"] = pd.to_datetime(df["Date"])
df = df.set_index("Date")

df["Trend"] = df["Revenue"].rolling(5).mean()
```

---

👉 Business insight:

* identify growth trends
* detect fluctuations

---

# 🔍 Interview Thinking (Added Layer)

* What are window functions?
  👉 calculations over data windows

* Most used?
  👉 rolling()

---

# ⚠️ Common Mistakes

* Wrong window size ❌
* Not sorting data by date ❌
* Misinterpreting rolling results ❌

---

# 💡 Key Takeaways

✔ rolling → fixed window
✔ expanding → cumulative
✔ ewm → weighted average
✔ used in time analysis

---

# 🎯 Final Insight

👉 Window functions = **advanced analytics layer**

---

# Summary 

In this lesson I learned:

* rolling()
* expanding()
* ewm()
* window-based calculations
* real-world trend analysis

---
