import csv
import folium
import webbrowser

fol = folium.Map(location=[22.6384542,120.3019452] , zoom_start=11)
with open("private.csv", 'r',encoding="utf-8") as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        name = row['收費標準']
        type = row['型式']
        longitude = row['經度']
        latitude = row['緯度']

        if(type == '建物平面'):
            fol.add_child(folium.Marker(location=[float(latitude),float(longitude)],  
                                      popup=folium.Popup( html = name , parse_html = False , max_width = '500' , show = False),
                                      tooltip = [float(latitude),float(longitude)],
                                      icon=folium.Icon(color='purple') ))
        if(type == '建物立體'):
            fol.add_child(folium.Marker(location=[float(latitude),float(longitude)],  
                                      popup=folium.Popup( html = name , parse_html = False , max_width = '500' , show = False),
                                      tooltip = [float(latitude),float(longitude)],
                                      icon=folium.Icon(color='blue') ))
        if(type == '平面'):
            fol.add_child(folium.Marker(location=[float(latitude),float(longitude)],  
                                      popup=folium.Popup( html = name , parse_html = False , max_width = '500' , show = False),
                                      tooltip = [float(latitude),float(longitude)],
                                      icon=folium.Icon(color='black') ))

                           

with open('public.csv', newline='',encoding="utf-8") as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        #print(row)
        #print(row['型式'],"[",row['座標-經度'],",",row['座標-緯度'],"]")
        
        name = row['收費標準']
        type = row['型式']
        longitude = row['座標-經度']
        latitude = row['座標-緯度']
        

        if(type == '平面'):
            fol.add_child(folium.Marker(location=[float(latitude),float(longitude)],  
                                      popup=folium.Popup( html = name , parse_html = False , max_width = '500' , show = False),
                                      tooltip = [float(latitude),float(longitude)] ,
                                      icon=folium.Icon(color='orange')))
        if(type == '立體'):
            fol.add_child(folium.Marker(location=[float(latitude),float(longitude)],  
                                      popup=folium.Popup( html = name , parse_html = False , max_width = '500' , show = False),
                                      tooltip = [float(latitude),float(longitude)],
                                      icon=folium.Icon(color='red') ))
        if(type == '路邊'):
            fol.add_child(folium.Marker(location=[float(latitude),float(longitude)],  
                                      popup=folium.Popup( html = name , parse_html = False , max_width = '500' , show = False),
                                      tooltip = [float(latitude),float(longitude)],
                                      icon=folium.Icon(color='pink') ))

fol.save("test.html")
webbrowser.open("test.html")
        