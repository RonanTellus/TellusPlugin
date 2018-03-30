# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TellusProcessingDialog
                                 A QGIS plugin
 Module de traitement de données
                             -------------------
        begin                : 2018-03-12
        git sha              : $Format:%H$
        copyright            : (C) 2018 by ISTIC
        email                : dimas.espinasse@etudiant.univ-rennes1.fr
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""


from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.utils import iface


from qgis import *
from qgis.core import *
from qgis.gui import *
from UI_tellus_processing_dialog_base import Ui_TellusProcessingDialogBase

from survey_reader import survey_reader
from radar_tools import radargram
import matplotlib.pyplot as plt 


import resources
import os
from os.path import dirname
from PyQt4 import QtGui
from math import sqrt


class Bar(QProgressBar):
  value = 0  
    
  @pyqtSlot()
  def increaseValue(self):    
    self.setValue(self.value)
    self.value = self.value+1

bar = Bar()



class TellusProcessingDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        """Constructor."""
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect

        self.ui = Ui_TellusProcessingDialogBase()
        self.ui.setupUi(self)
        self.connect(self.ui.parcourirBtn,SIGNAL("clicked()"),self.inFile)

        self.connect(self.ui.buttonLancer, SIGNAL("clicked()"),self.accept) 
        self.connect(self.ui.buttonLancer, SIGNAL("clicked()"),self.createtoline)

        self.connect(self.ui.buttonAnnuler, SIGNAL("clicked()"),self.reject)

        self.setWindowTitle("Lecteur SEG-Y")
        

       
    def inFile(self):
        """Opens an open file dialog"""  
        settings = QtCore.QSettings()
        key = '/UI/lastShapefileDir'
        workDir = settings.value(key)
        filter = 'SEG-Y Geophysical Data (*.sgy)'
        OpenInputShapeMsg = QtGui.QApplication.translate("Utility",  "Open input geophysical data file", None, QtGui.QApplication.UnicodeUTF8) 
        inFilePath = QtGui.QFileDialog.getOpenFileName(self, OpenInputShapeMsg, workDir, filter)
        inFilePath = unicode(inFilePath)
        if inFilePath:
            #  root, ext = splitext(inFilePath)
            # if ext.upper() != '.SHP':
            #    inFilePath = '%s.shp' % inFilePath
            workDir = dirname(inFilePath)
            settings.setValue(key, workDir)      
            
        self.ui.pathLineEdit.setText(inFilePath) 

        # Pushing widgets to the message bar



 
    
    def createtoline(self):

        bar =  Bar()
        iface.messageBar().pushWidget(bar, QgsMessageBar.INFO, 1) 
        
        file = self.ui.pathLineEdit.text()

        filename = os.path.splitext(os.path.basename(file))[0]

        seg = survey_reader(file)

        distance = self.ui.sbParamDistance.text()

        d = float(distance)/100
      
        
        rad_img = radargram(seg.get_traces())

        rad_metre  = rad_img.read_position_meter([0,-1,1])
        
        gps_sample  = rad_img.read_position([0,-1,1])
        #Prend en compte le paramère distance renseigné en cm dans le plugin afin de mettre en mémoire les point avec une distance égale à (cm) entre deux points
        xm = []
        ym = []
        zm = []
        xm.append(gps_sample[1][0]) 
        ym.append(gps_sample[0][0])
        zm.append(gps_sample[2][0])
        xc =  float(rad_metre[1][0])
        yc = float(rad_metre[0][0])
        zc = float(rad_metre[2][0])
        for i in range(len(rad_metre[0])):
            if gps_sample[1][i] != 0 or gps_sample[0][i] != 0:
                dista = float(round(sqrt((rad_metre[0][i]-yc)**2+ (rad_metre[1][i]-xc)**2 + (rad_metre[2][i]-zc)**2),4))
                if dista >= d:
                    xm.append(gps_sample[1][i])
                    ym.append(gps_sample[0][i])
                    zm.append(gps_sample[2][i])
                    xc =  float(rad_metre[1][i])
                    yc = float(rad_metre[0][i])
                    zc = float(rad_metre[2][i])
        
        
                        
        # Specify the geometry type
        layer = QgsVectorLayer('Point?crs=epsg:4326&field=Trace:int&field=x&field=y', filename , 'memory')
        
        # Set the provider to accept the data source
        prov = layer.dataProvider()
     

       #{↓AJout des points en memoire à partir de la distance renseigné en (cm)
        for i in range(len(xm)):
            x = xm[i]
            y = ym[i]

            # add a feature
            fet = QgsFeature()
            fet.setGeometry(QgsGeometry.fromPoint(QgsPoint(x,y)))
            fet.setAttributes([i,float(x), float(y)])
            prov.addFeatures([fet])

            # update layer's extent when new features have been added
            # because change of extent in provider is not propagated to the layer
            layer.updateExtents()

            QgsMapLayerRegistry.instance().addMapLayers([layer])
            #bar.increaseValue()