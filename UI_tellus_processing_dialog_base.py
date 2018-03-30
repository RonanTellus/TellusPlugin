# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_tellus_processing_dialog_base.ui'
#
# Created: Fri Mar 30 13:26:47 2018
#      by: PyQt4 UI code generator 4.10.4
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
        self.traces = QtGui.QWidget(TellusProcessingDialogBase)
        self.traces.setGeometry(QtCore.QRect(20, 80, 511, 61))
        self.traces.setObjectName(_fromUtf8("traces"))
        self.radBtnRadargramme = QtGui.QRadioButton(self.traces)
        self.radBtnRadargramme.setEnabled(True)
        self.radBtnRadargramme.setGeometry(QtCore.QRect(10, 10, 131, 20))
        self.radBtnRadargramme.setObjectName(_fromUtf8("radBtnRadargramme"))
        self.listWidget = QtGui.QListWidget(self.traces)
        self.listWidget.setEnabled(False)
        self.listWidget.setGeometry(QtCore.QRect(160, 0, 351, 61))
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.source = QtGui.QWidget(TellusProcessingDialogBase)
        self.source.setGeometry(QtCore.QRect(20, 20, 511, 61))
        self.source.setObjectName(_fromUtf8("source"))
        self.parcourirBtn = QtGui.QPushButton(self.source)
        self.parcourirBtn.setGeometry(QtCore.QRect(430, 0, 80, 31))
        self.parcourirBtn.setObjectName(_fromUtf8("parcourirBtn"))
        self.lblDG = QtGui.QLabel(self.source)
        self.lblDG.setGeometry(QtCore.QRect(30, 0, 131, 31))
        self.lblDG.setObjectName(_fromUtf8("lblDG"))
        self.pathLineEdit = QtGui.QLineEdit(self.source)
        self.pathLineEdit.setGeometry(QtCore.QRect(160, 0, 261, 31))
        self.pathLineEdit.setObjectName(_fromUtf8("pathLineEdit"))
        self.buttonLancer = QtGui.QPushButton(TellusProcessingDialogBase)
        self.buttonLancer.setGeometry(QtCore.QRect(450, 210, 80, 31))
        self.buttonLancer.setObjectName(_fromUtf8("buttonLancer"))
        self.buttonAnnuler = QtGui.QPushButton(TellusProcessingDialogBase)
        self.buttonAnnuler.setGeometry(QtCore.QRect(360, 210, 80, 31))
        self.buttonAnnuler.setObjectName(_fromUtf8("buttonAnnuler"))
        self.distance = QtGui.QWidget(TellusProcessingDialogBase)
        self.distance.setGeometry(QtCore.QRect(20, 150, 511, 51))
        self.distance.setObjectName(_fromUtf8("distance"))
        self.lblDistance = QtGui.QLabel(self.distance)
        self.lblDistance.setGeometry(QtCore.QRect(30, 10, 221, 31))
        self.lblDistance.setObjectName(_fromUtf8("lblDistance"))
        self.sbParamDistance = QtGui.QLineEdit(self.distance)
        self.sbParamDistance.setGeometry(QtCore.QRect(240, 10, 113, 27))
        self.sbParamDistance.setObjectName(_fromUtf8("sbParamDistance"))

        self.retranslateUi(TellusProcessingDialogBase)
        QtCore.QMetaObject.connectSlotsByName(TellusProcessingDialogBase)

    def retranslateUi(self, TellusProcessingDialogBase):
        TellusProcessingDialogBase.setWindowTitle(_translate("TellusProcessingDialogBase", "Tellus processing", None))
        self.radBtnRadargramme.setText(_translate("TellusProcessingDialogBase", "Affichage radargramme", None))
        self.parcourirBtn.setText(_translate("TellusProcessingDialogBase", "Parcourir", None))
        self.lblDG.setText(_translate("TellusProcessingDialogBase", "Données géoradar", None))
        self.buttonLancer.setText(_translate("TellusProcessingDialogBase", "Lancer", None))
        self.buttonAnnuler.setText(_translate("TellusProcessingDialogBase", "Annuler", None))
        self.lblDistance.setText(_translate("TellusProcessingDialogBase", "Distance entre chaque points (en cm)", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TellusProcessingDialogBase = QtGui.QDialog()
    ui = Ui_TellusProcessingDialogBase()
    ui.setupUi(TellusProcessingDialogBase)
    TellusProcessingDialogBase.show()
    sys.exit(app.exec_())

