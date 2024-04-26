#!/usr/bin/node

const requaest = require('request');
const idmovie = process.argv[2];
const url = 'https://swapi.dev/api/films/' + idmovie;

requaest.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const nput = JSON.parse(body);
  const characters = nput.characters;
  for (const character of characters) {
    requaest(character, (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      const datater = JSON.parse(body);
      console.log(datater.name);
    });
  }
});
