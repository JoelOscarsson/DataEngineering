#!/bin/bash

pokemon_list="data/pokemons/pokemon_list.txt"
pokemon_data_dir="data/pokemons"

# mkdir -p "$pokemon_data_dir"

while IFS= read -r pokemon
do
  # Check if the pokemon data file already exists
  if [ -f "$pokemon_data_dir/$pokemon.json" ]; then
    echo "Skipping $pokemon, data file already exists."
  else
    touch "$pokemon_data_dir/$pokemon.json"
    echo "Downloaded $pokemon."
  fi
done < "$pokemon_list"


