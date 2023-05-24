#!/usr/bin/node
const request = require('request');

function getTitle (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
  request.get(url, (error, response, body) => {
    if (error) {
      console.error('Error occurred while making GET request:');
      console.error(error);
    } else {
      const movieData = JSON.parse(body);
      console.log(movieData.title);
    }
  });
}

const movieId = process.argv[2];
getTitle(movieId);
