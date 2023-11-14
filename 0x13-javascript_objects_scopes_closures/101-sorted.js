#!/usr/bin/node

const { dict } = require('./101-data');
const occurUId = {};

for (const uId in dict) {
  const occur = dict[uId];
  if (occurUId[occur] === undefined) {
    occurUId[occur] = [uId];
  } else {
    occurUId[occur].push(uId);
  }
}

console.log(occurUId);
