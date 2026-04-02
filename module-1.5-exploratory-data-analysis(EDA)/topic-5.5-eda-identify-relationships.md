# 🚀 Module 1.5 — Exploratory Data Analysis (EDA)

## Topic 5.5: Identify Relationships

---

# 🔥 Real-World Perspective

In real-world analytics:

👉 Businesses don’t care about individual columns
👉 They care about relationships

Examples:

* Does income affect spending?
* Does discount increase sales?
* Does age influence behavior?

---

## 🧠 Real Insight

👉 Insights come from relationships, not isolated data

---

# What is this step?

Identifying relationships helps you understand how different variables interact with each other.

👉 This is where real insights start forming

---

# 📊 Data Analyst Perspective

Used for:

* finding influencing factors
* understanding dependencies
* building predictive thinking

---

# 🔹 Types of Relationships

---

## 1. Numerical vs Numerical

* Measure correlation between variables

Example:

* Income vs Spending

---

## 📊 Real Insight

👉 Helps identify:

* positive relationship
* negative relationship
* no relationship

---

## 🔥 Interview Thinking

* What is correlation?
  👉 measure of relationship strength

---

## 2. Categorical vs Numerical

* Compare numerical values across categories

Example:

* Average salary by department

---

## 📊 Real Insight

👉 Helps understand group behavior

---

## 3. Categorical vs Categorical

* Analyze frequency and distribution

Example:

* Gender vs Purchase behavior

---

## 📊 Real Insight

👉 Useful for segmentation

---

# 🔹 Tools You Use

```python id="rel1"
df.corr()
```

Other tools:

* Scatter plots
* Heatmaps
* GroupBy

---

# 🔹 Real Workflow Example

```python id="rel2"
df.corr()

df.groupby("department")["salary"].mean()
```

---

👉 Compare → analyze → interpret

---

# 🔹 Analyst Thinking

Ask:

* Which variables influence each other?
* Are relationships strong or weak?
* Are they positive or negative?

👉 "What affects what?"

---

# 🧠 Real Mini Case Study

## Problem: Sales Dataset

```text id="rel3"
Observation:
- discount ↑ → sales ↑  

Insight:
- discount drives sales  

Action:
- optimize discount strategy  
```

---

👉 Business impact

---

# ⚠️ Common Mistakes

❌ Assuming correlation = causation
❌ Ignoring weak relationships
❌ Not segmenting data
❌ Overlooking hidden patterns

---

# 💡 Key Takeaways

✔ Analyze variable relationships
✔ Use correlation and grouping
✔ Visualize interactions
✔ Focus on influencing factors

---

# 🎯 Final Insight

👉 Relationships reveal the hidden structure of data

---

# Summary

In this lesson I learned:

* Types of relationships
* Correlation analysis
* Group comparisons
* Real-world interpretation

---
