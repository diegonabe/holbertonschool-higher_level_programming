// Añade un nuevo elemento de lista a 'unorderList' cuando el usuario hace clic en el elemento 'div#add_item'
$(document).ready(() => {

    const unorderList = $('UL.my_list');
  
    $('DIV#add_item').click(() => {
      const listItem = '<li>Item</li>';
      unorderList.append(listItem);
    });
  });
  