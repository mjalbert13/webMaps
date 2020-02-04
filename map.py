import folium

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles= "Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

for coordinates in [[38.1,-99.1], [37.4, -98.9]]:
    fg.add_child(folium.Marker(location=coordinates, popup="hello world", icon=folium.Icon(color="green")))
map.add_child(fg)
map.save("map1.html")
