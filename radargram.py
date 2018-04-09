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
    
    def __init__(self,name = None):
        if name is None:
            self.name ="None"
        else :
            self.name = name
        
        self.fig = plt.figure()
	self.ax  = [self.fig.add_subplot(111)]
        
        cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick)
        self.signal = None
	self.cursor = None
        
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
        if self.signal is None:
                  
            self.cursor = [int(event.xdata),int(event.ydata)]
        else :
           self.signal.set_pos(event, self.name)







class cursor:
    
    def __init__(self):
        self.fig_to_update = None
        self.func_update = None
        self.transform = lambda x,y: [x,y]
        layer = QgsVectorLayer('Point?crs=epsg:4326&field=Trace:int&field=x&field=y', 'Mes points' , 'memory')
        prov = layer.dataProvider()
        QgsMapLayerRegistry.instance().addMapLayers([layer])
    def set_pos(self,event,name):
        print ("pos in pixel: ", int(event.xdata),int(event.ydata) )
        self.pos = self.transform(int(event.xdata),int(event.ydata))
        print("pos in data: ",self.pos)
        x = self.pos[0]
        y = self.pos[1]
            
        layer = iface.activeLayer()
        prov = layer.dataProvider()
        fet = QgsFeature()
        fet.setGeometry(QgsGeometry.fromPoint(QgsPoint(x,y)))
        fet.setAttributes([0,float(x),float(y)])
        prov.addFeatures([fet])
        # update layer's extent when new features have been added
        # because change of extent in provider is not propagated to the layer
        layer.updateExtents()

        #QgsMapLayerRegistry.instance().addMapLayers([layer])
        if self.fig_to_update is None:
            print ( "nothing to do")

        else:
          print "do something with matplotlib figure declare in: self.fig_to_update"



filename = "DAT_0001.sgy"

seg = survey_reader(filename)

# create a group of traces from seg-y
rad_img = radargram(seg.get_traces())


# extracte some traces
from_trace = 0
to_trace   = 2000
rad_sample  = rad_img.read_trace([from_trace,to_trace,1])           # extracte data 1 on 2
gps_sample  = rad_img.read_position([from_trace,to_trace,1])  # extracte gps 1 on 2


myfig = fig_gui()                                   # new fig object
myfig.update(rad_sample)                            # add data to plot



cli = cursor()              # new cursor object
myfig.signal = cli          # connect it with fig object 

#tr_list  = range(len(gps_sample[0]))       # list index

cli.transform = lambda x,y: [gps_sample[0][x] ,gps_sample[1][x]]