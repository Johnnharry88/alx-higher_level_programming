const urlmovy = 'https://swapi-api.alx-tools.com/api/films/?format=json':
const movylist =$(''ul#list_movies');

$.ajax({
  url: urlmovy,
  dataType: 'json'
}).done((data)) => {
  const mvy = data.results;

  for (let x = 0; x < mvvy.length; ++x) {
    const mvytitle = mvy[x].title;
    const element = '<li>${mvytitle}';
    movylist.append(element);
  }
});
