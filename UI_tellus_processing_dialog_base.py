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
        TellusProcessingDialogBase.resize(568, 533)
        self.traces = QtGui.QWidget(TellusProcessingDialogBase)
        self.traces.setGeometry(QtCore.QRect(10, 180, 551, 171))
        self.traces.setObjectName(_fromUtf8("traces"))
        self.lblFiltre = QtGui.QLabel(self.traces)
        self.lblFiltre.setGeometry(QtCore.QRect(290, 10, 41, 17))
        self.lblFiltre.setObjectName(_fromUtf8("lblFiltre"))
        self.tableWidget = QtGui.QTableWidget(self.traces)
        self.tableWidget.setGeometry(QtCore.QRect(10, 30, 531, 141))
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.setColumnWidth(5,27)
        self.tableWidget.verticalHeader().setVisible(False)
        self.lblVisualisation = QtGui.QLabel(self.traces)
        self.lblVisualisation.setGeometry(QtCore.QRect(430, 10, 101, 17))
        self.lblVisualisation.setObjectName(_fromUtf8("lblVisualisation"))
        self.frame2 = QtGui.QFrame(self.traces)
        self.frame2.setGeometry(QtCore.QRect(210, 0, 201, 31))
        self.frame2.setStyleSheet(_fromUtf8("border:1px solid lightgrey;"))
        self.frame2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame2.setObjectName(_fromUtf8("frame2"))
        self.frame3 = QtGui.QFrame(self.traces)
        self.frame3.setGeometry(QtCore.QRect(410, 0, 131, 31))
        self.frame3.setStyleSheet(_fromUtf8("border:1px solid lightgrey;border-top-right-radius: 5px;"))
        self.frame3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame3.setObjectName(_fromUtf8("frame3"))
        self.lblInfos = QtGui.QLabel(self.traces)
        self.lblInfos.setGeometry(QtCore.QRect(90, 10, 41, 17))
        self.lblInfos.setObjectName(_fromUtf8("lblInfos"))
        self.frame1 = QtGui.QFrame(self.traces)
        self.frame1.setGeometry(QtCore.QRect(10, 0, 201, 31))
        self.frame1.setStyleSheet(_fromUtf8("border:1px solid lightgrey;border-top-left-radius: 5px;"))
        self.frame1.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtGui.QFrame.Raised)
        self.frame1.setObjectName(_fromUtf8("frame1"))
        self.frame3.raise_()
        self.frame2.raise_()
        self.lblFiltre.raise_()
        self.tableWidget.raise_()
        self.lblVisualisation.raise_()
        self.lblInfos.raise_()
        self.frame1.raise_()
        self.source = QtGui.QWidget(TellusProcessingDialogBase)
        self.source.setGeometry(QtCore.QRect(10, 110, 551, 61))
        self.source.setObjectName(_fromUtf8("source"))
        self.parcourirBtn = QtGui.QPushButton(self.source)
        self.parcourirBtn.setGeometry(QtCore.QRect(450, 30, 80, 31))
        self.parcourirBtn.setObjectName(_fromUtf8("parcourirBtn"))
        self.lblDG = QtGui.QLabel(self.source)
        self.lblDG.setGeometry(QtCore.QRect(10, 30, 131, 31))
        self.lblDG.setObjectName(_fromUtf8("lblDG"))
        self.pathLineEdit = QtGui.QLineEdit(self.source)
        self.pathLineEdit.setGeometry(QtCore.QRect(150, 30, 291, 31))
        self.pathLineEdit.setObjectName(_fromUtf8("pathLineEdit"))
        self.lblSource = QtGui.QLabel(self.source)
        self.lblSource.setGeometry(QtCore.QRect(10, 10, 71, 17))
        self.lblSource.setObjectName(_fromUtf8("lblSource"))
        self.buttonLancer = QtGui.QPushButton(TellusProcessingDialogBase)
        self.buttonLancer.setGeometry(QtCore.QRect(470, 410, 80, 31))
        self.buttonLancer.setObjectName(_fromUtf8("buttonLancer"))
        self.buttonAnnuler = QtGui.QPushButton(TellusProcessingDialogBase)
        self.buttonAnnuler.setGeometry(QtCore.QRect(380, 410, 80, 31))
        self.buttonAnnuler.setObjectName(_fromUtf8("buttonAnnuler"))
        self.buttonExporter = QtGui.QPushButton(TellusProcessingDialogBase)
        self.buttonExporter.setGeometry(QtCore.QRect(40, 410, 80, 31))
        self.buttonExporter.setObjectName(_fromUtf8("buttonExporter"))
        self.distance = QtGui.QWidget(TellusProcessingDialogBase)
        self.distance.setGeometry(QtCore.QRect(10, 350, 541, 51))
        self.distance.setObjectName(_fromUtf8("distance"))
        self.lblDistance = QtGui.QLabel(self.distance)
        self.lblDistance.setGeometry(QtCore.QRect(10, 20, 261, 31))
        self.lblDistance.setObjectName(_fromUtf8("lblDistance"))
        self.sbParamDistance = QtGui.QSpinBox(self.distance)
        self.sbParamDistance.setGeometry(QtCore.QRect(290, 20, 71, 27))
        self.sbParamDistance.setMaximum(100000000)
        self.sbParamDistance.setObjectName(_fromUtf8("sbParamDistance"))
        self.label = QtGui.QLabel(TellusProcessingDialogBase)
        self.label.setGeometry(QtCore.QRect(27, 460, 230, 64))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(TellusProcessingDialogBase)
        self.label_2.setGeometry(QtCore.QRect(360, 460, 185, 64))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(TellusProcessingDialogBase)
        self.label_3.setGeometry(QtCore.QRect(150, 10, 278, 86))
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.frame = QtGui.QFrame(TellusProcessingDialogBase)
        self.frame.setGeometry(QtCore.QRect(10, 110, 551, 341))
        self.frame.setStyleSheet(_fromUtf8("border:1px solid lightgrey;border-radius: 5px;"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frameHeader = QtGui.QFrame(TellusProcessingDialogBase)
        self.frameHeader.setGeometry(QtCore.QRect(-10, 0, 581, 101))
        self.frameHeader.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.frameHeader.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameHeader.setFrameShadow(QtGui.QFrame.Raised)
        self.frameHeader.setObjectName(_fromUtf8("frameHeader"))
        self.frameHeader.raise_()
        self.frame.raise_()
        self.traces.raise_()
        self.source.raise_()
        self.buttonLancer.raise_()
        self.buttonAnnuler.raise_()
        self.buttonExporter.raise_()
        self.distance.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()

        self.retranslateUi(TellusProcessingDialogBase)
        QtCore.QMetaObject.connectSlotsByName(TellusProcessingDialogBase)

    def retranslateUi(self, TellusProcessingDialogBase):
        TellusProcessingDialogBase.setWindowTitle(_translate("TellusProcessingDialogBase", "Tellus processing", None))
        self.lblFiltre.setText(_translate("TellusProcessingDialogBase", "<html><head/><body><p><span style=\" font-weight:600;\">Filtre</span></p></body></html>", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("TellusProcessingDialogBase", "Name", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("TellusProcessingDialogBase", "Nb traces", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("TellusProcessingDialogBase", "From", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("TellusProcessingDialogBase", "To", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("TellusProcessingDialogBase", "Radagram", None))
        self.lblVisualisation.setText(_translate("TellusProcessingDialogBase", "<html><head/><body><p><span style=\" font-weight:600;\">Visualisation</span></p></body></html>", None))
        self.lblInfos.setText(_translate("TellusProcessingDialogBase", "<html><head/><body><p><span style=\" font-weight:600;\">Infos</span></p></body></html>", None))
        self.parcourirBtn.setText(_translate("TellusProcessingDialogBase", "Parcourir", None))
        self.lblDG.setText(_translate("TellusProcessingDialogBase", "Données géoradar", None))
        self.lblSource.setText(_translate("TellusProcessingDialogBase", "<html><head/><body><p><span style=\" font-weight:600;\">Source</span></p></body></html>", None))
        self.buttonLancer.setText(_translate("TellusProcessingDialogBase", "Lancer", None))
        self.buttonAnnuler.setText(_translate("TellusProcessingDialogBase", "Annuler", None))
        self.buttonExporter.setText(_translate("TellusProcessingDialogBase", "Exporter", None))
        self.lblDistance.setText(_translate("TellusProcessingDialogBase", "Distance entre chaque points (en cm)", None))
        self.label.setText(_translate("TellusProcessingDialogBase", "<html><head/><body><p><img src=\":/plugins/TellusProcessing/istic.png\"/></p></body></html>", None))
        self.label_2.setText(_translate("TellusProcessingDialogBase", "<html><head/><body><p><img src=\":/plugins/TellusProcessing/rennes1.png\"/></p></body></html>", None))
        self.label_3.setText(_translate("TellusProcessingDialogBase", "<html><head/><body><p><img src=\":/plugins/TellusProcessing/tellus.png\"/></p></body></html>", None))

