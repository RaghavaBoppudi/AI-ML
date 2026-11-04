### Use sakila throughout

USE sakila;

######################## Assignment 1 ########################
### 1. Get all customers whose first name starts with 'J' and who are active.

SELECT * 
FROM customer 
WHERE first_name LIKE 'J%' 
AND active = TRUE;

### 2. Find all films where the title contains the word 'ACTION' or the description contains 'WAR'.

SELECT film.title, film.description 
FROM film WHERE title 
LIKE '%action%' 
OR description LIKE '%war%';

### 3. List all customers whose last name is not 'SMITH' and whose first name ends with 'a'.

SELECT customer.first_name, customer.last_name 
FROM customer 
WHERE NOT last_name = 'SMITH' AND first_name LIKE '%a';

#### 4. Get all films where the rental rate is greater than 3.0 and the replacement cost is not null.

SELECT film.title, film.rental_rate, film.replacement_cost 
FROM film 
WHERE rental_rate > '3.0' AND replacement_cost IS NOT NULL;

### 5. Count how many customers exist in each store who have active status = 1.

select count(customer.customer_id) AS customerID, customer.store_id
FROM customer 
WHERE active = '1'
GROUP BY customer.store_id;

### 6. Show distinct film ratings available in the film table.

SELECT distinct(rating) from film;

### 7. Find the number of films for each rental duration where the average length is more than 100 minutes.

SELECT COUNT(*) AS FilmCount, film.rental_duration, AVG(film.length) AS AverageLength
FROM film
GROUP BY film.rental_duration
HAVING AVG(film.length) > 100;

### 8. List payment dates and total amount paid per date, but only include days where more than 100 payments were made.

SELECT DATE(payment_date) AS PaymentDate, SUM(amount) AS amount
FROM payment
GROUP BY DATE(payment_date)
HAVING COUNT(*) > 100; ## counts the transactions and makes sure it prints only the aggregated data that is greater than 100

### 9. Find customers whose email address is null or ends with '.org'.

SELECT customer_id, first_name, last_name, email
FROM customer
WHERE email IS NULL
OR email LIKE '%.org';

### 10. List all films with rating 'PG' or 'G', and order them by rental rate in descending order.

SELECT title, rating, rental_rate
FROM film
WHERE rating LIKE 'PG' OR rating LIKE 'G' ## Alternatively, use rating IN ('PG', 'G') -- much better actually
ORDER BY rental_rate DESC;

### 11. Count how many films exist for each length where the film title starts with 'T' and the count is more than 5.

SELECT count(*) AS NoOfFilms, length
FROM film
WHERE title LIKE 'T%'
GROUP BY length
HAVING count(*) > 5;

### 12. List all actors who have appeared in more than 10 films.

SELECT a.actor_id, a.first_name, a.last_name, COUNT(fa.film_id) AS NumOfFilms
FROM film_actor fa
JOIN actor a ## because film_actor table only has actor_id and not name, and the names are in film table, so we do a join
ON fa.actor_id = a.actor_id
GROUP BY a.actor_id
HAVING COUNT(fa.film_id) > 10;


### 13. Find the top 5 films with the highest rental rates and longest lengths combined, ordering by rental rate first and length second

SELECT f.title, f.rental_rate, f.length
FROM film f
ORDER BY f.rental_rate DESC, f.length DESC # order by rental rate first, and if they're equal, by length
LIMIT 5;

### 14. Show all customers along with the total number of rentals they have made, ordered from most to least rentals.

SELECT c.customer_id, c.first_name, c.last_name, count(r.rental_id) AS rentalCount # count of rental ID to count total rentals
FROM customer c
LEFT JOIN rental r
ON c.customer_id = r.customer_id # Joining customer and rental table using customer id.
GROUP BY c.customer_id # group the rentals by customer
ORDER BY rentalCount DESC;

### 15. List the film titles that have never been rented

# Essentially join film table (has film title and film id) and inventory table (has inventory id and film id) 
# and rental table (has inventory id)
SELECT f.title # because we only need to see these columns in the output
FROM film f
LEFT JOIN inventory i
ON f.film_id = i.film_id
LEFT JOIN rental r
ON r.inventory_id = i.inventory_id
GROUP BY f.title # group by the title
HAVING count(r.rental_id) = 0;








