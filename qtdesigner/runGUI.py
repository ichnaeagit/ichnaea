from PyQt4 import QtGui # Import the PyQt4 module we'll need
import sys # We need sys so that we can pass argv to QApplication
import graphTime
# For embedded graphing
from PyQt4.uic import loadUiType
from matplotlib.figure import * #Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import *

import design # This file holds our MainWindow and all design related things
              # it also keeps events etc that we defined in Qt Designer

class Main(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self, ):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(Main, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined
        self.genReport.clicked.connect(self.createReport)

    # define figure one
    def addmpl(self, fig1):
        self.canvas = FigureCanvas(fig1)
        self.mplvl.addWidget(self.canvas)
        self.canvas.draw()

    # define figure two
    def addmp2 (self, fig2):
        self.canvas = FigureCanvas(fig2)
        self.mplvl_2.addWidget(self.canvas)
        self.canvas.draw()
    

    def createReport(self):
        # sets durration for report
        if self.weekRad.isChecked():
            durr = 1
        if self.monthRad.isChecked():
            durr = 4
        if self.allRad.isChecked():
            durr = 0
        # Sets scope of report

        if self.PE.isChecked():
            group = ["PE"]
        else:
            print "you must pick a group"
            return 

        print "Graphing!"

        graphInfo = graphTime.graph(durr, group)


def mainProgram():

    import sys
    from PyQt4 import QtGui
    import numpy as np

    # Set up figure 1
    fig1 = Figure()
    graph1 = fig1.add_subplot(111)
    x = [1,2,3,4,5,6,7,8,9,10]
    y = [2,4,8,12,13,16,18,20,19,23]
    graph1.plot(x,y)
    graph1.set_ylabel('Minutes')
    graph1.set_title('Example plot')

    # set up figure 2
    fig2 = Figure()
    graph2 = fig2.add_subplot(111)
    graph2.bar([1,2], [2,8], align='center')
    names = ['A','B']
    graph2.set_xticks([1,2])
    graph2.set_xticklabels(names)
    graph2.set_ylabel('Minutes')
    graph2.set_title('Time plot by user')

    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    main = Main()                 # We set the form to be our mainApp (design)

    # Calls graphing
    main.addmpl(fig1)
    main.addmp2(fig2)

    main.show()                         # Show the form
    sys.exit(app.exec_())
    #app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    mainProgram()                              # run the main function
