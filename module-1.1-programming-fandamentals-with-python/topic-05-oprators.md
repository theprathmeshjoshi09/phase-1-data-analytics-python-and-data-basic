# 🚀 Module 1.1 — Programming Fundamentals With Python    

## Topic 05: Operators 

---

# 🔥 Real-World Perspective

Operators are not just symbols.

👉 They are the **core of all calculations, logic, and decision-making**

Every real-world system uses operators:

* Banking → interest calculation
* E-commerce → pricing & discounts
* Analytics → KPIs, metrics

---

# 5. Operators 

Operators are symbols used to **perform operations on data**

---

## 📊 Data Analyst Perspective

Operators are used in:

* calculating revenue, profit, growth
* filtering datasets
* creating conditions

Example:

```python id="c1s9yy"
revenue = 10000
cost = 7000

profit = revenue - cost
print(profit)
```

👉 This is basic business analytics logic

---

# 5.1 Arithmetic Operators

Used for **mathematical calculations**

---

## 📊 Real-World Use Case

```python id="xg6o4h"
price = 1000
discount = 200

final_price = price - discount
```

---

## 🔍 Important Use Cases

* `+` → total sales
* `-` → profit/loss
* `*` → scaling values
* `/` → ratios

---

## ⚠️ Division Insight

```python id="tsj7j3"
print(5 / 2)   # 2.5
print(5 // 2)  # 2
```

👉 Important in:

* averages
* data normalization

---

## 🔍 Interview Thinking

* Difference between `/` and `//`?
  👉 float vs integer division

---

# 5.2 Comparison Operators 

Used to **compare values**

---

## 📊 Real Data Use Case

```python id="ql1q3r"
age = 25

print(age >= 18)
```

👉 Used in:

* filtering data
* segmentation

---

## 📊 Pandas Insight

```python id="u8w4be"
df[df["age"] > 18]
```

👉 This is real-world filtering

---

## 🔍 Interview Thinking

* Output of comparison?
  👉 Boolean (True/False)

---

# 5.3 Logical Operators

Combine multiple conditions

---

## 📊 Real Use Case

```python id="jz7l0t"
age = 25
income = 50000

if age > 18 and income > 30000:
    print("Eligible")
```

---

## 🔥 Business Logic Example

* Loan approval
* Customer segmentation
* Fraud detection

---

## 🔍 Interview Thinking

* AND vs OR?
  👉 AND → both true
  👉 OR → at least one true

---

# 5.4 Assignment Operators 

Used to assign/update values

---

## 📊 Real Use Case

```python id="6mjvgs"
sales = 1000
sales += 200   # new sale added
```

---

## 🔥 Data Pipeline Insight

Used in:

* cumulative sums
* iterative calculations

---

## 🔍 Interview Thinking

* What does `+=` mean?
  👉 Add and assign

---

# 5.5 Bitwise Operators 

Used at **binary level**

---

## ⚠️ Reality Check

👉 Not heavily used in data analytics
👉 Important in:

* system programming
* optimization

---

## 🔍 When It Matters

* low-level programming
* performance optimization

---

# 🧠 Real Mini Case Study

## Problem: E-commerce Order Calculation

```python id="q9o6p6"
price = 1000
discount = 100
tax_rate = 0.18

subtotal = price - discount
tax = subtotal * tax_rate

final_price = subtotal + tax

print(final_price)
```

👉 This is real-world pricing logic

---

# 🔍 Interview Thinking (Added Layer)

* What are operators?
  👉 Symbols to perform operations

* Why important?
  👉 Used in all calculations

* Which operators used most in data?
  👉 Arithmetic + comparison + logical

---

# ⚠️ Common Mistakes

* Using wrong operator (`=` vs `==`) ❌
* Division mistakes ❌
* Ignoring operator precedence ❌

---

# 💡 Key Takeaways

✔ Operators perform all calculations
✔ Comparison returns boolean
✔ Logical operators combine conditions
✔ Assignment updates values

---

# 🎯 Final Insight

👉 Operators = logic engine of programs
👉 Without operators → no calculations, no decisions

---

# Summary 

In this lesson I learned:

* Arithmetic operations
* Comparison logic
* Logical conditions
* Assignment operations
* Bitwise basics
* Real-world applications in analytics

---
