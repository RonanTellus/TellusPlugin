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
from radar_tools import *
import matplotlib.pyplot as plt 
import os 
import csv

import resources
import os
from os.path import dirname
from PyQt4 import QtGui

from qgis.core import QGis, QgsFeatureRequest, QgsFeature, QgsGeometry, QgsWKBTypes

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

        self.connect(self.ui.buttonLancer, SIGNAL("clicked()"),self.createtoline)
      
        
       
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
    
    def createtoline(self):
        
        file = self.ui.pathLineEdit.text()

        filename = os.path.splitext(os.path.basename(file))[0]

        seg = survey_reader(file)
        
        rad_img = radargram(seg.get_traces())
        
        rad_sample  = rad_img.read_trace([0,-1,2000])
        
        gps_sample  = rad_img.read_position([0,-1,2000])
        
        
        test = rad_sample.T
        
        points = [""]*len(test)
        
        for i in range(len(test)):
            # Specify the geometry type
            layer = QgsVectorLayer('Point?crs=epsg:4326', 'point' , 'memory')
             
            # Set the provider to accept the data source
            prov = layer.dataProvider()
        
            for i in range(len(test)):
                x = gps_sample[1][i]
                y = gps_sample[0][i]
        
        
                # Add a new feature and assign the geometry
                feat = QgsFeature()
                feat.setGeometry(QgsGeometry.fromPoint(QgsPoint(x,y)))
                prov.addFeatures([feat])
                    
                points[i] = QgsPoint(x,y)
        
        # Specify the geometry type
        layer = QgsVectorLayer('LineString?crs=epsg:4326', filename , 'memory')
         
        # Set the provider to&nbsp;accept the data source
        prov = layer.dataProvider()
         
        # Add a new feature and assign the geometry
        feat = QgsFeature()
        feat.setGeometry(QgsGeometry.fromPolyline(points))
        prov.addFeatures([feat])
         
        # Update extent of the layer
        layer.updateExtents()
         
        # Add the layer to the Layers panel
        QgsMapLayerRegistry.instance().addMapLayers([layer])
