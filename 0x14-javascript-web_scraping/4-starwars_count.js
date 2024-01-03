#!/usr/bin/node
const req = require('request');
const url = process.argv[2];
const id = 18;

req(url, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const data = JSON.parse(body).results;
    const movies = data.filter((film) =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${id}/`)
    );
    console.log(movies.length);
  } else {
    console.error(err || res.statusCode);
    process.exit(1);
  }
});
