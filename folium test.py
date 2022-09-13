import folium
import webbrowser

m = folium.Map(location=[22.6384542,120.3019452] , zoom_start=11)
m.add_child(folium.Marker(location=[22.5027529, 120.3958744],
                             popup='立體'))
m.save("test.html")
webbrowser.open("test.html")