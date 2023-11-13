#!/usr/bin/node

let count = process.argv.slice(2)[0];
if (isNaN(count) || typeof count === 'undefined') {
  console.log('Missing number of occurrences');
} else {
  count = parseInt(count, 10);
  for (let i = 0; i < count; i++) {
    console.log('X'.repeat(count));
  }
}
