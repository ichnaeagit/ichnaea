# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timeReport.ui'
#
# Created: Wed Oct 19 19:13:31 2016
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
        MainWindow.resize(354, 132)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.genReport = QtGui.QPushButton(self.centralwidget)
        self.genReport.setObjectName(_fromUtf8("genReport"))
        self.verticalLayout.addWidget(self.genReport)
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
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.PE = QtGui.QCheckBox(self.centralwidget)
        self.PE.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PE.setObjectName(_fromUtf8("PE"))
        self.horizontalLayout_2.addWidget(self.PE)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.genReport.setText(_translate("MainWindow", "Generate Report", None))
        self.weekRad.setText(_translate("MainWindow", "Current week", None))
        self.monthRad.setText(_translate("MainWindow", "Current month", None))
        self.allRad.setText(_translate("MainWindow", "All time", None))
        self.PE.setText(_translate("MainWindow", "PE group", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))

