← [06. aiohttp](./06-aiohttp.md) | [Modules](./README.md) | **07. NumPy** | [08. Pandas →](./08-pandas.md)

---

# NumPy: Numerical Computing

**Purpose:** Fast array operations and mathematical computations.

## Simple: Arrays & Basic Operations

```python
import numpy as np

# Create arrays
arr = np.array([1, 2, 3, 4, 5])
zeros = np.zeros(5)
range_arr = np.arange(0, 10, 2)

# Operations
print(arr * 2)  # [2 4 6 8 10]
print(arr + arr)  # [2 4 6 8 10]
print(np.sum(arr))  # 15
print(np.mean(arr))  # 3.0
```

## Medium: Matrices & Linear Algebra

```python
import numpy as np

# 2D arrays
matrix = np.array([[1, 2], [3, 4]])
print(matrix.shape)  # (2, 2)

# Matrix operations
matrix2 = np.array([[5, 6], [7, 8]])
print(np.dot(matrix, matrix2))  # Matrix multiplication

# Statistics
data = np.array([1, 2, 3, 4, 5])
print(np.std(data))  # Standard deviation
print(np.percentile(data, 75))  # 75th percentile
```

## Complex: Broadcasting & Vectorization

```python
import numpy as np

# Broadcasting
a = np.array([1, 2, 3])
b = np.array([[1], [2], [3]])
result = a + b  # Shape (3, 3)

# Vectorized operations (faster than loops)
x = np.linspace(0, 2*np.pi, 1000)
y = np.sin(x)

# Advanced indexing
arr = np.arange(20).reshape(4, 5)
mask = arr > 10
filtered = arr[mask]

# Einsum for complex operations
a = np.random.rand(5, 3)
b = np.random.rand(3, 4)
c = np.einsum('ij,jk->ik', a, b)  # Matrix multiplication
```

**Install:** `pip install numpy` | **Use:** Data science, ML preprocessing, scientific computing

---

← [06. aiohttp](./06-aiohttp.md) | [Modules](./README.md) | **07. NumPy** | [08. Pandas →](./08-pandas.md)
