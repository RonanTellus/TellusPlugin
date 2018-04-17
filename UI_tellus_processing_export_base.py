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

class Ui_TellusProcessingExportBase(object):
    def setupUi(self, TellusProcessingExportBase):
        TellusProcessingExportBase.setObjectName(_fromUtf8("TellusProcessingExportBase"))
        TellusProcessingExportBase.resize(407, 203)

        self.label = QtGui.QLabel(TellusProcessingExportBase)
        self.label.setGeometry(QtCore.QRect(20, 20, 341, 61))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName(_fromUtf8("labelExport"))

        self.buttonExporter = QtGui.QPushButton(TellusProcessingExportBase)
        self.buttonExporter.setGeometry(QtCore.QRect(100, 100, 81, 31))
        self.buttonExporter.setObjectName(_fromUtf8("buttonExporter"))

        self.exit = QtGui.QPushButton(TellusProcessingExportBase)
        self.exit.setGeometry(QtCore.QRect(224, 100, 81, 31))
        self.exit.setObjectName(_fromUtf8("exit"))

        self.buttonExporter.raise_()
        self.exit.raise_()

        self.label.raise_()

        self.retranslateUi(TellusProcessingExportBase)
        QtCore.QMetaObject.connectSlotsByName(TellusProcessingExportBase)

    def retranslateUi(self, TellusProcessingExportBase):
        TellusProcessingExportBase.setWindowTitle(_translate("TellusProcessingExportBase", "Tellus processing Export", None))
        self.buttonExporter.setText(_translate("TellusProcessingExportBase", "OUI", None))
        self.exit.setText(_translate("TellusProcessingExportBase", "NON", None))
        self.label.setText(_translate("TellusProcessingExportBase", "<html><head/><body><p> Voulez-vous exporter vos donnees ? </p></body></html>", None))