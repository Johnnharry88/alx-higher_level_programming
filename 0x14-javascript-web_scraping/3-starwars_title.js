#!/usr/bin/node

const request = require('request');
const id_move = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id_move;

request.get (url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const file = JSON.parse(body);
    console.log(file.title);
  }
});
