#!/usr/bin/node

const arg = process.argv.slice(2)[0];
if (isNaN(arg) || typeof arg === "undefined") {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(arg, 10));
}
