# Stantech AI Assessment

## Task 1

- The SQL queries for creating the database schema and inserting dummy data are available in the [mysql-task-1.sql](./mysql-task-1.sql) file. This file also contains a complex query that:
  - Calculates the total spending per customer per product category in the last year.
  - Identifies the most purchased product category for each customer.
  - Computes the total amount spent by each customer.
  - Combines these results to list the top 5 customers based on their total spending.

## Task 2

- The Python code for implementing the functionality described in Task 2 can be found in the [python-task-2](./python-task-2) directory. This task includes:
  - Setting up a Flask application with SQLAlchemy to interact with the MySQL database.
  - Implementing API endpoints to retrieve customer spending information, handle orders, and manage product data.
  - Utilizing JWT for secure authentication.

## Versions
- MySQL: 8.0.3
- Python: 3.9.6