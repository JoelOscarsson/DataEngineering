#!/bin/bash

filename="pokemon_list.txt"

for pokemon in $(cat "$filename")
do
  echo "pokemon: $pokemon"
done
