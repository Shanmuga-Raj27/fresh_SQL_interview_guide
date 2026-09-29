# SQL Constraints — Theoretical Key Constraints

## 1. What Are SQL Constraints?

Interview Answer: SQL constraints are rules applied to table columns to ensure that the data stored in a database is valid, consistent, and reliable. They prevent unwanted values from being inserted or updated and help maintain data integrity.

## 2. Entity Integrity

Entity integrity ensures that every row in a table can be uniquely identified. It is mainly maintained using a `PRIMARY KEY`, which must contain unique and non-NULL values.

### Key Points

- Every table should have a way to uniquely identify each record.
- A primary key cannot contain duplicate values.
- A primary key cannot contain `NULL`.
- A table can have only one primary key, but it can consist of multiple columns (composite primary key).

### Example

```sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100)
);

-- employee_id uniquely identifies each employee.
-- Duplicate employee_id values are not allowed.
-- NULL values are not allowed in employee_id.
```

#### Example of Entity Integrity Violation

```sql
INSERT INTO employees (employee_id, name)
VALUES (101, 'Arun');

INSERT INTO employees (employee_id, name)
VALUES (101, 'Priya');
-- Error: Duplicate primary key value.
-- Two employees cannot have the same employee_id.
```

---

## 3. Referential Integrity

Referential integrity ensures that relationships between tables remain consistent. It is maintained using a `FOREIGN KEY`, which requires a referenced value to exist in the parent table, preventing invalid references between related records.

### Key Points

- Maintains relationships between two tables.
- A foreign key references a primary key or eligible unique key in another table.
- Prevents inserting a child record with a non-existing parent reference.
- Helps maintain consistency when related records are updated or deleted.
- Foreign keys can contain `NULL` unless the column has a `NOT NULL` constraint.

### Example

```sql
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100)
);

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100),
    department_id INT,
    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);
-- department_id is a foreign key.
-- It references department_id in departments.
-- An employee cannot reference a non-existing department.
```

#### Example of Referential Integrity Violation

```sql
INSERT INTO employees (employee_id, name, department_id)
VALUES (101, 'Arun', 50);
-- Error if department_id 50 does not exist in departments.
-- The foreign key prevents an invalid reference.
```

### Interview Example

Suppose we have an `employees` table and a `departments` table. An employee should belong to a department that actually exists. A foreign key ensures this relationship remains valid.

---

## 4. Domain Integrity

Domain integrity ensures that each column contains values that are valid according to its defined data type, allowed range, and conditions. It helps prevent invalid or unexpected data from being stored in a column.

### Key Points

- Ensures values follow the column's defined data type.
- Controls which values are allowed in a column.
- Maintained using constraints such as `NOT NULL`, `CHECK`, `DEFAULT`, and appropriate data types.
- Prevents invalid values based on business requirements.

### Example

```sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT CHECK (age >= 18),
    salary DECIMAL(10,2) DEFAULT 25000
);

-- name cannot be NULL.
-- age must be at least 18.
-- salary uses 25000 when no value is provided.
-- Data types restrict the kind of values stored.
```

#### Example of Domain Integrity Violation

```sql
INSERT INTO employees (employee_id, name, age, salary)
VALUES (101, 'Arun', 16, 30000);
-- Error: age violates the CHECK constraint.
-- The minimum allowed age is 18.
```

### Interview Example

If an employee's age must be at least 18, domain integrity ensures that values below 18 are rejected through a `CHECK` constraint.

---

## 5. Quick Interview Revision

| Integrity Type | Main Purpose |
|----------------|--------------|
| **Entity Integrity** | Every record must be uniquely identifiable. |
| **Referential Integrity** | Relationships between tables must remain valid. |
| **Domain Integrity** | Column values must follow defined rules. |

### Common Mechanisms

- **`PRIMARY KEY`** – Unique, non-null identifier for each row
- **`FOREIGN KEY`** – Enforces referential integrity between tables
- **`NOT NULL`** – Prevents NULL values in specified columns
- **`CHECK`** – Validates data ranges and conditions
- **`DEFAULT`** – Assigns automatic values when none provided

### Easy Memory Trick

- **Entity Integrity** → Who is this record? (Unique identification)
- **Referential Integrity** → Does the related record exist? (Valid relationship)
- **Domain Integrity** → Is this value valid? (Valid column data)

**Important Interview Point:** These are theoretical concepts of data integrity. SQL constraints such as `PRIMARY KEY`, `FOREIGN KEY`, `CHECK`, and `NOT NULL` are practical mechanisms used to enforce these rules in a database.