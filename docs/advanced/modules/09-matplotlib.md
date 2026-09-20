← [08. Pandas](./08-pandas.md) | [Modules](./README.md) | **09. Matplotlib** | [10. Pytest →](./10-pytest.md)

---

# Matplotlib: Data Visualization

**Purpose:** Create static, animated, and interactive plots.

## Simple: Line & Bar Charts

```python
import matplotlib.pyplot as plt

# Line plot
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Simple Plot")
plt.show()

# Bar chart
categories = ["A", "B", "C"]
values = [10, 20, 15]
plt.bar(categories, values)
plt.show()
```

## Medium: Subplots & Styling

```python
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Line plot
axes[0, 0].plot([1, 2, 3], [1, 4, 9])
axes[0, 0].set_title("Line Plot")

# Scatter plot
axes[0, 1].scatter([1, 2, 3], [1, 4, 9])
axes[0, 1].set_title("Scatter Plot")

# Histogram
axes[1, 0].hist(np.random.randn(1000), bins=30)
axes[1, 0].set_title("Histogram")

# Box plot
axes[1, 1].boxplot([[1, 2, 3, 4], [2, 3, 4, 5]])
axes[1, 1].set_title("Box Plot")

plt.tight_layout()
plt.show()
```

## Complex: Custom Styling & Annotations

```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(12, 6))

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

ax.plot(x, y1, label="sin(x)", color="blue", linewidth=2)
ax.plot(x, y2, label="cos(x)", color="red", linewidth=2)

# Annotations
ax.annotate("Peak", xy=(np.pi/2, 1), xytext=(np.pi/2 + 1, 1.5),
            arrowprops=dict(arrowstyle="->"))

# Fill between
ax.fill_between(x, y1, y2, alpha=0.3)

ax.set_xlabel("X", fontsize=12)
ax.set_ylabel("Y", fontsize=12)
ax.set_title("Advanced Plotting", fontsize=14)
ax.legend(loc="upper right")
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**Install:** `pip install matplotlib` | **Use:** Data visualization, exploratory analysis, reporting

---

← [08. Pandas](./08-pandas.md) | [Modules](./README.md) | **09. Matplotlib** | [10. Pytest →](./10-pytest.md)
