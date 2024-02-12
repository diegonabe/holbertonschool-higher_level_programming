fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(response => response.json())
  .then(data => {
    var helloElement = document.getElementById('hello');
    helloElement.textContent = data.hello;
  })
  .catch(error => {
    console.error('Hubo un problema con la solicitud fetch:', error);
  });
