# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_tellus_processing_dialog_base.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_TellusProcessingDialogBase(object):
    def setupUi(self, TellusProcessingDialogBase):
        TellusProcessingDialogBase.setObjectName(_fromUtf8("TellusProcessingDialogBase"))
        TellusProcessingDialogBase.resize(552, 254)
        self.distance = QtGui.QWidget(TellusProcessingDialogBase)
        self.distance.setGeometry(QtCore.QRect(20, 90, 511, 51))
        self.distance.setObjectName(_fromUtf8("distance"))
        self.lblNbTraces = QtGui.QLabel(self.distance)
        self.lblNbTraces.setGeometry(QtCore.QRect(30, 10, 61, 31))
        self.lblNbTraces.setObjectName(_fromUtf8("lblNbTraces"))
        self.sbParamTraces = QtGui.QLineEdit(self.distance)
        self.sbParamTraces.setGeometry(QtCore.QRect(80, 10, 113, 27))
        self.sbParamTraces.setObjectName(_fromUtf8("sbParamTraces"))
        self.source = QtGui.QWidget(TellusProcessingDialogBase)
        self.source.setGeometry(QtCore.QRect(20, 20, 511, 61))
        self.source.setObjectName(_fromUtf8("source"))
        self.parcourirBtn = QtGui.QPushButton(self.source)
        self.parcourirBtn.setGeometry(QtCore.QRect(430, 20, 80, 31))
        self.parcourirBtn.setObjectName(_fromUtf8("parcourirBtn"))
        self.lblDG = QtGui.QLabel(self.source)
        self.lblDG.setGeometry(QtCore.QRect(30, 20, 131, 31))
        self.lblDG.setObjectName(_fromUtf8("lblDG"))
        self.pathLineEdit = QtGui.QLineEdit(self.source)
        self.pathLineEdit.setGeometry(QtCore.QRect(160, 20, 261, 31))
        self.pathLineEdit.setObjectName(_fromUtf8("pathLineEdit"))
        self.lblSource = QtGui.QLabel(self.source)
        self.lblSource.setGeometry(QtCore.QRect(10, 0, 71, 17))
        self.lblSource.setObjectName(_fromUtf8("lblSource"))
        self.buttonLancer = QtGui.QPushButton(TellusProcessingDialogBase)
        self.buttonLancer.setGeometry(QtCore.QRect(450, 210, 80, 31))
        self.buttonLancer.setObjectName(_fromUtf8("buttonLancer"))
        self.buttonAnnuler = QtGui.QPushButton(TellusProcessingDialogBase)
        self.buttonAnnuler.setGeometry(QtCore.QRect(360, 210, 80, 31))
        self.buttonAnnuler.setObjectName(_fromUtf8("buttonAnnuler"))
        self.widget = QtGui.QWidget(TellusProcessingDialogBase)
        self.widget.setGeometry(QtCore.QRect(20, 150, 511, 51))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.lblDistance = QtGui.QLabel(self.widget)
        self.lblDistance.setGeometry(QtCore.QRect(30, 10, 221, 31))
        self.lblDistance.setObjectName(_fromUtf8("lblDistance"))
        self.sbParamDistance = QtGui.QLineEdit(self.widget)
        self.sbParamDistance.setGeometry(QtCore.QRect(240, 10, 113, 27))
        self.sbParamDistance.setObjectName(_fromUtf8("sbParamDistance"))

        self.retranslateUi(TellusProcessingDialogBase)
        QtCore.QMetaObject.connectSlotsByName(TellusProcessingDialogBase)

    def retranslateUi(self, TellusProcessingDialogBase):
        TellusProcessingDialogBase.setWindowTitle(_translate("TellusProcessingDialogBase", "Tellus processing", None))
        self.lblNbTraces.setText(_translate("TellusProcessingDialogBase", "Traces", None))
        self.parcourirBtn.setText(_translate("TellusProcessingDialogBase", "Parcourir", None))
        self.lblDG.setText(_translate("TellusProcessingDialogBase", "Données géoradar", None))
        self.lblSource.setText(_translate("TellusProcessingDialogBase", "<html><head/><body><p><span style=\" font-weight:600;\">Source</span></p></body></html>", None))
        self.buttonLancer.setText(_translate("TellusProcessingDialogBase", "Lancer", None))
        self.buttonAnnuler.setText(_translate("TellusProcessingDialogBase", "Annuler", None))
        self.lblDistance.setText(_translate("TellusProcessingDialogBase", "Distance entre chaque points", None))

