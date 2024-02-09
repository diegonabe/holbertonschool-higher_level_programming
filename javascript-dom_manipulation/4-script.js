//JavaScript que agrega un elemento <li> a una lista
//cuando hace clic en el id "add_item"

var addElement = document.getElementById("add_item");

addElement.addEventListener('click', function(){
    var newItem = document.createElement('li');
    newItem.textContent = 'Item';
    var myList = document.querySelector('.my_list');
    myList.appendChild(newItem);
});