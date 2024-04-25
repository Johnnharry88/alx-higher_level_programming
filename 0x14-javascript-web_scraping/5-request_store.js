#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const urlx = process.argv[2];
const filex = process.argv[3];

request(urlx, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filex, body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
