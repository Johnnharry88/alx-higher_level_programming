#!/usr/bin/node
const alx = require('fs');
const x = alx.readFileSync(process.argv[2], 'utf8');
const b = alx.readFileSync(process.argv[3], 'utf8');
alx.writeFileSync(process.argv[4], x + b);
