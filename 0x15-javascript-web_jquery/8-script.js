// This script changes the header color to red
$(document).ready(function () {
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const movies = data.results;
    const moviesList = $('ul#list_movies');
    $.each(movies, function (index, movie) {
      const title = movie.title;
      moviesList.append('<li>' + title + '</li>');
    });
  });
});
