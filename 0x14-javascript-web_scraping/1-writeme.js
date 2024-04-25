#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];
const cont = process.argv[3];

fs.writeFile(filename, cont, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
