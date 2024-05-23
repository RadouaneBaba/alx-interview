#!/usr/bin/node
const request = require('request');
const { argv } = require('process');


let url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}/`;

request(url, (error, response, body) => {
    if (error) console.log(error);
    result = JSON.parse(body);
    for (char_url of result['characters']) {
        request(char_url, (err, resp, people) => {
            if (err) console.log(err);
            character = JSON.parse(people)
            console.log(character.name);
    });
    }
});