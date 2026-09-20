← [10. Pytest](./10-pytest.md) | [Modules](./README.md) | **11. Scikit-learn** | [12. Flask →](./12-flask.md)

---

# Scikit-learn: Machine Learning

**Purpose:** Build and evaluate machine learning models.

## Simple: Classification

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load data
iris = load_iris()
X = iris.data
y = iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)

# Evaluate
predictions = clf.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy}")
```

## Medium: Pipeline & Cross-Validation

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=100, n_features=10)

# Pipeline
pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression())
])

# Cross-validation
scores = cross_val_score(pipe, X, y, cv=5)
print(f"CV Scores: {scores}, Mean: {scores.mean()}")

pipe.fit(X, y)
predictions = pipe.predict(X)
```

## Complex: Hyperparameter Tuning & Feature Selection

```python
from sklearn.model_selection import GridSearchCV
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=200, n_features=20, n_informative=10)

# Pipeline with feature selection
pipe = Pipeline([
    ("feature_selection", SelectKBest(f_classif, k=10)),
    ("classifier", SVC())
])

# Hyperparameter grid
param_grid = {
    "feature_selection__k": [5, 10, 15],
    "classifier__C": [0.1, 1, 10],
    "classifier__kernel": ["linear", "rbf"]
}

# Grid search
grid = GridSearchCV(pipe, param_grid, cv=5)
grid.fit(X, y)

print(f"Best params: {grid.best_params_}")
print(f"Best score: {grid.best_score_}")
```

**Install:** `pip install scikit-learn` | **Use:** Classification, regression, clustering, feature engineering

---

← [10. Pytest](./10-pytest.md) | [Modules](./README.md) | **11. Scikit-learn** | [12. Flask →](./12-flask.md)
