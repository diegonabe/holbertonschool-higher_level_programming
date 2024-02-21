// JS script que Añade la classe red al elemento header cuando el usuario da click al elemento div#red
$(document).ready(() => {

    const headerElement = $('header');
  
    $('DIV#red_header').click(() => {
      headerElement.addClass('red');
    });
  });