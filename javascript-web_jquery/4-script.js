// Alterna las clases 'red' y 'green' en el elemento <header> cuando el usuario hace clic en el elemento 'div#toggle_header'
$(document).ready(() => {

    const headerElement = $('header');
    
    $('DIV#toggle_header').click(() => {
    headerElement.toggleClass('red green');
    });
    });