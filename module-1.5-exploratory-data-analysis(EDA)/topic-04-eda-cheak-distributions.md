# 🚀 Module 1.5 — Exploratory Data Analysis (EDA)

## Topic 04: Check Distributions

---

# 🔥 Real-World Perspective

In real-world analytics:

👉 Most real data is NOT clean or normal

* it is skewed
* it contains outliers
* it is biased

---

## 🧠 Real Insight

👉 If you don’t understand distribution
👉 you will choose wrong methods and get wrong results

---

# What is this step?

Checking distributions helps you understand how your data is spread.

👉 It reveals patterns, bias, and unusual values in the dataset

---

# 📊 Data Analyst Perspective

Used for:

* understanding data behavior
* detecting bias
* preparing for modeling

---

# 🔹 What to Analyze

---

## 1. Normal Distribution

* Is the data evenly distributed?
* Bell-shaped curve?

---

## 📊 Real Insight

👉 Many statistical methods assume normal distribution

---

## 2. Skewness

* Left skewed (negative skew)
* Right skewed (positive skew)

---

## 📊 Real Insight

👉 Skewness affects:

* mean
* analysis decisions

---

## 3. Outliers

* Extreme values far from majority
* Can distort analysis

---

## 📊 Real Insight

👉 Outliers can be:

* errors
* or valuable signals

---

# 🔹 Tools You Use

* Histogram
* KDE plot
* Boxplot

---

# 🔹 Key Concepts

---

## Mean vs Median

* Mean → affected by outliers
* Median → robust

---

## 📊 Real Insight

👉 If mean ≠ median → data is skewed

---

## Skewness

* Indicates direction of spread

---

## Outliers

* Detect using:

  * boxplots
  * statistical methods

---

# 🔹 Real Workflow Example

```python id="dist1"
df["age"].hist()

df["age"].plot(kind="box")
```

---

👉 Visualize → understand → decide

---

# 🔹 Analyst Thinking

Ask:

* Is the data balanced or biased?
* Are there extreme values?
* Should I transform this data?

👉 "What does this data look like?"

---

# 🧠 Real Mini Case Study

## Problem: Salary Data

```text id="dist2"
Data:
[20k, 25k, 30k, 35k, 2 lakh]

Observation:
- highly skewed  
- outlier present  

Decision:
- use median instead of mean  
```

---

👉 Better accuracy

---

# ⚠️ Common Mistakes

❌ Assuming data is normal
❌ Ignoring skewness
❌ Not checking outliers
❌ Using mean blindly

---

# 💡 Key Takeaways

✔ Always check distribution
✔ Detect skewness
✔ Identify outliers
✔ Choose correct metrics

---

# 🎯 Final Insight

👉 Distribution tells you how to analyze data correctly

---

# Summary

In this lesson I learned:

* Distribution concepts
* Skewness
* Outliers
* Visualization tools
* Real-world decision-making

---
