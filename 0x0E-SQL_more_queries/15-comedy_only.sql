-- lIst all comedy shows in database

SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres
On tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres
ON tv_show_genres.genre.id = tv_genres.id
WHERE tv_genres.name = "Commedy"
ORDER BY tv_shows.title;
