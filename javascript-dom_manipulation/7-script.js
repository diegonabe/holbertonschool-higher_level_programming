fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    var films = data.results;
    var listMoviesElement = document.getElementById('list_movies');
    films.forEach(film => {
      var listItem = document.createElement('li');
      listItem.textContent = film.title;
      listMoviesElement.appendChild(listItem);
    });
  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
  });