# 🚀 Module 1.2 — NumPy 

## Topic 10: NumPy File Handling

---

# 🔥 Real-World Perspective

In real-world projects:
👉 Data is not always recomputed

Instead:

* we save processed data
* we reload it later
* we reuse it across pipelines

---

## 🧠 Real Insight

👉 Efficient data storage = faster workflows

Without this:

* repeated computation ❌
* slow pipelines ❌

---

# 2.10 File Handling 

NumPy allows:
👉 saving arrays
👉 loading arrays

---

## 📊 Data Analyst Perspective

Used in:

* saving processed datasets
* storing intermediate results
* caching computations

---

# 2.10.1 np.save() 

---

## 📊 Real Use Case

```python id="fh1"
import numpy as np

data = np.array([1,2,3,4])

np.save("data.npy", data)
```

---

## 📊 Real Application

👉 Save:

* cleaned data
* processed features

---

## 🔥 Insight

👉 `.npy` format is:

* fast
* compact
* NumPy optimized

---

# 🔍 Interview Thinking

* Why use np.save?
  👉 efficient storage of arrays

---

# 2.10.2 np.load()

---

## 📊 Real Use Case

```python id="fh2"
loaded = np.load("data.npy")
print(loaded)
```

---

## 📊 Application

👉 Reload saved datasets
👉 reuse data

---

## 🔥 Insight

👉 Exact same data is restored

---

# 🔍 Interview Thinking

* What does np.load do?
  👉 loads saved arrays

---

# 2.10.3 Working with Datasets 

---

## 📊 Real Use Case

```python id="fh3"
dataset = np.array([[1,2,3],[4,5,6]])

np.save("dataset.npy", dataset)

loaded = np.load("dataset.npy")
```

---

## 📊 Applications

* storing ML datasets
* caching processed data

---

## 🔥 Insight

👉 Avoid recomputation

---

# 2.10.4 Multiple Arrays (np.savez) 

---

## 📊 Real Use Case

```python id="fh4"
a = np.array([1,2,3])
b = np.array([4,5,6])

np.savez("data.npz", a=a, b=b)
```

---

## 📊 Load Multiple Arrays

```python id="fh5"
data = np.load("data.npz")

print(data["a"])
print(data["b"])
```

---

## 📊 Applications

* storing multiple datasets
* model inputs

---

## 🔥 Insight

👉 Organized storage in one file

---

# 🧠 Real Mini Case Study

## Problem: Save Processed Sales Data

```python id="fh6"
sales = np.array([100,200,300])

processed = sales * 1.1  # add 10% growth

np.save("processed_sales.npy", processed)
```

---

👉 Real-world pipeline:

* process → save → reuse

---

# 🔍 Interview Thinking (Added Layer)

* Why file handling important?
  👉 persistence

* When to use np.savez?
  👉 multiple arrays

---

# ⚠️ Common Mistakes

* Overwriting files unknowingly ❌
* Not organizing files ❌
* Not using efficient formats ❌

---

# 💡 Key Takeaways

✔ np.save → save array
✔ np.load → load array
✔ np.savez → multiple arrays
✔ Essential for data workflows

---

# 🎯 Final Insight

👉 Data is valuable
👉 Saving it efficiently = productivity boost

---

# Summary 

In this lesson I learned:

* Saving arrays
* Loading arrays
* Working with datasets
* Multiple array storage
* Real-world data workflows

---
