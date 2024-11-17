-- CREATE TABLE items2 (items_id SERIAL PRIMARY KEY,
-- items_name VARCHAR(50) NOT NULL,
-- price INT NOT NULL);

-- ALTER TABLE items
-- ALTER COLUMN price TYPE INT USING price::integer

-- SELECT * FROM customers

-- INSERT INTO items (items_name, price)
-- VALUES ('Small Desk', 100),
-- ('Large Desk', 300),
-- ('Fan', 80);

-- INSERT INTO customers (first_name, last_name)
-- VALUES ('Melanie', 'Johnson')

-- SELECT price from items where price > 80
-- SELECT price from items where price <= 300
-- SELECT last_name from customers where last_name = 'Jones'
-- SELECT first_name from customers where first_name != 'Scott'
-- SELECT last_name from customers where last_name = 'Smith' - Outcome not null
