# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 15:44:20 2017

@author: tellus_user2
"""


from tellus_tools.survey_reader import survey_reader
from tellus_tools.radar_tools import *
import matplotlib.pyplot as plt
import os 
import csv
import json

filename = "DAT_0001.sgy"

# create a seg-y manipulator
seg = survey_reader(filename)

# create a group of traces from seg-y
rad_img = radargram(seg.get_traces())

# extracte some traces
rad_sample  = rad_img.read_trace([0,-1,2]) 
gps_sample  = rad_img.read_position_meter([0,-1,2])



valeurs = [""]*len(test)

for i in range(len(test)):
    print(i)
    valeurs[i]= [gps_sample[0][i], gps_sample[1][i], gps_sample[2][i], test[i]]

text = ""
for i in range(len(test)): 
    print(i)
    if i == 0:
        vaj = '{"Trace":  "GPS":{"X":'+str(gps_sample[1][i])+', "Y":'+str(gps_sample[0][i])+',"Z":'+str(gps_sample[2][i])+'}, "Value":{"values":'+str(test[i])+'} }'
    elif i == len(test)-1:
        vaj = '"Trace": "GPS":{"X":'+str(gps_sample[1][i])+', "Y":'+str(gps_sample[0][i])+',"Z":'+str(gps_sample[2][i])+'}, "Value":{"values":'+str(test[i])+'} }}'
    else:
        vaj = '"Trace": "GPS":{"X":'+str(gps_sample[1][i])+', "Y":'+str(gps_sample[0][i])+',"Z":'+str(gps_sample[2][i])+'}, "Value":{"values":'+str(+test[i])+'} } '
    text = text+vaj

print(text)
with open('DAT_0001.json', 'w') as f:
     json.dump(text, f)
    
    

