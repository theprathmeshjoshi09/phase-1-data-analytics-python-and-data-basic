# 🚀 Module 1.3 — Pandas 

## Topic 3.15: Pandas Visualization

---

# 🔥 Real-World Perspective

Data alone is not useful.

👉 Insights must be **visualized** to be understood

---

## 🧠 Real Insight

👉 Visualization = communication of data

Used in:

* dashboards
* reports
* presentations

---

# 🔹 1. Introduction 

Pandas provides built-in plotting using:
👉 Matplotlib

---

## 📊 Data Analyst Perspective

Used for:

* quick analysis
* trend visualization
* reporting

---

# 🔹 2. Basic Plotting 

---

## 🔸 2.1 Line Plot

```python id="viz1"
df["Sales"].plot()
```

---

## 📊 Use Case

👉 trend over time

---

## 🔥 Insight

👉 Best for time series

---

# 🔍 Interview Thinking

* When to use line plot?
  👉 trend analysis

---

# 🔹 3. Bar Plot 

---

## 📊 Real Use Case

```python id="viz2"
df["Category"].value_counts().plot(kind="bar")
```

---

## 📊 Applications

* category comparison
* frequency analysis

---

## 🔥 Insight

👉 Best for discrete data

---

# 🔹 4. Histogram 

---

## 📊 Real Use Case

```python id="viz3"
df["Age"].plot(kind="hist")
```

---

## 📊 Applications

* distribution analysis

---

## 🔥 Insight

👉 Understand spread of data

---

# 🔹 5. Scatter Plot 

---

## 📊 Real Use Case

```python id="viz4"
df.plot.scatter(x="Age", y="Salary")
```

---

## 📊 Applications

* relationship between variables

---

## 🔥 Insight

👉 Used in correlation analysis

---

# 🔍 Interview Thinking

* When to use scatter?
  👉 relationship analysis

---

# 🔹 6. Box Plot 

---

## 📊 Real Use Case

```python id="viz5"
df["Salary"].plot(kind="box")
```

---

## 📊 Applications

* detect outliers

---

## 🔥 Insight

👉 Important in data cleaning

---

# 🔹 7. Subplots (Enhanced)

---

## 📊 Real Use Case

```python id="viz6"
df.plot(subplots=True)
```

---

## 📊 Applications

* multi-feature analysis

---

## 🔥 Insight

👉 Compare multiple variables

---

# 🔹 8. Workflow Example 

---

## 📊 Real Pipeline

```python id="viz7"
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

df["Sales"].plot()
plt.show()
```

---

👉 Quick visualization workflow

---

# 🧠 Real Mini Case Study

## Problem: Sales Trend Visualization

```python id="viz8"
df = pd.read_csv("sales.csv")

df["Date"] = pd.to_datetime(df["Date"])
df = df.set_index("Date")

df["Revenue"].plot()
```

---

👉 Insight:

* growth trend
* seasonal patterns

---

# 🔍 Interview Thinking (Added Layer)

* Why visualization important?
  👉 communicate insights

* Most used plot?
  👉 line + bar

---

# ⚠️ Common Mistakes

* Choosing wrong plot ❌
* Not labeling axes ❌
* Overcomplicated charts ❌

---

# 💡 Key Takeaways

✔ line → trends
✔ bar → comparison
✔ histogram → distribution
✔ scatter → relationships
✔ box → outliers

---

# 🎯 Final Insight

👉 Analysis is useless if you can’t explain it

---

# Summary 

In this lesson I learned:

* basic plotting
* different plot types
* choosing correct visualization
* real-world reporting

---
