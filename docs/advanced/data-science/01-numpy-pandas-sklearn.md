<!-- Navigation -->
**[← AI Agents](../ai-agents/01-langchain-langgraph.md)** | **[Back to Index](../../../README.md)**

---

# Advanced Python: Data Science with NumPy, Pandas & Scikit-Learn

## 2.35 NumPy Fundamentals

NumPy provides efficient numerical computing with N-dimensional arrays.

### Array Creation and Operations

```python
import numpy as np

# Create arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.zeros((3, 4))           # 3x4 zeros
arr3 = np.ones((2, 3))            # 2x3 ones
arr4 = np.arange(0, 10, 2)        # [0, 2, 4, 6, 8]
arr5 = np.linspace(0, 1, 5)       # 5 evenly spaced values

# Array properties
print(arr1.shape)                  # (5,)
print(arr1.dtype)                  # int64
print(arr1.size)                   # 5

# Element-wise operations
result = arr1 * 2                  # [2, 4, 6, 8, 10]
result = arr1 + np.array([1, 1, 1, 1, 1])

# Mathematical functions
print(np.sqrt(arr1))               # Square root
print(np.exp(arr1))                # Exponential
print(np.log(arr1))                # Natural log
```

### Array Indexing and Slicing

```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Indexing
print(arr[0, 0])                   # 1
print(arr[1, 2])                   # 6

# Slicing
print(arr[0, :])                   # [1, 2, 3]
print(arr[:, 1])                   # [2, 5, 8]
print(arr[0:2, 1:3])               # [[2, 3], [5, 6]]

# Boolean indexing
mask = arr > 5
print(arr[mask])                   # [6, 7, 8, 9]
```

### Statistical Operations

```python
import numpy as np

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(np.mean(data))               # 5.5
print(np.median(data))             # 5.5
print(np.std(data))                # Standard deviation
print(np.var(data))                # Variance
print(np.sum(data))                # 55
print(np.min(data))                # 1
print(np.max(data))                # 10
```

---

## 2.36 Pandas DataFrames

Pandas provides tabular data structures similar to SQL tables or Excel.

### DataFrame Creation and Inspection

```python
import pandas as pd

# Create DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 70000]
}
df = pd.DataFrame(data)

# From CSV
df = pd.read_csv('data.csv')

# From JSON
df = pd.read_json('data.json')

# Inspect
print(df.head())                   # First 5 rows
print(df.tail())                   # Last 5 rows
print(df.info())                   # Column info
print(df.describe())               # Statistical summary
```

### Data Selection and Filtering

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'Department': ['Sales', 'IT', 'HR', 'IT']
})

# Select column
print(df['Name'])

# Select multiple columns
print(df[['Name', 'Age']])

# Filter rows
print(df[df['Age'] > 28])

# Filter by condition
print(df[(df['Age'] > 25) & (df['Department'] == 'IT')])

# Using .loc and .iloc
print(df.loc[0])                   # By index label
print(df.iloc[0])                  # By position
```

### Data Cleaning

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', None, 'David'],
    'Age': [25, np.nan, 35, 28],
    'Salary': [50000, 60000, 70000, 55000]
})

# Check for missing values
print(df.isnull())

# Drop missing values
df_clean = df.dropna()

# Fill missing values
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Remove duplicates
df_unique = df.drop_duplicates()

# Data type conversion
df['Age'] = df['Age'].astype(int)
```

### Grouping and Aggregation

```python
import pandas as pd

df = pd.DataFrame({
    'Department': ['Sales', 'IT', 'Sales', 'HR', 'IT'],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Salary': [50000, 60000, 55000, 45000, 65000]
})

# Group by
grouped = df.groupby('Department')

# Aggregate
print(grouped['Salary'].mean())
print(grouped['Salary'].sum())
print(grouped['Salary'].count())

# Multiple aggregations
result = grouped['Salary'].agg(['mean', 'sum', 'count'])
print(result)
```

---

