# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timeReport.ui'
#
# Created: Wed Oct 26 14:52:10 2016
#      by: PyQt4 UI code generator 4.11.2
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(728, 640)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.genReport = QtGui.QPushButton(self.centralwidget)
        self.genReport.setObjectName(_fromUtf8("genReport"))
        self.verticalLayout.addWidget(self.genReport)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.PE = QtGui.QCheckBox(self.centralwidget)
        self.PE.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PE.setObjectName(_fromUtf8("PE"))
        self.horizontalLayout_2.addWidget(self.PE)
        self.QE = QtGui.QCheckBox(self.centralwidget)
        self.QE.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.QE.setObjectName(_fromUtf8("QE"))
        self.horizontalLayout_2.addWidget(self.QE)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.weekRad = QtGui.QRadioButton(self.centralwidget)
        self.weekRad.setChecked(True)
        self.weekRad.setObjectName(_fromUtf8("weekRad"))
        self.horizontalLayout.addWidget(self.weekRad)
        self.monthRad = QtGui.QRadioButton(self.centralwidget)
        self.monthRad.setObjectName(_fromUtf8("monthRad"))
        self.horizontalLayout.addWidget(self.monthRad)
        self.allRad = QtGui.QRadioButton(self.centralwidget)
        self.allRad.setObjectName(_fromUtf8("allRad"))
        self.horizontalLayout.addWidget(self.allRad)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.genReport_2 = QtGui.QPushButton(self.centralwidget)
        self.genReport_2.setObjectName(_fromUtf8("genReport_2"))
        self.verticalLayout_2.addWidget(self.genReport_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.QE_2 = QtGui.QCheckBox(self.centralwidget)
        self.QE_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.QE_2.setObjectName(_fromUtf8("QE_2"))
        self.horizontalLayout_4.addWidget(self.QE_2)
        self.PE_2 = QtGui.QCheckBox(self.centralwidget)
        self.PE_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PE_2.setObjectName(_fromUtf8("PE_2"))
        self.horizontalLayout_4.addWidget(self.PE_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.allRad_3 = QtGui.QRadioButton(self.centralwidget)
        self.allRad_3.setObjectName(_fromUtf8("allRad_3"))
        self.horizontalLayout_5.addWidget(self.allRad_3)
        self.allRad_2 = QtGui.QRadioButton(self.centralwidget)
        self.allRad_2.setObjectName(_fromUtf8("allRad_2"))
        self.horizontalLayout_5.addWidget(self.allRad_2)
        self.monthRad_2 = QtGui.QRadioButton(self.centralwidget)
        self.monthRad_2.setObjectName(_fromUtf8("monthRad_2"))
        self.horizontalLayout_5.addWidget(self.monthRad_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mlpfigs = QtGui.QListWidget(self.centralwidget)
        self.mlpfigs.setObjectName(_fromUtf8("mlpfigs"))
        self.gridLayout.addWidget(self.mlpfigs, 0, 1, 1, 1)
        self.mpwindow = QtGui.QWidget(self.centralwidget)
        self.mpwindow.setObjectName(_fromUtf8("mpwindow"))
        self.mplvl = QtGui.QVBoxLayout(self.mpwindow)
        self.mplvl.setMargin(0)
        self.mplvl.setObjectName(_fromUtf8("mplvl"))
        self.gridLayout.addWidget(self.mpwindow, 1, 0, 1, 1)
        self.mplfigs = QtGui.QListWidget(self.centralwidget)
        self.mplfigs.setMinimumSize(QtCore.QSize(0, 20))
        self.mplfigs.setObjectName(_fromUtf8("mplfigs"))
        self.gridLayout.addWidget(self.mplfigs, 0, 0, 1, 1)
        self.mplwindow = QtGui.QWidget(self.centralwidget)
        self.mplwindow.setMinimumSize(QtCore.QSize(0, 400))
        self.mplwindow.setObjectName(_fromUtf8("mplwindow"))
        self.mplvl_2 = QtGui.QVBoxLayout(self.mplwindow)
        self.mplvl_2.setMargin(0)
        self.mplvl_2.setObjectName(_fromUtf8("mplvl_2"))
        self.gridLayout.addWidget(self.mplwindow, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.genReport.setText(_translate("MainWindow", "Graph all users per group", None))
        self.PE.setText(_translate("MainWindow", "PE group", None))
        self.QE.setText(_translate("MainWindow", "QE Group", None))
        self.weekRad.setText(_translate("MainWindow", "Current week", None))
        self.monthRad.setText(_translate("MainWindow", "Current month", None))
        self.allRad.setText(_translate("MainWindow", "All time", None))
        self.genReport_2.setText(_translate("MainWindow", "Graph individual users by project", None))
        self.QE_2.setText(_translate("MainWindow", "QE Group", None))
        self.PE_2.setText(_translate("MainWindow", "PE group", None))
        self.allRad_3.setText(_translate("MainWindow", "Current Week", None))
        self.allRad_2.setText(_translate("MainWindow", "Current Month", None))
        self.monthRad_2.setText(_translate("MainWindow", "Current Week", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))

