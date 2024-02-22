// Obtiene los datos desde la API
$(document).ready(() => {
    const hello = $('DIV#hello');
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  
    $.get(url, (data) => {
      hello.text(data.hello);
    });
  });
  