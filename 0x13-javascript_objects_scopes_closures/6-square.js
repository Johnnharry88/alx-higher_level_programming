#!/usr/bin/node
module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let y = 0; y < this.height; y++) console.log(c.repeat(this.width));
    }
  }
};
