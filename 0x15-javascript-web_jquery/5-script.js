const listEle = $('ul.my_list');
const Additem = $('div#add_item');

Additem.on('click', () => {
  listEle.append('<li> Item</li>');
});
