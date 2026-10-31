"""Code from "Train/Test Split Explained (and Why It Matters)"
https://datascienceway.com/train-test-split-explained/
Author: Lucky Joseph. MIT licence.
"""

# --- Example 1 ---
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

X, y = load_breast_cancer(return_X_y=True, as_frame=True)
print(X.shape)            # 569 rows, 30 features
print(y.value_counts())   # 1 = benign, 0 = malignant

# Wrong: train and evaluate on the same data
tree = DecisionTreeClassifier(random_state=42).fit(X, y)
print("Accuracy on training data:", tree.score(X, y))


# --- Example 2 ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,      # 20% held back for testing
    random_state=42,    # makes the split reproducible
    stratify=y,         # keep class proportions the same in both sets
)
print(X_train.shape, X_test.shape)

tree = DecisionTreeClassifier(random_state=42).fit(X_train, y_train)
print("Train accuracy:", round(tree.score(X_train, y_train), 3))
print("Test accuracy: ", round(tree.score(X_test, y_test), 3))


# --- Example 3 ---
print(y_train.mean().round(3), y_test.mean().round(3))


# --- Example 4 ---
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
model.fit(X_train, y_train)          # scaler learns from training data only
print("Test accuracy:", round(model.score(X_test, y_test), 3))


# --- Example 5 ---
X_temp, X_test, y_temp, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)
X_train, X_val, y_train, y_val = train_test_split(
    X_temp, y_temp, test_size=0.25, random_state=42, stratify=y_temp)
# 0.25 of the remaining 80% = 20% of the total
print(len(X_train), len(X_val), len(X_test))

for depth in [2, 3, 5, None]:
    m = DecisionTreeClassifier(max_depth=depth, random_state=42).fit(X_train, y_train)
    print(depth, round(m.score(X_val, y_val), 3))


# --- Example 6 ---
import pandas as pd
import numpy as np

dates = pd.date_range("2023-01-01", periods=365, freq="D")
ts = pd.DataFrame({"date": dates, "sales": np.random.default_rng(0).poisson(100, 365)})

cutoff = pd.Timestamp("2023-10-01")
train_ts = ts[ts["date"] < cutoff]
test_ts = ts[ts["date"] >= cutoff]
print(len(train_ts), len(test_ts))


# --- Example 7 ---
from sklearn.model_selection import GroupShuffleSplit

rng = np.random.default_rng(1)
customers = rng.integers(0, 50, size=len(X))   # pretend customer IDs
gss = GroupShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
train_idx, test_idx = next(gss.split(X, y, groups=customers))
overlap = set(customers[train_idx]) & set(customers[test_idx])
print("Customers in both sets:", len(overlap))
