#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduceRight(function (array, currt) {
    array.push(currt);
    return array;
  }, []);
};
