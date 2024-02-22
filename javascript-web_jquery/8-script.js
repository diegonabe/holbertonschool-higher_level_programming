// Obtiene los datos de las películas desde la API
$(document).ready(() => {
    const unorderedList = $('UL#list_movies');
    const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  
    $.get(url, (data) => {
      data.results.forEach((movie) => {
        unorderedList.append(`<li>${movie.title}</li>`);
      });
    });
  });
  