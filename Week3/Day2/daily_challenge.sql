-- CREATE TABLE FirstTab (
--      id integer, 
--      name VARCHAR(10)
-- )

-- INSERT INTO FirstTab VALUES
-- (5,'Pawan'),
-- (6,'Sharlee'),
-- (7,'Krish'),
-- (NULL,'Avtaar')

-- SELECT * FROM FirstTab

-- CREATE TABLE SecondTab (
--     id integer 
-- )

-- INSERT INTO SecondTab VALUES
-- -- (5),
-- (NULL)


-- SELECT * FROM SecondTab


--Q1

-- What will be the OUTPUT of the following statement?
-- SELECT COUNT(*) 
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )

-- Since IS NULL = 0, then it will not be able to count it and resposne will be 0

--Q2
-- SELECT COUNT(*) 
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )

-- I think it will count 0 since it also has NULL

-- --Q3
--  SELECT COUNT(*) 
--  FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )

 -- This one selects SecondTab which has a NULL value, but alos counts the NULL in FirstTab, therefore it counts as 0


 --Q4
 SELECT COUNT(*) 
 FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )

 -- Will count 2

 
	




