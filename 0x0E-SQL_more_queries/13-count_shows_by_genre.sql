-- A script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT tv_show_genres.name AS genre,
COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres
GROUP BY genre
ORDER BY number_of_shows DESC;
