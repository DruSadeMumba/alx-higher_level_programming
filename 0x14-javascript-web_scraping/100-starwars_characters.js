#!/usr/bin/env node
const req = require('request');
const id = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${id}`;

req(apiUrl, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const data = JSON.parse(body);
    data.characters.forEach((url) => {
      req(url, (error, response, bodies) => {
        if (!error && response.statusCode === 200) {
          const character = JSON.parse(bodies);
          console.log(character.name);
        } else {
          console.log(error || response.statusCode);
        }
      });
    });
  } else {
    console.log(err || res.statusCode);
  }
});
