# 🚀 Module 1.1 — Programming Fundamentals With Python

## Topic 09: Functions

---

# 🔥 Real-World Perspective

Functions are the **building blocks of real-world software**

👉 Without functions:

* Code becomes repetitive
* Difficult to manage
* Hard to scale

Every real system uses functions:

* APIs → functions
* Data pipelines → functions
* ML models → functions

---

# 9. Functions 

A function is a reusable block of code that performs a **specific task**

---

## 📊 Data Analyst Perspective

Functions are used to:

* clean data
* transform datasets
* calculate metrics

Example:

```python id="y3n8kx"
def calculate_profit(revenue, cost):
    return revenue - cost

print(calculate_profit(10000, 7000))
```

👉 Reusable business logic

---

# 9.1 What is a Function

A function is a **named reusable block of logic**

---

## 🔧 Real Use Case

```python id="k7d2mq"
def calculate_discount(price, discount):
    return price - discount
```

---

## 🔍 Interview Thinking

* Why use functions?
  👉 Reusability + clean code

---

# 9.2 Function Definition 

Defined using `def`

---

## 📊 Real Insight

👉 Functions separate logic from execution

---

# 9.3 Function Calling 

Function must be called to execute

---

## 📊 Real Use Case

```python id="t4x9lp"
def greet():
    print("Welcome")

greet()
```

---

## 🔥 Insight

👉 Same function can be reused multiple times

---

# 9.4 Parameters 

Inputs to function

---

## 📊 Real Example

```python id="n2p8rs"
def calculate_tax(amount):
    return amount * 0.18
```

---

# 9.5 Arguments 

Values passed to function

---

## 📊 Example

```python id="v6m1qa"
calculate_tax(1000)
```

---

# 🔍 Interview Thinking

* Parameter vs Argument?
  👉 Definition vs actual value

---

# 9.6 Return Values 

Return sends result back

---

## 📊 Real Use Case

```python id="p3r7vd"
def average(a, b):
    return (a + b) / 2
```

---

## 🔥 Important Insight

👉 Without return → function gives no usable output

---

# 9.7 Default Arguments 

---

## 📊 Real Use Case

```python id="r9w3kx"
def greet(name="User"):
    print("Hello", name)
```

---

## 📊 Application

* optional inputs
* flexible functions

---

# 9.8 Keyword Arguments 

---

## 📊 Real Use Case

```python id="c1z7kt"
def create_user(name, age):
    print(name, age)

create_user(age=21, name="Rahul")
```

---

## 🔥 Insight

👉 Improves readability

---

# 9.9 Variable Length Arguments 

---

## 📊 Real Use Case

```python id="z8p2mw"
def total_sales(*sales):
    return sum(sales)

print(total_sales(100, 200, 300))
```

---

## 📊 Application

* dynamic data inputs
* flexible APIs

---

# 9.10 Lambda Functions

---

## 📊 Real Use Case

```python id="q4x9bt"
square = lambda x: x * x
print(square(5))
```

---

## 📊 Data Use Case

```python id="m6k2rv"
numbers = [1, 2, 3]
squared = list(map(lambda x: x*x, numbers))
```

👉 Used in:

* data transformation
* quick operations

---

# 🔍 Interview Thinking

* When to use lambda?
  👉 small, one-line functions

---

# 9.11 Docstrings (Enhanced)

---

## 📊 Real Use Case

```python id="t7q4vy"
def add(a, b):
    """Returns sum of two numbers"""
    return a + b
```

---

## 🔥 Why Important

👉 Documentation for:

* team collaboration
* readability

---

# 🧠 Real Mini Case Study

## Problem: Sales Analytics Function

```python id="v2k9rn"
def analyze_sales(sales):
    total = sum(sales)
    avg = total / len(sales)
    return total, avg

result = analyze_sales([100, 200, 300])
print(result)
```

👉 Real-world reusable logic

---

# 🔍 Interview Thinking (Added Layer)

* What is function?
  👉 reusable block of code

* Why important?
  👉 modularity + reuse

* What is return?
  👉 output of function

---

# ⚠️ Common Mistakes

* Forgetting return ❌
* Confusing parameters and arguments ❌
* Writing very large functions ❌

---

# 💡 Key Takeaways

✔ Functions make code reusable
✔ Parameters accept input
✔ Return provides output
✔ Lambda for quick logic

---

# 🎯 Final Insight

👉 Functions = structure of professional code
👉 Without functions → no scalable systems

---

# Summary 

In this lesson I learned:

* Function basics
* Parameters and arguments
* Return values
* Default and keyword arguments
* Variable length arguments
* Lambda functions
* Docstrings and documentation
* Real-world applications

---
