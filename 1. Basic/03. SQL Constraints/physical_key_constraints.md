# SQL Constraints — Physical Key Constraints

## 1. PRIMARY KEY

Interview Answer: A primary key is a column or combination of columns used to uniquely identify each record in a table. It does not allow duplicate or `NULL` values, ensuring that every row has a unique identity.

### Key Points

- Uniquely identifies each record in a table.
- Does not allow duplicate values or `NULL`.
- A table can have only one primary key.
- A primary key can consist of one or multiple columns.
- Commonly used to establish relationships with other tables.

### Example

```sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100),
    salary DECIMAL(10,2)
);

-- employee_id uniquely identifies each employee.
-- Duplicate and NULL employee_id values are not allowed.
```

### Example with Duplicate Value

```sql
INSERT INTO employees VALUES (101, 'Arun', 40000);

INSERT INTO employees VALUES (101, 'Priya', 45000);
-- Error: Duplicate primary key value.
-- employee_id 101 already exists.
```

**Remember:** `PRIMARY KEY` = Unique + NOT NULL.

## 2. FOREIGN KEY

Interview Answer: A foreign key is a column or combination of columns that creates a relationship between two tables. It references a primary key or eligible unique key in another table and ensures that related records remain consistent.

### Key Points

- Establishes relationships between parent and child tables.
- References a primary key or eligible unique key.
- Prevents invalid references to non-existing parent records.
- A foreign key can contain duplicate values.
- A foreign key can contain `NULL` unless `NOT NULL` is specified.
- Supports actions such as `ON DELETE CASCADE` and `ON UPDATE CASCADE`.

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

-- department_id references the parent departments table.
-- Employees can only reference existing department IDs.
```

### Foreign Key with ON DELETE CASCADE

```sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100),
    department_id INT,
    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
        ON DELETE CASCADE
);

-- If a department is deleted, its related employees are also deleted.
```

### Common Referential Actions

- `ON DELETE CASCADE` → Automatically deletes matching child records.
- `ON DELETE SET NULL` → Sets the child foreign key to NULL.
- `ON DELETE RESTRICT` → Prevents deletion of a referenced parent record.
- `ON UPDATE CASCADE` → Automatically updates matching foreign key values.

**Remember:** `FOREIGN KEY` = Maintains relationships between tables.

## 3. UNIQUE

Interview Answer: The `UNIQUE` constraint ensures that all values in a column or combination of columns are different. It is commonly used for fields such as email addresses, phone numbers, or usernames where duplicate values should not be allowed.

### Key Points

- Prevents duplicate values in a column.
- A table can have multiple `UNIQUE` constraints.
- Unlike a primary key, a `UNIQUE` column can allow `NULL` values in MySQL.
- Multiple `NULL` values are allowed in a MySQL UNIQUE index.
- Can be applied to a single column or multiple columns.

### Example

```sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    email VARCHAR(150) UNIQUE,
    name VARCHAR(100)
);

-- email must contain unique values.
-- Duplicate email addresses are not allowed.
```

### Example of Duplicate Value

```sql
INSERT INTO employees VALUES (101, 'arun@gmail.com', 'Arun');

INSERT INTO employees VALUES (102, 'arun@gmail.com', 'Priya');
-- Error: Duplicate email value.
-- The UNIQUE constraint prevents duplicate emails.
```

**Remember:** `UNIQUE` = No duplicate values, but NULL handling differs from PRIMARY KEY.

## 4. COMPOSITE KEY

Interview Answer: A composite key is a key formed by combining two or more columns to uniquely identify a record. It is useful when a single column cannot uniquely identify records, but their combination can.

### Key Points

- Contains two or more columns.
- The combination of columns must be unique.
- Individual columns can contain duplicate values.
- Commonly used in junction tables and many-to-many relationships.
- Can be created using a composite primary key or composite unique constraint.

### Example

Consider a student enrollment table where one student can register for multiple courses, and one course can have multiple students.

```sql
CREATE TABLE enrollments (
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    PRIMARY KEY (student_id, course_id)
);

-- student_id and course_id together form a composite primary key.
-- A student can enroll in multiple courses.
-- A course can have multiple students.
-- The same student cannot enroll in the same course twice.
```

### Example Data

| student_id | course_id | enrollment_date |
|------------|-----------|-----------------|
| 101        | 201       | 2026-09-01      |
| 101        | 202         | 2026-09-02      |
| 102        | 201       | 2026-09-03      |
| 202        | 202         | 2026-09-04      |

**Remember:** Composite Key = Combination of columns used to uniquely identify a record.

## 5. AUTO_INCREMENT

Interview Answer: `AUTO_INCREMENT` is a MySQL column attribute that automatically generates a sequential numeric value whenever a new record is inserted without specifying that column's value. It is commonly used with an integer primary key to generate unique record IDs.

### Key Points

- Automatically generates numeric values.
- Commonly used with primary key columns.
- Usually starts from `1` and increases automatically.
- The starting value can be customized.
- Deleted IDs are not necessarily reused.
- Only one `AUTO_INCREMENT` column is allowed per table.

### Example

```sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    salary DECIMAL(10,2)
);

-- employee_id is generated automatically.
-- No need to manually provide the employee ID.
```

### Insert Without AUTO_INCREMENT Column

```sql
INSERT INTO employees (name, salary)
VALUES ('Arun', 40000);

-- MySQL automatically generates employee_id.
-- Assuming the table is empty, the ID will normally be 1.
```

### Insert Multiple Rows

```sql
INSERT INTO employees (name, salary)
VALUES ('Priya', 45000);

-- MySQL automatically generates the next available ID.
-- Normally, the ID will be 2.
```

### Set Starting Value

```sql
ALTER TABLE employees
AUTO_INCREMENT = 100;

-- Sets the next generated value to 100,
-- provided it is greater than the current maximum ID.
```

**Remember:** `AUTO_INCREMENT` = Automatically generates numeric IDs; it is not itself a key constraint.

## 6. Quick Interview Revision

| Key / Constraint | Main Purpose |
|------------------|--------------|
| **PRIMARY KEY** | Uniquely identifies each record. |
| **FOREIGN KEY** | Connects related tables. |
| **UNIQUE** | Prevents duplicate values. |
| **COMPOSITE KEY** | Uses multiple columns to uniquely identify a record. |
| **AUTO_INCREMENT** | Automatically generates numeric IDs. |

### Easy Memory Trick

- **PRIMARY KEY** → Who is this record?
- **FOREIGN KEY** → Which parent record is related?
- **UNIQUE** → Is this value already present?
- **COMPOSITE KEY** → Can multiple columns identify the record together?
- **AUTO_INCREMENT** → Can MySQL generate the ID automatically?

### Important Interview Confusions

1. A table can have only one primary key, but that primary key can contain multiple columns.
2. A table can have multiple foreign keys and multiple unique constraints.
3. A foreign key does not have to contain unique values.
4. A composite key is not a separate constraint type; it describes a key made from multiple columns.
5. `AUTO_INCREMENT` is a MySQL feature, not a standalone SQL key constraint.
6. A `UNIQUE` constraint allows multiple `NULL` values in MySQL, whereas a primary key does not allow `NULL`.
