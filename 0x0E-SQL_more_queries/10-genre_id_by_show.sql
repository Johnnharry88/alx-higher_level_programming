-- lists all shows combined in the database

SELECT tv_show.title, tv_show_genre_id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_show.id=tv_show_genres.genre_id;
