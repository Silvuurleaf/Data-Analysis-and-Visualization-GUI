import sys
#Importing PyQt5 library to construct widgets for Graphic User Interface (GUI) application
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QSlider, QApplication, QVBoxLayout, QHBoxLayout,
                             QApplication, QWidget, QLabel, QCheckBox, QRadioButton, QPlainTextEdit, QSizePolicy,
                             QMainWindow,QFrame, QFileDialog, QTableWidgetItem, QTableWidget)
from PyQt5.QtCore import Qt, QAbstractTableModel

import matplotlib
matplotlib.use("Qt5Agg")
from PyQt5 import QtCore

from numpy import arange, sin, pi

from matplotlib import pyplot as plt

#Backend door for matplotlib importation required to use Pyqt with matpltlib libray
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationBar
from matplotlib.figure import Figure

import csv
import pandas as pd
import numpy as np




#<editor-fold desc="Ideas for implementation of DataTable">
# class TableWidget(QAbstractTableModel):
#     def __init__(self, parent=None, *args):
#         super(TableModel, self).__init__()
#         self.datatable = None
#
#     def update(self, dataIn):
#         print('Updating Model')
#         self.datatable = dataIn
#         print('Datatable : {0}').format(self.datatable)
# class TableCreation(QtableWidgetItem):
#     def __init__(self):
#         self.tableWidget = QTableWidget()
#</editor-fold>

"""
### PYQT LEGEND ###

Qlabel = block of text non-interactable
QPushButton = ordinary button that can be pushed/interacted with
QLineEdit = text input box and can be interacted with
QSlider = slider widget moved back/forth up/down to change the value of something
QCheckbox = interactable checkbox

"""

#Create Canvas to plot data on
class CanvasCreation(FigureCanvas):

    def __init__(self, parent):
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)


        #NOTESELF:need to grab a class to get the data

        self.x = np.arange(0.0, 3.0, 0.01)
        self.y = np.cos(2 * np.pi * self.x)
        self.axes.plot(self.x, self.y)

        #draws the figure
        FigureCanvas.__init__(self, self.figure)

        # #Max/mins for x and y axis
        # self.axes.set_xlim(0,5)
        # self.axes.set_ylim(-3,3)
        # self.axes.set_autoscale_on(False)

        self.axes.legend()

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

class Plotter(CanvasCreation):
    def __init__(self, data): #mutltiple graphs???, overlay, side by side??, GraphHeader, x_title, y_title
        self.data = data
        #self.GraphHeader = GraphHeader
        #self.x_Axes = x_title
        #self.y_Axes = y_title

