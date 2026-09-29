# Basic SQL Query Clauses — Fast Revision & Interview Notes

> **Note:** Some topics below overlap with earlier sections. For a cleaner study file, you can later consolidate Section 6 with 7.1, and consider whether the full Section 8 table duplicates the revision already covered in Sections 1–7.

## 1. DISTINCT

`DISTINCT` is used to retrieve only unique values from a column or combination of columns, removing duplicate rows from the result. It is commonly used when we want to identify unique departments, cities, or categories from a table.

### 1.1 Select Unique Values

```SQL
SELECT DISTINCT department
FROM employees;
-- Returns each department only once.
-- Duplicate department names are removed.
```

### 1.2 DISTINCT with Multiple Columns

```SQL
SELECT DISTINCT department, city
FROM employees;
-- Returns unique combinations of department and city.
-- A combination is considered duplicate only when both values match.
```

### 1.3 DISTINCT with COUNT

```SQL
SELECT COUNT(DISTINCT department)
FROM employees;
-- Counts the number of unique departments.
```

Remember: `DISTINCT` removes duplicate rows from the query result, not from the original table.

## 2. WHERE

`WHERE` is used to filter records based on a specific condition. It returns only the rows that satisfy the given condition, making it useful when we need particular records instead of the entire table.

### 2.1 Basic WHERE Condition

```SQL
SELECT *
FROM employees
WHERE salary > 40000;
-- Returns employees whose salary is greater than 40000.
```

### 2.2 Comparison Operators

```SQL
SELECT *
FROM employees
WHERE salary >= 50000;
-- Returns employees earning 50000 or more.
```

Remember: `WHERE` filters individual rows before grouping and aggregation.

## 3. ORDER BY

`ORDER BY` is used to arrange query results based on one or more columns. By default, it sorts values in ascending order, but we can use `DESC` to display results in descending order.

### 3.1 Ascending Order (ASC)

```SQL
SELECT *
FROM employees
ORDER BY salary ASC;
-- Displays employees from lowest salary to highest salary.
-- ASC means ascending order.
```

### 3.2 Descending Order (DESC)

```SQL
SELECT *
FROM employees
ORDER BY salary DESC;
-- Displays employees from highest salary to lowest salary.
-- DESC means descending order.
```

### 3.3 Sort Using Multiple Columns

```SQL
SELECT *
FROM employees
ORDER BY department ASC, salary DESC;
-- First sorts employees by department alphabetically.
-- Within each department, sorts salary from highest to lowest.
```

### 3.4 ORDER BY with Column Position

```SQL
SELECT id, name, salary
FROM employees
ORDER BY 3 DESC;
-- Sorts using the third selected column (salary).
-- Column positions are based on the SELECT column order.
```

Remember: `ASC` is the default sorting order. Use `DESC` when you want the highest or latest values first.

## 4. LIMIT

`LIMIT` is used to restrict the number of rows returned by a query. It is especially useful when displaying a small number of records, such as the top 5 highest-paid employees.

### 4.1 Basic LIMIT

```SQL
SELECT *
FROM employees
LIMIT 5;
-- Returns only the first 5 rows.
```

### 4.2 LIMIT with ORDER BY

```SQL
SELECT name, salary
FROM employees
ORDER BY salary DESC
LIMIT 3;
-- Sorts employees by salary in descending order.
-- Returns the top 3 highest-paid employees.
```

Remember: Always use `ORDER BY` with `LIMIT` when you need predictable results, such as top 5 or bottom 10 records.

## 5. OFFSET

`OFFSET` is used to skip a specified number of rows before returning the remaining results. It is commonly used with `LIMIT` to implement pagination, where records are displayed page by page.

### 5.1 Basic OFFSET

```SQL
SELECT *
FROM employees
LIMIT 5 OFFSET 5;
-- Skips the first 5 rows.
-- Returns the next 5 rows.
```

### 5.2 Pagination Example

