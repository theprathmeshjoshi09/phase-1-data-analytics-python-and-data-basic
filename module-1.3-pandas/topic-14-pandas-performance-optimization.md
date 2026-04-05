# 🚀 Module 1.3 — Pandas 

## Topic 14: Pandas Performance Optimization

---

# 🔥 Real-World Perspective

In real-world systems:

👉 Data is HUGE

* millions of rows
* multiple datasets
* complex transformations

---

## 🧠 Real Insight

👉 Code that works is not enough
👉 Code must be **efficient**

---

# 🔹 1. Introduction 

Performance optimization focuses on:
👉 speed
👉 memory efficiency
👉 scalability

---

## 📊 Data Analyst Perspective

Used in:

* large datasets
* production pipelines
* real-time analytics

---

# 🔹 2. Avoid Loops (VERY IMPORTANT 🔥)

---

## ❌ Bad Practice

```python id="perf1"
for i in range(len(df)):
    df.loc[i, "A"] = df.loc[i, "A"] * 2
```

---

## ✅ Good Practice (Vectorization)

```python id="perf2"
df["A"] = df["A"] * 2
```

---

## 🔥 Insight

👉 Vectorization = fastest approach

---

# 🔍 Interview Thinking

* Why avoid loops?
  👉 slow in Python

---

# 🔹 3. Use Built-in Functions

---

## 📊 Example

```python id="perf3"
df["A"].sum()
df["A"].mean()
```

---

## 🔥 Insight

👉 Built-in functions are optimized in C

---

# 🔹 4. Optimize Data Types 

---

## 📊 Real Use Case

```python id="perf4"
df["A"] = df["A"].astype("int32")
df["Category"] = df["Category"].astype("category")
```

---

## 🔥 Insight

👉 Smaller dtype → less memory

---

# 🔍 Interview Thinking

* Why dtype important?
  👉 memory + speed

---

# 🔹 5. Use .loc Efficiently 

---

## 📊 Example

```python id="perf5"
df.loc[df["A"] > 10, "B"] = 0
```

---

## 🔥 Insight

👉 Efficient conditional updates

---

# 🔹 6. Avoid Chained Operations 

---

## ❌ Bad Practice

```python id="perf6"
df[df["A"] > 10]["B"] = 0
```

---

## ✅ Correct

```python id="perf7"
df.loc[df["A"] > 10, "B"] = 0
```

---

## 🔥 Insight

👉 Prevents bugs + improves performance

---

# 🔹 7. Use apply() Carefully 

---

## 📊 Example

```python id="perf8"
df["A"] = df["A"].apply(lambda x: x + 1)
```

---

## 🔥 Insight

👉 Slower than vectorized operations

---

# 🔹 8. Memory Usage Check 

---

## 📊 Real Use Case

```python id="perf9"
df.info(memory_usage="deep")
```

---

## 🔥 Insight

👉 Helps optimize large datasets

---

# 🔹 9. Use Chunking for Large Data 

---

## 📊 Example

```python id="perf10"
for chunk in pd.read_csv("large.csv", chunksize=10000):
    process(chunk)
```

---

## 📊 Applications

* big data processing
* limited memory systems

---

## 🔥 Insight

👉 Process data in parts

---

# 🔹 10. Workflow Example 

---

## 📊 Real Pipeline

```python id="perf11"
df = pd.read_csv("data.csv")

df["Category"] = df["Category"].astype("category")

df["A"] = df["A"] * 2
```

---

👉 Optimized pipeline

---

# 🧠 Real Mini Case Study

## Problem: Optimize Large Dataset

```python id="perf12"
df = pd.read_csv("large_data.csv")

df["Category"] = df["Category"].astype("category")

df["Revenue"] = df["Price"] * df["Quantity"]
```

---

👉 Faster + memory efficient

---

# 🔍 Interview Thinking (Added Layer)

* How to optimize Pandas?
  👉 vectorization + dtype

* Biggest mistake?
  👉 loops

---

# ⚠️ Common Mistakes

* Using loops ❌
* Not optimizing dtype ❌
* Chained indexing ❌

---

# 💡 Key Takeaways

✔ Avoid loops
✔ Use vectorization
✔ Optimize dtypes
✔ Use built-in functions
✔ Handle large data efficiently

---

# 🎯 Final Insight

👉 Efficient code = scalable code

---

# Summary 

In this lesson I learned:

* Performance optimization
* Vectorization
* dtype optimization
* efficient indexing
* handling large datasets

---
