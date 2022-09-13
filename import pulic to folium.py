import csv
import folium
import webbrowser

m = folium.Map(location=[22.6384542,120.3019452] , zoom_start=11)

#m.add_child(folium.Marker(location=[22.5027529, 120.3958744],
#                             popup='立體'))
with open('public.csv', newline='',encoding="utf-8") as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        #print(row)
        print(row['型式'],"[",row['座標-經度'],",",row['座標-緯度'],"]")
        
        name = row['收費標準']
        type = row['型式']
        longitude = row['座標-經度']
        latitude = row['座標-緯度']
        

        if(type == '平面'):
            m.add_child(folium.Marker(location=[float(latitude),float(longitude)],  
                                      popup=name ))
        if(type == '立體'):
            m.add_child(folium.Marker(location=[float(latitude),float(longitude)],  
                                      popup=name,
                                      icon=folium.Icon(color='red') ))
        if(type == '路邊'):
            m.add_child(folium.Marker(location=[float(latitude),float(longitude)],  
                                      popup=name,
                                      icon=folium.Icon(color='pink') ))

m.save("test.html")
webbrowser.open("test.html")
        