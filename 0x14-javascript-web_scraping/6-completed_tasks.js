#!/usr/bin/node
const req = require('request');
const url = process.argv[2];

req(url, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const data = JSON.parse(body);
    const complete = {};

    data.forEach((todo) => {
      if (todo.completed) {
        const id = todo.userId;
        complete[id] = (complete[id] || 0) + 1;
      }
    });
    console.log(complete);
  } else {
    console.log(err || res.statusCode);
  }
});
