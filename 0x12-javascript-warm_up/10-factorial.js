#!/usr/bin/node
function factoria (x) {
  return x === 0 || isNaN(x) ? 1 : x * factoria(x - 1);
}
console.log(factoria(Number(process.argv[2])));
