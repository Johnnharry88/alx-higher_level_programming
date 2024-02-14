-- lists all the cities of California that si in database 

select id, name from cities where state_id = (select id from states where name = 'California') order by id;
