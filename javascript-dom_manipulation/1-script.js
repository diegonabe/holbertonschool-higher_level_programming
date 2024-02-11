//JavaScript que actualiza el color del texto del encabezado a rojo
//cuando el usuario hace click al elemento con el ID "red_header"

var redHeaderElement = document.getElementById('red_header');

redHeaderElement.addEventListener('click', function(){
    var paintRed = document.querySelector('header');
    paintRed.style.color = '#FF0000';
});
