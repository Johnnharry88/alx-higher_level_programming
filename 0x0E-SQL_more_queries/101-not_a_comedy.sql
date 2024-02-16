-- Lists all shows without the eenre Comedy in database

SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN
(SELECT tv_shows.id
FROM tv_shows
INNER JOIN tv_shows_genres
ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres
ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres
WHERE tv_genres.name = "Commedy")
ORDER BY tv_shows.title;
