import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import *


#All of these values must have the same item count. 

#Initilize list for left side of graph
left = []
#Initilize list for data points of graph
height = []
#Initilize list for bottom of graph
tick_label = []
#Initilize colors of the bars
colors = []

count = 10

new_dict = { 'Marc': 45 , 'Jack' : 19 , 'Max' : 16}

for keys in new_dict:
	tick_label.append(keys)

for data in new_dict.values():
	height.append(data)
	left.append(count)
	count = count + 10
	if data < 40:
		colors.append('black')
	else:
		colors.append('green')

#print(tick_label)
#print(height)
#print(left) 
 


#set the size of the frame
plt.figure(figsize=(12, 12))

#takes the values from left, height, ticklabel and colors and biulds the graph
plt.bar(left, height, tick_label = tick_label,
        width = 6, color = colors)

#adds values to the tops of the bars
count2 = 10
for value in height:
     str_value = str(value)
     plt.text(count2, value + .5, str_value)
     count2 = count2 + 10

# Labels
plt.xlabel('Names')
plt.ylabel('Age')
plt.title('Ages')

#savename = '/graph.jpg'
#savename1 = savePath + savename
#plt.savefig(savename1, dpi = 300, bbox_inches = 'tight')
plt.show()
