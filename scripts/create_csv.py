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


def createtocsv(filename):

# create a seg-y manipulator
    seg = survey_reader(filename)

# create a group of traces from seg-y
    rad_img = radargram(seg.get_traces())

# extracte some traces
    rad_sample  = rad_img.read_trace([0,-1,10]) 
    gps_sample  = rad_img.read_position_meter([0,-1,10])



    test = rad_sample.T

    valeurs = [""]*len(test)

    for i in range(len(test)):
        print(i)
        valeurs[i]= [i,gps_sample[1][i], gps_sample[0][i], gps_sample[2][i], test[i]]





    entetes = [
        u'Trace',
        u'X',
        u'Y',
        u'Z',
        u'Valeurs',
        ]


    f = open('DAT_0001.csv', 'w')
    ligneEntete = ";".join(entetes) + "\n"
    writer = csv.writer(f, delimiter=";")
    f.write(ligneEntete)    
    writer.writerows(valeurs)

    f.close()


