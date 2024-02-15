--Lists all cities found in database 

select c.'id', c.'name', s.'name'
from 'cities' as c 
inner join 'states' as s
on c.'state_id'= s.'id'
order by c.'id';
