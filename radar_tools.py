#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 14:07:59 2017

@author: tellus_user2
"""


import numpy as np

from decimal import *            



            
from pyproj import Proj, transform   
        
def Reproj(X,Y, Elevation= None, fromESPG =None, toESPG= None, Print = None):
  if fromESPG is None:
     fromESPG = Proj(init='epsg:4326',preserve_units=True)
  else: 
     fromESPG = Proj(init='epsg:'+str(fromESPG),preserve_units=True)
  if toESPG is None:   
     toESPG   = Proj(init='epsg:2154')
  else:
     toESPG = Proj(init='epsg:'+str(toESPG),preserve_units=True)
  if Print ==1:
      print("from : ",fromESPG," to :", toESPG)
  if Elevation is None:
     return transform(fromESPG,toESPG,X,Y)
  else:
     return transform(fromESPG,toESPG,X,Y, Elevation)

       

class radargram:
    def __init__(self, data = None):
        self.x_pix = 0      # longueur en pixel
        self.z_pix = 0      # hauteur en pixel
        self.x_m   = 0.0    # longueur en metre
        self.z_m   = 0.0    # hauteur en metre
        self.E     = 5
        self.z_interv = 100
        self.c        =    1
        self.gain     = [1]
        self.nb_traces    = 0
        self.sample_inter = 0
        self.nb_sample    = 0
        
        if data is None:
            self.traces = None
        else :
            self.traces = data 
            self.nb_traces = len(data)
            self.is_read =  self.get_trace_info() 
            
    def get_traces(self,seq,data= None):
        index = self.ind_from_liste(seq) 
        if data is None:
            return np.array([self.traces[i] for i in index ])                  
        else:
            pass
        
    def read_trace(self, seq,data=None):
        index = self.ind_from_liste(seq) 
        if data is None:
            return np.array([ self.traces[i].trace for i in index ]).T
        else:
            return np.array([ data[i].trace for i in index ]).T
                 
    def read_position(self, seq,data=None):
         index = self.ind_from_liste(seq)
         return np.array([ self.traces[i].get_position() for i in index ]).T             
    
    def read_position_meter(self, seq,data=None):
         index = self.ind_from_liste(seq)
         POS = np.array([ self.traces[i].get_position() for i in index ]).T             
         return Reproj(POS[1,:],POS[0,:],POS[2,:])

    def read_quality(self,seq,data= None):
        index = self.ind_from_liste(seq)
        return np.array([ self.traces[i].unpack_data('GPS_quality') for i in index ]).T   
                      
    def ind_from_liste(self,Ilist=None,HV =None):
         if HV == None:
             HV='H'
         if HV == 'H':
             list_max = self.nb_traces
         elif HV =='V':
             list_max = self.trace_len    
         if Ilist is None:                  # default
             return range(0, list_max, 4)
         if type(Ilist) is int:             # Une seule trace
             return Ilist
         elif type(Ilist) is list:
             if len(Ilist) == 2:
                 step = 1
             elif len(Ilist) ==3:
                 step = Ilist[2]
             if Ilist[1] >0:
                 return range(Ilist[0],Ilist[1], step)
             else:
                 return range(Ilist[0],list_max, step)
         else:
             print("Index type unkown")
             
    def get_img(self):
        return self.img

    def get_depth_from_trace(self,trace):
        return False

    def get_trace_info(self):
        self.sample_inter, self.nb_sample, mark = self.traces[0].get_trace_info()
        return True

    def get_z_interval(self,seq =None):
        if seq == None:
            i = 0
        else:
            i = seq
        return self.traces[i].get_trace_info()[0]
        





from scipy import interpolate


class auto_gain():
    def __init__(self,data = None, param = None):
        self.name = "Gain"
        self.data_out  = []
        self.gain_fig  = None
        self.l_data  = 512
        self.parameter = None
        self.data_in = [1]
        if (data is None) and (param is None):
            print("no input data")
        else: 
            self.process(data,param)
            

    def process(self, data=None, parameter=None):  
        print(" auto gain computing: ", str(parameter))
        if data is None:
            pass
        else:
            self.data_in = data 
        self.l_data = len(self.data_in)
        if parameter is None:
            print("parameter is none")
            if self.parameter is None:
                self.interpolate(None,[1,1]) 
        else:
            print("parameter is ", parameter)
            self.parameter = parameter
        self.interpolate(None,self.parameter)
        self.data_out =  np.reshape(self.parameter,(-1,1))*self.data_in

    def interpolate(self,xgain=None,ygain=None, kind_interpol='linear'):
        if xgain is None:        
            xgain = np.linspace(0,self.l_data,len(ygain))
            
        if xgain[-1] != self.l_data:    
            xgain.append(self.l_data)
            ygain.append(ygain[-1])
        print (xgain[0], xgain[-1] ,len(ygain), len(xgain) ,self.l_data,list(range(1,self.l_data+1,1))[0] ,list(range(1,self.l_data+1,1))[-1] )
        f = interpolate.interp1d(xgain,ygain, kind=kind_interpol)
        self.parameter =  f(list(range(0,self.l_data,1)))
        return np.reshape(self.parameter,(-1,1))

