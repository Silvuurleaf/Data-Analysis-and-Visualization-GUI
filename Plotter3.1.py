import sys
#Importing PyQt5 library to construct widgets for Graphic User Interface (GUI) application
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QSlider, QApplication, QVBoxLayout, QHBoxLayout,
                             QApplication, QWidget, QLabel, QCheckBox, QRadioButton, QPlainTextEdit, QSizePolicy,
                             QMainWindow,QFrame, QFileDialog, QTableWidgetItem, QTableWidget, QMenu, QMessageBox,
                             QAction, QToolBar)
from PyQt5.QtCore import Qt, QAbstractTableModel


import matplotlib
matplotlib.use("Qt5Agg")


from numpy import arange, sin, pi

from matplotlib import pyplot as plt

#Backend door for matplotlib importation required to use Pyqt with matpltlib libray
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationBar
from matplotlib.figure import Figure

import csv
import pandas as pd
import numpy as np



"""
### PYQT LEGEND ###

Qlabel = block of text non-interactable
QPushButton = ordinary button that can be pushed/interacted with
QLineEdit = text input box and can be interacted with
QSlider = slider widget moved back/forth up/down to change the value of something
QCheckbox = interactable checkbox

"""

#Create Canvas to plot data on
# class CanvasCreation(FigureCanvas):
#
#     def __init__(self, parent):
#         self.figure = Figure()
#         self.axes = self.figure.add_subplot(111)
#         self.axes.hold(False)
#
#         #draws the figure
#         FigureCanvas.__init__(self, self.figure)
#
#         self.axes.legend()
#
#         FigureCanvas.setSizePolicy(self,
#                                    QSizePolicy.Expanding,
#                                    QSizePolicy.Expanding)
#         FigureCanvas.updateGeometry(self)
#
# class MatpltWidget(QWidget): #MatpltlibWidget
#     def __init__(self, parent=None):
#         QWidget.__init__(self, parent)
#         self.canvas = CanvasCreation()
#         self.vboxRight.addWidget(self.canvas)
#     def Plotter(self, ydata, xdata):
#         x = range(0, 10)
#         y = range(0, 20, 2)
#         self.canvas.axes.plot(x,y)
#         self.canvas.draw()

"""
Purpose of CanvasCreation is to initialize the creation of a canvas where graphs and plots can be displayed on and inherit aspects of the class
"""
class CanvasCreation(FigureCanvas):

    def __init__(self, parent):
        #Create an object figure where a graph(s) can be displayed
        self.figure = Figure()
        #defines a variable axes to besubplot where we will plot our data. The numbers 111 represent plot sub-number
        self.axes = self.figure.add_subplot(111)
        #this resets the canvas each time the class is called (clears)
        self.axes.hold(False)


        #NOTESELF:need to grab a class to get the data

        #self.x = np.arange(0.0, 5, 0.01)
        #self.y = np.cos(1 * np.pi * self.x)
        #self.axes.plot(self.x, self.y)


        #draws the figure
        FigureCanvas.__init__(self, self.figure)

        self.axes.legend()

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

class Plotter(CanvasCreation):
    print("in plotter")
    def __init__(self, y_data, x_data): #mutltiple graphs???, overlay, side by side??, GraphHeader, x_title, y_title
            print("in initialization")

            #super(MainWindow, self).__init__()
            self.figure = Figure()
            self.axes = self.figure.add_subplot(111)
            print("data is about to be defined")
            print(y_data)
            print(x_data)
            self.x = np.arange(0.0, 5.0, 0.01)
            self.y = np.cos(5 * np.pi * self.x)

            #self.x = [0,1,2,3,4,5,6,7,8,9]
            #self.y = y_data

            print("data has been defined about to plot")

            self.axes.plot(self.x, self.y)
            print("after plot next step is draw")

            FigureCanvas.__init__(self, self.figure)

            self.show()

            #self.figure.canvas.draw()

            #self.vboxRight.addWidget(self.axes)

            print("data has been assigned right before plot is called")



