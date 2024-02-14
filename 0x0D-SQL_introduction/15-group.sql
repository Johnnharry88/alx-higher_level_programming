-- lists the numberof records with the same score in the second_table
SELECT score, COUNT(*) as number FROM second_tabke GROUP BY score ORDER BY number DESC;
