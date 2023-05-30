#!/bin/bash

filename="pokemon_list.txt"

for pokemon in $(cat "$filename")
do
  echo "pokemon: $pokemon"
  
  # make the api request
  response=$(curl -s "https://pokeapi.co/api/v2/pokemon-species/$pokemon")

  # save response to JSON file
  echo "$response" > "${pokemon}_response.json"

  echo "API response saved to ${pokemon}_response.json"

  # Pause for 2 seconds
  sleep 2

done