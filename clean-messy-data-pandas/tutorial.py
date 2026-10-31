"""Code from "Cleaning Messy Data with Pandas: A Practical Checklist"
https://datascienceway.com/clean-messy-data-pandas/
Author: Lucky Joseph. MIT licence.
"""

# --- Example 1 ---
import pandas as pd
import numpy as np

raw = pd.DataFrame({
    "Customer Name": ["  Alice Smith", "bob jones", "Alice Smith", "CHARLIE KHAN ", "Dana Lee", None],
    "City": ["London", "london", "London", "Manchester", "manchester ", "Leeds"],
    "Order Value": ["£120.50", "£89.99", "£120.50", "1,250.00", "n/a", "£45"],
    "Order Date": ["05/01/2024", "06/01/2024", "05/01/2024", "07/01/2024", "32/01/2024", "08/01/2024"],
    "Age": [34, 29, 34, -1, 41, 230],
})
print(raw)


# --- Example 2 ---
print(raw.shape)
print(raw.dtypes)
print(raw.isna().sum())
print(raw["City"].value_counts(dropna=False))
print(raw.describe())


# --- Example 3 ---
df = raw.copy()
df.columns = (
    df.columns.str.strip()
              .str.lower()
              .str.replace(r"\s+", "_", regex=True)
)
print(df.columns.tolist())


# --- Example 4 ---
df["customer_name"] = df["customer_name"].str.strip().str.title()
df["city"] = df["city"].str.strip().str.title()
print(df[["customer_name", "city"]])
print(df["city"].value_counts())


# --- Example 5 ---
df["order_value"] = (
    df["order_value"]
      .str.replace("£", "", regex=False)
      .str.replace(",", "", regex=False)
)
df["order_value"] = pd.to_numeric(df["order_value"], errors="coerce")
print(df["order_value"])


# --- Example 6 ---
print(raw.loc[df["order_value"].isna(), "Order Value"])


# --- Example 7 ---
df["order_date"] = pd.to_datetime(df["order_date"], format="%d/%m/%Y", errors="coerce")
print(df["order_date"])


# --- Example 8 ---
valid_age = df["age"].between(0, 110)
print(df.loc[~valid_age, ["customer_name", "age"]])
df["age"] = df["age"].where(valid_age)  # out-of-range values become NaN
print(df["age"])


# --- Example 9 ---
df = df.dropna(subset=["customer_name"])
df["age_filled"] = df["age"].fillna(df["age"].median())
print(df[["customer_name", "age", "age_filled"]])


# --- Example 10 ---
print(df.duplicated().sum())
df = df.drop_duplicates()
print(df)


# --- Example 11 ---
assert df["customer_name"].notna().all()
assert df["order_value"].dropna().ge(0).all()
assert df["city"].isin(["London", "Manchester", "Leeds"]).all()
assert not df.duplicated().any()
print("All checks passed. Rows:", len(df))
print(df.dtypes)


# --- Example 12 ---
def clean_orders(raw):
    df = raw.copy()
    df.columns = df.columns.str.strip().str.lower().str.replace(r"\s+", "_", regex=True)
    df["customer_name"] = df["customer_name"].str.strip().str.title()
    df["city"] = df["city"].str.strip().str.title()
    df["order_value"] = pd.to_numeric(
        df["order_value"].str.replace(r"[£,]", "", regex=True), errors="coerce"
    )
    df["order_date"] = pd.to_datetime(df["order_date"], format="%d/%m/%Y", errors="coerce")
    df["age"] = df["age"].where(df["age"].between(0, 110))
    df = df.dropna(subset=["customer_name"]).drop_duplicates()
    return df

print(clean_orders(raw))
