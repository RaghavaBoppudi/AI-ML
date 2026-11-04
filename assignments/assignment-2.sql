############################ JOINS ASSIGNMENT ###########################

USE sakila;

### List all customers along with the films they have rented.

SELECT c.customer_id, c.first_name, c.last_name, f.title
FROM customer c
LEFT JOIN rental r
ON c.customer_id = r.customer_id
LEFT JOIN inventory i
ON r.inventory_id = i.inventory_id
LEFT JOIN film f
ON i.film_id = f.film_id;

### List all customers and show their rental count, including those who haven't rented any films.

SELECT c.customer_id, c.first_name, c.last_name, COUNT(r.rental_id) AS NumRentals
FROM customer c
LEFT JOIN rental r # left join because you want null values (people who never rented anything) to also show up
ON c.customer_id = r.customer_id
GROUP BY c.customer_id; # grouping by customer because we have an aggregation to be done (count())

### Show all films along with their category. Include films that don't have a category assigned.

SELECT f.title, c.name
FROM film f
LEFT JOIN film_category fc
ON f.film_id = fc.film_id
LEFT JOIN category c
ON fc.category_id = c.category_id;

### Show all customers and staff emails from both customer and staff tables using a full outer join (simulate using LEFT + RIGHT + UNION).

SELECT c.email AS customerEmail, s.email AS staffEmail
FROM customer c
LEFT JOIN staff s ### MySQL doesn't have full outer join, so use LEFT JOIN, UNION ALL and RIGHT OUTER
ON c.store_id = s.store_id

UNION ALL

SELECT c.email AS customerEmail, s.email AS staffEmail
FROM customer c
RIGHT JOIN staff s
on c.store_id = s.store_id
WHERE c.customer_id IS NULL;

### Find all actors who acted in the film "ACADEMY DINOSAUR".

SELECT a.actor_id, a.first_name, a.last_name
FROM actor a
JOIN film_actor fa
ON a.actor_id = fa.actor_id
JOIN film f
ON fa.film_id = f.film_id
WHERE f.title = "ACADEMY DINOSAUR";

### List all stores and the total number of staff members working in each store, even if a store has no staff.

SELECT s.store_id, a.address, count(st.staff_id) AS totalStaff
FROM store s
LEFT JOIN staff st ## because a store should be returned even if it had no staff (staff is null)
ON s.store_id = st.store_id
JOIN address a
ON s.address_id = a.address_id
GROUP BY s.store_id;

### List the customers who have rented films more than 5 times. Include their name and total rental count.

SELECT c.customer_id, c.first_name, c.last_name, count(r.rental_id) AS numberOfRentals
FROM customer c
JOIN rental r
ON c.customer_id = r.customer_id
GROUP BY c.customer_id
HAVING count(r.rental_id) > 5;

