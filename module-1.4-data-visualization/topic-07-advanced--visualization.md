# 🚀 Module 1.4 — Data Visualization

## Topic 07: Advanced Visualization Libraries

---

# 🔥 Real-World Perspective

In real-world analytics:

👉 Static charts are not enough anymore

Companies want:

* interactive dashboards
* zoomable charts
* real-time updates

---

## 🧠 Real Insight

👉 Static visualization = reporting
👉 Interactive visualization = decision-making

---

# 7. Advanced Visualization Libraries

These tools help you move from **basic charts → interactive, professional visualization**

---

## 📊 Data Analyst Perspective

Used for:

* dashboards
* presentations
* web-based analytics
* real-time systems

---

# 🔹 7.1 Why Advanced Libraries Matter

* interactive charts
* better user experience
* scalable dashboards
* modern reporting

---

## 📊 Real Insight

👉 This is what makes your projects **stand out**

---

# 🔥 Must-Know Libraries

---

# 7.2 Plotly

Plotly is a powerful library for **interactive and dynamic visualizations**

---

## 📊 Features

* zoom, hover, click
* 3D plots
* dashboards (Dash)
* web-ready

---

## 📊 Real Use Case

```python id="advv1"
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length")
fig.show()
```

---

## 📊 Applications

* dashboards
* business analytics
* presentations

---

## 🔥 Insight

👉 Best tool for interactive charts

---

# 🔍 Interview Thinking

* Why Plotly used?
  👉 interactivity

---

# 7.3 Bokeh

Used for **web-based visualization**

---

## 📊 Features

* browser-based charts
* streaming data
* interactive tools

---

## 📊 Real Use Case

```python id="advv2"
from bokeh.plotting import figure, show

p = figure()
p.line([1,2,3], [4,5,6])
show(p)
```

---

## 📊 Applications

* web apps
* live dashboards

---

## 🔥 Insight

👉 Strong for real-time visualization

---

# 7.4 Altair

Declarative visualization library

---

## 📊 Features

* simple syntax
* automatic transformations
* clean design

---

## 📊 Real Use Case

```python id="advv3"
import altair as alt
import pandas as pd

df = pd.DataFrame({
    "x": [1,2,3],
    "y": [4,5,6]
})

alt.Chart(df).mark_line().encode(
    x='x',
    y='y'
)
```

---

## 📊 Applications

* clean reports
* simple dashboards

---

## 🔥 Insight

👉 Focus on clarity and simplicity

---

# 🔹 Comparison

| Library | Best For               |
| ------- | ---------------------- |
| Plotly  | Interactive dashboards |
| Bokeh   | Web apps               |
| Altair  | Clean visuals          |

---

# 🔹 When to Use What

👉 Quick EDA → Pandas / Seaborn
👉 Full control → Matplotlib
👉 Interactive dashboards → Plotly
👉 Web apps → Bokeh
👉 Clean reports → Altair

---

# 🧠 Real Mini Case Study

## Problem: Business Dashboard

```text id="v1k8sz"
Use:
- Plotly → interactive dashboard  
- Bokeh → web-based app  
- Altair → clean report  
```

---

# 🔍 Interview Thinking (Added Layer)

* Which library for dashboards?
  👉 Plotly

* Which for web apps?
  👉 Bokeh

---

# ⚠️ Common Mistakes

❌ Using Matplotlib for dashboards
❌ Ignoring interactivity
❌ Overcomplicating visuals

---

# 💡 Key Takeaways

✔ Plotly → interactive
✔ Bokeh → web apps
✔ Altair → clean design
✔ Choose tool based on use case

---

# 🎯 Final Insight

👉 Modern analytics = interactive visualization

---

# Summary

In this lesson I learned:

* Plotly
* Bokeh
* Altair
* Use cases of each
* Industry applications

---
