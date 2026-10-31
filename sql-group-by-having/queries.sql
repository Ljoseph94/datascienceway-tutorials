-- Queries from https://datascienceway.com/sql-group-by-having/
-- Each query is separated by a blank line and ends with ;

SELECT COUNT(*)        AS rows_in_table,
       COUNT(amount)   AS rows_with_amount,
       SUM(amount)     AS total,
       AVG(amount)     AS average,
       MIN(amount)     AS smallest,
       MAX(amount)     AS largest
FROM sales;

SELECT store,
       COUNT(*)              AS sales_count,
       ROUND(SUM(amount), 2) AS revenue
FROM sales
GROUP BY store
ORDER BY revenue DESC;

-- Invalid in most databases: which category should be shown for Leeds?
-- SELECT store, category, SUM(amount) FROM sales GROUP BY store;

SELECT store,
       category,
       COUNT(*)    AS sales_count,
       SUM(amount) AS revenue
FROM sales
GROUP BY store, category
ORDER BY store, category;

SELECT strftime('%Y-%m', sale_date) AS month,
       COUNT(*)                     AS sales_count,
       ROUND(SUM(amount), 2)        AS revenue
FROM sales
GROUP BY month
ORDER BY month;

SELECT store,
       COUNT(*)                    AS sales_count,
       COUNT(DISTINCT customer_id) AS unique_customers
FROM sales
GROUP BY store;

SELECT store, SUM(amount) AS revenue
FROM sales
GROUP BY store
HAVING SUM(amount) > 50;

SELECT store,
       COUNT(*)    AS book_sales,
       SUM(amount) AS book_revenue
FROM sales
WHERE category = 'Books'
GROUP BY store
HAVING COUNT(*) >= 2;

SELECT store,
       SUM(CASE WHEN category = 'Books' THEN amount ELSE 0 END) AS books,
       SUM(CASE WHEN category = 'Games' THEN amount ELSE 0 END) AS games,
       SUM(CASE WHEN category = 'Music' THEN amount ELSE 0 END) AS music,
       SUM(amount) AS total
FROM sales
GROUP BY store
ORDER BY store;

SELECT store,
       SUM(amount) AS revenue,
       ROUND(100.0 * SUM(amount) / (SELECT SUM(amount) FROM sales), 1) AS pct_of_total
FROM sales
GROUP BY store
ORDER BY revenue DESC;
