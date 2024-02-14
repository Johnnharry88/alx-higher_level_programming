-- list all records of the second_table
SELECT score, name FROM second_table WHERE name IS NOT NULL and name != '' ORDER BY score DESC;
