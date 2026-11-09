############################ SUBQUERY ASSIGNMENT ###########################

USE sakila;

### Display all customer details who have made more than 5 payments

SELECT customer.first_name, customer.last_name
FROM customer ## Uses the inner query's returned customer_IDs to find the names
WHERE customer_id IN (
    SELECT customer_id ## Selects all customer_IDs with more than 5 payments
    FROM payment
    GROUP BY customer_id
    HAVING COUNT(*) > 5
);

### Find the names of actors who have acted in more than 10 films

SELECT a.actor_ID, a.first_name, a.last_name
FROM actor a
WHERE a.actor_ID IN (
SELECT fa.actor_ID
FROM film_actor fa
GROUP BY fa.actor_id
HAVING COUNT(*) > 10
);

### Find the names of customers who never made a payment

SELECT c.first_name, c.last_name
FROM customer c
WHERE customer_id IN (
    SELECT customer_id
    FROM payment
    GROUP BY customer_id
    HAVING COUNT(*) > 1
);