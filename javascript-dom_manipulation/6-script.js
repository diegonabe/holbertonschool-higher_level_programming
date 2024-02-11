// Hacer una solicitud GET a la URL del API de Star Wars
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => {
    // Verificar si la respuesta es exitosa
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    // Convertir la respuesta a formato JSON
    return response.json();
  })
  .then(data => {
    // Obtener el nombre del personaje del objeto JSON
    var characterName = data.name;
    // Seleccionar el elemento con el ID "character"
    var characterElement = document.getElementById('character');
    // Asignar el nombre del personaje al contenido del elemento
    characterElement.textContent = characterName;
  })
  .catch(error => {
    // Manejar cualquier error de la solicitud
    console.error('There was a problem with the fetch operation:', error);
  });
