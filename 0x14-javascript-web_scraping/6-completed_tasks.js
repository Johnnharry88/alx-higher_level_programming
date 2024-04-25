#!/usr/bin/node

const request = require('request');
const urlx = process.argv[2];

request.get(urlx, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const completed = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!completed[todo.userId]) {
        completed[todo.userId] = 1;
      } else {
        completed[todo.userId] += 1;
      }
    }
  });
  console.log(completed);
});
