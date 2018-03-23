# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_tellus_processing_dialog_base.ui'
#
# Created: Thu Mar 22 21:18:50 2018
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
        TellusProcessingDialogBase.resize(457, 300)
        self.BtnBoxOkCancel = QtGui.QDialogButtonBox(TellusProcessingDialogBase)
        self.BtnBoxOkCancel.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.BtnBoxOkCancel.setOrientation(QtCore.Qt.Horizontal)
        self.BtnBoxOkCancel.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.BtnBoxOkCancel.setObjectName(_fromUtf8("BtnBoxOkCancel"))
        self.widget = QtGui.QWidget(TellusProcessingDialogBase)
        self.widget.setGeometry(QtCore.QRect(0, 10, 451, 41))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.lblDG = QtGui.QLabel(self.widget)
        self.lblDG.setGeometry(QtCore.QRect(10, 0, 91, 21))
        self.lblDG.setObjectName(_fromUtf8("lblDG"))
        self.parcourirBtn = QtGui.QPushButton(self.widget)
        self.parcourirBtn.setGeometry(QtCore.QRect(350, 0, 80, 21))
        self.parcourirBtn.setObjectName(_fromUtf8("parcourirBtn"))
        self.pathLineEdit = QtGui.QLineEdit(self.widget)
        self.pathLineEdit.setGeometry(QtCore.QRect(110, 0, 231, 21))
        self.pathLineEdit.setObjectName(_fromUtf8("pathLineEdit"))

        self.retranslateUi(TellusProcessingDialogBase)
        QtCore.QObject.connect(self.BtnBoxOkCancel, QtCore.SIGNAL(_fromUtf8("accepted()")), TellusProcessingDialogBase.accept)
        QtCore.QObject.connect(self.BtnBoxOkCancel, QtCore.SIGNAL(_fromUtf8("rejected()")), TellusProcessingDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(TellusProcessingDialogBase)

    def retranslateUi(self, TellusProcessingDialogBase):
        TellusProcessingDialogBase.setWindowTitle(_translate("TellusProcessingDialogBase", "Tellus processing", None))
        self.lblDG.setText(_translate("TellusProcessingDialogBase", "Données géoradar", None))
        self.parcourirBtn.setText(_translate("TellusProcessingDialogBase", "Parcourir", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TellusProcessingDialogBase = QtGui.QDialog()
    ui = Ui_TellusProcessingDialogBase()
    ui.setupUi(TellusProcessingDialogBase)
    TellusProcessingDialogBase.show()
    sys.exit(app.exec_())

