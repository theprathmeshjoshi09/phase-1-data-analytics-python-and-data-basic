# 🚀 Module 1.1 — Programming Fundamentals With Python

## Topic 1.4: Data Types  

---

# 🔥 Real-World Perspective

Data types are not just “types”.

👉 They define **how data behaves, how it is stored, and what operations you can perform**

In real-world systems:

* Numbers → revenue, salary, transactions
* Strings → names, emails, categories
* Booleans → status flags (active/inactive)

---

# 4. Data Types 

Data types define the **kind of value a variable holds** and how it can be used.

---

## 📊 Data Analyst Perspective

In data analytics:

* Data types directly affect:

  * calculations
  * memory usage
  * performance
  * analysis accuracy

Example:

```python id="f3y3ra"
revenue = 10000       # int
growth_rate = 0.12    # float
company = "TCS"       # string
is_profitable = True  # boolean
```

👉 Wrong data type = wrong analysis

---

# 4.1 Primitive Data Types 

Primitive types are the **foundation of all data operations**

---

## 🔢 Integers (int)

### 📊 Real Use Case

* Number of customers
* Orders count

```python id="b7rq7r"
customers = 120
```

---

## 💰 Floats (float)

### 📊 Real Use Case

* Prices
* Revenue
* Percentages

```python id="l3a1uy"
price = 99.99
discount_rate = 0.15
```

---

## 📝 Strings (str)

### 📊 Real Use Case

* Names
* Product categories
* IDs

```python id="t8c6r6"
product_name = "Laptop"
```

---

## ✅ Booleans (bool)

### 📊 Real Use Case

* Login status
* Payment success

```python id="g8c7wr"
is_active = True
```

---

# 🔍 Interview Thinking

* Difference between int and float?
  👉 float has decimal precision

---

# 4.2 Data Structures 

Data structures store **multiple values**

---

## 📋 Lists

### 📊 Real Use Case

* Sales data
* Transactions

```python id="c0clb8"
sales = [100, 200, 300]
```

👉 Used heavily in:

* Pandas preprocessing

---

## 📦 Tuples

### 📊 Real Use Case

* Fixed data (coordinates, constants)

```python id="j69y2x"
location = (18.52, 73.85)
```

---

## 🔁 Sets

### 📊 Real Use Case

* Unique values
* Removing duplicates

```python id="2o8zz5"
unique_users = {1, 2, 2, 3}
```

---

## 📊 Dictionaries

### 📊 Real Use Case

* JSON data
* API responses

```python id="rjfx8r"
user = {"name": "Prathmesh", "age": 21}
```

👉 Very important for:

* real-world data processing

---

# 🔍 Interview Thinking

* List vs Tuple?
  👉 Mutable vs Immutable

* Dictionary use?
  👉 Key-value mapping

---

# 4.3 Type Conversion 

Converting one type into another

---

## 📊 Real Data Scenario

User input:

```python id="o1z9ko"
age = input("Enter age: ")
```

👉 Problem:

* It's a string

Solution:

```python id="frnxy3"
age = int(age)
```

---

## 🔥 Important Insight

👉 Data cleaning often involves type conversion

---

# 4.4 Type Casting 

Explicit conversion for operations

---

## 📊 Example

```python id="l7h7u5"
a = 5
b = 2

result = float(a) / b
```

👉 Ensures correct output

---

# 🔍 Interview Thinking

* Why type casting?
  👉 To control operations

---

# 4.5 Dynamic Typing 

Python automatically assigns types

---

## 🔧 Example

```python id="qg5wh7"
x = 10
x = "Data"
```

---

## 📊 Real Insight

👉 Useful in:

* fast prototyping
* data exploration

---

## ⚠️ Risk

👉 Can cause bugs if not careful

---

# 4.6 Memory Representation (Insight)

Variables store values in memory

---

## 🔥 Important Concept

```python id="8c8dkw"
a = 10
b = a
```

👉 Both may point to same memory

---

## 📊 Why It Matters

* Memory optimization
* Performance in large datasets

---

# 🧠 Real Mini Case Study

## Problem: Customer Data Processing

```python id="86cbtv"
customer = {
    "name": "Rahul",
    "age": 25,
    "is_active": True
}

print(customer["name"])
```

👉 Real-world structure (like APIs, databases)

---

# 🔍 Interview Thinking (Added Layer)

* What is data type?
  👉 Type of value stored

* Why important?
  👉 Controls operations

* What is dynamic typing?
  👉 No explicit type declaration

---

# ⚠️ Common Mistakes

* Mixing data types ❌
* Not converting input ❌
* Using wrong data structure ❌

---

# 💡 Key Takeaways

✔ Every value has a type
✔ Data structures store collections
✔ Type conversion is critical
✔ Python is dynamically typed

---

# 🎯 Final Insight

👉 Data types define how data behaves
👉 Understanding them = better data analysis

---

# Summary 

In this lesson I learned:

* Primitive data types
* Data structures (list, tuple, set, dictionary)
* Type conversion and casting
* Dynamic typing
* Memory behavior
* Real-world applications in data analytics

---
