import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

tables = soup.find_all("table")

table = tables[2]  
rows = table.find_all("tr")

star_names = []
radii = []
masses = []
distances = []


for row in rows:
    data = row.find_all("td")
    if len(data) == 0:
        continue
    star_names.append(data[0].text.strip())
    radii.append(data[7].text.strip())
    masses.append(data[8].text.strip())
    distances.append(data[9].text.strip())


data = {
    "Star Name": star_names,
    "Radius": radii,
    "Mass": masses,
    "Distance": distances
}

df = pd.DataFrame(data)

df.to_csv("dwarf_stars.csv", index=False)
