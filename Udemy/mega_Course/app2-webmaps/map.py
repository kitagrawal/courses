import folium
import pandas as pd


#-------adding the volcano data on the map with coloring and styling ------------
map = folium.Map(location=[40.76,-111.92], zoom_start=6, tiles="Mapbox Bright")
dataset = pd.read_csv("Volcanoes.txt")

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation <= 3000:
        return "orange"
    else:
        return "red"

html = """
Volcanp name: %s
Height: %s m
"""

fgv = folium.FeatureGroup(name = "Volcanoes")

for lat, lon, name, el in zip(list(dataset["LAT"]),list(dataset["LON"]),list(dataset["NAME"]),list(dataset["ELEV"])):
    iframe = folium.IFrame(html=html % (name,str(el)), width = 200, height = 100)
    fgv.add_child(folium.CircleMarker(location=[lat,lon],
                            popup=folium.Popup(iframe),radius = 6, fill_color=color_producer(el),
                            color='grey', fill_opacity=0.7)) #icon=folium.Icon(color=color_producer(el))))

fgp = folium.FeatureGroup(name = "Population")

# ----- drawing blue polygons bordering all countries (Choropleth maps)---------------
fgp.add_child(folium.GeoJson(data=open("world.json",'r', encoding = 'utf-8-sig').read(),
        style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
        else 'orange' if 10000000 <= x['properties']['POP2005'] <= 20000000
        else 'red'} ))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("tryMap.html")
