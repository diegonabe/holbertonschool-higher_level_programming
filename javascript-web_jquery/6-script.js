// Actualiza el texto del elemento <header> a '¡Nuevo encabezado!!!' cuando el usuario hace clic en el elemento 'div#update_header'
$(document).ready(() => {
    const headerElement = $('header');
  
    $('DIV#update_header').click(() => {
      headerElement.text('¡Nuevo encabezado!!!');
    });
  });
  