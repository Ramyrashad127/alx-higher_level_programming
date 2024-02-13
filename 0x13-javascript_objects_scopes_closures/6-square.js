#!/usr/bin/node
const Rectangle = require('./5-square');
module.exports = class Square extends Rectangle {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      let s = '';
      for (let i = 0; i < this.width; i++) {
        s += c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(s);
      }
    }
  }
};
