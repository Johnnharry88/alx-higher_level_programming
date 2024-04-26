#!/usr/bin/node

const request = require('request');
const idmovie = process.argv[2];
const urlx = 'https://swapi-api.alx-tools.com/api/films/' + idmovie;

request.get(urlx, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const nput = JSON.parse(body);
  const characters = nput.characters;
  for (const character of characters) {
    request(character, (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      const datater = JSON.parse(body);
      console.log(datater.name);
    });
  }
});
