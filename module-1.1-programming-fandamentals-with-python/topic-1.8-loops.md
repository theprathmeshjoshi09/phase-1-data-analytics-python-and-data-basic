# 🚀 Module 1.1 — Programming Fundamentals With Python

## Topic 1.8: Loops

---

# 🔥 Real-World Perspective

Loops are the **engine of automation**

👉 Without loops:

* You cannot process large datasets
* You cannot automate tasks
* You cannot build scalable systems

Real-world usage:

* Processing 1 million records
* Cleaning datasets
* Running batch operations

---

# 8. Loops 

Loops allow programs to **execute code repeatedly**

---

## 📊 Data Analyst Perspective

Loops are used to:

* iterate through datasets
* clean data
* transform values

Example:

```python id="f4z7kp"
sales = [100, 200, 300]

total = 0
for s in sales:
    total += s

print(total)
```

👉 This is basic data aggregation

---

# 8.1 Loop Concepts 

---

## 🔁 Iteration

Repeating steps

---

## 📊 Real Use Case

```python id="j7x2dm"
for i in range(3):
    print("Processing row", i)
```

---

## 🔢 Counters

Used to track loop execution

---

## 📊 Real Example

```python id="t2v8ql"
count = 0

for i in range(5):
    count += 1

print(count)
```

---

# 🔍 Interview Thinking

* What is iteration?
  👉 Repeated execution

---

# 8.2 Types of Loops 

---

# 🔁 For Loop 

Used for iterating over sequences

---

## 📊 Real Data Use Case

```python id="m8w3kp"
customers = ["A", "B", "C"]

for customer in customers:
    print(customer)
```

---

## 📊 Data Processing Example

```python id="k1r9tx"
sales = [100, 200, 300]

for s in sales:
    print(s * 2)
```

👉 Transformation of data

---

## 🔍 Interview Thinking

* When to use for loop?
  👉 When sequence is known

---

# 🔁 While Loop 

Runs until condition is False

---

## 📊 Real Use Case

```python id="d3n7px"
count = 1

while count <= 5:
    print("Processing batch", count)
    count += 1
```

---

## ⚠️ Important Insight

👉 Risk of infinite loops

---

## 🔍 Interview Thinking

* When to use while loop?
  👉 When condition-based execution needed

---

# 8.3 Loop Control Statements 

---

# 🛑 Break

Stops loop

---

## 📊 Real Use Case

```python id="q7w3bt"
for i in range(10):
    if i == 5:
        break
    print(i)
```

👉 Used in:

* stopping conditions
* search operations

---

# 🔄 Continue

Skips iteration

---

## 📊 Real Use Case

```python id="z9x1ke"
for i in range(5):
    if i == 2:
        continue
    print(i)
```

👉 Used in:

* filtering data

---

# ⏸ Pass

Placeholder

---

## 📊 Use Case

```python id="y4p8lm"
for i in range(5):
    pass
```

👉 Used in:

* incomplete code
* structure planning

---

# 8.4 Nested Loops 

Loop inside loop

---

## 📊 Real Use Case

```python id="n6k3rs"
for i in range(3):
    for j in range(2):
        print(i, j)
```

---

## 📊 Data Use Case

* comparing datasets
* matrix operations

---

# ⚠️ Performance Insight

👉 Nested loops = slower
👉 Important in large data

---

# 8.5 Loop Patterns (Thinking)

---

## 📊 Why Patterns Matter

👉 Improves logic building
👉 Helps in problem solving

---

# 🧠 Real Mini Case Study

## Problem: Sales Analysis

```python id="r3t8bn"
sales = [100, 200, 300, 400]

total = 0

for s in sales:
    if s > 150:
        total += s

print(total)
```

👉 Filtering + aggregation

---

# 🔍 Interview Thinking (Added Layer)

* What is loop?
  👉 Repeated execution

* Difference between for and while?
  👉 Sequence vs condition

* Why loops important?
  👉 Automation + data processing

---

# ⚠️ Common Mistakes

* Infinite loops ❌
* Wrong conditions ❌
* Not updating counter ❌

---

# 💡 Key Takeaways

✔ Loops automate repetition
✔ for → sequence-based
✔ while → condition-based
✔ break/continue control flow

---

# 🎯 Final Insight

👉 Loops are the foundation of:

* data processing
* automation
* scalable systems

---

# Summary

In this lesson I learned:

* Loop concepts and iteration
* for and while loops
* Loop control statements
* Nested loops
* Real-world data processing use cases

---
