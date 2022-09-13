# -*- coding: utf-8 -*-
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.transform import dodge
import csv
num1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
num2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
num3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
list = ['三民區','大社區','大寮區','大樹區','小港區','仁武區','左營區','永安區','田寮區','甲仙區','杉林區','岡山區','林園區','阿蓮區','前金區','前鎮區','美濃區','苓雅區','茄萣區','梓官區','鳥松區','湖內區','新興區','楠梓區','路竹區','鼓山區','旗山區','旗津區','鳳山區','橋頭區','彌陀區','鹽埕區']
f = open("private.csv", 'r',encoding="utf-8")
for row in csv.reader(f):
    for i in range(0,32):
        if(row[1] == list[i]):
            num3[i] = num3[i] + 1
            if(row[2] == '平面' or row[2] == '建物平面'):
                num2[i] = num2[i] + 1
            elif(row[2] == '建物立體'):
                num1[i] = num1[i] + 1

output_file("Private_ParkingLot_Counts.html")

Private_P = []
counts1 = []
counts2 = []
counts3 = []
for i in range(0,32):
    Private_P.append(list[i])
    counts1.append(num1[i])
    counts2.append(num2[i])
    counts3.append(num3[i])

type = ['立體', '平面', '總數']

data = {'Private_P' : Private_P,
        '立體'   : counts1,
        '平面'   : counts2,
        '總數'   : counts3}

source = ColumnDataSource(data=data)

p = figure(x_range=Private_P, y_range=(0, 10), plot_height=350, title="高雄市各地區民營停車場數量",
           toolbar_location=None, tools="")

p.vbar(x=dodge('Private_P', -0.25, range=p.x_range), top='立體', width=0.2, source=source,
       color="#c9d9d3", legend_label="立體")

p.vbar(x=dodge('Private_P',  0.0,  range=p.x_range), top='平面', width=0.2, source=source,
       color="#718dbf", legend_label="平面")

p.vbar(x=dodge('Private_P',  0.25, range=p.x_range), top='總數', width=0.2, source=source,
       color="#e84d60", legend_label="總數")

p.y_range.start = 0
p.y_range.end = 200
p.x_range.range_padding = 0.05
p.xgrid.grid_line_color = None
p.xaxis.major_label_orientation = 1.2
p.outline_line_color = None

show(p)

f.close()

