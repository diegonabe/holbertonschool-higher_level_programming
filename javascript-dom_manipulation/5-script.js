//JavaScript que actualiza el elemento header
//a new header cuando se hace click en id update_header

var updateHeader = document.getElementById('update_header');

updateHeader.addEventListener('click', function(){
    var selectHeader = document.querySelector('header');
    selectHeader.textContent = 'New Header!!!';
});