class MainWindow(QMainWindow):
    """
        MainWindow class will be the centeral widget and main screen for application
        Inherits behavior from the class QMainWindow from PyQt5 library.
        *see index for difference between QMainWindow and QWidget

        Purpose: Creation of widgets and controls their layout
    """


    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Perspective")

        self.initializeUI()

    def initializeUI(self):

        #Main Widget
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)


        #CREATION OF WIDGETS
        # <editor-fold desc="Widgets Creation Site">

        ###Graph Title Entry###
        #button and line entry made to change the name of the graph before or after data has been plotted
        self.TitlEdit = QLineEdit('Graph Title')
        self.TitleBtn = QPushButton('Enter')

        ###first file###
        #buttons associated with the first browse button
        """
            Buttons related to the first file being uploaded
        """
        self.FileNmLabel = QLabel('FileName')
        self.FileNameEdit = QLineEdit('"Filename"')
        self.BrowseBtn = QPushButton('Browse')

        self.OpacityLabel = QLabel('Opacity')
        self.OpacitySlider = QSlider(Qt.Horizontal)
        self.OpacitySlider.setMinimum(0)
        self.OpacitySlider.setMaximum(100)
        self.OpacitySlider.setValue(100)
        self.OpacitySlider.setTickInterval(10)
        self.OpacitySlider.setTickPosition(QSlider.TicksBelow)

        self.ShowChkbx = QCheckBox('show')


        ###Plot Selection###
        #Radiobuttons are choosen because the difference between radio and check buttons are that only one radio button can be selected at any given time
        #give user ability to choose between Boxplot, whisker, or scatter
        self.BoxPlt = QRadioButton('Box Plot')
        self.WhiskerPlt = QRadioButton('Whisker Plot')
        self.ScatterPlt = QRadioButton('Scatter Plot')

        #NOTE SELF:for functionality .toggled() might be more appropriate than .clicked()

        ###Overlay Plot###
        #checkbox to give user ability to overlay data
        self.Overlay = QCheckBox('Overlay Plots')




        #self.canvas....


        # <editor-fold desc="Trend Report Button Repetition">

        ###2nd trend report###
        self.FileNmLabel2 = QLabel('FileNames')
        self.FileNameEdit2 = QLineEdit('')
        self.BrowseBtn2 = QPushButton('Browse')

        self.OpacityLabel2 = QLabel('Opacity')

        self.OpacitySlider2 = QSlider(Qt.Horizontal)
        self.OpacitySlider2.setMinimum(0)
        self.OpacitySlider2.setMaximum(100)
        self.OpacitySlider2.setValue(100)
        self.OpacitySlider2.setTickInterval(10)
        self.OpacitySlider2.setTickPosition(QSlider.TicksBelow)

        self.ShowChkbx2 = QCheckBox('show')

        ###3rd report###
        self.FileNmLabel3 = QLabel('FileNames')
        self.FileNameEdit3 = QLineEdit('')
        self.BrowseBtn3 = QPushButton('Browse')

        self.OpacityLabel3 = QLabel('Opacity')

        self.OpacitySlider3 = QSlider(Qt.Horizontal)
        self.OpacitySlider3.setMinimum(0)
        self.OpacitySlider3.setMaximum(100)
        self.OpacitySlider3.setValue(100)
        self.OpacitySlider3.setTickInterval(10)
        self.OpacitySlider3.setTickPosition(QSlider.TicksBelow)

        self.ShowChkbx3 = QCheckBox('show')


        ###TEXT EDIT TEST WIDGET
        self.TextEdit = QPlainTextEdit()

        # </editor-fold>________________________________________END OF TREND REPORTS

        ###PLOT###________________________________________________________EXPIREMENTAL AF


        #self.figure = Figure()  # don't use matplotlib.pyplot at all!
        #self.canvas = FigureCanvas(self.figure)

        self.canvas = CanvasCreation(self.main_widget)
        self.NavBar = NavigationBar(self.canvas, self.main_widget)

        # </editor-fold> ________________________________________END OF CREATION WIDGETS


        #Button Functionality___________________________________________________________________________________________
        # <editor-fold desc="Button Functionality">

        ###Graph Title###
        self.TitleBtn.clicked.connect(self.TitleClicked)

        #import1
        self.BrowseBtn.clicked.connect(self.import1)

        self.OpacitySlider.valueChanged.connect(self.OpacityVal)

        ###GraphChoice###
        #self.CatDogBtn.clicked.connect(lambda :self.CatDog_click(self.RadioBtn1.isChecked(), self.RadioLabel))
        #self.BoxPlt.toggled.connect(lambda: self.PlotChoice(self.WhiskerPlt.isChecked(), self.ScatterPlt.isChecked()))
        self.BoxPlt.clicked.connect(self.PlotChoice)
        self.WhiskerPlt.clicked.connect(self.PlotChoice)
        self.ScatterPlt.clicked.connect(self.PlotChoice)


        ##Table###


        # </editor-fold>_____________________________________________________________________END OF BUTTON FUNCTIONALITY


        #Widget Layout
        # <editor-fold desc="Layout">


        self.hMAIN = QHBoxLayout(self.main_widget)

        ###Graph Title###
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.TitlEdit)
        self.hbox.addWidget(self.TitleBtn)
        self.hbox.addStretch()

        ###First File Labels###
        self.hbox2 = QHBoxLayout()
        self.hbox2.addWidget(self.FileNmLabel)
        self.hbox2.addStretch()
        self.hbox2.addWidget(self.OpacityLabel)

        ###First File Widgets###
        self.hbox3 = QHBoxLayout()
        self.hbox3.addWidget(self.FileNameEdit)
        self.hbox3.addWidget(self.BrowseBtn)
        self.hbox3.addWidget(self.OpacitySlider)
        self.hbox3.addWidget(self.ShowChkbx)

        ###Plot Types###
        self.hbox4 = QHBoxLayout()
        self.hbox4.addWidget(self.BoxPlt)
        self.hbox4.addWidget(self.WhiskerPlt)
        self.hbox4.addWidget(self.ScatterPlt)

        ###OverLay###
        self.hbox5 = QHBoxLayout()
        self.hbox5.addWidget(self.Overlay)


        #________________________________________________Additional Trend Reports
        # <editor-fold desc="ADDITIONAL TREND REPORTS">
        ###Second File Labels###
        self.hbox6 = QHBoxLayout()
        self.hbox6.addWidget(self.FileNmLabel2)
        self.hbox6.addStretch()
        self.hbox6.addWidget(self.OpacityLabel2)

        ###Second File Widgets###
        self.hbox7 = QHBoxLayout()
        self.hbox7.addWidget(self.FileNameEdit2)
        self.hbox7.addWidget(self.BrowseBtn2)
        self.hbox7.addWidget(self.OpacitySlider2)
        self.hbox7.addWidget(self.ShowChkbx2)

        ###3rd File Widgets###
        self.hbox8 = QHBoxLayout()
        self.hbox8.addWidget(self.FileNmLabel3)
        self.hbox8.addStretch()
        self.hbox8.addWidget(self.OpacityLabel3)

        ###Second File Widgets###
        self.hbox9 = QHBoxLayout()
        self.hbox9.addWidget(self.FileNameEdit3)
        self.hbox9.addWidget(self.BrowseBtn3)
        self.hbox9.addWidget(self.OpacitySlider3)
        self.hbox9.addWidget(self.ShowChkbx3)
        # </editor-fold>

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.vbox.addLayout(self.hbox5)
        self.vbox.addLayout(self.hbox6)
        self.vbox.addLayout(self.hbox7)
        self.vbox.addLayout(self.hbox8)
        self.vbox.addLayout(self.hbox9)

        self.vboxRightBottom = QVBoxLayout()



        self.vboxRIGHT = QVBoxLayout()
        #vboxRIGHT.addWidget(Plot)
        self.vboxRIGHT.addWidget(self.canvas)
        self.vboxRIGHT.addWidget(self.NavBar)
        self.vboxRIGHT.addLayout(self.vboxRightBottom)




        self.hMAIN.addLayout(self.vbox)
        self.hMAIN.addLayout(self.vboxRIGHT)

        # </editor-fold>___________________________________________________________________________________END OF LAYOUT



        self.show()

    def import1(self):
        ###Actual importation and manipulation of Data CSV Files
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                      "(*.csv)")
        if fileName:
            print(fileName)
            self.FileNameEdit.setText(fileName)
            Data = pd.read_csv(open(fileName))
            #print(Data)

            self.BaseStats = Data.drop('Nominal Value', axis=1)
            self.BaseStats.drop('median', axis=1, inplace=True)
            self.BaseStats.drop('Tolerance', axis=1, inplace=True)
            self.BaseStats.drop('mean', axis=1, inplace=True)
            self.BaseStats.drop('min', axis=1, inplace=True)
            self.BaseStats.drop('max', axis=1, inplace=True)
            self.BaseStats.drop('range', axis=1, inplace=True)
            self.BaseStats.drop('Deviation', axis=1, inplace=True)
            self.BaseStats.drop('variance', axis=1, inplace=True)
            self.BaseStats.drop('Standard Deviation', axis=1, inplace=True)
            self.BaseStats.drop('LowerBound', axis=1, inplace=True)
            self.BaseStats.drop('UpperBound', axis=1, inplace=True)
            self.BaseStats.drop('Unnamed: 0', axis=1, inplace=True)

            #print("Data has been dropped")

            rowHeaders = self.BaseStats.index
            colHeaders = self.BaseStats.columns.values

            col = len(colHeaders)
            row = len(rowHeaders)

            print("table is about to be made")

            self.Table = CreateTable(self.BaseStats, row, col, colHeaders, rowHeaders)

            self.vboxRightBottom.addWidget(self.Table)



    def PlotChoice(self):
        sender = self.sender()
        if sender.text() == "Whisker Plot":
            #set the graph to whisker plot
            print("whisker plot has been selected")
        elif sender.text() == "Box Plot":
            print("Box Plot has been selected")
        else:
            print("Scatter Plot has been selected")

    def TitleClicked(self):
        print("Enter Title")
        sender = self.sender()
        if sender.text() == "Enter":
            ax.set_title(self.TitlEdit.text())
            self.canvas.draw()
    def OpacityVal(self):
        print("Opacity value is being changed")

