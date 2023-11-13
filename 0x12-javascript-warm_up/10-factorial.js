#!/usr/bin/node

function factorial (n) {
  if (n < 0) {
    return -1;
  }
  if (n === 0 || isNaN(n)) {
    return 1;
  }
  return n * factorial(n - 1);
}

const num = parseInt(process.argv.slice(2)[0]);
console.log(factorial(num));