class CreateTable(QTableWidget):
    """
        All the commentted out sections here are for when I want to import real csv data and store it in my QtableWidget
        Commented out sections can be ignorned
    """
    #def __init__(self, Data, row, col, colHeaders, rowHeaders, parent = None): #Index, ColumnHeaders,
    def __init__(self):
        # self.tableWidget = QTableWidget()
        # self.tableWidget.setRowCount(row)
        # self.tableWidget.setColumnCount(col)
        # self.data = Data
        # self.setHorizontalHeaderLabels(colHeaders)
        #
        # # for row, columnvalues in enumerate(data):
        # #     for column, value in enumerate(columnvalues):
        # #         item = QTableWidgetItem(value)
        # #         mytable.setItem(row, column, item)
        # n = len(Data)
        # for i in range(n):
        #     values = BaseStats.iloc[i, :]
        #     m = len(values)
        #     ConvertedVals = pd.to_numeric(values)
        #     for index, val in ConvertedVals.iteritems():
        #         item = QTableWidgetItem(val)
        #         self.tableWidget.setItem(n,m,item)




        #Test Data Static Example QTableWidget
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setItem(0,0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setItem(1,0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget.setItem(1,1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget.setItem(2,0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget.setItem(2,1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget.setItem(3,0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget.setItem(3,1, QTableWidgetItem("Cell (4,2)"))





class MainWindow(QMainWindow):
    """
        MainWindow class will be the centeral widget and main screen for application
        Inherits behavior from the class QMainWindow from PyQt5 library.
        *see index for difference between QMainWindow and QWidget

        Purpose: Creation of widgets and controls their layout
    """


    def __init__(self):
        super().__init__()

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

        # </editor-fold>_____________________________________________________________________END OF BUTTON FUNCTIONALITY


        #Widget Layout
        # <editor-fold desc="Layout">


        hMAIN = QHBoxLayout(self.main_widget)

        ###Graph Title###
        hbox = QHBoxLayout()
        hbox.addWidget(self.TitlEdit)
        hbox.addWidget(self.TitleBtn)
        hbox.addStretch()

        ###First File Labels###
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.FileNmLabel)
        hbox2.addStretch()
        hbox2.addWidget(self.OpacityLabel)

        ###First File Widgets###
        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.FileNameEdit)
        hbox3.addWidget(self.BrowseBtn)
        hbox3.addWidget(self.OpacitySlider)
        hbox3.addWidget(self.ShowChkbx)

        ###Plot Types###
        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.BoxPlt)
        hbox4.addWidget(self.WhiskerPlt)
        hbox4.addWidget(self.ScatterPlt)

        ###OverLay###
        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.Overlay)


        #________________________________________________Additional Trend Reports
        # <editor-fold desc="ADDITIONAL TREND REPORTS">
        ###Second File Labels###
        hbox6 = QHBoxLayout()
        hbox6.addWidget(self.FileNmLabel2)
        hbox6.addStretch()
        hbox6.addWidget(self.OpacityLabel2)

        ###Second File Widgets###
        hbox7 = QHBoxLayout()
        hbox7.addWidget(self.FileNameEdit2)
        hbox7.addWidget(self.BrowseBtn2)
        hbox7.addWidget(self.OpacitySlider2)
        hbox7.addWidget(self.ShowChkbx2)

        ###3rd File Widgets###
        hbox8 = QHBoxLayout()
        hbox8.addWidget(self.FileNmLabel3)
        hbox8.addStretch()
        hbox8.addWidget(self.OpacityLabel3)

        ###Second File Widgets###
        hbox9 = QHBoxLayout()
        hbox9.addWidget(self.FileNameEdit3)
        hbox9.addWidget(self.BrowseBtn3)
        hbox9.addWidget(self.OpacitySlider3)
        hbox9.addWidget(self.ShowChkbx3)
        # </editor-fold>

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)
        vbox.addLayout(hbox6)
        vbox.addLayout(hbox7)
        vbox.addLayout(hbox8)
        vbox.addLayout(hbox9)

        vboxRightBottom = QVBoxLayout()


        vboxRIGHT = QVBoxLayout()
        #vboxRIGHT.addWidget(Plot)
        vboxRIGHT.addWidget(self.canvas)
        vboxRIGHT.addWidget(self.NavBar)
        vboxRIGHT.addLayout(vboxRightBottom)




        hMAIN.addLayout(vbox)
        hMAIN.addLayout(vboxRIGHT)

        # </editor-fold>___________________________________________________________________________________END OF LAYOUT


        #self.setCentralWidget(self.main_widget)


        self.show()
    def import1(self):
        self.Table = CreateTable()

        #In my main window I have essentially 3 sections left, top right, and bottom right. I want my
        #DataTable to be in the bottom right corner
        vboxRightBottom.addWidget(self.Table)
    def import2(self):
        ###Actual importation and manipulation of Data CSV Files
        # fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
        #                                               "(*.csv)")
        # if fileName:
        #     print(fileName)
        #     self.FileNameEdit.setText(fileName)
        #     Data = pd.read_csv(open(fileName))
        #     print(Data)
        #
        #     BaseStats = Data.drop('Nominal Value', axis=1)
        #     BaseStats.drop('median', axis=1, inplace=True)
        #     BaseStats.drop('Tolerance', axis=1, inplace=True)
        #     BaseStats.drop('mean', axis=1, inplace=True)
        #     BaseStats.drop('min', axis=1, inplace=True)
        #     BaseStats.drop('max', axis=1, inplace=True)
        #     BaseStats.drop('range', axis=1, inplace=True)
        #     BaseStats.drop('Deviation', axis=1, inplace=True)
        #     BaseStats.drop('variance', axis=1, inplace=True)
        #     BaseStats.drop('Standard Deviation', axis=1, inplace=True)
        #     BaseStats.drop('LowerBound', axis=1, inplace=True)
        #     BaseStats.drop('UpperBound', axis=1, inplace=True)
        #     BaseStats.drop('Unnamed: 0', axis=1, inplace=True)
        #
        #     rowHeaders = BaseStats.index
        #     colHeaders = BaseStats.columns.values
        #
        #     col = len(colHeaders)
        #     row = len(rowHeaders)
        #     #self.Table = CreateTable(BaseStats, row, col, colHeaders, rowHeaders)

            #I know this isn't the proper way to embed my table not sure what the right way is.#cc
            self.Table = CreateTable()
            vboxRightBottom.addWidget(self.Table)


        """
        EXTRA CODE PAST PLOTTER STATIC DRAFT IGNORE
            #self.plot(lambda:...)
            #self.plot(BaseStats)

            # plt.cla()
            ax = self.figure.add_subplot(111)
            #x = [1,2,3,4,5,6,7,8,9,10]
            #x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
            # #y = [BaseStats.iloc[3, :]]
            y = [2,5,1,6,8,9,9,9,3,22]
            #
            ax.plot(x, y, 'b.-')
            ax.set_title(self.TitlEdit.text())
            self.canvas.draw()
        """

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
def main():
    #main loop
    app = QtWidgets.QApplication(sys.argv)
    #instance
    appWindow = MainWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()