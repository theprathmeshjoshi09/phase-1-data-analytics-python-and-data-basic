# 🚀 Module 1.1 — Programming Fundamentals With Python

## Topic 1.13: Debugging

---

# 🔥 Real-World Perspective

Writing code is only **50% of the job**

👉 The other 50% is:

* finding errors
* understanding failures
* fixing bugs

---

## 🧠 Real Insight

Even professional developers:

* spend more time debugging than coding
* rely heavily on debugging skills

---

# 13. Debugging 

Debugging is the process of:
👉 identifying
👉 analyzing
👉 fixing errors in a program

---

## 📊 Data Analyst Perspective

In data analytics, debugging is used for:

* fixing incorrect calculations
* handling missing data
* resolving data type issues
* validating outputs

---

## 🔧 Real Example

```python id="z8n3kp"
def calculate_profit(revenue, cost):
    return revenue - cost

print(calculate_profit(1000, 5000))
```

👉 Output is negative → debugging needed

---

# 13.1 Debugging Techniques 

---

## 📊 Practical Approach

1. Understand the problem
2. Reproduce the error
3. Isolate the issue
4. Fix and test

---

## 🔥 Real Insight

👉 Debugging is a **thinking process**, not just tools

---

# 🔍 Interview Thinking

* What is debugging?
  👉 Finding and fixing errors

---

# 13.2 Print Debugging 

---

## 📊 Real Use Case

```python id="m4k8qx"
a = 10
b = 0

print("Before division")
print("a =", a, "b =", b)

result = a / b
```

---

## 🔥 Insight

👉 Helps track:

* variable values
* execution flow

---

## 📊 Data Use Case

* checking data values
* verifying transformations

---

# 13.3 Python Debugger (`pdb`) 

---

## 📊 Real Use Case

```python id="q7t2kp"
import pdb

pdb.set_trace()
```

---

## 🔥 What You Can Do

* step through code
* inspect variables
* test expressions

---

## 📊 When to Use

* complex bugs
* large programs

---

# 13.4 Breakpoints 

---

## 📊 Real Insight

Breakpoints pause execution

---

## 📊 Use Case

* inspect data
* analyze logic

---

## 🔥 Real Tools

* VS Code debugger
* PyCharm debugger

---

# 13.5 Stack Traces 

---

## 📊 Example

```python id="x3p9rv"
def divide(a, b):
    return a / b

divide(10, 0)
```

---

## 🔥 Insight

👉 Stack trace shows:

* where error happened
* execution path

---

## 📊 Why Important

👉 Helps locate bugs quickly

---

# 13.6 Logging 

---

## 📊 Real Use Case

```python id="c6k8mn"
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Processing data")
```

---

## 🔥 Why Logging > Print

✔ structured
✔ persistent
✔ used in production

---

## 📊 Real Applications

* monitoring systems
* tracking pipelines
* debugging production issues

---

# 13.7 Debugging Tools 

---

## 📊 Common Tools

* pdb
* IDE debugger
* logging systems

---

## 📊 Real Insight

👉 Professionals use:

* breakpoints
* variable inspection
* step execution

---

# 🧠 Real Mini Case Study

## Problem: Data Error

```python id="r5t8kp"
data = [10, 20, 30]

average = sum(data) / len(data)

print(average)
```

---

## Debug Scenario

```python id="n8k2pz"
data = []

average = sum(data) / len(data)
```

👉 Error: division by zero

---

## Fix

```python id="u4m9rx"
if len(data) == 0:
    print("No data available")
else:
    print(sum(data)/len(data))
```

👉 Real-world error handling

---

# 🔍 Interview Thinking (Added Layer)

* What is debugging?
  👉 finding and fixing errors

* Difference between bug types?
  👉 syntax vs logical

* Best debugging approach?
  👉 step-by-step analysis

---

# ⚠️ Common Mistakes

* Ignoring error messages ❌
* Guessing instead of analyzing ❌
* Not checking edge cases ❌

---

# 💡 Key Takeaways

✔ Debugging is essential skill
✔ Print helps small debugging
✔ pdb for deep debugging
✔ Logging for real systems

---

# 🎯 Final Insight

👉 Coding makes you a programmer
👉 Debugging makes you a **professional**

---

# Summary 

In this lesson I learned:

* Debugging concepts
* Debugging techniques
* Print debugging
* Python debugger (pdb)
* Breakpoints
* Stack traces
* Logging
* Real-world debugging practices

---
