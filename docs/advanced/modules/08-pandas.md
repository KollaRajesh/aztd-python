← [07. NumPy](./07-numpy.md) | [Modules](./README.md) | **08. Pandas** | [09. Matplotlib →](./09-matplotlib.md)

---

# Pandas: Data Analysis

**Purpose:** Data manipulation, cleaning, and analysis.

## Simple: DataFrames & Series

```python
import pandas as pd

# Create DataFrame
data = {"name": ["Alice", "Bob", "Charlie"], "age": [25, 30, 35]}
df = pd.DataFrame(data)
print(df)

# Access columns
print(df["name"])

# Basic stats
print(df["age"].mean())
print(df.describe())
```

## Medium: Filtering, Grouping & Merging

```python
import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "department": ["Sales", "IT", "Sales"],
    "salary": [50000, 60000, 55000]
})

# Filter
high_earners = df[df["salary"] > 52000]

# Group by
by_dept = df.groupby("department")["salary"].mean()

# Merge
df2 = pd.DataFrame({"name": ["Alice", "Bob"], "bonus": [5000, 8000]})
merged = pd.merge(df, df2, on="name", how="left")
```

## Complex: Time Series & Advanced Operations

```python
import pandas as pd
import numpy as np

# Time series
dates = pd.date_range("2024-01-01", periods=100)
df = pd.DataFrame({"date": dates, "value": np.random.randn(100)})
df.set_index("date", inplace=True)

# Resampling
monthly = df.resample("M").mean()

# Rolling window
df["rolling_avg"] = df["value"].rolling(window=7).mean()

# Pivot table
data = pd.DataFrame({
    "date": pd.date_range("2024-01-01", periods=10),
    "category": ["A", "B"] * 5,
    "amount": np.random.rand(10)
})
pivot = data.pivot_table(values="amount", index="date", columns="category", aggfunc="sum")
```

**Install:** `pip install pandas` | **Use:** Data analysis, cleaning, ML features

---

← [07. NumPy](./07-numpy.md) | [Modules](./README.md) | **08. Pandas** | [09. Matplotlib →](./09-matplotlib.md)
