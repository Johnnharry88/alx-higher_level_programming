-- lists all genres from the database

SELECT g.'name' AS 'genre', 
       COUNT(*) AS 'number_of_shows'
  FROM 't_genres' AS g
       INNER JOIN 'tv_show_genres' AS t
       ON g. 'id' = t.'genre_id'
GROUP BY g.'name'
ORDER BY 'number_of_ shows' DESC;

