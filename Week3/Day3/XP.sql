------------ PART 1 --------------

-- SELECT * FROM public.language
-- ORDER BY language_id ASC;

--EX2
-- SELECT film.title, film.description, language.name
-- from film
-- FULL JOIN Language
-- ON language.language_id = film.language_id


--EX3
-- SELECT film.title, film.description, language.name
-- from film
-- RIGHT JOIN Language
-- ON language.language_id = film.language_id

--EX4
-- CREATE TABLE new_film(
-- new_film_id SERIAL,
-- new_film_name VARCHAR(100) NOT NULL)

-- INSERT INTO new_film (new_film_name) 
-- VALUES ('Avengers End Game'),('El Secreto de sus Ojos')

-- SELECT * from new_film

--EX5 FOR CHECKER. 
-- I did not understand if we have to join the tables language_id and film_id. How would the client know which movie is what? 
-- Is it even possible to join tables while creating tables?

-- CREATE TABLE customer_review(
-- review_id SERIAL PRIMARY KEY,
-- film_id SERIAL FOREIGN KEY,
-- language_id INTEGER NOT NULL,
-- title VARCHAR(50),
-- score SMALLINT,
-- review_text VARCHAR(100),
-- last_update DATE,
-- CONSTRAINT fk_film
-- FOREIGN KEY(film_id) REFERENCES film (film_id)
-- ON DELETE RESTRICT)


--EX6 FOR CHECKER. 
-- I did not understand if we have to join the tables language_id and film_id. How would the client know which movie is what? 
-- Is it even possible to join tables while inserting values?

-- INSERT INTO customer_review ('film_id', 'language_id','title','score', 'review_text', 'last_update') 
-- VALUES (1, 2, 'Best movie of all time', 10, 'The best movie of all time. Enjoyed it pretty much', 2024/11/19)

--EX7
-- Since I used a ON DELETE RESTRICT, it will not be possible to delete the review on a film since I assume that it should have been linked to another table.

-------------PART 2-----------------

--EX1
-- SELECT * from language
-- UPDATE language SET name='Spanish' WHERE language_id=3

-- SELECT * from language
-- ORDER BY language_id ASC;

--EX2
-- By checking the constraints for the customer's table, it shows that address_id and store_id are a FK

--EX3 FOR CHECKER. I had issues with that table creation.
-- I assume that while deleting it is important to check the foreign keys and try to avoid cascading since it may alter the entire db.

--EX4

-- SELECT COUNT(*) as Outstanding_Rentals from rental
-- WHERE return_date IS NULL;

--EX5 FOR CHECKER 

-- How do you take from I need to link inventory_id into the 
-- inventory table. From there retrieve the film_id and relate it to the film_id that is in the film table, to extract the title of the film (film.title)
-- I was able to JOIN rentals and payments but there are no title names.

-- Select * from rental
-- WHERE return_date IS NULL

-- SELECT rental.return_date, payment.amount, rental.inventory_id, rental.rental_id
-- FROM payment
-- FULL JOIN rental
-- ON rental.rental_id = payment.rental_id
-- WHERE rental.return_date IS NULL
-- ORDER BY amount DESC
-- LIMIT 30;

--EX6 #We did not learn how to JOIN 3 or more tables.

SELECT  actor.first_name, actor.last_name, actor.actor_id, film_actor.film_id
FROM actor
JOIN film_actor
ON film_actor.actor_id = actor.actor_id
WHERE last_name ILIKE 'Monroe'
LIMIT 30;









