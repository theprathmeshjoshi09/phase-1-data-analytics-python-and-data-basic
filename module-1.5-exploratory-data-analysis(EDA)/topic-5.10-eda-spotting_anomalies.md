# 🚀 Module 1.5 — Exploratory Data Analysis (EDA)

## Topic 5.10: Spotting Anomalies

---

# 🔥 Real-World Perspective

In real-world analytics:

👉 Some of the most important insights come from **unusual data**

Examples:

* sudden spike in sales
* unexpected drop in traffic
* fraudulent transactions

---

## 🧠 Real Insight

👉 Anomalies are not always errors
👉 They can be **signals of something important**

---

# What is this step?

Spotting anomalies means identifying unusual or unexpected data points.

👉 These values differ significantly from the rest of the dataset

---

# 📊 Data Analyst Perspective

Used for:

* detecting errors
* identifying risks
* discovering opportunities

---

# 🔹 What are Anomalies?

Anomalies = data points that are very different from others

They may represent:

* data errors
* rare events
* important signals

---

# 🔹 Examples

* sudden spike in sales
* drop in user activity
* unusual transactions

---

# 🔹 Tools You Use

* Boxplot
* Z-score
* IQR (Interquartile Range)

---

# 🔹 Real Workflow Example

```python id="ano1"
df["sales"].plot(kind="box")
```

---

👉 Detect → investigate → decide

---

# 🔹 Analyst Thinking

Ask:

* What looks unusual?
* Why did this happen?
* Is it error or meaningful?

👉 "What looks strange — and why?"

---

# 🧠 Real Mini Case Study

## Problem: Fraud Detection

```text id="ano2"
Observation:
- unusually high transaction  

Insight:
- possible fraud  

Action:
- investigate transaction  
```

---

👉 Risk prevention

---

# 🔹 Decision Step

After detecting anomaly:

👉 Decide:

* remove it (if error)
* keep it (if meaningful)

---

## 📊 Real Insight

👉 Never blindly remove anomalies

---

# ⚠️ Common Mistakes

❌ Ignoring anomalies
❌ Removing without investigation
❌ Assuming all anomalies are errors
❌ Not checking impact

---

# 💡 Key Takeaways

✔ Identify unusual data
✔ Investigate before action
✔ Use statistical tools
✔ Understand context

---

# 🎯 Final Insight

👉 Anomalies can be:

* risks
* errors
* opportunities

---

# Summary

In this lesson I learned:

* What anomalies are
* Detection techniques
* Real-world importance
* Decision-making process

---
