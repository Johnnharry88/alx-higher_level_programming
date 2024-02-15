--Lists all cities found in database 

SELECT c.'id', c.'name', s.'name'
FROM 'cities' as c 
INNER JOIN 'states' AS s
ON c.'state_id'= s.'id'
ORDER BY c.'id';
