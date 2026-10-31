"""Code from "How to Read CSV Files in Pandas (and Fix the Usual Errors)"
https://datascienceway.com/pandas-read-csv-guide/
Author: Lucky Joseph. MIT licence.
"""

# --- Example 1 ---
import pandas as pd

csv_text = """order_id,order_date,customer,region,postcode,amount
1001,2024-01-05,Smith,North,01234,120.50
1002,2024-01-06,Jones,South,04567,89.99
1003,2024-01-06,Patel,North,,45.00
1004,2024-01-07,Brown,East,07890,210.10
"""
with open("orders.csv", "w", encoding="utf-8") as f:
    f.write(csv_text)

df = pd.read_csv("orders.csv")
print(df)
print(df.dtypes)


# --- Example 2 ---
df = pd.read_csv("orders.csv", dtype={"postcode": "string", "order_id": "string"})
print(df[["order_id", "postcode"]])
print(df.dtypes)


# --- Example 3 ---
df = pd.read_csv(
    "orders.csv",
    dtype={"postcode": "string"},
    parse_dates=["order_date"],
)
print(df.dtypes)
print(df["order_date"].dt.day_name())


# --- Example 4 ---
uk = pd.DataFrame({"d": ["05/01/2024", "13/01/2024"]})
uk["d"] = pd.to_datetime(uk["d"], format="%d/%m/%Y")
print(uk)


# --- Example 5 ---
df = pd.read_csv("orders.csv", usecols=["order_id", "region", "amount"])
print(df.head())


# --- Example 6 ---
euro_text = "product;price\nWidget;12,50\nGadget;7,99\n"
with open("euro.csv", "w", encoding="utf-8") as f:
    f.write(euro_text)

euro = pd.read_csv("euro.csv", sep=";", decimal=",")
print(euro, euro.dtypes, sep="\n")


# --- Example 7 ---
messy_text = "name,score\nAnna,78\nBen,-\nCara,unknown\nDev,91\n"
with open("scores.csv", "w", encoding="utf-8") as f:
    f.write(messy_text)

scores = pd.read_csv("scores.csv", na_values=["-", "unknown"])
print(scores)
print(scores["score"].mean())


# --- Example 8 ---
totals = {}
for chunk in pd.read_csv("orders.csv", chunksize=2):
    for region, amount in chunk.groupby("region")["amount"].sum().items():
        totals[region] = totals.get(region, 0) + amount
print(totals)


# --- Example 9 ---
df = pd.read_csv("orders.csv", dtype={"postcode": "string"}, parse_dates=["order_date"])
print(df.shape)          # rows, columns
print(df.dtypes)         # are the types what you expect?
print(df.isna().sum())   # missing values per column
print(df.head())         # eyeball the first rows


# --- Example 10 ---
with open("latin.csv", "w", encoding="cp1252") as f:
    f.write("city,price\nCafé Town,£5\n")

latin = pd.read_csv("latin.csv", encoding="cp1252")
print(latin)


# --- Example 11 ---
from pathlib import Path
print(Path.cwd())
print(Path("orders.csv").exists())


# --- Example 12 ---
def load_orders(path):
    df = pd.read_csv(
        path,
        dtype={"order_id": "string", "postcode": "string", "region": "category"},
        parse_dates=["order_date"],
        na_values=["-", "unknown"],
    )
    assert df["order_id"].is_unique, "Duplicate order IDs found"
    return df

orders = load_orders("orders.csv")
print(orders.dtypes)
