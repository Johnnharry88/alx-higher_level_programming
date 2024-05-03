const urlcharacter = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
const divcharacter = $('div#character');

$.ajax({
  url: urlcharacter,
  dataType: 'json'
}).done((data) => {
  divcharacter.text(data.name);
});
