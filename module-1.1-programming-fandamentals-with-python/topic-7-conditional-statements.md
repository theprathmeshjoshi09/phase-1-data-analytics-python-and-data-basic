# 🚀 Module 1.1 — Programming Fundamentals with Python

## Topic 1.7: Conditional Statements

---

# 🔥 Real-World Perspective

Conditional statements are the **decision-making brain** of any program.

👉 Every real-world system uses conditions:

* ATM → check balance before withdrawal
* E-commerce → apply discount if eligible
* Login system → verify credentials

---

# 7. Conditional Statements 

Conditional statements allow programs to **make decisions based on conditions**

---

## 📊 Data Analyst Perspective

In data analytics, conditions are used for:

* filtering data
* segmentation
* classification

Example:

```python id="r5c7ka"
sales = 5000

if sales > 3000:
    print("High Sales")
```

👉 This is basic data classification

---

# 7.1 Boolean Logic 

Boolean values are:

* `True`
* `False`

---

## 📊 Real Use Case

```python id="d9m2fa"
is_paid = True
is_active = False
```

---

## 🔥 Insight

👉 Most business logic runs on boolean conditions

---

# 🔍 Interview Thinking

* What is boolean?
  👉 True/False value

---

# 7.2 if Statement 

Executes code if condition is True

---

## 📊 Real Use Case

```python id="f7b2ka"
age = 25

if age >= 18:
    print("Eligible")
```

---

## 📊 Data Use Case

```python id="c3k8zn"
if revenue > 10000:
    print("Top Performer")
```

---

# 7.3 else Statement 

Executes when condition is False

---

## 📊 Real Use Case

```python id="q2p9hd"
if balance >= 500:
    print("Transaction allowed")
else:
    print("Insufficient balance")
```

---

## 🔥 Business Example

* Loan rejection
* Payment failure

---

# 7.4 elif Statement 

Used for multiple conditions

---

## 📊 Real Use Case

```python id="p6k1vx"
marks = 82

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("D")
```

---

## 📊 Data Segmentation Example

* Customer tiers
* Performance categories

---

# 🔍 Interview Thinking

* Order of execution?
  👉 Top to bottom

---

# 7.5 Nested Conditions 

Condition inside another condition

---

## 📊 Real Use Case

```python id="x1t7yu"
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Allowed")
```

---

## 🔥 Real Application

* KYC verification
* Multi-step validation

---

# 7.6 Logical Expressions 

Combining conditions

---

## 📊 Real Use Case

```python id="j4c9re"
age = 25
income = 40000

if age > 18 and income > 30000:
    print("Eligible for loan")
```

---

## 📊 Fraud Detection Example

```python id="z8w3nt"
if amount > 10000 or location == "suspicious":
    print("Flag transaction")
```

---

# 🔍 Interview Thinking

* AND vs OR?
  👉 AND → both required
  👉 OR → any one

---

# 7.7 Ternary Operator 

Short form of if-else

---

## 📊 Example

```python id="m3r8lw"
age = 20
status = "Adult" if age >= 18 else "Minor"
```

---

## 📊 Real Use Case

* labeling
* quick classification

---

# 🧠 Real Mini Case Study

## Problem: Customer Classification

```python id="w6y2kp"
purchase = 5000

if purchase > 10000:
    category = "Premium"
elif purchase > 5000:
    category = "Gold"
else:
    category = "Regular"

print(category)
```

👉 Real-world segmentation logic

---

# 🔍 Interview Thinking (Added Layer)

* What is conditional statement?
  👉 Decision-making structure

* Why important?
  👉 Controls program flow

* Where used in data?
  👉 Filtering and classification

---

# ⚠️ Common Mistakes

* Wrong condition logic ❌
* Missing indentation ❌
* Confusing == and = ❌

---

# 💡 Key Takeaways

✔ Conditions control logic
✔ Boolean drives decisions
✔ elif handles multiple cases
✔ Logical operators combine conditions

---

# 🎯 Final Insight

👉 Data analysis = filtering + decision-making
👉 Conditions are at the core of both

---

# Summary

In this lesson I learned:

* Conditional statements
* Boolean logic
* if, else, elif
* Nested conditions
* Logical operators
* Real-world decision-making

---
