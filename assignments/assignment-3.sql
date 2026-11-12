############################ SUBQUERY ASSIGNMENT ###########################

USE sakila;

############################ 1. Display all customer details who have made more than 5 payments

SELECT customer.first_name, customer.last_name
FROM customer ## Uses the inner query's returned customer_IDs to find the names
WHERE customer_id IN (
    SELECT customer_id ## Selects all customer_IDs with more than 5 payments
    FROM payment
    GROUP BY customer_id
    HAVING COUNT(*) > 5
);

############################ 2. Find the names of actors who have acted in more than 10 films

SELECT 
    a.actor_ID, 
    a.first_name, 
    a.last_name
FROM actor a
WHERE a.actor_ID IN (
SELECT fa.actor_ID
FROM film_actor fa
GROUP BY fa.actor_id
HAVING COUNT(*) > 10
);

############################ 3. Find the names of customers who never made a payment

SELECT
    c.customer_id,
    c.first_name,
    c.last_name
FROM customer c
WHERE c.customer_id NOT IN (
    SELECT p.customer_id ## since customers who have never made a payment are not in the payment table, we use NOT IN payment table
    FROM payment p
);

############################ 4. List all films whose rental rate is higher than the average rental rate of all films.

#### Find avg rental rate
SELECT AVG(rental_rate)
FROM film;

#### Find films that have rental rate higher than this

SELECT 
    film_id, 
    title, 
    rental_rate
FROM film
WHERE rental_rate > (
    SELECT AVG(rental_rate)
    FROM film
);

############################ 5. List the titles of films that were never rented.

#### Same logic as 3, find films not on rental table

SELECT 
    film.title
FROM film
WHERE film.film_id NOT IN ( ## selects films that are not in the rental table
    SELECT film_id
    FROM inventory
    JOIN rental
    ON inventory.inventory_id = rental.inventory_id
);


############################ 6. Display the customers who rented films in the same month as customer with ID 5.

WITH customer_5_month AS ( ## Defining a CTE for extracting the different months and years customer 5 has rented.
    SELECT DISTINCT
        YEAR(rental_date) AS rental_year,
        MONTH(rental_date) AS rental_month
    FROM rental
    WHERE customer_id = 5
)

SELECT DISTINCT
    customer.customer_id,
    customer.first_Name,
    customer.last_name
FROM customer
JOIN rental
    ON customer.customer_ID = rental.rental_ID
JOIN customer_5_month
    ON YEAR(rental.rental_date) = customer_5_month.rental_year
    AND MONTH(rental.rental_date) = customer_5_month.rental_month
WHERE customer.customer_ID <> 5;

############################ 7. Find all staff members who handled a payment greater than the average payment amount.

WITH average_payment AS ( ## find the average payment amount from the payment table
    SELECT AVG(amount) AS avg_amount
    FROM payment
)

SELECT DISTINCT ## DISTINCT makes sure each staff member appears only once
    s.staff_id,
    s.first_name,
    s.last_name
FROM staff s
JOIN payment p
    ON s.staff_id = p.staff_id ## join staff to the payment table
JOIN average_payment ap
    ON p.amount > ap.avg_amount; ## join the CTE to the tables with the condition

############################ 8. Show the title and rental duration of films whose rental duration is greater than the average.

WITH average_duration AS (
    SELECT AVG(rental_duration) AS avg_duration
    FROM film
)

SELECT
    f.title,
    f.rental_duration
FROM film f
JOIN average_duration ad
    ON f.rental_duration > ad.avg_duration;

############################ 9. Find all customers who have the same address as customer with ID 1.

#### create temp table to find address of customer_1

CREATE TEMPORARY TABLE address_c1 AS
SELECT address_id
FROM customer
WHERE customer_id = 1;

SELECT
    c.customer_id,
    c.first_name,
    c.last_name
FROM customer c
JOIN address_c1 c1 ## join the temp table and customer table
    ON c.address_id = c1.address_id
WHERE c.customer_id <> 1; ## exclude customer_id 1 because you need people other than him that stay there

############################ 10. List all payments that are greater than the average of all payments.

#### Creating a view
CREATE OR REPLACE VIEW vw_payments_above_average AS

SELECT
    payment_id,
    customer_id,
    staff_id,
    rental_id,
    amount,
    payment_date
FROM payment
WHERE amount > (
    SELECT AVG(amount)
    FROM payment
);

#### Querying the view

SELECT * FROM vw_payments_above_average;