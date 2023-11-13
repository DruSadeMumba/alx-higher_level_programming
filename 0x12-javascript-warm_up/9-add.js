#!/usr/bin/node

function add (a, b) {
  return (a + b);
}

const int1 = parseInt(process.argv.slice(2)[0]);
const int2 = parseInt(process.argv.slice(2)[1]);

console.log(add(int1, int2));
