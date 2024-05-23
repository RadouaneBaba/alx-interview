#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}/`;

function makeRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(body);
      }
    });
  });
}

async function printCharacters () {
  const characters = await makeRequest(url);
  for (const charUrl of JSON.parse(characters).characters) {
    const people = await makeRequest(charUrl);
    const character = JSON.parse(people);
    console.log(character.name);
  }
}

printCharacters();
