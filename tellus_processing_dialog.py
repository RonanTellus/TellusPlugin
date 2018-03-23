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

from qgis import *
from qgis.core import *
from qgis.gui import *
from UI_tellus_processing_dialog_base import Ui_TellusProcessingDialogBase


import resources
import os
from os.path import dirname
from PyQt4 import QtGui

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
    
