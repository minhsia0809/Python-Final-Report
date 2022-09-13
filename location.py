import csv
import folium
import webbrowser
lati,longi = input('請輸入使用者座標：').split()
radi = float(input('請輸入欲查詢之半徑(公尺)：'))

fol = folium.Map(location=[lati,longi] , zoom_start=15)
fol.add_child(folium.Circle(location=[float(lati),float(longi)],
                             color='green', # Circle 顏色
                             radius=radi, # Circle 寬度
                             popup=[lati,longi], # 彈出視窗內容
                             fill=True, # 填滿中間區域
                             fill_opacity=0.5 # 設定透明度
                             ))
with open("private.csv", 'r',encoding="utf-8") as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        name = row['收費標準']
        type = row['型式']
        longitude = row['經度']
        latitude = row['緯度']

        if(type == '建物平面'):
            fol.add_child(folium.Marker(location=[float(latitude),float(longitude)],  
                                      popup=name ,
                                      icon=folium.Icon(color='purple') ))
        if(type == '建物立體'):
            fol.add_child(folium.Marker(location=[float(latitude),float(longitude)],  
                                      popup=name,
                                      icon=folium.Icon(color='blue') ))
        if(type == '平面'):
            fol.add_child(folium.Marker(location=[float(latitude),float(longitude)],  
                                      popup=name,
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
                                      popup=name, 
                                      icon=folium.Icon(color='orange')))
        if(type == '立體'):
            fol.add_child(folium.Marker(location=[float(latitude),float(longitude)],  
                                      popup=name,
                                      icon=folium.Icon(color='red') ))
        if(type == '路邊'):
            fol.add_child(folium.Marker(location=[float(latitude),float(longitude)],  
                                      popup=name,
                                      icon=folium.Icon(color='pink') ))


fol.save("test.html")
webbrowser.open("test.html")