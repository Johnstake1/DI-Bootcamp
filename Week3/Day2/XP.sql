-- SELECT * from customer

-- SELECT CONCAT(first_name,' ', last_name) as full_name from customer

-- SELECT DISTINCT create_date from customer; - removes duplicates

-- SELECT * from customer
-- ORDER BY first_name DESC;

-- SELECT film_id, title, description, release_year, rental_rate FROM film
-- ORDER BY rental_rate ASC;

-- SELECT address, address2, phone, district from address
-- WHERE district in ('Texas');

-- SELECT * from film
-- WHERE film_id = 15 or film_id = 150;

-- SELECT film_id, title, description, release_year, length, rental_rate from film
-- WHERE title = 'Streak Ridgemont'

-- SELECT film_id, title, description, release_year, length, rental_rate from film
-- WHERE title LIKE 'St%';

-- SELECT * from payment
-- ORDER BY amount ASC;

-- SELECT * FROM film ORDER BY rental_rate ASC OFFSET 10 FETCH FIRST  10  ROWS ONLY

-- SELECT customer.first_name, customer.last_name, payment.amount, payment.payment_date
-- FROM customer
-- INNER JOIN payment
-- ON customer.customer_id = payment.customer_id;

-- SELECT film.title, inventory.film_id
-- from film
-- LEFT JOIN inventory ON film.film_id = inventory.film_id
-- WHERE inventory.film_id IS NULL


-- SELECT city.city, country.country
-- from city
-- INNER JOIN country
-- ON country.country_id = city.country_id


-- SELECT customer.first_name, customer.last_name, customer.customer_id, payment.amount, payment.payment_date
-- from customer
-- FULL JOIN payment 
-- ON customer.customer_id = payment.customer_id
-- ORDER BY payment.staff_id;







