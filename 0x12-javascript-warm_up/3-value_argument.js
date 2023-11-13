#!/usr/bin/env node

const count = process.argv.slice(2);
if (!count[0]) {
  console.log('No argument');
} else if (count[0]) {
  console.log(count[0]);
}
