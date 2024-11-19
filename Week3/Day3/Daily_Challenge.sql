---PART 1----

-- CREATE TABLE customer (id SERIAL, FirstNAme VARCHAR(50) NOT NULL, 
-- LastName VARCHAR (50) NOT NULL, Primary key (id))

-- CREATE TABLE customer_profile (
--     id SERIAL PRIMARY KEY,
--     IsLoggedIn BOOLEAN DEFAULT false,
--     customer_id INT,
--     FOREIGN KEY (customer_id) REFERENCES customer(id)
-- );


-- INSERT INTO customer (FirstNAme, LastName) 
-- VALUES 
-- ('John', 'Doe'),
-- ('Jerome', 'Lalu'),
-- ('Lea', 'Rive');


-- INSERT INTO customer_profile (IsLoggedIn, customer_id)
-- VALUES (
--     true,
--     (SELECT id FROM customer WHERE FirstNAme = 'John' AND LastName = 'Doe')
-- )


-- INSERT INTO customer_profile (IsLoggedIn, customer_id)
-- VALUES (
--     false,
--     (SELECT id FROM customer WHERE FirstNAme = 'Jerome' AND LastName = 'Lalu')
-- );

--First name of LoggedIn users--

-- SELECT FirstNAme
-- FROM customer
-- JOIN customer_profile on customer.id = customer_profile.customer_id
-- WHERE customer_profile.IsLoggedIn = true;

-- --All the customer firstnaem
-- SELECT customer.FirstNAme, COALESCE(customer_profile.IsLoggedIn, false) AS IsLoggedIn
-- FROM customer
-- LEFT JOIN customer_profile  ON customer.id = customer_profile.customer_id;

-- -- Number of customers that are not logged in

-- SELECT COUNT(*)
-- FROM customer 
-- LEFT JOIN customer_profile ON customer.id = customer_profile.customer_id
-- WHERE customer_profile.IsLoggedIn = false OR customer_profile.IsLoggedIn IS NULL;


----PART 2----

-- CREATE TABLE Book (
--     book_id SERIAL PRIMARY KEY,
--     title VARCHAR(50) NOT NULL,
--     author VARCHAR(50) NOT NULL
-- );

-- INSERT INTO Book (title, author) VALUES 
-- ('Alice In Wonderland', 'Lewis Carroll'),
-- ('Harry Potter', 'J.K Rowling'),
-- ('To Kill a Mockingbird', 'Harper Lee');

-- Select * from book;

-- CREATE TABLE Student (
--     student_id SERIAL PRIMARY KEY,
--     name VARCHAR(100) NOT NULL UNIQUE,
--     age INT CHECK (age <= 15)
-- );


-- INSERT INTO Student (name, age) VALUES
-- ('John', 12),
-- ('Lera', 11),
-- ('Patrick', 10),
-- ('Bob', 14);

-- Select * from student

-- CREATE TABLE Library (
--     book_fk_id INT,
--     student_fk_id INT,
--     borrowed_date DATE,
--     PRIMARY KEY (book_fk_id, student_fk_id),
--     FOREIGN KEY (book_fk_id) REFERENCES Book(book_id) 
--         ON DELETE CASCADE 
--         ON UPDATE CASCADE,
--     FOREIGN KEY (student_fk_id) REFERENCES Student(student_id) 
--         ON DELETE CASCADE 
--         ON UPDATE CASCADE
-- );

-- -- John borrowed Alice In Wonderland on 15/02/2022
-- INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
-- VALUES (
--     (SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
--     (SELECT student_id FROM Student WHERE name = 'John'),
--     '2022-02-15'
-- );

-- -- Bob borrowed To Kill a Mockingbird on 03/03/2021
-- INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
-- VALUES (
--     (SELECT book_id FROM Book WHERE title = 'To Kill a Mockingbird'),
--     (SELECT student_id FROM Student WHERE name = 'Bob'),
--     '2021-03-03'
-- );

-- -- Lera borrowed Alice In Wonderland on 23/05/2021
-- INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
-- VALUES (
--     (SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
--     (SELECT student_id FROM Student WHERE name = 'Lera'),
--     '2021-05-23'
-- );

-- -- Bob borrowed Harry Potter on 12/08/2021
-- INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
-- VALUES (
--     (SELECT book_id FROM Book WHERE title = 'Harry Potter'),
--     (SELECT student_id FROM Student WHERE name = 'Bob'),
--     '2021-08-12'
-- );

-- SELECT * from Library;


-- SELECT s.name, b.title
-- FROM Library l
-- JOIN Student s ON l.student_fk_id = s.student_id
-- JOIN Book b ON l.book_fk_id = b.book_id;


-- SELECT AVG(s.age) AS average_age
-- FROM Library l
-- JOIN Student s ON l.student_fk_id = s.student_id
-- JOIN Book b ON l.book_fk_id = b.book_id
-- WHERE b.title = 'Alice In Wonderland';

-- DELETE FROM Student WHERE name = 'Bob';