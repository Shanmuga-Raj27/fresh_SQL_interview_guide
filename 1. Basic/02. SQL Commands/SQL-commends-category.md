# SQL Commands — Fast Revision & Interview Notes

## SQL Command Categories

SQL commands are usually grouped based on **what they do**. For interview preparation, remember them like this:

* **DDL** → Defines or changes the **structure**
* **DML** → Changes the **data**
* **DQL** → Reads or **retrieves data**
* **DCL** → Controls **user permissions**
* **TCL** → Controls **transactions**

---

# 1. DDL — Data Definition Language

DDL is used to create and manage the structure of a database, such as tables and databases. It helps us create new tables, modify existing table structures, or remove them when they are no longer needed.

### 1.1 `CREATE`

`CREATE` is used when we want to create a new database object, such as a table.

```sql
CREATE TABLE employees (
    id INT,
    name VARCHAR(100)
);
-- Creates a new table named employees.
-- The table contains id and name columns.
```

**Remember:** `CREATE` = **create something new**

---

### 1.2 `ALTER`

`ALTER` is used to change the structure of an existing table. For example, we can add, modify, or remove a column.

```sql
ALTER TABLE employees
ADD salary DECIMAL(10,2);
-- Adds a new salary column to the existing employees table.
```

**Remember:** `ALTER` = **change the structure**

---

### 1.3 `DROP`

`DROP` removes the database object itself. When we drop a table, both its structure and stored data are removed.

```sql
DROP TABLE employees;
-- Completely removes the employees table.
-- The table structure and its data are deleted.
```

**Remember:** `DROP` = **remove the object**

---

### 1.4 `TRUNCATE`

`TRUNCATE` removes **all rows** from a table but keeps the table structure.

```sql
TRUNCATE TABLE employees;
-- Removes all records from employees.
-- The table itself still exists.
```

**Remember:** `TRUNCATE` = **empty the table**

**Interview point:** Unlike `DELETE`, `TRUNCATE` does not remove individual rows using a `WHERE` condition.

---

# 2. DML — Data Manipulation Language

DML is used to work with the actual data stored in database tables. It allows us to add new records, update existing information, and delete unwanted records without changing the table structure.

### 2.1 `INSERT`

`INSERT` adds new records to a table.

```sql
INSERT INTO employees (id, name)
VALUES (101, 'Arun');
-- Adds a new employee record to the table.
```

**Remember:** `INSERT` = **add data**

---

### 2.2 `UPDATE`

`UPDATE` changes existing records.

```sql
UPDATE employees
SET name = 'Arun Kumar'
WHERE id = 101;
-- Finds employee 101.
-- Changes the existing name.
```

**Remember:** `UPDATE` = **change existing data**

**Interview point:** Be careful with `UPDATE` without a `WHERE` condition because it can change every row.

---

### 2.3 `DELETE`

`DELETE` removes existing records from a table.

```sql
DELETE FROM employees
WHERE id = 101;
-- Removes the employee whose id is 101.
```

**Remember:** `DELETE` = **remove data**

---

# 3. DQL — Data Query Language

DQL is used to retrieve data from database tables whenever we need specific information. The SELECT command is mainly used to read data based on our requirements.

### 3.1 `SELECT`

`SELECT` is used whenever we want to read data from a table.

```sql
SELECT id, name
FROM employees;
-- Retrieves the id and name of employees.
```

**Remember:** `SELECT` = **read data**

**Interview point:** `SELECT` is commonly treated as DQL in interview terminology, although MySQL's official documentation groups `SELECT` under its data manipulation statements.

---

# 4. DCL — Data Control Language

DCL is used to manage database permissions and decide what actions a user can perform. For example, we can give a user permission to read or modify data and remove those permissions whenever required.

### 4.1 `GRANT`

`GRANT` gives permissions to a user.

```sql
GRANT SELECT
ON company.employees
TO 'app_user'@'localhost';
-- Gives app_user permission to read the employees table.
```

**Remember:** `GRANT` = **give permission**

---

### 4.2 `REVOKE`

`REVOKE` removes permissions that were previously given.

```sql
REVOKE SELECT
ON company.employees
FROM 'app_user'@'localhost';
-- Removes SELECT permission from app_user.
```

**Remember:** `REVOKE` = **take permission back**

---

# 5. TCL — Transaction Control Language

 TCL is used to manage transactions, which are groups of database operations treated as a single logical unit. It allows us to save changes using COMMIT, undo uncommitted changes using ROLLBACK, and create checkpoints using SAVEPOINT.

### 5.1 `COMMIT`

`COMMIT` permanently saves the changes made in the current transaction.

```sql
COMMIT;
-- Saves the transaction changes permanently.
```

**Remember:** `COMMIT` = **save changes**

---

### 5.2 `ROLLBACK`

`ROLLBACK` cancels changes that have not yet been committed.

```sql
ROLLBACK;
-- Undoes the uncommitted changes of the current transaction.
```

**Remember:** `ROLLBACK` = **undo changes**

---

### 5.3 `SAVEPOINT`

`SAVEPOINT` creates a checkpoint inside a transaction. It is useful when we want to undo only part of the transaction instead of everything.

```sql
SAVEPOINT update_point;
-- Creates a checkpoint named update_point.
```

Later, we can return to that point:

```sql
ROLLBACK TO SAVEPOINT update_point;
-- Undoes changes made after update_point.
-- Earlier changes in the transaction are kept.
```

**Remember:** `SAVEPOINT` = **create a checkpoint**

---

# Final Interview Revision

| Category | Commands                              | Main Purpose            |
| -------- | ------------------------------------- | ----------------------- |
| **DDL**  | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` | Manage **structure**    |
| **DML**  | `INSERT`, `UPDATE`, `DELETE`          | Manage **data**         |
| **DQL**  | `SELECT`                              | **Retrieve data**       |
| **DCL**  | `GRANT`, `REVOKE`                     | Manage **permissions**  |
| **TCL**  | `COMMIT`, `ROLLBACK`, `SAVEPOINT`     | Manage **transactions** |

### Easy Memory Trick

```text
DDL → Structure
DML → Data
DQL → Query/Read
DCL → Control Access
TCL → Transaction
```

### Most Common Interview Confusions

* `DROP` → removes the **table itself**
* `TRUNCATE` → removes **all rows**, keeps the table
* `DELETE` → removes **rows**
* `SELECT` → **reads** data
* `COMMIT` → **saves** transaction changes
* `ROLLBACK` → **undoes** uncommitted changes
* `SAVEPOINT` → creates a **checkpoint** inside a transaction