## 2.37 Data Visualization with Matplotlib

```python
import matplotlib.pyplot as plt
import numpy as np

# Line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, label='sin(x)')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Sine Wave')
plt.legend()
plt.grid(True)
plt.show()

# Scatter plot
x = np.random.randn(100)
y = np.random.randn(100)
plt.scatter(x, y, alpha=0.5)
plt.show()

# Histogram
data = np.random.randn(1000)
plt.hist(data, bins=30, edgecolor='black')
plt.title('Distribution')
plt.show()

# Bar plot
categories = ['A', 'B', 'C', 'D']
values = [10, 24, 36, 18]
plt.bar(categories, values)
plt.show()

# Multiple subplots
fig, axes = plt.subplots(2, 2)
axes[0, 0].plot(x, y)
axes[0, 1].scatter(x, y)
axes[1, 0].hist(data)
axes[1, 1].bar(categories, values)
plt.tight_layout()
plt.show()
```

---

## 2.38 Scikit-Learn Machine Learning

### Train-Test Split and Model Training

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Generate data
X = np.random.randn(100, 1)
y = 2 * X.ravel() + np.random.randn(100)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MSE: {mse:.4f}")
print(f"R² Score: {r2:.4f}")
```

### Classification Example

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load data
iris = load_iris()
X = iris.data
y = iris.target

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
```

### Feature Scaling and Preprocessing

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

# StandardScaler - zero mean, unit variance
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_train)

# MinMaxScaler - range [0, 1]
min_max = MinMaxScaler()
X_minmax = min_max.fit_transform(X_train)

# Pipeline - chain preprocessing and model
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])

pipeline.fit(X_train, y_train)
predictions = pipeline.predict(X_test)
```

---

## 2.39 Dimensionality Reduction

### Principal Component Analysis (PCA)

```python
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()
X = iris.data

# PCA to 2 dimensions
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

# Explained variance
print(f"Explained variance: {pca.explained_variance_ratio_}")

# Plot
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=iris.target)
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.show()
```

---

## 2.40 Cross-Validation and Hyperparameter Tuning

```python
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

iris = load_iris()
X, y = iris.data, iris.target

# Cross-validation
model = RandomForestClassifier()
scores = cross_val_score(model, X, y, cv=5)  # 5-fold CV
print(f"Cross-validation scores: {scores}")
print(f"Mean: {scores.mean():.4f}, Std: {scores.std():.4f}")

# Grid search for hyperparameter tuning
params = {
    'n_estimators': [10, 50, 100],
    'max_depth': [3, 5, 10],
    'min_samples_split': [2, 5]
}

grid_search = GridSearchCV(
    RandomForestClassifier(),
    params,
    cv=5
)

grid_search.fit(X, y)

print(f"Best parameters: {grid_search.best_params_}")
print(f"Best score: {grid_search.best_score_:.4f}")
```

---

## 2.41 Real-World Example: Iris Classifier

```python
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

class IrisClassifier:
    def __init__(self):
        self.model = None
        self.scaler = None
        self.feature_names = None
    
    def load_data(self):
        """Load iris dataset"""
        iris = load_iris()
        X = iris.data
        y = iris.target
        self.feature_names = iris.feature_names
        
        return train_test_split(X, y, test_size=0.2, random_state=42)
    
    def train(self, X_train, y_train):
        """Train model"""
        # Scale features
        self.scaler = StandardScaler()
        X_train_scaled = self.scaler.fit_transform(X_train)
        
        # Train model
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train_scaled, y_train)
    
    def evaluate(self, X_test, y_test):
        """Evaluate model"""
        X_test_scaled = self.scaler.transform(X_test)
        y_pred = self.model.predict(X_test_scaled)
        
        accuracy = accuracy_score(y_test, y_pred)
        
        return {
            'accuracy': accuracy,
            'predictions': y_pred,
            'report': classification_report(y_test, y_pred)
        }
    
    def predict(self, features):
        """Predict on new data"""
        features_scaled = self.scaler.transform([features])
        return self.model.predict(features_scaled)[0]
    
    def feature_importance(self):
        """Get feature importance"""
        importances = self.model.feature_importances_
        return dict(zip(self.feature_names, importances))

