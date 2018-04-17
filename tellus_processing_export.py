# coding: utf-8
"""
/***************************************************************************
 TellusProcessingExport
                                 A QGIS plugin
 Module de traitement de données
                             -------------------
        begin                : 2018-03-12
        git sha              : $Format:%H$
        copyright            : (C) 2018 by ISTIC
        email                : siham.makroumm@etudiant.univ-rennes1.fr
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

from PyQt4.QtGui import QProgressBar, QApplication
from PyQt4 import QtCore
from qgis.utils import iface
from qgis.core import QgsMessageLog

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.utils import iface


from qgis import *
from qgis.core import *
from qgis.gui import *
from UI_tellus_processing_export_base import Ui_TellusProcessingExportBase

from survey_reader import survey_reader
from radar_tools import radargram
import matplotlib.pyplot as plt 


import resources
import os
import sys
from os.path import dirname
from PyQt4 import QtGui
from math import sqrt

import processing
from functools import partial

from radargram import *


class TellusProcessingExport(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        """Constructor."""
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-Exports-with-auto-connect

        self.ui = Ui_TellusProcessingExportBase()
        self.ui.setupUi(self)
        self.connect(self.ui.exit, SIGNAL("clicked()"),self.reject)

        self.connect(self.ui.buttonExporter, SIGNAL("clicked()"),self.exportData)
        self.connect(self.ui.buttonExporter, SIGNAL("clicked()"),self.reject)

        self.setWindowTitle("Export Data csv")
        
    def exportData(self):
            name = QtGui.QFileDialog.getSaveFileName(self, 'Save your Data',"export_data","CSV flies (*.csv)")  
            if (name !="") :      
                selectedIndexes = iface.legendInterface().selectedLayers()
                selectedLayers = []
                if len(selectedIndexes) == 0:
                    print "Selection vide "
                elif len(selectedIndexes) == 1:
                    selectedLayers = [iface.activeLayer()]
                else:
                    selectLayers = iface.legendInterface().selectedLayers()
                    for layer in selectLayers:
                        selectedLayers.append(layer)
                        if layer.wkbType() == QGis.WKBLineString:
                            print "couche selectionnee type ligne: :",  layer.name()
                            selectedLayers.append(layer)

                exportFile = open(name, "w")
                exportFile.write("Trace,x,y\n")
                #name source
                for line in selectedLayers:
                    with edit(line):
                        features = line.getFeatures()
                        #f = line.getFeatures().next()
                        for f in features:
                            aux =""
                            for ii in f.attributes():
                                aux = aux + ","+str(ii)
                            exportFile.write(aux[1:]+"\n")
                exportFile.close()



class progressBar():
    """!@brief Manage progressBar and loading cursor.
    Allow to add a progressBar in Qgis and to change cursor to loading
    input:
        -inMsg : Message to show to the user (str)
        -inMax : The steps of the script (int)
    
    output:
        nothing but changing cursor and print progressBar inside Qgis
    """
    def __init__(self,inMsg=' Loading...',inMaxStep=1):
            # initialize progressBar            
            """
            """# Save reference to the QGIS interface
            QApplication.processEvents() # Help to keep UI alive
            
            widget = iface.messageBar().createMessage('Please wait  ',inMsg)            
            prgBar = QProgressBar()
            self.prgBar=prgBar
            self.iface=iface
            widget.layout().addWidget(self.prgBar)
            iface.messageBar().pushWidget(widget, iface.messageBar().WARNING)
            QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
            
            # if Max 0 and value 0, no progressBar, only cursor loading
            # default is set to 0
            prgBar.setValue(1)
            # set Maximum for progressBar
            prgBar.setMaximum(inMaxStep)
            
    def addStep(self):
        """!@brief Add a step to the progressBar
        addStep() simply add +1 to current value of the progressBar
        """
        plusOne=self.prgBar.value()+1
        self.prgBar.setValue(plusOne)
    def reset(self):
        """!@brief Simply remove progressBar and reset cursor
        
        """
        # Remove progressBar and back to default cursor
        self.iface.messageBar().clearWidgets()
        self.iface.mapCanvas().refresh()
        QApplication.restoreOverrideCursor()