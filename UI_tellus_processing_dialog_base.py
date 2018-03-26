# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_tellus_processing_dialog_base.ui'
#
# Created: Mon Mar 26 14:33:52 2018
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
        TellusProcessingDialogBase.resize(552, 281)
        self.radioButtonDossier = QtGui.QRadioButton(TellusProcessingDialogBase)
        self.radioButtonDossier.setGeometry(QtCore.QRect(170, 40, 117, 22))
        self.radioButtonDossier.setObjectName(_fromUtf8("radioButtonDossier"))
        self.label_3 = QtGui.QLabel(TellusProcessingDialogBase)
        self.label_3.setGeometry(QtCore.QRect(30, 15, 101, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.radioButtonFichier = QtGui.QRadioButton(TellusProcessingDialogBase)
        self.radioButtonFichier.setGeometry(QtCore.QRect(50, 40, 117, 22))
        self.radioButtonFichier.setObjectName(_fromUtf8("radioButtonFichier"))
        self.distance = QtGui.QWidget(TellusProcessingDialogBase)
        self.distance.setGeometry(QtCore.QRect(20, 165, 511, 51))
        self.distance.setObjectName(_fromUtf8("distance"))
        self.sbParamDistance = QtGui.QSpinBox(self.distance)
        self.sbParamDistance.setGeometry(QtCore.QRect(230, 10, 51, 31))
        self.sbParamDistance.setObjectName(_fromUtf8("sbParamDistance"))
        self.label = QtGui.QLabel(self.distance)
        self.label.setGeometry(QtCore.QRect(20, 10, 221, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.source = QtGui.QWidget(TellusProcessingDialogBase)
        self.source.setGeometry(QtCore.QRect(20, 95, 511, 61))
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
        self.label_2 = QtGui.QLabel(self.source)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 71, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.radioButtonDatabase = QtGui.QRadioButton(TellusProcessingDialogBase)
        self.radioButtonDatabase.setGeometry(QtCore.QRect(290, 40, 117, 22))
        self.radioButtonDatabase.setObjectName(_fromUtf8("radioButtonDatabase"))
        self.buttonLancer = QtGui.QPushButton(TellusProcessingDialogBase)
        self.buttonLancer.setGeometry(QtCore.QRect(360, 250, 80, 16))
        self.buttonLancer.setObjectName(_fromUtf8("buttonLancer"))
        self.buttonAnnuler = QtGui.QPushButton(TellusProcessingDialogBase)
        self.buttonAnnuler.setGeometry(QtCore.QRect(450, 250, 80, 16))
        self.buttonAnnuler.setObjectName(_fromUtf8("buttonAnnuler"))

        self.retranslateUi(TellusProcessingDialogBase)
        QtCore.QMetaObject.connectSlotsByName(TellusProcessingDialogBase)

    def retranslateUi(self, TellusProcessingDialogBase):
        TellusProcessingDialogBase.setWindowTitle(_translate("TellusProcessingDialogBase", "Tellus processing", None))
        self.radioButtonDossier.setText(_translate("TellusProcessingDialogBase", "Dossier", None))
        self.label_3.setText(_translate("TellusProcessingDialogBase", "<html><head/><body><p><span style=\" font-weight:600;\">Source type</span></p></body></html>", None))
        self.radioButtonFichier.setText(_translate("TellusProcessingDialogBase", "Fichier", None))
        self.label.setText(_translate("TellusProcessingDialogBase", "Distance entre chaque points", None))
        self.parcourirBtn.setText(_translate("TellusProcessingDialogBase", "Parcourir", None))
        self.lblDG.setText(_translate("TellusProcessingDialogBase", "Données géoradar", None))
        self.label_2.setText(_translate("TellusProcessingDialogBase", "<html><head/><body><p><span style=\" font-weight:600;\">Source</span></p></body></html>", None))
        self.radioButtonDatabase.setText(_translate("TellusProcessingDialogBase", "Database", None))
        self.buttonLancer.setText(_translate("TellusProcessingDialogBase", "Lancer", None))
        self.buttonAnnuler.setText(_translate("TellusProcessingDialogBase", "Annuler", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TellusProcessingDialogBase = QtGui.QDialog()
    ui = Ui_TellusProcessingDialogBase()
    ui.setupUi(TellusProcessingDialogBase)
    TellusProcessingDialogBase.show()
    sys.exit(app.exec_())
