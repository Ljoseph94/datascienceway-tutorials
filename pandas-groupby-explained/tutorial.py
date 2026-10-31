"""Code from "Pandas groupby Explained with Real Examples"
https://datascienceway.com/pandas-groupby-explained/
Author: Lucky Joseph. MIT licence.
"""

# --- Example 1 ---
import pandas as pd

sales = pd.DataFrame({
    "date": pd.to_datetime(["2024-01-03", "2024-01-15", "2024-01-20", "2024-02-02",
                            "2024-02-10", "2024-02-18", "2024-03-05", "2024-03-22"]),
    "region": ["North", "South", "North", "East", "South", "North", "East", "South"],
    "product": ["Laptop", "Mouse", "Mouse", "Laptop", "Laptop", "Monitor", "Mouse", "Monitor"],
    "units": [2, 10, 5, 1, 3, 2, 8, 4],
    "revenue": [1800.0, 150.0, 75.0, 950.0, 2700.0, 380.0, 120.0, 760.0],
})
print(sales)


# --- Example 2 ---
print(sales.groupby("region")["revenue"].sum())


# --- Example 3 ---
by_region = sales.groupby("region", as_index=False)["revenue"].sum()
print(by_region.sort_values("revenue", ascending=False))


# --- Example 4 ---
summary = sales.groupby("region").agg(
    orders=("revenue", "size"),
    total_revenue=("revenue", "sum"),
    avg_order=("revenue", "mean"),
    units_sold=("units", "sum"),
    products=("product", "nunique"),
).round(2)
print(summary)


# --- Example 5 ---
rp = sales.groupby(["region", "product"], as_index=False)["revenue"].sum()
print(rp)


# --- Example 6 ---
grid = sales.pivot_table(index="region", columns="product",
                         values="revenue", aggfunc="sum", fill_value=0)
print(grid)


# --- Example 7 ---
monthly = sales.groupby(sales["date"].dt.to_period("M"))["revenue"].sum()
print(monthly)


# --- Example 8 ---
sales["region_total"] = sales.groupby("region")["revenue"].transform("sum")
sales["share_of_region"] = (sales["revenue"] / sales["region_total"]).round(3)
print(sales[["region", "product", "revenue", "region_total", "share_of_region"]])


# --- Example 9 ---
big_regions = sales.groupby("region").filter(lambda g: g["revenue"].sum() > 1500)
print(big_regions[["region", "revenue"]])


# --- Example 10 ---
top_sale = (sales.sort_values("revenue", ascending=False)
                 .groupby("region")
                 .head(1)[["region", "product", "revenue"]])
print(top_sale)

sales["rank_in_region"] = sales.groupby("region")["revenue"].rank(ascending=False, method="dense")
print(sales[["region", "revenue", "rank_in_region"]])


# --- Example 11 ---
def revenue_range(s):
    return s.max() - s.min()

print(sales.groupby("region")["revenue"].agg(revenue_range))


# --- Example 12 ---
report = (
    sales.assign(month=sales["date"].dt.to_period("M"))
         .groupby(["month", "region"], as_index=False)
         .agg(revenue=("revenue", "sum"), orders=("revenue", "size"))
)
report["month_share"] = (
    report["revenue"] / report.groupby("month")["revenue"].transform("sum")
).round(3)
print(report)
