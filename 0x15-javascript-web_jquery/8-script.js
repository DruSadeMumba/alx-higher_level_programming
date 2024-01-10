$.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", (data) => {
  const listMovies = $('#list_movies');
  data.results.forEach((movie) => {
    listMovies.append($('<li>').text(movie.title));
  });
});
