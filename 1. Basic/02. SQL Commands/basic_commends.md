# B. SQL Commands — Basic SQL Commands (MySQL)

> **Note:** Some topics below overlap with `basic_query_clause.md` and `SQL-commends-category.md`. For a cleaner study file, you can later consolidate duplicate coverage of `DISTINCT`, `SELECT`, `INSERT`, `UPDATE`, and `DELETE`.

## 1. CREATE DATABASE

`CREATE DATABASE` is used to create a new database in MySQL where we can store and manage related tables and their data. We generally create a database first before creating tables inside it.

```SQL
CREATE DATABASE company;
-- Creates a new database named company.
```

## 2. CREATE TABLE

`CREATE TABLE` is used to create a new table inside a database by defining its column names, data types, and constraints. It provides the structure where we can store related records.

```SQL
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    salary DECIMAL(10,2)
);
-- Creates an employees table.
```

## 3. USE

`USE` is used to select a particular database as the current working database. After selecting it, we can execute queries on its tables without specifying the database name every time.

```SQL
USE company;
-- Selects company as the current database.
```

## 4. SHOW DATABASES

`SHOW DATABASES` displays the databases available in the MySQL server that the current user has permission to see. It is commonly used to check whether a database has been created successfully.

```SQL
SHOW DATABASES;
-- Displays the available databases.
```

## 5. SHOW TABLES

`SHOW TABLES` displays all tables available inside the currently selected database. It helps us quickly check which tables exist in the database.

```SQL
SHOW TABLES;
-- Displays all tables in the current database.
```

To check tables from a specific database:

```SQL
SHOW TABLES FROM company;
-- Displays tables inside the company database.
```

## 6. DESCRIBE (DESC)

`DESCRIBE` is used to view the structure of an existing table, including its column names, data types, NULL restrictions, keys, and default values. It is useful when we want to understand a table before writing queries.

```SQL
DESCRIBE employees;
-- Displays the structure of the employees table.
```

The shorter form is:

```SQL
DESC employees;
-- Same as DESCRIBE employees.
```

## 7. INSERT INTO

`INSERT INTO` is used to add new records to an existing table. We can insert a single record or multiple records by providing values for the required columns.

### 7.1 Insert a Single Record

```SQL
INSERT INTO employees (id, name, age, salary)
VALUES (101, 'Arun', 23, 35000.00);
-- Inserts one employee record.
```

### 7.2 Insert Multiple Records

```SQL
INSERT INTO employees (id, name, age, salary)
VALUES
    (102, 'Priya', 24, 40000.00),
    (103, 'Rahul', 25, 45000.00);
-- Inserts two employee records in one query.
```

## 8. SELECT

`SELECT` is used to retrieve data from one or more database tables. We can fetch all columns or only the specific columns we need.

### 8.1 Select All Columns

```SQL
SELECT *
FROM employees;
-- Retrieves all columns and records.
```

### 8.2 Select Specific Columns

```SQL
SELECT name, salary
FROM employees;
-- Retrieves only name and salary.
```

### 8.3 SELECT with WHERE

```SQL
SELECT *
FROM employees
WHERE age > 23;
-- Retrieves employees whose age is greater than 23.
```

### 8.4 SELECT DISTINCT

```SQL
SELECT DISTINCT age
FROM employees;
-- Returns unique age values without duplicates.
```

### 8.5 SELECT with ORDER BY

```SQL
SELECT *
FROM employees
ORDER BY salary DESC;
-- Sorts employees by salary in descending order.
-- DESC means highest to lowest.
```

### 8.6 SELECT with LIMIT

```SQL
SELECT *
FROM employees
LIMIT 5;
-- Returns only the first five records.
```

## 9. UPDATE

`UPDATE` is used to modify existing records in a table. We use the `SET` clause to specify the new values and the `WHERE` clause to identify which records should be updated.

### 9.1 Update a Single Column

```SQL
UPDATE employees
SET salary = 50000
WHERE id = 101;
-- Updates the salary of employee 101.
```

### 9.2 Update Multiple Columns

```SQL
UPDATE employees
SET age = 24,
    salary = 55000
WHERE id = 101;
-- Updates both age and salary for employee 101.
```

> **Important:** Without `WHERE`, the UPDATE statement affects all rows in the table.

## 10. DELETE

