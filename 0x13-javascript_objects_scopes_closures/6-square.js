#!/usr/bin/node

const Sq = require('./5-square');

class Square extends Sq {
  charPrint (c = 'X') {
    console.log(Array(this.height).fill(c.repeat(this.width)).join('\n'));
  }
}

module.exports = Square;
