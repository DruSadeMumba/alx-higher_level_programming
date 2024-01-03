#!/usr/bin/node
const req = require('request');
const url = process.argv[2];

req(url, (err, res, body) => {
  if (res.statusCode !== 200 || err) {
    console.log(err || res.statusCode);
    process.exit(1);
  }
  try {
    const data = JSON.parse(body).results;
    const movies = data.filter((film) =>
      film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    );
    console.log(movies.length);
  } catch (err) {
    console.error(err.message);
    process.exit(1);
  }
});
