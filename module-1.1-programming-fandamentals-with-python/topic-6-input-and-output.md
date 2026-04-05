# 🚀 Module 1.1 — Programming Fundamentals With Python

## Topic 1.6: Input and Output

---

# 🔥 Real-World Perspective

Input & Output is where programs become **useful in the real world**

👉 Without I/O:

* No user interaction
* No data collection
* No results display

Every real system depends on it:

* Forms → input
* Dashboards → output
* APIs → input/output

---

# 6. Input and Output 

Programs interact with users and systems through:

* **Input → data coming into system**
* **Output → processed results**

---

## 📊 Data Analyst Perspective

In real-world analytics:

* Input → CSV files, APIs, databases
* Output → reports, dashboards, insights

Example:

```python id="q4c7rm"
sales = [100, 200, 300]
print("Total Sales:", sum(sales))
```

👉 Output becomes **decision-making data**

---

# 6.1 `print()` Function 

Used to display output

---

## 📊 Real Use Case

```python id="b1a8zv"
revenue = 10000
print("Revenue:", revenue)
```

👉 Used in:

* debugging
* displaying results
* logs

---

## 🔥 Insight

👉 In real projects, `print()` is replaced by:

* logging
* dashboards
* reports

---

# 6.2 `input()` Function 

Used to collect user input

---

## 📊 Real Use Case

```python id="d2m3kp"
name = input("Enter customer name: ")
```

---

## ⚠️ Critical Insight

```python id="sxr7lt"
age = input("Enter age: ")
```

👉 This is always **string**

---

## ✅ Correct Way

```python id="k9x2op"
age = int(input("Enter age: "))
```

---

## 📊 Real-World Scenario

* Forms
* User registrations
* CLI tools

---

# 🔍 Interview Thinking

* What does input() return?
  👉 String

---

# 6.3 Output Formatting 

Formatting makes output **readable and professional**

---

## 📊 Example

```python id="n8y1tb"
name = "Rahul"
age = 25

print("Name:", name)
print("Age:", age)
```

---

## 🔥 Why It Matters

👉 Clean output = better understanding

---

# 6.4 f-Strings 

Modern and best way for formatting

---

## 📊 Real Use Case

```python id="m4t8kl"
name = "Rahul"
revenue = 5000

print(f"Customer {name} generated {revenue} revenue")
```

---

## 🔥 Advantage

* clean
* readable
* powerful

---

## 🔍 Interview Thinking

* Why f-strings better?
  👉 readability + performance

---

# 6.5 `format()` Method (Insight)

Older method but still useful

---

## 📊 Use Case

```python id="f9r2bx"
print("Revenue: {}".format(5000))
```

---

## ⚠️ Insight

👉 Mostly replaced by f-strings today

---

# 6.6 Command Line Input 

Programs can take input from terminal

---

## 📊 Real Use Case

```bash id="f7m1op"
python script.py Rahul
```

---

## 🔧 Python Example

```python id="l2s8nv"
import sys

name = sys.argv[1]
print("Hello", name)
```

---

## 📊 Where Used

* automation scripts
* data pipelines
* batch processing

---

# 6.7 Reading Multiple Inputs 

---

## 📊 Real Data Example

```python id="q5h7dp"
name = input("Enter name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")

print(f"{name} is {age} years old from {city}")
```

---

## 🔥 Real Use Case

* surveys
* forms
* CLI apps

---

# 🧠 Real Mini Case Study

## Problem: Customer Data Collection

```python id="m9z6tw"
name = input("Enter customer name: ")
purchase = float(input("Enter purchase amount: "))

print(f"{name} spent ₹{purchase}")
```

👉 This is real-world data collection

---

# 🔍 Interview Thinking (Added Layer)

* What is input?
  👉 Data entering system

* What is output?
  👉 Processed result

* Why formatting important?
  👉 readability

---

# ⚠️ Common Mistakes

* Not converting input ❌
* Messy output ❌
* Overusing print instead of structured output ❌

---

# 💡 Key Takeaways

✔ Input collects data
✔ Output displays results
✔ Formatting improves readability
✔ f-strings are best practice

---

# 🎯 Final Insight

👉 Input = raw data
👉 Output = insights

This is the foundation of **data analytics pipelines**

---

# Summary 

In this lesson I learned:

* Input and output concepts
* print() and input() usage
* Output formatting techniques
* f-strings and format()
* Command-line input
* Real-world data interaction

---
