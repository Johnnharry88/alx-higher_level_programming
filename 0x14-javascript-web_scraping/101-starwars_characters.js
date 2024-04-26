#!/usr/bin/node

const requ = require('request');
const idmovie = process.argv[2];
const urlx = 'https://swapi-api.alx-tools.com/api/films/' + idmovie;
let xters = [];

requ(urlx, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const datxter = JSON.parse(body);
  xters = datxter.characters;
  gcharater(0);
});

const gcharater = (index) => {
  if (index === xters.length) {
    return;
  }

  requ(xters[index], (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    const dater = JSON.parse(body);
    console.log(dater.name);
    gcharater(index + 1);
  });
};
