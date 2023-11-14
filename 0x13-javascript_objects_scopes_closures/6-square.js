#!/usr/bin/node

const Sq = require('./5-square');

module.exports = class Square extends Sq {
  charPrint (c = 'X') {
    console.log(Array(this.height).fill(c.repeat(this.width)).join('\n'));
  }
};
