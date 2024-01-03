#!/usr/bin/node
const req = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

req(url, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf-8', (error) => {
      if (error) console.log(error);
    });
  } else {
    console.log(err || res.statusCode);
  }
});
