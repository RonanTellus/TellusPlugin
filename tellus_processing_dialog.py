# coding: utf-8
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
from UI_tellus_processing_dialog_base import Ui_TellusProcessingDialogBase

from survey_reader import survey_reader
from radar_tools import radargram
import matplotlib.pyplot as plt 


import resources
import os
from os.path import dirname
from PyQt4 import QtGui
from math import sqrt

import processing
from functools import partial

from radargram import *


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
        self.connect(self.ui.buttonAnnuler, SIGNAL("clicked()"),self.resetData)

        self.setWindowTitle("Lecteur SEG-Y")
        

       
    def inFile(self):
       """Opens an open file dialog"""  
       settings = QtCore.QSettings()
       key = '/UI/lastShapefileDir'
       workDir = settings.value(key)
       filter = 'SEG-Y Geophysical Data (*.sgy)'
       OpenInputShapeMsg = QtGui.QApplication.translate("Utility",  "Open input geophysical data file", None, QtGui.QApplication.UnicodeUTF8)
       inFilePath = QtGui.QFileDialog.getOpenFileNames(self, OpenInputShapeMsg, workDir, filter)
       inFilePath = unicode(inFilePath)
       if inFilePath:
           #  root, ext = splitext(inFilePath)
           # if ext.upper() != '.SHP':
           #    inFilePath = '%s.shp' % inFilePath
           workDir = dirname(inFilePath)
           settings.setValue(key, workDir)      
           
       self.ui.pathLineEdit.setText(inFilePath)
       files = eval(self.ui.pathLineEdit.text())
       for f in files:
           filename = os.path.splitext(os.path.basename(f))[0]

           seg = survey_reader(f)
           rowPosition = self.ui.tableWidget.rowCount()
           
           combo = QComboBox()
           combo.addItem("non")
           combo.addItem("oui")
           
           name = str(rowPosition)
           print(name)
           boutonSup = QtGui.QPushButton(name, self)
           boutonSup.setToolTip(name)
           print("nameobject")

           boutonSup.setText("X")
           boutonSup.setStyleSheet('QPushButton{background-color: "#FFFFFF";color:black; font-weight: bold;}   QPushButton:hover{background-color: "#FF0000";color:white; font-weight: bold;}')
           print(str(boutonSup.toolTip()))
           boutonSup.clicked.connect(partial(self.make_delete,rowPosition))  
           #boutonSup.clicked.connect(SLOT("delete(rowPosition)"))
                       

           nbTraces = QtGui.QTableWidgetItem()
           nbTraces.setText(str(seg.nb_traces))
           nbTraces.setFlags(QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled)
           self.ui.tableWidget.insertRow(rowPosition)
           self.ui.tableWidget.setItem(rowPosition , 0, QtGui.QTableWidgetItem(f))
           self.ui.tableWidget.setItem(rowPosition , 1, nbTraces)
           self.ui.tableWidget.setItem(rowPosition , 2, QtGui.QTableWidgetItem('0'))
           self.ui.tableWidget.setItem(rowPosition , 3, QtGui.QTableWidgetItem(str(seg.nb_traces)))
           self.ui.tableWidget.setCellWidget(rowPosition,4,combo)
           self.ui.tableWidget.setCellWidget(rowPosition,5,boutonSup)
        

    def make_delete(self,ligne):
       l = int(ligne)
       print(45)
       print(l)
       self.ui.tableWidget.removeRow(l)  
       rowPosition = self.ui.tableWidget.rowCount()
       while l< rowPosition:
           name = str(l)
           print(name)
           boutonSup = QtGui.QPushButton(name, self)
           boutonSup.setToolTip(name)
           print("nameobject")

           boutonSup.setText("X")
           boutonSup.setStyleSheet('QPushButton{background-color: "#FFFFFF";color:black; font-weight: bold;}   QPushButton:hover{background-color: "#FF0000";color:white; font-weight: bold;}')
           print(str(boutonSup.toolTip()))
           boutonSup.clicked.connect(partial(self.make_delete,l))  
           self.ui.tableWidget.setCellWidget(l,5,boutonSup)
           l = l+1


 
    
    def createtoline(self):


        
        files = eval(self.ui.pathLineEdit.text())

        for row in xrange(self.ui.tableWidget.rowCount()):
            selected = self.ui.tableWidget.currentRow()
            print selected


            item = self.ui.tableWidget.item(row, 0)
            item1 = self.ui.tableWidget.item(row, 1)
            item2 = self.ui.tableWidget.item(row, 2)
            item3 = self.ui.tableWidget.item(row, 3)
            item4 = self.ui.tableWidget.cellWidget(row, 4)

            text = item.text()
            text1 = item1.text()
            text2 = item2.text()
            text3 = item3.text()
            text4 = item4.currentText()



            filename = os.path.splitext(os.path.basename(text))[0]

            seg = survey_reader(text)

            distance = self.ui.sbParamDistance.text()

            d = float(distance)/100
          
            a = 0.15
            
            rad_img = radargram(seg.get_traces())

            from_trace = int(text2)
            to_trace = int(text3)
            
            rad_metre  = rad_img.read_position_meter([from_trace,to_trace,1])


            gps_sample  = rad_img.read_position([from_trace,to_trace,1])

            print rad_metre
            print gps_sample

            if (text4 == "oui"):
                rad_sample  = rad_img.read_trace([from_trace,to_trace,1])           # extracte data 1 on 2


                myfig = fig_gui()                                   # new fig object
                myfig.update(rad_sample)                            # add data to plot



                cli = cursor()              # new cursor object
                myfig.signal = cli          # connect it with fig object 

                #tr_list  = range(len(gps_sample[0]))       # list index

                cli.transform = lambda x,y: [gps_sample[0][x] ,gps_sample[1][x]]

            self.Progress=progressBar(' Lecture du SEG-Y ',len(rad_metre[0]))

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
                self.Progress.addStep()
                if gps_sample[1][i] != 0 or gps_sample[0][i] != 0:
                    dista = float(round(sqrt((rad_metre[0][i]-yc)**2+ (rad_metre[1][i]-xc)**2 + (rad_metre[2][i]-zc)**2),4))
                    if dista >= d:
                        xm.append(gps_sample[1][i])
                        ym.append(gps_sample[0][i])
                        zm.append(gps_sample[2][i])
                        xc =  float(rad_metre[1][i])
                        yc = float(rad_metre[0][i])
                        zc = float(rad_metre[2][i])
            self.Progress.reset()

            
                            
            # Specify the geometry type
            layer = QgsVectorLayer('Point?crs=epsg:4326&field=Trace:int&field=x&field=y', filename , 'memory')

            # Set the provider to accept the data source
            prov = layer.dataProvider()
          

            self.Progress=progressBar(' Creation des points ',len(xm))

            #Ajout des points en memoire à partir de la distance renseigné en (cm)
            for i in range(len(xm)):
                x = xm[i]
                y = ym[i]
                self.Progress.addStep()

               
                # add a feature
                fet = QgsFeature()
                fet.setGeometry(QgsGeometry.fromPoint(QgsPoint(x,y)))
                fet.setAttributes([from_trace+i,float(x), float(y)])
                prov.addFeatures([fet])

                # update layer's extent when new features have been added
                # because change of extent in provider is not propagated to the layer
                layer.updateExtents()

                QgsMapLayerRegistry.instance().addMapLayers([layer])
                #bar.increaseValue()
            self.Progress.reset()


    def resetData(self):
        self.ui.tableWidget.setRowCount(0)
        self.ui.pathLineEdit.setText("")



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
            