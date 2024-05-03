const hdElem = $('header');
const updatehdElem = $('div#update_header');

updatehdElem.on('click', () => {
  hdElem.text('New header!!!');
});