# Usage
classifier = IrisClassifier()
X_train, X_test, y_train, y_test = classifier.load_data()

classifier.train(X_train, y_train)

results = classifier.evaluate(X_test, y_test)
print(f"Accuracy: {results['accuracy']:.4f}")
print(results['report'])

# Feature importance
importance = classifier.feature_importance()
for feature, imp in importance.items():
    print(f"{feature}: {imp:.4f}")
```

---

## 2.42 Time Series Analysis

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create time series data
dates = pd.date_range('2024-01-01', periods=100)
values = np.cumsum(np.random.randn(100)) + 100

ts_data = pd.DataFrame({
    'date': dates,
    'value': values
})

ts_data.set_index('date', inplace=True)

# Rolling mean
ts_data['rolling_mean'] = ts_data['value'].rolling(window=7).mean()

# Exponential moving average
ts_data['ema'] = ts_data['value'].ewm(span=7).mean()

# Plot
plt.figure(figsize=(12, 6))
plt.plot(ts_data.index, ts_data['value'], label='Original')
plt.plot(ts_data.index, ts_data['rolling_mean'], label='7-day MA')
plt.plot(ts_data.index, ts_data['ema'], label='EMA')
plt.legend()
plt.show()

# Resample to monthly
monthly = ts_data['value'].resample('M').mean()
print(monthly)
```

---

## 2.43 Data Pipeline Example

```python
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

class DataPipeline:
    def __init__(self):
        self.pipeline = Pipeline([
            ('features', PolynomialFeatures(degree=2)),
            ('scaler', StandardScaler()),
            ('model', LinearRegression())
        ])
    
    def train(self, X, y):
        """Train pipeline"""
        self.pipeline.fit(X, y)
    
    def evaluate(self, X, y, cv=5):
        """Cross-validation score"""
        scores = cross_val_score(self.pipeline, X, y, cv=cv, scoring='r2')
        return {
            'mean': scores.mean(),
            'std': scores.std(),
            'scores': scores
        }
    
    def predict(self, X):
        """Make predictions"""
        return self.pipeline.predict(X)

# Usage
X = np.random.randn(100, 3)
y = X[:, 0] ** 2 + 2 * X[:, 1] + np.random.randn(100)

pipeline = DataPipeline()
pipeline.train(X[:80], y[:80])

results = pipeline.evaluate(X, y)
print(f"CV Score: {results['mean']:.4f} +/- {results['std']:.4f}")
```

---

## Summary Table

| Library | Purpose | Use Case |
|---------|---------|----------|
| **NumPy** | Numerical computing | Matrix operations, math |
| **Pandas** | Data manipulation | Tabular data, cleaning |
| **Matplotlib** | Visualization | Plots, charts |
| **Scikit-Learn** | Machine learning | Regression, classification |
| **SciPy** | Scientific computing | Optimization, stats |

| Task | Method | Output |
|------|--------|--------|
| **Load CSV** | `pd.read_csv()` | DataFrame |
| **Filter data** | `df[df['col'] > value]` | Filtered DataFrame |
| **Group data** | `df.groupby()` | GroupBy object |
| **Train model** | `model.fit(X, y)` | Trained model |
| **Evaluate** | `accuracy_score()` | Metric value |

---

## Best Practices

1. Always split data into train/test sets
2. Scale features before training
3. Use cross-validation for robust evaluation
4. Handle missing values before modeling
5. Check for data leakage
6. Use pipelines for reproducibility
7. Visualize data before analysis

---

<!-- Navigation Footer -->
**[← AI Agents](../ai-agents/01-langchain-langgraph.md)** | **[Back to Index](../../../README.md)**

**Sections:** 2.35-2.43 | **Time:** 1-2 hours
