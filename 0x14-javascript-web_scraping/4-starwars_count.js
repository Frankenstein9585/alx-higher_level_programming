#!/usr/bin/node
const request = require('request');

function getCharacterCount (apiUrl, characterId) {
  request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error occurred while making GET request:');
      console.error(error);
    } else {
      const movieData = JSON.parse(body).results;
      const moviesWithCharacter = movieData.filter((film) => {
        return film.characters.some((characterUrl) => {
          return characterUrl.includes(characterId);
        });
      });
      console.log(moviesWithCharacter.length);
    }
  });
}

const apiUrl = process.argv[2];
const characterId = '18';
getCharacterCount(apiUrl, characterId);
