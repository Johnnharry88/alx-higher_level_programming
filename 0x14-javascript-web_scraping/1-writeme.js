#!/usr/bin/node

const fs = require('fs');
const file_name = process.argv[2];
const cont = process.argv[3];

fs.writeFile(file_name, cont, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
