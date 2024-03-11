#!/usr/bin/node
const argx = process.argv.length;

if (argx > 2) {
  console.log('Argument' + (argx > 3 ? 's' : '') + ' found');
} else {
  console.log('No argument');
}
