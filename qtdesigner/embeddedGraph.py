# Embedded graphing
from PyQt4.uic import loadUiType
from matplotlib.figure import * #Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import * #(
    #FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar)

# means there is no design.py generation needed!
Ui_MainWindow, QMainWindow = loadUiType('timeReport.ui')

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, ):
        super(Main, self).__init__()
        self.setupUi(self)

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


if __name__ == '__main__':
    import sys
    from PyQt4 import QtGui
    import numpy as np

    # Set up figure 1
    fig1 = Figure()
    graph1 = fig1.add_subplot(111)
    x = [1,2,3]
    y = [5,4,2]
    graph1.plot(x,y)

    # set up figure 2
    fig2 = Figure()
    graph2 = fig2.add_subplot(111)
    graph2.bar([1,2], [2,8], align='center')
    names = ['hi','yo']
    graph2.set_xticks([1,2])
    graph2.set_xticklabels(names)
    graph2.set_ylabel('Minutes')
    graph2.set_title('Time plot by user')
    
    app = QtGui.QApplication(sys.argv)
    main = Main()

    # Calls graphing
    main.addmpl(fig1)
    main.addmp2(fig2)

    main.show()
    sys.exit(app.exec_())
