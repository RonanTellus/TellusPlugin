# coding: utf-8

from radar_tools import *
import matplotlib.pyplot as plt
from survey_reader import survey_reader
import os 
from matplotlib.widgets import Button

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.utils import iface
from qgis import *
from qgis.core import *
from qgis.gui import *

class fig_gui:
    
    def __init__(self,name = None,rad_sample=[],gps_sample = [],from_trace = 0, to_trace = 0):
        if name is None:
            self.name ="None"
            self.rad_sample=[];
            self.gps_sample=[];
        else :
            #nom du fichier
            self.name = name
            self.rad_sample=rad_sample;
            self.gps_sample=gps_sample;
            #numéro du début des traces
            self.fr = from_trace
            #fin de l'intervale du fichier
            self.tr=to_trace

     
        
        self.fig = plt.figure()
        self.fig.canvas.set_window_title(self.name) 
        seg = survey_reader(self.name)
        # create a group of traces from seg-y 
        self.ax  = [self.fig.add_subplot(111)]
        self.update(self.rad_sample)                            # add data to plot
        
        cli = cursor(self.name,self.fr)              # new cursors object
        self.fig.signal = cli          # connect it with fig object 

                #tr_list  = range(len(gps_sample[0]))       # list index
    
    
        
        cli.transform = lambda x,y: [self.gps_sample[1][x] ,self.gps_sample[0][x],self.gps_sample[2][x],y,self]
        cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick)
        
	
        
    def update(self,data,plt_type=None , plot_number = 0):

                if plt_type == "equal":
                    print( "equalized")
                    data = exposure.equalize_hist(data)

                elif plt_type == "expos":
                    p2, p98 = np.percentile(data, (2, 98))
                    data = exposure.rescale_intensity(data, in_range=(p2, p98))

                self.ax[plot_number].imshow(data, interpolation='nearest', aspect='auto',clim=[np.min(data),np.max(data)])
                plt.show()
        
    def onclick(self,event):
        if self.fig.signal is None:
                  
            self.cursor = [int(event.xdata),int(event.ydata)]
        else :
           self.fig.signal.set_pos(event, self.name)







class cursor:
    
    def __init__(self,name = None,fr = 0):
        self.name=name
        self.fr=fr
        self.fig_to_update = None
        self.func_update = None
        self.transform = lambda x,y,z: [x,y,z]
        exist = len(QgsMapLayerRegistry.instance().mapLayersByName('Points d\'interet')) != 0
        if (exist == False):
            #création des colonnes dans le tableau d'attributs points d'intérêt
            layer = QgsVectorLayer('Point?crs=epsg:4326&field=Trace:int&field=x&field=y&field=z&field=Profondeur&field=Nom du fichier&field=Commentaire', 'Points d\'interet' , 'memory')
            self.layer = layer
             #self.prov sert remplir les données du tableau
            self.prov = layer.dataProvider()
            QgsMapLayerRegistry.instance().addMapLayers([layer])
        else:
            #création de la couche nommée points d'intérêt
            layers = QgsMapLayerRegistry.instance().mapLayersByName('Points d\'interet')
            for layer in layers:
                self.layer = layer
                #self.prov sert à remplir les données du tableau
                self.prov = self.layer.dataProvider()

    
    def set_pos(self,event,name):
        #vérifie que le click soit bien dans le cadre
        if(event.xdata != None):
            self.pos = self.transform(int(event.xdata),int(event.ydata))
            #x : Longitude
            #y : Latitude
            #z : altitude
            #w : profondeur
            x = self.pos[0]
            y = self.pos[1]
            z = self.pos[2]
            w = self.pos[3]
            # la couche
            layer = self.layer
            # reprend le prov dans l'init
            prov = self.prov
            fet = QgsFeature()
            #ajoute le point
            fet.setGeometry(QgsGeometry.fromPoint(QgsPoint(x,y)))
            #ajoute les valeurs 
            fet.setAttributes([ self.fr + int(event.xdata),float(x),float(y),float(z),float(w),self.name,""])
            prov.addFeatures([fet])
            # update layer's extent when new features have been added
            # because change of extent in provider is not propagated to the layer
            layer.updateExtents()
            layer.triggerRepaint()
            #QgsMapLayerRegistry.instance().addMapLayers([layer])
            if self.fig_to_update is None:
                print ( "nothing to do")
    
            else:
              print "do something with matplotlib figure declare in: self.fig_to_update"
    

