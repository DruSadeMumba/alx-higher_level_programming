#!/usr/bin/node
const req = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

req(url, (err, res, body) => {
  if (res.statusCode !== 200) {
    console.log(res.statusCode);
    process.exit(1);
  }
  try {
    const data = JSON.parse(body);
    console.log(data.title);
  } catch (err){
    console.error(err.message);
    process.exit(1);
  }
});
