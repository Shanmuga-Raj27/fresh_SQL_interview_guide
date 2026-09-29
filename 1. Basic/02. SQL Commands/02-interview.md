# 02. SQL Commands — Interview Questions

## 1. What is SQL?

SQL stands for Structured Query Language. It is the standard language used to communicate with relational databases. We use it to create, read, update, and delete data, as well as to manage the database structure itself. It is essential for anyone working with databases.

## 2. What is a relational database?

A relational database stores data in tables with rows and columns. Each table represents a specific entity, like employees or products, and relationships link these tables together. SQL is used to manage and query this structured data efficiently.

## 3. What are the main categories of SQL commands?

SQL commands are grouped into five categories based on their purpose:

- **DDL (Data Definition Language)** – defines or changes the database structure, such as CREATE, ALTER, DROP, and TRUNCATE.
- **DML (Data Manipulation Language)** – manages the actual data inside tables, such as INSERT, UPDATE, and DELETE.
- **DQL (Data Query Language)** – retrieves data from the database. The main command is SELECT.
- **DCL (Data Control Language)** – controls user permissions, such as GRANT and REVOKE.
- **TCL (Transaction Control Language)** – manages transactions, such as COMMIT, ROLLBACK, and SAVEPOINT.

## 4. What is the difference between DDL and DML?

DDL commands deal with the database structure or schema. They create, modify, or remove database objects like tables and databases. Examples include CREATE, ALTER, and DROP.

DML commands deal with the data stored inside those structures. They allow us to insert new records, update existing ones, or delete records. Examples include INSERT, UPDATE, and DELETE.

A key difference is that DDL commands are auto-committed, meaning changes take effect immediately, while DML changes can be rolled back before committing.

## 5. What is a transaction in SQL?

A transaction is a sequence of one or more SQL operations treated as a single logical unit. It ensures that either all operations succeed together or none of them take effect, maintaining data consistency and integrity.

## 6. What is the difference between COMMIT and ROLLBACK?

COMMIT permanently saves all changes made in the current transaction to the database. Once committed, the changes cannot be undone.

ROLLBACK cancels all changes made in the current transaction and restores the database to its state before the transaction began. It is used when something goes wrong during a transaction.

## 7. What is the difference between DROP and TRUNCATE?

DROP removes the entire table object from the database, including its structure and all data. Once dropped, the table no longer exists and must be recreated.

TRUNCATE removes all rows from a table but keeps the table structure intact. The table still exists and can accept new data. TRUNCATE is generally faster than DELETE because it does not log individual row deletions.

## 8. What are DCL commands and why are they important?

DCL commands control access to the database. The two main commands are:

- **GRANT** – gives specific permissions to a user, such as the ability to SELECT or UPDATE data.
- **REVOKE** – removes previously granted permissions from a user.

These commands are important for database security, ensuring that only authorized users can access or modify specific data.

## 9. What is the purpose of SELECT in SQL?

SELECT is the primary command for retrieving data from a database. It allows us to fetch specific columns, filter rows using conditions, sort results, and limit the number of rows returned. It is the most frequently used SQL command and is often categorized under DQL.

## 10. What is the difference between CREATE DATABASE and CREATE TABLE?

CREATE DATABASE creates a new database, which is a container for storing related tables and other objects. It is usually the first step when setting up a new database system.

CREATE TABLE creates a new table within an existing database. A table defines the structure for storing specific data using columns, data types, and constraints. You must select a database using USE before creating a table inside it.
