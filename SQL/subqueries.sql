########################## Sub Queries ##########################

USE sakila;

########################## Discovering the contents of tables ##########################

## To see all the tables in a database, use

SHOW tables;

## If unsure what table to use, use DESCRIBE

DESCRIBE customer;

## Inspect Table Definitions - know how a specific table connects to other tables

SHOW CREATE TABLE customer; ## Shows the relations used while creating the table

## Sub query is essentially a query inside a query
## Say you need to perform an operation like "Find all customers who live in the the district California"

SELECT * FROM customer;

## You see how customer table has the address_id but not the city, as needed by the question?
## That data is in the address TABLE

SELECT * FROM address;

## To answer that question, you can use a join statement to join the both of those and then filter out the necessary columns, which is fine.

## But another way to do it is to use a Sub Query
## The inner query retrieves information that the outer query needs to complete its job

SELECT c.first_name, c.last_name
FROM customer c
WHERE address_id IN ( ## This sub-query returns every address_id that has the district as California
    SELECT a.address_id
    FROM address a
    WHERE district LIKE 'California'
);


## Structure of a typical subquery

/*
SELECT columns
FROM table
WHERE column = (
    SELECT column
    FROM another_table
    WHERE condition
);
*/

## If the question is "Find all customers who live in the same city as customer 5"
## We have to first have a query to find out what the city for customer 5 is
## Then we need to return just the customers who have the same city_id

SELECT c.customer_id, c.first_name, c.last_name, a.city_id ## view only the necessary columns
FROM customer c
JOIN address a
ON c.address_id = a.address_id ## Join the 2 tables on address_id first
WHERE a.city_id = ( ## add a sub=query inside a where statement
    SELECT a.city_id # select city_id of customer_id 5
    FROM customer c
    JOIN address a
    ON c.address_id = a.address_id
    WHERE c.customer_id = 5
);

####### You can use Sub queries in three places - called SUB-QUERIES BY POSITION

## 1. WHERE
## 2. SELECT
## 3. FROM


########################## SUB QUERY INSIDE WHERE ##########################

## Q: Find films whose rental rate is higher than the average rental rate
## Break it down - find the average rental rate first

SELECT AVG(rental_rate)
FROM film;

## Now use that in the outer query

SELECT f.title, f.rental_rate
FROM film f
WHERE f.rental_rate > ( ## Where the film's rental rate is greater than the average rental rate
    SELECT AVG(f.rental_rate)
    FROM film f
);

########################## SUB QUERY INSIDE SELECT ##########################

## A subquery inside the SELECT clause can produce an additional calculated column

## Q: Show every customer and the total number of payments they have made

SELECT c.customer_id,
c.first_name,
c.last_name, 
(
    SELECT COUNT(*) 
    FROM payment p
    WHERE p.customer_id = c.customer_id ## inner table is counting total number of payments made by a specific customer_id
) AS totalPayments ## returns the value as totalPayments
FROM customer c;


## Essentially a "Correlated" subquery -- LATER

########################## SUB QUERY INSIDE FROM ##########################

## These are also called "DERIVED TABLES"
## Sub query as an alias - because you'll use a sub-query and give it an alias - read below

/*
FROM (
    SELECT ...
) AS table_name
*/

## These subqueries give a separate table that can be used

#### Q: Find customers who have made more than five payments

## Calculate the number of payments made by each customer

SELECT customer_id, COUNT(*) AS total_payments
FROM payment
GROUP BY customer_id;

## above table returns a table containing customer_id and the total payments made by them

SELECT paymentInfo.customer_id, paymentInfo.total_payments
FROM (
    SELECT customer_id, COUNT(*) AS total_payments ## calulates total_payments
    FROM payment
    GROUP BY customer_id
) AS paymentInfo ## creates a paymentInfo (an alias) table containing containing customer_id and the total payments made by them
WHERE paymentInfo.total_payments > 5; # only return those with more than 5 total_payments

## inner query groups payments by customer and calculates total_payments
## result is a derived table with the alias paymentInfo
## filters customers whose payment count is greater than five

## A derived table MUST ALWAYS HAVE AN ALIAS - because the outer table needs a name to reference IMPORT TABLE FROM

## Scalar Subquery
# A subquery that returns only 1 value
# = , > , < return one scalar values
# IN returns one column and allows multiple rows


########################## Handling multiple rows ##########################

## If a subquery returns more than one row, we must use a IN construct
SELECT
    customer_id,
    first_name
FROM customer
WHERE customer_id IN (
    SELECT customer_id
    FROM payment ## selects the customer_ids from the payment table
);

# Usual WHERE clause like WHERE customer_id = () doesn't work here because the sub-query inside results in more than one value

########################## Subquery operators ##########################

#### IN ####

# checks whether a value matches any value in a list

SELECT
    customer_id,
    first_name,
    last_name
FROM customer
WHERE customer_id IN (
    SELECT customer_id
    FROM payment
); ## Retrieve customers whose customer ID appears in the payment table

#### EXISTS ####



#### NOT IN ####

#### NOT EXISTS ####

#### ANY ####

#### ALL ####