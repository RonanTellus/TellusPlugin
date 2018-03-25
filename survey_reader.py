#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 09:07:37 2017

@author: tellus_user2
"""
import re
import os
import time
from struct import *
import numpy as np


class survey_reader:
    def __init__(self, seg_file=None):
        
        self.filename    = seg_file.split('/')[-1]
        self.folder      = os.getcwd()
        self.date        = None
 
       # Header Meta-data
        self.antenne     = None
        self.depth       = None
        self.medium      = None
        self.gain        = None
        self.filter      = None
        self.scan_rate   = None
        self.pulse_delay = None
        self.position    = None
        self.prism_v     = None        
        self.direction   = None
        self.prism_info  = None
        self.nb_byte     = None
        self.nb_traces   = None
        self.traces      = None
        try:       
            with open(seg_file,'rb') as fi:
                self.read_prism_info(fi)
                self.read_record(fi)
        except: 
            print ("no readable file")
            
        
    def read_prism_info(self,file_in):
         info = []
         magic_words = ["Date","Control","Unit","Antenna", "Time range","Sounding","Samples per trace","Channels mode","Tx/Rx","Gain","High-pass","Stacking","Scan","Pulse","Positioning","version","Direction"]
         words_re     = re.compile("|".join(magic_words))
         file_in.seek(0)
         for i in range(28):   # nb max de ligne de texte dans les fichiers prism
            line = file_in.readline()
            if b'\x00' in line:
                break
            if words_re.search(line.decode("utf-8", "ignore")):
               print (line)
               info.append(line.decode().replace("\r\n","").split(':') )
         self.info = self.prism_info    
         
    def read_record(self,file_in):
    
        file_in.seek(0, 2)
        self.nb_byte = file_in.tell()
        file_in.seek(0)
        print("file length:", self.nb_byte,"bytes")
        
        """ Standard SEG-Y """
        bin_header_offset = 3200
        bin_header_len    = 400
        
        trace_header_offset = 3600
        trace_header_len    = 240
        
        
        """Calcul temps d'execution """
        tic = time.clock()
        """ Saut vers le binary header 3200 """
        file_in.seek(bin_header_offset)

        """ lecture du binary header """
        Header = Bin_header()
        Header.reader(bytearray(file_in.read(bin_header_len) ) )
        self.trace_len = (Header.get_Nmb_sample_per_trace()) * 2      # Check header for real size
         

        """ Saut vers vers premiere trace """
        file_in.seek(trace_header_offset)
        """ lecture du trace header """
        self.nb_traces = (self.nb_byte - 3600)/(240 + 2*Header.get_Nmb_sample_per_trace() ) # because 16bit format
        
        traces = [] 
        print("nb_of_traces", self.nb_traces)
        for i in range (int(self.nb_traces)):
            tr1 = bytearray(file_in.read(trace_header_len+self.trace_len) )            
            traces.append(Traces(tr1) )
        self.traces = traces
        tac = time.clock()
        print ("Time of process:", tac-tic)
        
    def get_traces(self):
        return  self.traces


        
########### Binary Header Reader ############
class Bin_header:
    # dir(Bin_header)
    # Bin_header.__dict__
    def __init__(self,data = None):
        if data is None:
            self.bin_data = None
        else: 
            self.bin_data = data     
            self.reader(self.bin_data)
            
        self.INDEX_HEADER =  { 'Sample_int': 16, 'Nmb_sample_per_trace': 20, 'Unit_sys': 24, 'Mes_sys': 54 }
        self.DATA_FMT     =  { 'Sample_int': '<h', 'Nmb_sample_per_trace': '<h', 'Unit_sys': '<h', 'Mes_sys': '<h' }
        self.FMT_LEN      =  {'<h': 2, '<i': 4, '<f': 4, '<d': 8}
        self.DATA_TYPE    =  {1: '32-bit Floating point', 2: '32-bit Fixed point', 3: '16-bit Fixed point', 4: '16-bit Fixed point with gain'   }

        self.Unit_sys   = [0]  # Unit System of Data
        self.Data_fmt   = [1]  # type of data
        self.Nmb_tr     = [0]  # Number of Samples per Traces
        self.Sample_int = [0]  # Sample interval in picoSec
         
    def reader(self, data = None):
        if data is None:
            data = self.bin_data
        self.Data_fmt, self.Nmb_tr, self.Sample_int, self.Unit_sys = [ unpack(self.DATA_FMT[i] , data[self.INDEX_HEADER[i]: self.FMT_LEN [self.DATA_FMT[i]] + self.INDEX_HEADER[i] ]) \
       for i in sorted(self.INDEX_HEADER)]

    def get_Sample_interval(self):
        return self.Sample_int[0]

    def get_Nmb_sample_per_trace(self):
        return self.Nmb_tr[0]

    def get_Data_type(self):
        print ( self.DATA_TYPE[ self.Data_fmt[0] ] )
        return self.Data_fmt[0]



        

