# 🚀 Module 1.5 — Exploratory Data Analysis (EDA)

## Topic 5.9: Finding Trends

---

# 🔥 Real-World Perspective

In real-world analytics:

👉 Almost every business decision depends on trends

Examples:

* Is sales growing or declining?
* Is user engagement increasing?
* Is demand seasonal?

---

## 🧠 Real Insight

👉 Trends show direction
👉 Direction drives decisions

---

# What is this step?

Finding trends helps you understand how data changes over time.

👉 Trends show the direction in which data is moving

---

# 📊 Data Analyst Perspective

Used for:

* forecasting
* business planning
* performance tracking

---

# 🔹 What is a Trend?

Trend = Direction over time

It answers:

* Is data increasing?
* Is it decreasing?
* Is it repeating?

---

# 🔹 Types of Trends

---

## 1. Increasing Trend

* Values rise over time

---

## 2. Decreasing Trend

* Values fall over time

---

## 3. Seasonal Trend

* Repeating patterns at intervals

Example:

* festival sales
* holiday demand

---

## 📊 Real Insight

👉 Most businesses have seasonal patterns

---

# 🔹 Tools You Use

* Line plots
* Moving averages

---

# 🔹 Real Workflow Example

```python id="trend1"
df.groupby("month")["sales"].sum()

df["sales"].rolling(3).mean()
```

---

👉 Aggregate → smooth → analyze

---

# 🔹 Analyst Thinking

Ask:

* What direction is data moving?
* Is this trend stable?
* Will it continue?

👉 "Where is this going?"

---

# 🧠 Real Mini Case Study

## Problem: Sales Trend

```text id="trend2"
Observation:
- steady increase in sales  

Insight:
- business is growing  

Action:
- expand operations  
```

---

👉 Strategic decision

---

# 🔹 Advanced Thinking

👉 Combine trends with:

* seasonality
* external factors
* business context

---

## 📊 Real Insight

👉 Trend alone is not enough
👉 Context makes it meaningful

---

# ⚠️ Common Mistakes

❌ Ignoring time dimension
❌ Confusing noise with trend
❌ Not smoothing data
❌ Missing seasonal effects

---

# 💡 Key Takeaways

✔ Trends show direction
✔ Use time-based analysis
✔ Apply smoothing techniques
✔ Combine with context

---

# 🎯 Final Insight

👉 Trends help you predict the future

---

# Summary

In this lesson I learned:

* Trend concept
* Types of trends
* Time-based analysis
* Real-world applications

---
