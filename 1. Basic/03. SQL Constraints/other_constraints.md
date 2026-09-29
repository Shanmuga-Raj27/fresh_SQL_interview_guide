# SQL Constraints — Other Constraints

## 1. NOT NULL

Interview Answer: `NOT NULL` is a constraint used to ensure that a column always contains a value and does not accept `NULL`. It is useful for important fields such as employee names, email addresses, or registration dates that should not be left empty.

### Key Points

- Prevents inserting `NULL` values into a column.
- Ensures mandatory fields always have a value.
- Can be applied to multiple columns in a table.
- Does not prevent duplicate values.
- An empty string (`''`) and `0` are not considered `NULL`.

### Example

```sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150)
);

-- name cannot contain NULL values.
-- email can contain NULL because NOT NULL is not specified.
```

### Example of NOT NULL Violation

```sql
INSERT INTO employees (employee_id, name)
VALUES (101, NULL);
-- Error: name cannot be NULL.
-- The NOT NULL constraint rejects the insertion.
```

**Remember:** `NOT NULL` = A value must be provided.

## 2. DEFAULT

Interview Answer: `DEFAULT` is used to automatically assign a predefined value to a column when no value is provided during insertion. It helps avoid missing values and is useful when a column commonly uses the same initial value.

### Key Points

- Assigns a predefined value when a column is omitted from an `INSERT` statement.
- Can be used with different data types.
- Explicitly inserting `NULL` does not normally trigger the default value.
- The default value can be a constant or an expression, depending on the column type and MySQL support.

### Example

```sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(50) DEFAULT 'General',
    salary DECIMAL(10,2) DEFAULT 25000
);

-- department defaults to General.
-- salary defaults to 25000.
```

### Insert Without Providing Default Columns

```sql
INSERT INTO employees (employee_id, name)
VALUES (101, 'Arun');

-- department automatically becomes General.
-- salary automatically becomes 25000.
```

### Explicitly Provide a Value

```sql
INSERT INTO employees (employee_id, name, department, salary)
VALUES (102, 'Priya', 'Backend', 45000);

-- Uses the provided values instead of DEFAULT values.
```

### Using DEFAULT Keyword

```sql
INSERT INTO employees (employee_id, name, department)
VALUES (103, 'Rahul', DEFAULT);

-- Explicitly uses the default department value General.
```

**Remember:** `DEFAULT` = Automatically uses a predefined value when no value is supplied.

## 3. CHECK

Interview Answer: `CHECK` is a constraint used to ensure that values satisfy a specified condition before they are inserted or updated. It is useful for enforcing business rules, such as minimum age requirements, positive salaries, or valid quantity ranges.

### Key Points

- Validates values based on a specified condition.
- Prevents records that violate the condition.
- Can be applied to a single column or multiple columns.
- Supports comparison operators and logical conditions.
- MySQL 8.0.16 and later enforces `CHECK` constraints.

### Example — Single Column CHECK

```sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT CHECK (age >= 18)
);

-- age must be 18 or above.
-- Values below 18 are rejected.
```

### Example of CHECK Violation

```sql
INSERT INTO employees (employee_id, name, age)
VALUES (101, 'Arun', 16);
-- Error: age violates the CHECK condition.
-- The minimum allowed age is 18.
```

### CHECK with Salary

```sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100),
    salary DECIMAL(10,2) CHECK (salary > 0)
);

-- Salary must be greater than zero.
-- Zero and negative salary values are rejected.
```

### CHECK with Multiple Conditions

```sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    salary DECIMAL(10,2),
    CHECK (age >= 18 AND salary > 0)
);

-- Both conditions must be satisfied.
-- Age must be at least 18.
-- Salary must be greater than zero.
```

### Named CHECK Constraint

```sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    CONSTRAINT chk_employee_age CHECK (age >= 18)
);

-- Creates a named CHECK constraint.
-- chk_employee_age is the constraint name.
-- Makes the constraint easier to identify and manage.
```

**Remember:** `CHECK` = Accepts only values that satisfy the specified condition.

## 4. Quick Interview Revision

| Constraint | Main Purpose |
|------------|--------------|
| **NOT NULL** | Prevents missing values. |
| **DEFAULT** | Provides a predefined value. |
| **CHECK** | Validates values using conditions. |

### Easy Memory Trick

- **NOT NULL** → Value is mandatory.
- **DEFAULT** → Use a predefined value.
- **CHECK** → Value must satisfy a condition.

### Important Interview Confusions

1. `NOT NULL` does not mean a column must have a unique value.
2. An empty string (`''`) is different from `NULL`.
3. `DEFAULT` is normally applied when a column is omitted, not when `NULL` is explicitly inserted.
4. `CHECK` validates conditions during `INSERT` and `UPDATE`.
5. In MySQL, `CHECK` constraints are enforced from version 8.0.16 onwards.
6. A `CHECK` condition that evaluates to `UNKNOWN` because of `NULL` does not reject the row. Use `NOT NULL` separately when NULL values must be prevented.
