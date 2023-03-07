#Taking the Data from the Website and put them in the variable stadtteile

import json
import urllib.request

url = "https://opendata.duesseldorf.de/sites/default/files/Wohnquartiere_ETRS89.geojson"

# Load the Data
response = urllib.request.urlopen(url)
data = json.loads(response.read())

# Get the coordinates
Stadtteile = []
for feature in data['features']:
    if feature['geometry']['type'] == 'Polygon':
        coordinates = feature['geometry']['coordinates'][0]
        for coordinate in coordinates:
            Stadtteile.append(coordinate)

# testing
if len(Stadtteile) > 0:
    print("Die Daten wurden erfolgreich abgespeichert.")
else:
    print("Fehler beim Abspeichern der Daten.")


#Now programming the Heatmap with folium

import folium
from folium.plugins import HeatMap


coordinates = Stadtteile

# Map
m = folium.Map(location=[51.225842, 6.768077], zoom_start=13)

# Heatmap
HeatMap(coordinates).add_to(m)

# safe the map
m.save("heatmap.html")
