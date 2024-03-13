#!/usr/bin/node
let alx = 0;
exports.logMe = function (item) {
  console.log(alx + ': ' + item);
  alx = alx + 1;
};
