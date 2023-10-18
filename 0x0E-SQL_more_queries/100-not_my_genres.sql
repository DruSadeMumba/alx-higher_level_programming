-- A script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE title IS NULL OR title <> 'Dexter'
GROUP BY name
ORDER BY name ASC;
