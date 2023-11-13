#!/usr/bin/node

const count = process.argv.slice(2)[0];
if (!count) {
  console.log('No argument');
} else if (count) {
  console.log(count);
}
