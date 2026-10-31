-- Sample data for https://datascienceway.com/sql-group-by-having/
CREATE TABLE sales (
    sale_id    INTEGER PRIMARY KEY,
    sale_date  TEXT,
    store      TEXT,
    category   TEXT,
    customer_id INTEGER,
    amount     REAL
);
INSERT INTO sales VALUES
 (1,  '2024-01-04', 'Leeds',   'Books',  10, 24.00),
 (2,  '2024-01-09', 'Leeds',   'Games',  11, 55.00),
 (3,  '2024-01-15', 'York',    'Books',  10, 12.50),
 (4,  '2024-01-20', 'York',    'Music',  12, 9.99),
 (5,  '2024-02-02', 'Leeds',   'Books',  13, 31.00),
 (6,  '2024-02-11', 'Leeds',   'Games',  11, 70.00),
 (7,  '2024-02-14', 'Hull',    'Books',  14, 18.00),
 (8,  '2024-02-21', 'York',    'Games',  15, NULL),
 (9,  '2024-03-03', 'Hull',    'Music',  14, 14.99),
 (10, '2024-03-18', 'Leeds',   'Books',  10, 22.00);
