#!/usr/bin/env node
const req = require('request');
const url = process.argv[2]

req(url, (err, res) => {
  console.log(err || `code: ${res.statusCode}`)
});
