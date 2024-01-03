#!/usr/bin/node
const req = require('request');
const id = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${id}`;

const getChar = (url) => {
  return new Promise((resolve, reject) => {
    req(url, (error, response, charBody) => {
      if (!error && response.statusCode === 200) {
        const character = JSON.parse(charBody);
        resolve(character.name);
      } else {
        reject(error || response.statusCode);
      }
    });
  });
}

req(apiUrl, async (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const data = JSON.parse(body);
    const chars = await Promise.all(data.characters.map(getChar));
    chars.forEach((charName) => {
      console.log(charName);
    });
  } else {
    console.error(err || res.statusCode);
  }
});
