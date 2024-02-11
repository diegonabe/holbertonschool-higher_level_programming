//JavaScript que agrega la clase red al elemento de encabezado
//cuando el usuario hace clic en el elemento con el ID "red_header"

var redHeaderElement = document.getElementById('red_header');

redHeaderElement.addEventListener('click', function(){
    var paintRed = document.querySelector('header');
    paintRed.classList.add('red');
});