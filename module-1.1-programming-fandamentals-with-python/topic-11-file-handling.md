# 🚀 Module 1.1 — Programming Fundamentals With Python

## Topic 1.11: File Handling  

---

# 🔥 Real-World Perspective

File handling is where programs move from **temporary memory → permanent storage**

👉 Without file handling:

* Data is lost after program ends
* No datasets can be processed
* No real-world applications possible

Real-world usage:

* reading CSV datasets
* storing logs
* saving reports
* handling user data

---

# 11. File Handling 

File handling allows programs to **store and retrieve data from files**

---

## 📊 Data Analyst Perspective

This is one of the **most important topics**

👉 Because:

* All real data comes from files
* CSV, JSON, Excel → all handled using file operations

Example:

```python id="k3p9rx"
with open("sales.txt", "r") as file:
    data = file.read()
    print(data)
```

👉 This is how datasets are loaded

---

# 11.1 File Systems 

A file system organizes files on disk

---

## 📊 Real Insight

Projects follow structured storage:

```id="u7n2lp"
project/
 ┣ data/
 ┣ scripts/
 ┣ outputs/
```

---

## 🔥 Why It Matters

👉 Clean structure = professional project

---

# 11.2 Reading Files 

Reading retrieves stored data

---

## 📊 Real Use Case

```python id="t5q8kp"
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
```

---

## 📊 Data Use Case

* loading datasets
* reading logs
* reading configuration files

---

# 🔍 Interview Thinking

* Difference between read modes?
  👉 `"r"` → read only

---

# 11.3 Writing Files 

Writing stores data into file

---

## 📊 Real Use Case

```python id="m8k3vt"
with open("output.txt", "w") as file:
    file.write("Processed data")
```

---

## ⚠️ Important Insight

👉 `"w"` overwrites existing data

---

## 📊 Real Scenario

* saving analysis results
* exporting reports

---

# 11.4 File Modes 

---

## 📊 Practical Understanding

| Mode | Use Case       |
| ---- | -------------- |
| r    | read data      |
| w    | overwrite file |
| a    | append logs    |

---

## 🔥 Real Insight

👉 `"a"` is used in:

* logging systems
* audit trails

---

# 11.5 Text Files 

---

## 📊 Real Use Cases

* `.csv` → datasets
* `.json` → APIs
* `.txt` → logs

---

## 📊 Example

```python id="q4n7xs"
with open("data.txt", "r") as file:
    print(file.read())
```

---

# 11.6 Binary Files 

---

## 📊 Real Use Cases

* images
* audio
* videos

---

## ⚠️ Important Insight

👉 Cannot read as text

---

# 11.7 File Paths 

---

## 📊 Real Use Case

```python id="r2p8mx"
with open("data/sales.csv", "r") as file:
    print(file.read())
```

---

## 🔥 Best Practice

👉 Use relative paths in projects

---

# 🔍 Interview Thinking

* Absolute vs relative path?
  👉 full path vs current directory path

---

# 11.8 File Operations 

---

# 🔧 open()

```python id="x8v2rt"
file = open("data.txt", "r")
```

---

# 🔧 read()

```python id="c5p1wk"
file.read()
```

---

# 🔧 write()

```python id="n9t3lz"
file.write("Hello")
```

---

# 🔧 append()

```python id="u6m2pq"
file.write("\nNew Data")
```

---

# 🔧 close()

```python id="z3q7mk"
file.close()
```

---

## 🔥 Important Insight

👉 Always close files OR use `with`

---

# Using Context Manager (`with`) (Enhanced)

---

## 📊 Best Practice

```python id="y1k8rm"
with open("data.txt", "r") as file:
    content = file.read()
```

---

## 🔥 Why Important

👉 Automatically closes file
👉 Prevents memory issues

---

# 🧠 Real Mini Case Study

## Problem: Save Processed Data

```python id="v4p9sx"
sales = [100, 200, 300]

total = sum(sales)

with open("result.txt", "w") as file:
    file.write(f"Total Sales: {total}")
```

👉 This is real-world pipeline:

* process data
* store result

---

# 🔍 Interview Thinking (Added Layer)

* What is file handling?
  👉 reading/writing data from files

* Why important?
  👉 persistent storage

* Best practice?
  👉 use `with` statement

---

# ⚠️ Common Mistakes

* Forgetting to close file ❌
* Overwriting data unintentionally ❌
* Using wrong file path ❌

---

# 💡 Key Takeaways

✔ Files store permanent data
✔ read/write/append are core operations
✔ Use `with` for safety
✔ Essential for data analytics

---

# 🎯 Final Insight

👉 File handling = entry point to **real datasets**

Without this → no data analysis

---

# Summary 

In this lesson I learned:

* File handling concepts
* Reading and writing files
* File modes and paths
* Text and binary files
* Context managers
* Real-world data handling

---
