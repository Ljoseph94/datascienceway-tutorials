# Prompt templates from the tutorial

```text
Weak:
"Analyse my sales data."

Strong:
"I'm analysing retail orders in pandas 2.x. The DataFrame `df` has these columns:
[paste output of describe_for_ai]
Write Python code that:
1. Calculates monthly total basket_value by channel.
2. Calculates each channel's share of each month's total.
3. Plots both channels as lines on one chart with matplotlib, with labelled axes.
Use only pandas and matplotlib. Don't invent columns that aren't listed.
Add brief comments. Return code only."
```

```text
Data cleaning:
"Given these columns [paste], write pandas code to: strip whitespace from text columns,
standardise 'region' to title case, convert 'order_date' from DD/MM/YYYY strings,
and report how many values failed to convert. Don't drop any rows."

SQL:
"Using tables orders(order_id, customer_id, order_date, amount) and
customers(customer_id, region), write a SQLite query for monthly revenue by region,
including regions with zero revenue. Explain how the query handles NULLs."

Debugging:
"This code raises [paste full error]. Here is the code [paste]. pandas version 2.2.
Explain the cause, then give the minimal fix."

Review:
"Review this code for bugs, data leakage or incorrect logic. List issues by severity.
Don't rewrite the whole thing."
```
