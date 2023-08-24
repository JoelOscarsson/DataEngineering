import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Pokémon list website
url = "https://sv.wikipedia.org/wiki/Lista_över_Pokémon"

# Send an HTTP GET request to fetch the page content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    print(soup)
    # Find all the rows (adjust the CSS selector based on the actual structure)
    rows = soup.select(".pokemon-row")

    # Initialize lists to store data
    engelskt_namn = []
    japanskt_namn = []
    pokedex_nummer = []
    typ = []

    # Loop through each row and extract data
    for row in rows:
        columns = row.find_all("td")
        engelskt_namn.append(columns[0].text.strip())
        japanskt_namn.append(columns[1].text.strip())
        pokedex_nummer.append(columns[2].text.strip())
        typ.append(columns[3].text.strip())

    # Create a DataFrame from the scraped data
    pokemon_df = pd.DataFrame({
        "EngelsktNamn": engelskt_namn,
        "JapansktNamn": japanskt_namn,
        "PokedexNummer": pokedex_nummer,
        "Typ": typ
    })

    # Print the DataFrame
    print(pokemon_df)
else:
    print("Failed to fetch the website:", response.status_code)

print(pokemon_df)