`DELETE` is used to remove existing records from a table. We can delete specific records using a `WHERE` condition or remove all records while keeping the table structure.

### 10.1 Delete a Specific Record

```SQL
DELETE FROM employees
WHERE id = 103;
-- Deletes the employee whose id is 103.
```

### 10.2 Delete All Records

```SQL
DELETE FROM employees;
-- Removes all records from the table.
-- The table structure remains unchanged.
```

> **Important:** Always check your `WHERE` condition before executing DELETE to avoid accidentally removing unwanted records.

## 11. ALTER TABLE

`ALTER TABLE` is used to change the structure of an existing table without recreating it. We can add new columns, modify existing columns, rename columns, or remove columns based on our requirements.

### 11.1 Add a Column

```SQL
ALTER TABLE employees
ADD email VARCHAR(100);
-- Adds a new email column.
```

### 11.2 Modify a Column

```SQL
ALTER TABLE employees
MODIFY salary DECIMAL(12,2);
-- Changes the salary column definition.
```

### 11.3 Rename a Column

```SQL
ALTER TABLE employees
RENAME COLUMN name TO employee_name;
-- Renames name to employee_name.
```

### 11.4 Drop a Column

```SQL
ALTER TABLE employees
DROP COLUMN email;
-- Permanently removes the email column.
```

### 11.5 Rename a Table

```SQL
ALTER TABLE employees
RENAME TO staff;
-- Changes the table name from employees to staff.
```

## 12. IF NOT EXISTS

`IF NOT EXISTS` is used with certain CREATE statements to avoid an error when the database or table already exists. It allows us to execute creation queries more safely without checking manually every time.

### 12.1 Create Database

```SQL
CREATE DATABASE IF NOT EXISTS company;
-- Creates company only if it does not already exist.
```

### 12.2 Create Table

```SQL
CREATE TABLE IF NOT EXISTS employees (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);
-- Creates employees only if the table does not exist.
```

## 13. DROP DATABASE

`DROP DATABASE` is used to completely remove an existing database along with its tables and stored data. It should be used carefully because the removed database cannot be recovered through a normal SQL rollback.

```SQL
DROP DATABASE company;
-- Completely removes the company database.
```

### 13.1 Safe Version

```SQL
DROP DATABASE IF EXISTS company;
-- Removes company only if it exists.
-- Avoids an error if the database is absent.
```

## 14. DROP TABLE

`DROP TABLE` is used to completely remove an existing table, including its structure and stored records. Unlike DELETE, it removes the table itself from the database.

```SQL
DROP TABLE employees;
-- Removes the employees table completely.
```

### 14.1 Safe Version

```SQL
DROP TABLE IF EXISTS employees;
-- Removes the table only if it exists.
```

## 15. TRUNCATE TABLE

`TRUNCATE TABLE` is used to remove all records from a table while keeping its structure available for future use. It is commonly used when we want to empty a table completely without deleting it.

```SQL
TRUNCATE TABLE employees;
-- Removes all records from employees.
-- Keeps the table structure.
```

> **Remember:** `DELETE` removes rows, `TRUNCATE` quickly empties the table, `DROP` removes the table itself.

## 16. COMMENT (SQL Comments)

Comments are used to explain SQL queries and make code easier to understand. MySQL ignores comments during execution, so they do not affect the actual query result.

### 16.1 Single-Line Comment

```SQL
-- This is a single-line comment.

SELECT * FROM employees;
-- Retrieves all employee records.
```

### 16.2 Multi-Line Comment

```SQL
/*
This is a multi-line comment.
It can contain multiple lines of explanation.
*/

SELECT name, salary
FROM employees;
-- Retrieves employee names and salaries.
```

# Basic SQL Commands — Quick Revision

- `CREATE DATABASE` → Create a database
- `CREATE TABLE` → Create a table
- `USE` → Select a database
- `SHOW DATABASES` → See available databases
- `SHOW TABLES` → See tables in the current database
- `DESCRIBE / DESC` → Check table structure
- `SHOW CREATE TABLE` → See the complete CREATE statement
- `INSERT INTO` → Add records
- `SELECT` → Read records
- `UPDATE` → Modify records
- `DELETE` → Remove records
- `ALTER TABLE` → Change table structure
- `TRUNCATE TABLE` → Remove all rows, keep structure
- `DROP TABLE` → Remove the table
- `DROP DATABASE` → Remove the database
