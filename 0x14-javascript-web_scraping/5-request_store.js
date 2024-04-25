#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url_x = process.argv[2];
const file_x = process.argv[3];

request(url_x, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(file_x, body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
