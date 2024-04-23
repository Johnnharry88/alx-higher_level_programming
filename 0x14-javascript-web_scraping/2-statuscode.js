#!/usr/bin/node
const request = require('request');
const url_used = process.argv[2];

request.get(url_used, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ${response.statusCode}');
  }
});
