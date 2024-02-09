//JavaScript que alterna la clase del Elemento Header entre
//rojo y verde.

var toggleElementHeader = document.getElementById('toggle_header');

toggleElementHeader.addEventListener('click', function(){
    var headerElement = document.querySelector('header');
    if (headerElement.classList.contains('red')) {
        headerElement.classList.remove('red');
        headerElement.classList.add('green');
    } else if (headerElement.classList.contains('green')) {
        headerElement.classList.remove('green');
        headerElement.classList.add('red');
    } else {
        headerElement.classList.add('red');
    }
});