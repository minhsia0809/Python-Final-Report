# -*- coding: utf-8 -*-
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.transform import dodge
import csv
num1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
num2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
list = ['三民區','大社區','大寮區','大樹區','小港區','仁武區','左營區','永安區','田寮區','甲仙區','杉林區','岡山區','林園區','阿蓮區','前金區','前鎮區','美濃區','苓雅區','茄萣區','梓官區','鳥松區','湖內區','新興區','楠梓區','路竹區','鼓山區','旗山區','旗津區','鳳山區','橋頭區','彌陀區','鹽埕區']
f1 = open("public.csv", 'r',encoding="utf-8")
for row in csv.reader(f1):
    for i in range(0,32):
        if(row[0] == list[i]):
            num1[i] = num1[i] + 1
f2 = open("private.csv", 'r',encoding="utf-8")
for row in csv.reader(f2):
    for i in range(0,32):
        if(row[1] == list[i]):
            num2[i] = num2[i] + 1

output_file("All_ParkingLot_Counts.html")

All_P = []
counts1 = []
counts2 = []
counts3 = []
for i in range(0,32):
    All_P.append(list[i])
    counts1.append(num1[i])
    counts2.append(num2[i])
    counts3.append(num1[i] + num2[i])

type = ['公有', '民營', '總數']

data = {'All_P' : All_P,
        '公有'   : counts1,
        '民營'   : counts2,
        '總數'   : counts3}

source = ColumnDataSource(data=data)

p = figure(x_range=All_P, y_range=(0, 10), plot_height=350, title="高雄市各地區所有停車場數量",
           toolbar_location=None, tools="")

p.vbar(x=dodge('All_P', -0.25, range=p.x_range), top='公有', width=0.2, source=source,
       color="#c9d9d3", legend_label="公有")

p.vbar(x=dodge('All_P',  0.0,  range=p.x_range), top='民營', width=0.2, source=source,
       color="#718dbf", legend_label="民營")

p.vbar(x=dodge('All_P',  0.25, range=p.x_range), top='總數', width=0.2, source=source,
       color="#e84d60", legend_label="總數")

p.y_range.start = 0
p.y_range.end = 180
p.x_range.range_padding = 0.05
p.xgrid.grid_line_color = None
p.xaxis.major_label_orientation = 1.2
p.outline_line_color = None

show(p)

f1.close()
f2.close()
