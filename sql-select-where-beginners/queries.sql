-- Queries from https://datascienceway.com/sql-select-where-beginners/
-- Each query is separated by a blank line and ends with ;

SELECT *
FROM employees;

SELECT name, department, salary
FROM employees;

SELECT name,
       salary,
       salary / 12 AS monthly_salary,
       salary * 1.03 AS salary_after_3pc_rise
FROM employees;

SELECT name, city
FROM employees
WHERE city = 'London';

SELECT name, salary
FROM employees
WHERE salary >= 50000;

-- Data team members in London
SELECT name, department, city
FROM employees
WHERE department = 'Data' AND city = 'London';

-- Anyone in Sales or Marketing
SELECT name, department
FROM employees
WHERE department = 'Sales' OR department = 'Marketing';

-- Probably NOT what you mean: Sales staff (any salary) OR Finance staff over 50k
SELECT name, department, salary
FROM employees
WHERE department = 'Sales' OR department = 'Finance' AND salary > 50000;

-- What you probably mean: Sales or Finance staff, earning over 40k
SELECT name, department, salary
FROM employees
WHERE (department = 'Sales' OR department = 'Finance') AND salary > 40000;

-- IN: match any value in a list
SELECT name, city
FROM employees
WHERE city IN ('Leeds', 'Manchester', 'Glasgow');

-- BETWEEN: inclusive range
SELECT name, salary
FROM employees
WHERE salary BETWEEN 40000 AND 55000;

-- Dates between two values (ISO text compares correctly)
SELECT name, start_date
FROM employees
WHERE start_date BETWEEN '2021-01-01' AND '2021-12-31';

-- LIKE: pattern matching. % = any characters, _ = one character
SELECT name
FROM employees
WHERE name LIKE 'S%';

SELECT name FROM employees WHERE department = NULL;

SELECT name FROM employees WHERE department IS NULL;

SELECT name, salary FROM employees WHERE salary IS NOT NULL;

SELECT name, department
FROM employees
WHERE department <> 'Sales' OR department IS NULL;

SELECT name, COALESCE(department, 'Unassigned') AS department
FROM employees;

SELECT name, salary
FROM employees
WHERE salary IS NOT NULL
ORDER BY salary DESC
LIMIT 3;

SELECT DISTINCT city
FROM employees
ORDER BY city;
