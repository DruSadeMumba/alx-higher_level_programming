#!/usr/bin/env node

let count = process.argv.slice(2)[0];
if (isNaN(count) || typeof count === 'undefined') {
  console.log('Missing number of occurrences');
} else {
  count = parseInt(process.argv.slice(2)[0], 10);
  for (let i = 0; i < count; i++) {
    console.log('C is fun');
  }
}
