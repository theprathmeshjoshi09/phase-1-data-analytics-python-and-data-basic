# 🚀 Module 1.1 — Programming Fundamentals 

## Topic 1.10: Recursion    

---

# 🔥 Real-World Perspective

Recursion is not just a concept — it’s a **thinking approach**

👉 It helps solve problems that:

* repeat themselves
* break into smaller versions of the same problem

Real-world usage:

* file systems (folders inside folders)
* tree structures (organization hierarchy)
* algorithms (searching, sorting)

---

# 10. Recursion 

Recursion is when a function **calls itself** to solve a problem.

---

## 📊 Data Analyst Perspective

Recursion is not heavily used in daily analytics, but:

👉 It builds:

* problem-solving skills
* algorithmic thinking

Used in:

* hierarchical data
* tree-based models
* advanced algorithms

---

# 10.1 Recursive Functions 

A recursive function calls itself during execution

---

## 🔧 Real Example

```python id="k3n7xp"
def process_levels(level):
    if level > 0:
        print("Processing level", level)
        process_levels(level - 1)
```

---

## 🔍 Interview Thinking

* What is recursion?
  👉 Function calling itself

---

# 10.2 Base Case (Enhanced)

Base case stops recursion

---

## 🔥 Critical Insight (Very Important)

👉 Without base case → infinite recursion → crash

---

## 📊 Example

```python id="t6m2qa"
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n-1)
```

---

# 10.3 Recursive Case 

The part where function calls itself

---

## 📊 Insight

👉 Each call reduces problem size

---

# 🔍 Interview Thinking

* What are two parts of recursion?
  👉 Base case + recursive case

---

# 10.4 Call Stack 

Every function call is stored in **stack memory**

---

## 🔥 Important Insight

```python id="u8k4pl"
factorial(3)
→ factorial(2)
→ factorial(1)
→ return
```

👉 Stack builds → then unwinds

---

## 📊 Why It Matters

* memory usage
* performance

---

# 10.5 Recursion vs Iteration 

---

## 📊 Real Insight

| Feature     | Recursion  | Iteration |
| ----------- | ---------- | --------- |
| Readability | High       | Medium    |
| Performance | Slower     | Faster    |
| Memory      | Uses stack | Efficient |

---

## 🔥 Rule

👉 Use recursion for:

* tree problems
* divide-and-conquer

👉 Use loops for:

* simple repetition

---

# 10.6 Recursion Problems 

---

## 📊 Common Use Cases

* factorial
* Fibonacci
* tree traversal
* search algorithms

---

# 10.7 Factorial Example 

```python id="c9r3wd"
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
```

---

## 📊 Real Thinking

👉 Break:

```
5! = 5 × 4!
```

---

# 10.8 Fibonacci Example 

```python id="m4x8lp"
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

---

## ⚠️ Performance Insight

👉 Very slow for large n

---

# 10.9 Tree Traversal 

---

## 📊 Real Use Case

* file systems
* decision trees

---

## 🔧 Example Thinking

```python id="v2k6rt"
def traverse(node):
    if node is None:
        return
    traverse(node.left)
    traverse(node.right)
```

---

# 🧠 Real Mini Case Study

## Problem: Sum of Numbers

```python id="p5r2nx"
def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n-1)

print(sum_numbers(5))
```

👉 Breaking problem into smaller parts

---

# 🔍 Interview Thinking (Added Layer)

* What is recursion?
  👉 Self-calling function

* Why use it?
  👉 Simplifies complex problems

* Biggest risk?
  👉 Infinite recursion

---

# ⚠️ Common Mistakes

* Missing base case ❌
* Stack overflow ❌
* Using recursion where loop is better ❌

---

# 💡 Key Takeaways

✔ Recursion breaks problems into smaller parts
✔ Base case stops recursion
✔ Call stack manages execution
✔ Not always efficient

---

# 🎯 Final Insight

👉 Recursion improves your **problem-solving ability**, not just coding

---

# Summary 

In this lesson I learned:

* What recursion is
* Recursive functions
* Base case and recursive case
* Call stack behavior
* Recursion vs iteration
* Real-world use cases

---
