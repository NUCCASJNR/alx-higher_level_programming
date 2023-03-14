-- Write a script that prints the full description of the table first_table
-- from the database hbtn_0c_0 in your MySQL server.

-- The database name will be passed as an argument of the mysql command
-- You are not allowed to use the DESCRIBE or EXPLAIN statements

SELECT column_name, data_type, character_maximum_length
FROM information_schema.columns
WHERE table_schema = 'hbtn_0c_0' AND table_name = 'first_table';
