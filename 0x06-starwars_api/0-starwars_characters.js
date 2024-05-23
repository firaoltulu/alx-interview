#!/usr/bin/node
const util = require('util');
const request = util.promisify(require('request'));
const filmID = process.argv[2];

async function starwarsCharacters(filmId) {
    const endpoint = 'https://swapi-api.hbtn.io/api/films/' + filmId;
    let response = await (await request(endpoint)).body;
    response = JSON.parse(response);
    const one = response.characters;

    for (let i = 0; i < one.length; i++) {
        const two = one[i];
        let three = await (await request(two)).body;
        three = JSON.parse(three);
        console.log(three.name);
    }
}

starwarsCharacters(filmID);