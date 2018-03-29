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
from math import sqrt

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

        self.connect(self.ui.buttonLancer, SIGNAL("clicked()"),self.accept)

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
    
    def createtoline(self):
        
        file = self.ui.pathLineEdit.text()

        filename = os.path.splitext(os.path.basename(file))[0]

        seg = survey_reader(file)
        
        distance = self.ui.sbParamDistance.text()
            
        d = float(distance)/100
        
        a = 0.15
        
        rad_img = radargram(seg.get_traces())

        nbTraces = int(self.ui.sbParamTraces.text())
        
        rad_metre  = rad_img.read_position_meter([0,-1,nbTraces])
        
        gps_sample  = rad_img.read_position([0,-1,1])

        xm = []
        ym = []
        xm.append(gps_sample[1][0]) 
        ym.append(gps_sample[0][0])
        xc =  float(rad_metre[1][0])
        yc = float(rad_metre[0][0])
        for i in range(len(rad_metre[0])):
            if gps_sample[1][i] != 0 or gps_sample[0][i] != 0:
                dista = float(round(sqrt((rad_metre[0][i]-yc)**2+ (rad_metre[1][i]-xc)**2),4))
                if dista >= d:
                    xm.append(gps_sample[1][i])
                    ym.append(gps_sample[0][i])
                    xc =  float(rad_metre[1][i])
                    yc = float(rad_metre[0][i])
    
        #test = rad_sample.T
    
        valeurs = [""]*len(xm)

        for i in range(len(xm)):
            if gps_sample[0][i] != 0 and gps_sample[1][i] != 0:
                valeurs[i]= [xm[i], ym[i]]





        entetes = [
             u'X',
             u'Y',
        ]

        #valeurs = [
        #
        #     [gps_sample[0][0], gps_sample[1][0], gps_sample[2][0], test[0]],
        #     [u'Valeur6', u'Valeur7', u'Valeur8', u'Valeur9', u'Valeur10'],
        #     [u'Valeur11', u'Valeur12', u'Valeur13', u'Valeur14', u'Valeur15']
        #]


        f = open(file[:-3]+"csv", 'w')
        ligneEntete = ";".join(entetes) + "\n"
        writer = csv.writer(f, delimiter=";")
        f.write(ligneEntete)    
        writer.writerows(valeurs)

        f.close()


        Input_Table = file[:-3]+"csv"  # set the filepath for the input CSV
        lon_field = 'x' # set the name for the field containing the longitude
        lat_field = 'y' # set the name for the field containing the latitude
        crs = 4326 # set the crs as needed
        Output_Layer = file[:-3]+"shp" # set the filepath for the output shapefile
         
        spatRef = QgsCoordinateReferenceSystem(crs, QgsCoordinateReferenceSystem.EpsgCrsId)
         
        inp_tab = QgsVectorLayer(Input_Table, 'Input_Table', 'ogr')
        prov = inp_tab.dataProvider()
        fields = inp_tab.pendingFields()
        outLayer = QgsVectorFileWriter(Output_Layer, None, fields, QGis.WKBPoint, spatRef)
         
        pt = QgsPoint()
        outFeature = QgsFeature()
         
        for feat in inp_tab.getFeatures():
            attrs = feat.attributes()
            pt.setX(float(feat[lon_field]))
            pt.setY(float(feat[lat_field]))
            outFeature.setAttributes(attrs)
            outFeature.setGeometry(QgsGeometry.fromPoint(pt))
            outLayer.addFeature(outFeature)
        del outLayer

        layer = iface.addVectorLayer(Output_Layer, 
                             filename, "ogr")

        os.remove(Input_Table)


dialog = TellusProcessingDialog()
if dialog.exec_() == QDialog.Accepted:
    dialog.createtoline()
    