class QTable(QTableWidget):
  def __init__(self):
    super(QTable, self).__init__()
class PassMain(MainWindow):
  def __init__(self):
    super(PassMain, self).__init__()
class PassMainTable(PassMain, QTable):
  def __init__(self):
    super(PassMainTable, self).__init__()

class CreateTable(PassMainTable): #QTableWidget
    def __init__(self, Data, row, col, colHeaders, rowHeaders): #Index, ColumnHeaders
        super(CreateTable, self).__init__()


        self.setSelectionBehavior(self.SelectRows)

        print("Start initialization")
        self.ColHeader = colHeaders
        self.setRowCount(row)
        self.setColumnCount(col)
        self.data = Data
        self.setHorizontalHeaderLabels(colHeaders)

        print("Right before for loop")

        n = len(Data)
        m = len(colHeaders)

        for i in range(n):
            DataValues = self.data.iloc[i,:]
            print("values are {}".format(DataValues))
            #m = len(values)
            ConvertedVals = pd.to_numeric(DataValues)

            ValList = DataValues.values.tolist()
            print(ValList)

            for j in range(0,m):
                self.item = QTableWidgetItem(str(round(ValList[j],5)))
                #print("{}, {}".format(i, j))
                self.setItem(i,j, self.item)

    def contextMenuEvent(self, event):

        menu = QMenu(self)
        graphAction = menu.addAction("Graph")
        compareAction = menu.addAction("Compare")
        scatterAction = menu.addAction("Plot types")
        aboutAction = menu.addAction("about")
        quitAction = menu.addAction("quit")
        printAction = menu.addAction("Print Row")
        action = menu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAction:
            qApp.quit()
        elif action == printAction:
            self.selected = self.selectedItems()
            n = len(self.selected)
            print("n is {}".format(n))
            for i in range(n):
                self.selected[i] = str(self.selected[i].text())
            for i in range(n):
                self.selected[i] = float(self.selected[i])
            print(self.selected)
        elif action == graphAction:
            self.selected = self.selectedItems()
            n = len(self.selected)
            for i in range(n):
                self.selected[i] = str(self.selected[i].text())
            for i in range(n):
                self.selected[i] = float(self.selected[i])
            print("right before plotter called")

            self.Graph = Plotter(self.selected, self.ColHeader)

            self.vboxRight.addWidget(self.Graph)
        else:
            print("u clicked something other than quit")


def main():
    #main loop
    app = QtWidgets.QApplication(sys.argv)
    #instance
    appWindow = MainWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
