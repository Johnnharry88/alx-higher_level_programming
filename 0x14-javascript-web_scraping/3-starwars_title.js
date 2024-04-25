#!/usr/bin/node

const request = require('request');
const idmove = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + idmove;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const file = JSON.parse(body);
    console.log(file.title);
  }
});
