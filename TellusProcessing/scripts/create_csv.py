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


filename = "DAT_0001.sgy"

# create a seg-y manipulator
seg = survey_reader(filename)

# create a group of traces from seg-y
rad_img = radargram(seg.get_traces())

# extracte some traces
rad_sample  = rad_img.read_trace([0,-1,2]) 
gps_sample  = rad_img.read_position_meter([0,-1,2])


# algo 1
auto_G = auto_gain()
G  = 1/(np.exp(-0.8*np.linspace(0.05,7,350)))
auto_G.parameter =G
auto_G.process(rad_sample)


test = rad_sample.T
# result show
plt.figure("radargramme")
plt.subplot(211)
plt.imshow( rad_sample , interpolation='nearest', aspect='auto' ) 
plt.subplot(212)
plt.plot(test[67])
plt.show()
print(gps_sample[0][0])
print(gps_sample[0][64])
print(gps_sample[0][65])
print(gps_sample[0][66])
print(gps_sample[0][67])
print(len(test))
print(len(gps_sample[0]))
print(len(gps_sample[1]))
print(len(gps_sample[2]))

valeurs = [""]*len(test)

for i in range(len(test)):
    print(i)
    valeurs[i]= [gps_sample[0][i], gps_sample[1][i], gps_sample[2][i], test[i]]





entetes = [
     u'X',
     u'Y',
     u'Z',
     u'Valeurs',
]

#valeurs = [
#
#     [gps_sample[0][0], gps_sample[1][0], gps_sample[2][0], test[0]],
#     [u'Valeur6', u'Valeur7', u'Valeur8', u'Valeur9', u'Valeur10'],
#     [u'Valeur11', u'Valeur12', u'Valeur13', u'Valeur14', u'Valeur15']
#]


f = open('DAT_0001.csv', 'w')
ligneEntete = ";".join(entetes) + "\n"
writer = csv.writer(f, delimiter=";")
f.write(ligneEntete)    
writer.writerows(valeurs)

f.close()



plt.imshow( auto_G.data_out , interpolation='nearest', aspect='auto' )