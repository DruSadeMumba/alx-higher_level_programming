#!/usr/bin/node
const req = require('request');
const url = process.argv[2];

req(url, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const data = JSON.parse(body).results;
    const movies = data.filter((film) =>
      film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    );
    console.log(movies.length);
  } else {
    console.log(err || res.statusCode);
  }
});
