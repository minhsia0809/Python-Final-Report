import csv
with open('public.csv', newline='',encoding="utf-8") as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        #print(row)
        print(row['停車場名稱'],row['型式'],"[",row['座標-經度'],",",row['座標-緯度'],"]")