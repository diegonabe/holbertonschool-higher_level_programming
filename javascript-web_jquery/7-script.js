// Obtiene los datos del personaje desde la API
$(document).ready(() => {
    const textContainer = $('DIV#character');
    const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  
    $.get(url, (data) => {
      textContainer.text(data.name);
    });
  });
  