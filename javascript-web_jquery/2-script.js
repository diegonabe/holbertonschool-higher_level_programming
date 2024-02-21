// Js Script que cambia el color a rojo cuando se hace click en el elementos div#red_header
$(document).ready(() => {

    const headerElement = $('header');
  
    $('DIV#red_header').click(() => {
      headerElement.css('color', '#FF0000');
    });
  });