#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const idxter = '10';
let rec = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const input = JSON.parse(body);
    input.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(idxter)) {
          rec = rec + 1;
        }
      });
    });
    console.log(rec);
  }
});
