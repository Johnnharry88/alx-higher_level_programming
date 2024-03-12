#!/usr/bin/node
exports.callMeMoby = function (b, theFunction) {
  for (let a = 1; a <= b; a++) {
    theFunction();
  }
};