class Traces:       
    def __init__(self, bin_data = None):
        self.INDEX_HEADER =  {  'seq_num':0,'altitude':40, 'height_of_geoid': 44, 'elevation':52,\
                               'direction':48,'Coord_scale': 70,'Src_X': 72, 'Src_Y': 76,\
                               'Coord_unit': 88, 'GPS_quality': 90,'Nb_sample': 114, 'Sample_int': 116,\
                               'HHMMSS': 160, 'time_base': 166, 'Long_64': 182,\
                               'Lat_64': 190, 'Time_scale': 214, 'Mark_flag': 236,\
                               'Mark_num': 238}
        self.DATA_FMT     =  {'seq_num':'<i', 'altitude':'<f', 'height_of_geoid': '<f','elevation':'<f',\
                              'direction':'<i', 'Coord_scale': '<h', 'Src_X': '<f',\
                              'Src_Y': '<f', 'Coord_unit': '<h', 'GPS_quality': '<i',\
                              'Nb_sample': '<h', 'Sample_int': '<h', 'HHMMSS': '<hhh',\
                              'time_base': '<h', 'Long_64': '<d','Lat_64': '<d', 'Time_scale': '<h',\
                              'Mark_flag': '<h', 'Mark_num': '<h'}
        self.FMT_LEN      =  {'<h': 2, '<i': 4, '<f': 4, '<d': 8, '<hhh' : 6}
        self.DATA_TYPE    =  {1: '32-bit Floating point', 2: '32-bit Fixed point', 3: '16-bit Fixed point', 4: '16-bit Fixed point with gain'   }
        
        self.bin_data = bin_data
        self.unit_syst = None
        self.data_fmt  = None
        self.nb_sample = None
        
        self.altitude        = None
        self.height_of_geoid = None
        self.elevation       = None
        self.direction       = None
        self.coord_scal      = None
        self.Long_32         = None
        self.Lat_32          = None        
        self.coord_unit      = None
        self.gps_quality     = None
        self.Lat_64          = None
        self.Long_64         = None

        self.lag_time        = None
        self.nb_smple        = None
        self.time_of_tr      = None
        
        self.is_marked       = None
        self.mark_num        = None
        self.trace           = None
        
        self.sample_inter    = None
        
        if self.bin_data is None:
            print("No data available")
        else:
            self.ID =  self.unpack_data( 'seq_num' )
            self.get_trace(0)
            
    def get_trace_info(self):
        self.sample_inter = self.unpack_data('Sample_int')
        self.nb_sample    = self.unpack_data('Nb_sample')
        self.is_marked    = self.unpack_data('Mark_flag')
        if self.is_marked  == b'\X5555':
            self.mark_num     = self.unpack_data('Mark_num')
        return   self.sample_inter, self.nb_sample, self.mark_num    
       
    def get_position(self,option=None):
        if option is None:
            self.Lat_64    = self.unpack_data('Lat_64')
            self.Long_64   = self.unpack_data('Long_64')
            self.altitude  = self.unpack_data('altitude')
            #self.Elevation = self.unpack_data('elevation')
        return DMS_to_Deg(self.Lat_64, 1), DMS_to_Deg(self.Long_64,1), self.altitude
         
    def get_pos_info(self, option = None):
        if option is None: 
           self.altitude        = self.unpack_data('altitude')
           self.height_of_geoid = self.unpack_data('height_of_geoid')
           self.direction       = self.unpack_data('direction')
           self.coord_unit      = self.unpack_data('Coord_unit')
           self.gps_quality     = self.unpack_data('GPS_quality')
           
    def get_trace(self, option = None):
        if option is None:            
            return self.trace   
        elif option == 0:
             self.trace = unpack('<'+'h'*(512), self.bin_data[240:240+(512)*2])
           
    def unpack_data(self, data):
        fmt    = self.DATA_FMT[data]
        from_p = self.INDEX_HEADER[data]
        to_p   = self.INDEX_HEADER[data] + self.FMT_LEN[fmt]
        return unpack(fmt,self.bin_data[from_p:to_p])[0]
        
        



from decimal import *            

def DMS_to_Deg(data,fast=None):
    getcontext().prec = 16
    if data<0:
        return int(data/100)-Decimal((np.abs(data))%100)/Decimal(60.0) 
    else:
        return int(data/100)+Decimal((data)%100)/Decimal(60.0) 
    


        
        
        
