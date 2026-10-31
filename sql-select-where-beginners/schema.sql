-- Sample data for https://datascienceway.com/sql-select-where-beginners/
CREATE TABLE employees (
    id          INTEGER PRIMARY KEY,
    name        TEXT NOT NULL,
    department  TEXT,
    city        TEXT,
    salary      INTEGER,
    start_date  TEXT
);

INSERT INTO employees VALUES
 (1, 'Amira Hassan',   'Finance',   'London',     52000, '2019-03-01'),
 (2, 'Tom Wright',     'Sales',     'Leeds',      38000, '2021-07-15'),
 (3, 'Priya Shah',     'Data',      'London',     61000, '2018-11-05'),
 (4, 'Owen Davies',    'Sales',     'Cardiff',    41000, '2022-01-10'),
 (5, 'Grace Okafor',   'Data',      'Manchester', 57000, '2020-06-22'),
 (6, 'Liam Murphy',    'Finance',   'Leeds',      47000, '2023-02-01'),
 (7, 'Sophie Brown',   NULL,        'London',     35000, '2024-04-08'),
 (8, 'Jack Wilson',    'Marketing', 'Glasgow',    NULL,  '2021-09-30');
