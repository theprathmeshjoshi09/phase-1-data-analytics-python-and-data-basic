
# 🚀 Module 1.4 — Data Visualization

## Topic 04: Matplotlib (Core Engine)

---

# 🔥 Real-World Perspective

In real-world analytics:

👉 Almost every visualization library in Python is built on top of Matplotlib

* Seaborn → built on Matplotlib
* Pandas plotting → uses Matplotlib
* Even advanced tools depend on its concepts

---

## 🧠 Real Insight

👉 If you understand Matplotlib:

* you understand visualization fundamentals
* you gain full control over charts

---

# 4. Matplotlib

Matplotlib is the **core visualization library in Python**.
It gives you full control over how charts are built and customized.

---

## 📊 Data Analyst Perspective

Used for:

* custom visualizations
* fine control over charts
* building complex plots

---

# 4.1 Figure & Axes System

Matplotlib works using two main components:

* **Figure** → entire canvas
* **Axes** → individual plot

---

## 📊 Real Use Case

```python id="mpl1"
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1,2,3], [4,5,6])
plt.show()
```

---

## 🔥 Insight

👉 Think of:

* Figure = page
* Axes = chart inside page

---

# 🔍 Interview Thinking

* What is Figure vs Axes?
  👉 canvas vs plot

---

# 4.2 Subplots & Layouts

Used to create multiple plots

---

## 📊 Real Use Case

```python id="mpl2"
fig, axs = plt.subplots(2, 2)

axs[0,0].plot([1,2,3], [1,4,9])
axs[0,1].plot([1,2,3], [2,5,8])

plt.show()
```

---

## 📊 Applications

* dashboards
* comparisons

---

## 🔥 Insight

👉 Used in real reports

---

# 4.3 Styling (Colors, Markers, Linestyles)

Customize chart appearance

---

## 📊 Real Use Case

```python id="mpl3"
plt.plot([1,2,3], [4,5,6],
         color='red',
         linestyle='--',
         marker='o')
plt.show()
```

---

## 📊 Applications

* highlighting trends
* improving readability

---

## 🔥 Insight

👉 Good styling = better communication

---

# 4.4 Annotations & Text

Add labels or highlight points

---

## 📊 Real Use Case

```python id="mpl4"
plt.plot([1,2,3], [4,5,6])
plt.text(2, 5, "Important Point")
plt.show()
```

---

## 📊 Applications

* storytelling
* highlighting insights

---

## 🔥 Insight

👉 Helps explain charts

---

# 4.5 Legends & Grids

Improve readability

---

## 📊 Real Use Case

```python id="mpl5"
plt.plot([1,2,3], [4,5,6], label="Line 1")
plt.legend()
plt.grid()
plt.show()
```

---

## 🔥 Insight

👉 Essential for professional charts

---

# 4.6 Saving Plots

Save charts as files

---

## 📊 Real Use Case

```python id="mpl6"
plt.plot([1,2,3], [4,5,6])
plt.savefig("plot.png")
```

---

## 📊 Applications

* reports
* dashboards
* presentations

---

## 🔥 Insight

👉 This is how charts reach stakeholders

---

# 🔥 Advanced Concepts

---

# 4.7 Custom Themes

```python id="mpl7"
plt.style.use('ggplot')
```

---

## 📊 Insight

👉 Consistent design

---

# 4.8 Twin Axes

Two y-axes

---

## 📊 Real Use Case

```python id="mpl8"
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()

ax1.plot([1,2,3], [10,20,30])
ax2.plot([1,2,3], [100,200,300])

plt.show()
```

---

## ⚠️ Warning

👉 Can mislead if used incorrectly

---

# 4.9 3D Plotting

```python id="mpl9"
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot([1,2,3], [4,5,6], [7,8,9])
plt.show()
```

---

## 📊 Applications

* scientific data
* simulations

---

# 4.10 Animation

```python id="mpl10"
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

x, y = [], []

def update(frame):
    x.append(frame)
    y.append(frame**2)
    ax.clear()
    ax.plot(x, y)

ani = FuncAnimation(fig, update, frames=range(10))
plt.show()
```

---

## 📊 Applications

* dynamic visualization
* simulations

---

# 🧠 Real Mini Case Study

## Problem: Sales Dashboard

```text id="d6u8pc"
Use:
- subplots → multiple metrics  
- styling → readability  
- annotations → highlight insights  
```

---

# 🔍 Interview Thinking (Added Layer)

* Why Matplotlib important?
  👉 foundation

* Most important concept?
  👉 figure + axes

---

# ⚠️ Common Mistakes

❌ Not using labels
❌ Poor styling
❌ Overcrowded plots
❌ Misusing twin axes

---

# 💡 Key Takeaways

✔ Figure & Axes = core concept
✔ Subplots = dashboards
✔ Styling = clarity
✔ Annotation = storytelling
✔ Save plots = real-world usage

---

# 🎯 Final Insight

👉 Matplotlib gives you **complete control over visualization**

---

# Summary

In this lesson I learned:

* Figure & Axes
* Subplots
* Styling
* Annotations
* Legends & grids
* Saving plots
* Advanced features

---
