-- Queries from https://datascienceway.com/sql-joins-explained/
-- Each query is separated by a blank line and ends with ;

SELECT c.name, o.order_id, o.amount
FROM customers AS c
INNER JOIN orders AS o
    ON o.customer_id = c.customer_id
ORDER BY o.order_id;

SELECT c.name, o.order_id, o.amount
FROM customers AS c
LEFT JOIN orders AS o
    ON o.customer_id = c.customer_id
ORDER BY c.customer_id;

SELECT c.name
FROM customers AS c
LEFT JOIN orders AS o
    ON o.customer_id = c.customer_id
WHERE o.order_id IS NULL;

SELECT c.name
FROM customers AS c
WHERE NOT EXISTS (
    SELECT 1 FROM orders AS o WHERE o.customer_id = c.customer_id
);

SELECT c.name, o.order_id, o.amount
FROM customers AS c
FULL OUTER JOIN orders AS o
    ON o.customer_id = c.customer_id
ORDER BY o.order_id;

SELECT c.name,
       COUNT(o.order_id)          AS orders,
       COALESCE(SUM(o.amount), 0) AS total_spent
FROM customers AS c
LEFT JOIN orders AS o
    ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_spent DESC;

-- A: condition in WHERE. Customers without a qualifying order disappear.
SELECT c.name, o.amount
FROM customers AS c
LEFT JOIN orders AS o ON o.customer_id = c.customer_id
WHERE o.amount > 100;

-- B: condition in ON. Every customer kept, only big orders attached.
SELECT c.name, o.amount
FROM customers AS c
LEFT JOIN orders AS o
    ON o.customer_id = c.customer_id
   AND o.amount > 100;

WITH o AS (
    SELECT customer_id, SUM(amount) AS total_spent
    FROM orders GROUP BY customer_id
),
t AS (
    SELECT customer_id, COUNT(*) AS tickets
    FROM tickets GROUP BY customer_id
)
SELECT c.name,
       COALESCE(o.total_spent, 0) AS total_spent,
       COALESCE(t.tickets, 0)     AS tickets
FROM customers AS c
LEFT JOIN o ON o.customer_id = c.customer_id
LEFT JOIN t ON t.customer_id = c.customer_id;