```SQL
-- Page 1
SELECT *
FROM employees
ORDER BY id
LIMIT 5 OFFSET 0;
-- Returns records 1 to 5.

-- Page 2
SELECT *
FROM employees
ORDER BY id
LIMIT 5 OFFSET 5;
-- Skips 5 records and returns the next 5.

-- Page 3
SELECT *
FROM employees
ORDER BY id
LIMIT 5 OFFSET 10;
-- Skips 10 records and returns the next 5.
```

### 5.3 LIMIT with Offset Shorthand

MySQL also supports the following syntax:

```SQL
SELECT *
FROM employees
ORDER BY id
LIMIT 5, 10;
-- First value (5) represents OFFSET.
-- Second value (10) represents LIMIT.
-- Skips 5 rows and returns the next 10 rows.
```

Remember: `OFFSET` skips rows, while `LIMIT` controls how many rows are returned.

## 6. Column Aliases

A column alias is a temporary name given to a column or calculated expression in the query result. It helps make output more readable, especially when working with calculations or aggregate functions.

### 6.1 Alias Using AS

```SQL
SELECT name AS employee_name
FROM employees;
-- Displays the name column using employee_name as its heading.
```

### 6.2 Alias Without AS

```SQL
SELECT name employee_name
FROM employees;
-- AS is optional when assigning a column alias.
```

### 6.3 Alias with Calculated Columns

```SQL
SELECT name, salary * 12 AS annual_salary
FROM employees;
-- Calculates annual salary by multiplying monthly salary by 12.
-- Displays the calculated result using annual_salary as its heading.
```

### 6.4 Alias with Aggregate Functions

```SQL
SELECT department, COUNT(*) AS total_employees
FROM employees
GROUP BY department;
-- Counts employees in each department.
-- Displays the result using the alias total_employees.
```

### 6.5 Table Alias

Aliases can also be used to give shorter names to tables.

```SQL
SELECT e.name, e.salary
FROM employees AS e;
-- Assigns the alias e to the employees table.
-- Uses e instead of writing employees repeatedly.
```

Remember: Column aliases change the displayed column name in the query result. They do not rename the actual column in the database.

## 7. Additional Basic Query Clauses — Quick Revision

### 7.1 AS

`AS` is used to assign an alias to a column or table. It improves query readability but does not change the original database object.

```SQL
SELECT salary AS monthly_salary
FROM employees;
-- Displays salary with the heading monthly_salary.
```

### 7.2 ALL

`ALL` is the default behavior of `SELECT`, meaning duplicate rows are included unless `DISTINCT` is specified.

```SQL
SELECT ALL department
FROM employees;
-- Returns department values including duplicates.
```

### 7.3 Parentheses in WHERE Conditions

Parentheses help control the order in which multiple conditions are evaluated.

```SQL
SELECT *
FROM employees
WHERE department = 'Backend'
AND (salary > 50000 OR salary < 30000);
-- First evaluates the conditions inside parentheses.
-- Then checks whether the department is Backend.
```

## 8. Basic Query Clauses — Quick Revision

| Clause | Purpose |
|--------|---------|
| `DISTINCT` | Removes duplicate rows from query results |
| `WHERE` | Filters records based on conditions |
| `ORDER BY` | Sorts query results |
| `ASC` | Sorts in ascending order |
| `DESC` | Sorts in descending order |
| `LIMIT` | Restricts the number of returned rows |
| `OFFSET` | Skips a specified number of rows |
| `AS` | Assigns temporary aliases to columns or tables |
| `ALL` | Includes duplicate values (default behavior) |

### Important Interview Points

- `DISTINCT` works on the combination of selected columns.
- `WHERE` filters rows before grouping.
- `ORDER BY` sorts the final query result.
- `LIMIT` is commonly used to find top N records.
- `LIMIT` and `OFFSET` are commonly used for pagination.
- `AS` creates a temporary alias; it does not rename the original database column.
- `ORDER BY` should be used with `LIMIT` when consistent row selection is important.
