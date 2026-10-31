-- Sample data for https://datascienceway.com/sql-joins-explained/
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name        TEXT,
    city        TEXT
);
INSERT INTO customers VALUES
 (1, 'Ava',   'London'),
 (2, 'Ben',   'Bristol'),
 (3, 'Chloe', 'Leeds'),
 (4, 'Dan',   'York');

CREATE TABLE orders (
    order_id    INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date  TEXT,
    amount      REAL
);
INSERT INTO orders VALUES
 (101, 1, '2024-03-01', 120.00),
 (102, 1, '2024-03-08',  35.50),
 (103, 2, '2024-03-09',  80.00),
 (104, 3, '2024-03-10', 210.00),
 (105, 9, '2024-03-11',  15.00);

CREATE TABLE staff (id INTEGER, name TEXT, manager_id INTEGER);
INSERT INTO staff VALUES (1, 'Rosa', NULL), (2, 'Sam', 1), (3, 'Tara', 1), (4, 'Umar', 2);

SELECT e.name AS employee, m.name AS manager
FROM staff AS e
LEFT JOIN staff AS m ON m.id = e.manager_id;

CREATE TABLE tickets (ticket_id INTEGER, customer_id INTEGER);
INSERT INTO tickets VALUES (1, 1), (2, 1), (3, 1);

-- WRONG: Ava's 2 orders x 3 tickets = 6 rows, so her spend is tripled
SELECT c.name, SUM(o.amount) AS total_spent, COUNT(t.ticket_id) AS tickets
FROM customers AS c
LEFT JOIN orders  AS o ON o.customer_id = c.customer_id
LEFT JOIN tickets AS t ON t.customer_id = c.customer_id
GROUP BY c.name;
