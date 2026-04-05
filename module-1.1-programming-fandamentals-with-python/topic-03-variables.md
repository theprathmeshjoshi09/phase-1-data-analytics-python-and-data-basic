# 🚀 Module 1.1 — Programming Fundamentals With Python

## Topic 03: Variables

---

# 🔥 Real-World Perspective

Variables are not just “containers”.

👉 They represent **real-world data**

Examples:

* `revenue` → company earnings
* `age` → customer age
* `price` → product cost
* `is_active` → user activity status

---

# 3. Variables 

Variables allow programs to **store, modify, and use data dynamically**.

---

## 📊 Data Analyst Perspective

In data analytics:

* Variables store **columns of data**
* Used in:

  * calculations
  * filtering
  * transformations

Example:

```python
sales = 5000
cost = 3000
profit = sales - cost

print(profit)
```

👉 This is basic business logic using variables

---

# 3.1 What is a Variable 

A variable is a **named memory location** that stores data.

---

## 🔧 Real-World Example

```python
customer_name = "Rahul"
order_amount = 1200
discount = 100

final_price = order_amount - discount
```

👉 This is how real applications calculate values

---

## 🔍 Interview Thinking

* Why use variables?
  👉 To reuse and manipulate data efficiently

---

# 3.2 Variable Declaration (Insight)

Python does **automatic declaration**.

---

## 📊 Why this matters

👉 Faster development compared to languages like C

---

## ⚠️ Important Insight

Python is:
👉 **Dynamically typed**

---

# 3.3 Variable Assignment 

Assignment means storing a value.

---

## 🔧 Practical Example (Data Use Case)

```python
product_price = 100
tax = 18

total_price = product_price + tax
```

---

## 📊 Multiple Assignment Use Case

```python
revenue, cost, profit = 10000, 7000, 3000
```

Used in:

* data pipelines
* quick calculations

---

# 🔍 Interview Thinking

* What is assignment operator?
  👉 `=`

---

# 3.4 Variable Naming Rules (Thinking)

Good naming = professional code

---

## ❌ Bad

```python
x = 100
```

## ✅ Good

```python
monthly_revenue = 100
```

---

## 📊 Data Analyst Standard

Always use:

* meaningful names
* snake_case

---

# ⚠️ Common Mistakes

* Using unclear names ❌
* Using reserved keywords ❌
* Mixing naming styles ❌

---

# 3.5 Variable Scope 

Scope defines **where variables can be used**

---

## 🔧 Real Example

```python
total_sales = 1000

def calculate():
    tax = 100
    return total_sales - tax
```

👉 `total_sales` → global
👉 `tax` → local

---

## 📊 Why It Matters

In large projects:

* Avoids bugs
* Controls data flow

---

# 🔍 Interview Thinking

* Difference between local and global?
  👉 Scope accessibility

---

# 3.6 Mutable vs Immutable (Insight)

---

## 🔥 Important Concept (Very Important)

👉 Mutable → can change
👉 Immutable → cannot change

---

## 📊 Real Data Example

```python
data = [1, 2, 3]
data.append(4)
```

👉 Used in:

* data cleaning
* transformations

---

## Immutable Example

```python
name = "Rahul"
name = "Amit"
```

👉 New object created

---

# 🔍 Interview Thinking

* Why immutability matters?
  👉 Safer data handling

---

# 3.7 Constants 

Constants are fixed values.

---

## 📊 Real Use Cases

```python
TAX_RATE = 0.18
MAX_USERS = 1000
```

Used in:

* business rules
* configurations

---

# 🧠 Real Mini Case Study

## Problem: E-commerce Pricing

```python
price = 1000
discount = 200
tax = 0.18

final_price = (price - discount) + (price * tax)

print(final_price)
```

👉 This is real-world pricing logic

---

# 🔍 Interview Thinking (Added Layer)

* What is variable?
  👉 Named memory location

* Why naming is important?
  👉 Readability + maintainability

* Mutable vs immutable?
  👉 Changeable vs fixed

---

# ⚠️ Common Mistakes

* Overwriting variables accidentally
* Using same variable for multiple purposes
* Not understanding scope

---

# 💡 Key Takeaways

✔ Variables store data
✔ Good naming = clean code
✔ Scope controls accessibility
✔ Mutable vs immutable is critical

---

# 🎯 Final Insight

👉 Variables are not just syntax
👉 They represent **real-world data models**

---

# Summary 

In this lesson I learned:

* What variables are
* How they store and manage data
* Naming conventions and best practices
* Scope and memory behavior
* Mutable vs immutable concepts
* Real-world applications in data analytics