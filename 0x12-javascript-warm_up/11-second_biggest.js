#!/usr/bin/env node

const nums = process.argv.slice(2).map(Number);
if (nums.length <= 1) {
  console.log(0);
} else {
  const sortNums = nums.sort((a, b) => b - a)[1];
  console.log(sortNums);
}
