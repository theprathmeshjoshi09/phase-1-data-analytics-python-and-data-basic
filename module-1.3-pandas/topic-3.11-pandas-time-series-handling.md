# 🚀 Module 1.3 — Pandas 

## Topic 3.11: Time Series Analysis

---

# 🔥 Real-World Perspective

Most real-world data is time-based:

* sales over time
* stock prices
* website traffic
* user activity

---

## 🧠 Real Insight

👉 Time series = **data with a time dimension**

---

# 🔹 1. Introduction

Time series data:
👉 indexed by time
👉 analyzed over intervals

---

## 📊 Data Analyst Perspective

Used for:

* trend analysis
* forecasting
* seasonality detection

---

# 🔹 2. Working with Dates 

---

## 🔸 2.1 Convert to datetime

```python id="ts1"
import pandas as pd

df["Date"] = pd.to_datetime(df["Date"])
```

---

## 📊 Why Important

👉 Enables time-based operations

---

## 🔥 Insight

👉 Always convert dates first

---

# 🔍 Interview Thinking

* Why convert datetime?
  👉 enable time analysis

---

# 🔹 3. Setting Date as Index 

---

## 📊 Real Use Case

```python id="ts2"
df = df.set_index("Date")
```

---

## 📊 Applications

* time-based filtering
* resampling

---

## 🔥 Insight

👉 Time index unlocks full power

---

# 🔹 4. Resampling (VERY IMPORTANT 🔥)

---

## 📊 Real Use Case

```python id="ts3"
df.resample("M").sum()
```

---

## 📊 Examples

* "D" → daily
* "M" → monthly
* "Y" → yearly

---

## 📊 Applications

* monthly sales
* yearly trends

---

## 🔥 Insight

👉 Converts time granularity

---

# 🔍 Interview Thinking

* What is resampling?
  👉 changing time frequency

---

# 🔹 5. Rolling Window 

---

## 📊 Real Use Case

```python id="ts4"
df["Sales"].rolling(window=3).mean()
```

---

## 📊 Applications

* moving average
* smoothing data

---

## 🔥 Insight

👉 Used in trend analysis

---

# 🔹 6. Date Filtering 

---

## 📊 Real Use Case

```python id="ts5"
df["2024-01"]
```

---

## 📊 Applications

* monthly analysis
* time-based filtering

---

## 🔥 Insight

👉 Works only with datetime index

---

# 🔍 Interview Thinking

* How to filter by date?
  👉 datetime index

---

# 🔹 7. Workflow Example 

---

## 📊 Real Pipeline

```python id="ts6"
df = pd.read_csv("sales.csv")

df["Date"] = pd.to_datetime(df["Date"])

df = df.set_index("Date")

monthly_sales = df.resample("M").sum()
```

---

👉 Real-world time analysis

---

# 🧠 Real Mini Case Study

## Problem: Monthly Sales Trend

```python id="ts7"
df = pd.read_csv("sales.csv")

df["Date"] = pd.to_datetime(df["Date"])
df = df.set_index("Date")

trend = df.resample("M")["Revenue"].sum()

print(trend)
```

---

👉 Business insight:

* growth patterns
* seasonal trends

---

# 🔍 Interview Thinking (Added Layer)

* What is time series?
  👉 time-indexed data

* Most important function?
  👉 resample()

---

# ⚠️ Common Mistakes

* Not converting to datetime ❌
* Not setting index ❌
* Wrong resampling frequency ❌

---

# 💡 Key Takeaways

✔ datetime conversion is critical
✔ resampling = core operation
✔ rolling = trend smoothing
✔ time index enables analysis

---

# 🎯 Final Insight

👉 Time series = understanding change over time

---

# Summary 

In this lesson I learned:

* datetime conversion
* time indexing
* resampling
* rolling window
* time-based filtering
* real-world analysis

---
