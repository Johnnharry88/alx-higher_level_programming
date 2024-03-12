#!/usr/bin/node
function sum (x, y) {
  return x + y;
}
console.log(sum(Number(process.argv[2]), Number(process.argv[3])));
