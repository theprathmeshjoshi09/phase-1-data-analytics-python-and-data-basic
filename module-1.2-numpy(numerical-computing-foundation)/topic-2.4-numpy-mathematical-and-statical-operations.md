# 🚀 Module 1.2 — NumPy 

## Topic 2.4: NumPy Mathematical & Statistical Operations

---

# 🔥 Real-World Perspective

This is where **data becomes insights**

👉 Raw data → Numbers
👉 Statistical operations → Meaning

Used in:

* business analytics
* financial analysis
* machine learning
* decision making

---

## 🧠 Real Insight

👉 Every dashboard, report, or ML model
is built using these operations

---

# 2.4 Mathematical & Statistical Operations 

NumPy provides functions to perform:
👉 statistical analysis
👉 mathematical computations

---

## 📊 Data Analyst Perspective

Used to:

* calculate KPIs
* understand trends
* analyze distributions

---

# 2.4.1 Mean, Median, Standard Deviation 

---

## 📊 Mean (Average)

```python id="stat1"
import numpy as np

sales = np.array([100,200,300,400])

print(np.mean(sales))
```

👉 Business use:

* average revenue
* average customer spend

---

## 📊 Median

```python id="stat2"
print(np.median(sales))
```

👉 Used when:

* data has outliers

---

## 📊 Standard Deviation

```python id="stat3"
print(np.std(sales))
```

👉 Measures:

* variability
* risk (finance)

---

## 🔥 Real Insight

* Mean → general trend
* Median → robust center
* Std → spread

---

# 🔍 Interview Thinking

* When to use median over mean?
  👉 when outliers exist

---

# 2.4.2 Minimum and Maximum 

---

## 📊 Real Use Case

```python id="stat4"
prices = np.array([50, 100, 200, 500])

print(np.min(prices))
print(np.max(prices))
```

---

## 📊 Applications

* lowest price
* highest revenue
* range detection

---

# 🔍 Interview Thinking

* Why min/max important?
  👉 detect extremes

---

# 2.4.3 Percentiles 

---

## 📊 Real Use Case

```python id="stat5"
arr = np.array([10,20,30,40,50])

print(np.percentile(arr, 25))
print(np.percentile(arr, 75))
```

---

## 📊 Business Insight

* 25% → low performers
* 50% → median
* 75% → top performers

---

## 🔥 Real Application

👉 Customer segmentation

---

# 🔍 Interview Thinking

* What is percentile?
  👉 data distribution measure

---

# 2.4.4 Correlation 

---

## 📊 Real Use Case

```python id="stat6"
x = np.array([1,2,3,4])
y = np.array([2,4,6,8])

print(np.corrcoef(x,y))
```

---

## 📊 Real Applications

* feature relationships
* market trends
* prediction models

---

## 🔥 Interpretation

* +1 → strong positive
* 0 → no relation
* -1 → negative

---

# 🔍 Interview Thinking

* What is correlation?
  👉 relationship between variables

---

# 🧠 Real Mini Case Study

## Problem: Customer Spending Analysis

```python id="stat7"
spending = np.array([1000, 2000, 3000, 10000])

mean = np.mean(spending)
median = np.median(spending)

print(mean, median)
```

---

## Insight:

👉 If mean ≠ median → outliers exist

---

# 🔍 Interview Thinking (Added Layer)

* Difference between mean and median?
  👉 sensitivity to outliers

* Why std important?
  👉 measures variability

---

# ⚠️ Common Mistakes

* Using mean with outliers ❌
* Ignoring distribution ❌
* Misinterpreting correlation ❌

---

# 💡 Key Takeaways

✔ Mean, median, std = core metrics
✔ Percentiles = distribution insight
✔ Correlation = relationship analysis
✔ Used in all data analysis

---

# 🎯 Final Insight

👉 These operations turn:
data → information → decisions

---

# Summary 

In this lesson I learned:

* Mean, median, standard deviation
* Min and max values
* Percentiles
* Correlation
* Real-world data insights

---
