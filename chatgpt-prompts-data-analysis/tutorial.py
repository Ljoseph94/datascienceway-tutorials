"""Code from "How to Use ChatGPT for Data Analysis (Safely and Effectively)"
https://datascienceway.com/chatgpt-prompts-data-analysis/
Author: Lucky Joseph. MIT licence.
"""

# --- Example 1 ---
import pandas as pd
import numpy as np

# Example data - replace with your own pd.read_csv(...)
rng = np.random.default_rng(0)
df = pd.DataFrame({
    "order_date": pd.date_range("2024-01-01", periods=500, freq="D"),
    "region": rng.choice(["North", "South", "East", "West"], 500),
    "channel": rng.choice(["Online", "Store"], 500, p=[0.6, 0.4]),
    "basket_value": rng.gamma(2.0, 25.0, 500).round(2),
    "customer_email": [f"user{i}@example.com" for i in range(500)],
})

def describe_for_ai(df, sensitive=()):
    lines = [f"Rows: {len(df)}, Columns: {df.shape[1]}"]
    for col in df.columns:
        s = df[col]
        info = f"- {col} ({s.dtype}), missing={s.isna().sum()}"
        if col in sensitive:
            info += ", SENSITIVE - values withheld"
        elif pd.api.types.is_numeric_dtype(s):
            info += f", min={s.min()}, median={s.median()}, max={s.max()}"
        elif pd.api.types.is_datetime64_any_dtype(s):
            info += f", from {s.min().date()} to {s.max().date()}"
        else:
            info += f", {s.nunique()} unique, e.g. {list(s.dropna().unique()[:4])}"
        lines.append(info)
    return "\n".join(lines)

print(describe_for_ai(df, sensitive=["customer_email"]))


# --- Example 2 ---
df["month"] = df["order_date"].dt.to_period("M")
monthly = df.groupby(["month", "channel"])["basket_value"].sum().unstack()
share = monthly.div(monthly.sum(axis=1), axis=0)
print(share.head())


# --- Example 3 ---
assert np.allclose(share.sum(axis=1), 1.0)

jan_online = df[(df["month"] == "2024-01") & (df["channel"] == "Online")]["basket_value"].sum()
assert np.isclose(jan_online, monthly.loc["2024-01", "Online"])
print("Checks passed")
