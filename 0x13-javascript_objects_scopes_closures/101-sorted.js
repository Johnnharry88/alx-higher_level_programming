#!/usr/bin/node
const dict = require('./101-data.js').dict;
let n_dict = {};
for (let k in dict) {
  if (n_dict[dict[k]] === undefined) {
    n_dict[dict[k]] = [k];
  } else {
    n_dict[dict[k]].push(k);
  }
}
console.log(n_dict);
