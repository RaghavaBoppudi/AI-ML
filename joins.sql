############################# Create a sample DB #############################
drop database IF EXISTS join_demo;

create database join_demo;

use join_demo;

############################# Create sample tables #############################
drop table if exists departments;
drop table if exists employees;

create table departments (
    department_id INT primary key,
    department_name VARCHAR(50)
);

create table employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    department_id INT,
    manager_id INT
);

############################# Insert sample records #############################

insert into departments
VALUES
(10, 'Engineering'),
(20, 'HR'),
(30, 'Sales'),
(40, 'Finance');

insert into employees
VALUES
(1, 'Alice', 10, NULL), ## Alice does not have a manager
(2, 'Bob', 10, 1),
(3, 'Carol', 20, 1),
(4, 'David', 30, 2),
(5, 'Emma', NULL, 2); # Emma does not belong in a department


############################# INNER JOIN #############################

### Return all the employees that belong to a department

SELECT employees.employee_name, departments.department_name ## select the rows to return
FROM employees ## Selects the employees table
INNER JOIN departments ## connects the departments table
ON employees.department_id = departments.department_id; ## connect based on the primary key

### Note how the above only prints out the employees who belong in a department and departments that have employees but not null values? - Inner join

############################# LEFT JOIN #############################

### Return the list of all the employees and their department names

SELECT employees.employee_name, departments.department_name
FROM employees
LEFT JOIN departments ## essentially prints out all the data from table A (employees) and the matching data from table B (departments)
ON employees.department_id = departments.department_id;

### Note how the above prints the employee name even if they don't belong in a department - left join.

############################# Right Join #############################

### Return all the departments and the employees present in IMPORT TABLE FROM

SELECT employees.employee_name, departments.department_name
FROM employees
RIGHT JOIN departments ## returns all the data from table B (departments) and matching data from Table A (employees)
ON employees.department_id = departments.department_id;

### Note how the above prints all the departments even if they don't have any employees? - Right join

############################# Full outer join #############################

### Give me a list of all the employees and departments
### MySQL doesn't support FULL OUTER JOIN. Use left join - union all - right join

SELECT employees.employee_name, departments.department_name
FROM employees
LEFT JOIN departments ## left join - everything from table A and the common ones from table B
ON employees.department_id = departments.department_id

UNION ALL

SELECT employees.employee_name, departments.department_name
FROM employees
RIGHT JOIN departments # right join - everything from table B and the common ones from table A
ON employees.department_id = departments.department_id ### stopping here prints the common values twice, since both right and left joins include the common elements
WHERE employees.employee_id IS NULL; ### that's why we use this filter - to only return departments that don't have an employee - since departments that have employees already come under the common elements and will be printed during left join

### Notice how everything from both the tables is printed? - FULL OUTER JOIN

### Why use UNION ALL instead of UNION?
### The first query has already returned all the matching records. UNION ALL avoids the extra duplicate-removal operation.

############################# SELF JOIN #############################

### Say you have only one table - employees table - notice how we have a manager_id but no separate manager table?
### Since every manager is also an employee, we can answer questions like "which employee reports to which manager?" by using a Self Join

## Select the employee name from employee table and call it Employee, and the employee_name from the "manager" table and call it Manager.
## This is alias too, but just for the column names in the returned table
SELECT employees.employee_name AS Employee, mngr.employee_name AS Manager 

## use the employees table twice, once used with the alias employees, next used with the manager alias
FROM employees employees
LEFT JOIN employees mngr

## Now match the employee's manager ID to another employee's ID
ON employees.manager_id = mngr.employee_id;

############################# CROSS JOIN (Carterian Product) #############################

## If you want every employee and every department paired, or maybe you have two shirt colors - red and blue, and have three sizes Small Medium and large
## Cartesian Product essentially gives you the total numnber of combinations you have
SELECT employees.employee_name, departments.department_name
FROM employees
CROSS JOIN departments;

############################# LEFT ANTI JOIN #############################

## Will give the values of table A that do not have a matching record in table B

SELECT employees.employee_id, employees.employee_name, employees.department_id
FROM employees
LEFT JOIN departments
ON employees.department_id = departments.department_id
WHERE departments.department_ID IS NULL; ### returns Emma because she alone doesnt belong to a department

############################# RIGHT ANTI JOIN #############################

## Will give the values of table B that do not have a matching record in table A

SELECT departments.department_id, departments.department_name ## make sure you sleect the columsn of table you want printed - question asks for table B so use column names of table B
FROM employees
RIGHT JOIN departments
ON employees.department_id = departments.department_id
WHERE employees.employee_ID IS NULL; ### returns Emma because she alone doesnt belong to a department