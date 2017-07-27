
#imports/libraries
#<editor-fold desc="Imports and Libraries">
import sys
#Importing PyQt5 library to construct widgets for Graphic User Interface (GUI) application
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QSlider, QApplication, QVBoxLayout, QHBoxLayout,
                             QApplication, QWidget, QLabel, QCheckBox, QRadioButton, QPlainTextEdit, QSizePolicy,
                             QMainWindow,QFrame, QFileDialog, QTableWidgetItem, QTableWidget, QMenu, QMessageBox,
                             QAction, QToolBar)
from PyQt5.QtCore import Qt, QAbstractTableModel, pyqtSignal


import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.ticker as mticker

from matplotlib import pyplot as plt
plt.style.use(['ggplot'])

#Backend door for matplotlib importation required to use Pyqt with matpltlib libray
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationBar
from matplotlib.figure import Figure
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})


import csv
import pandas as pd
import numpy as np
from numpy import arange, sin, pi
import statistics

from functools import partial

import shlex

#</editor-fold>


class createFIG():
    def __init__(self):
        super(createFIG, self).__init__()
        self.figure = plt.figure()
        self.axes = self.figure.add_subplot(111)
        self.axes.set_xlabel('x label')
        self.axes.set_ylabel('y label')


    def plotData(self, xdata,ydata, PlotVal):
        print("plotting")
        print("elements data type of list x is {}".format(type(xdata[1])))
        print("elements data type of list y is {}".format(type(ydata[1])))
        print("PlotVal data type is {}" .format(type(PlotVal)))

        self.axes.grid()


        # #self.y = ydata
        # #self.x = xdata
        # xdata =xdata.tolist()
        # print("about plot")
        # self.boxplot(xdata)

        if PlotVal == "box":

            self.x = xdata
            print("data type of static x is {}".format(type(self.x[1])))
            self.axes.boxplot(self.x)
            self.axes.grid()
        elif PlotVal == "scatter":

            self.x = xdata
            self.y = ydata
            print("about to assign n")

            n = len(self.y)
            print(n)
            print(self.x)
            print(self.y)


            self.NumTicks = np.arange(n)
            print(self.NumTicks)
            self.axes.set_xticks(self.NumTicks)
            print("ticks have been created ")

            self.axes.set_xticklabels(self.y, rotation = 60)
            print("strings have been set as labels")

            self.axes.scatter(self.NumTicks, self.x)
            self.axes.grid()
            #self.axes.plt.tight_layout()


        plt.show()
        print("graph appears")

class CompareWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setWindowTitle("Perspective - MultiGraph Window")

        self.CompareUI()

    def CompareUI(self):
        print("initialize widgets")

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.TableHeader = QLabel("Tables")
        self.RowHeader = QLabel("Row Selection")
        self.Instructions = QLabel("Format to enter ' Table Number, [row, numbers, seperated, with, commas] ' ")


        """
        These aren't a QtableWidget these are my QlineEdits that ask the user to input which table and which rows they
        want to pull data from
        """
        self.TableRowEntry1 = QLineEdit(' "Table1", "[ Rows ]" ')
        self.TableRowEntry2 = QLineEdit(' "Table2", "[ Rows ]" ')
        self.TableRowEntry3 = QLineEdit(' "Table3", "[ Rows ]" ')

        self.BoxPlot = QPushButton("Box Plot")
        self.ScatterPlot = QPushButton("Scatter Plot")


        #Initial values
        self.Label = QLabel("Empty right now")
        self.text = "initial string"

        #Currently these values are just the strings from default setting of the QlineEdit
        self.Entry1 =self.TableRowEntry1.text()
        self.Entry2 = self.TableRowEntry2.text()
        self.Entry3 = self.TableRowEntry3.text()

        self.TableRowEntry1.textChanged[str].connect(self.onChanged)
        self.TableRowEntry2.textChanged[str].connect(self.onChanged)
        self.TableRowEntry3.textChanged[str].connect(self.onChanged)



        ###OLD METHOD I TRIED TO IMPLEMENT HAD SAME RESULTS AS NEW METHOD I"M HAVING TROUBLE WITH###

        # self.Entry1 = self.TableRowEntry1.textChanged.connect(partial(self.TextAssign, 1))
        # print("THIS IS WHERE ENTRY IS BEING REPLACED {}".format(self.Entry1))
        # self.Entry2 = self.TableRowEntry2.textChanged.connect(partial(self.TextAssign, 2))
        # self.Entry3 = self.TableRowEntry3.textChanged.connect(partial(self.TextAssign, 3))


        ### I'm only testing out the first QLineEdit
        self.Entry1 = self.TableRowEntry1.textChanged[str].connect(self.onChanged)

        ###Takes the Entrys that have been made connects it my my methods Box/ScatterPlotCall###
        self.BoxPlot.clicked.connect(partial(self.BoxPlotCall, self.Entry1, self.Entry2, self.Entry3))
        self.ScatterPlot.clicked.connect(partial(self.ScatterPlotCall, self.Entry1, self.Entry2, self.Entry3))

        ###LAYOUT###
        # <editor-fold desc="Layout">
        self.vboxMain = QVBoxLayout(self.main_widget)
        self.VboxCOMP1 = QVBoxLayout()

        self.vboxMain.addLayout(self.VboxCOMP1)

        self.Header = QHBoxLayout()
        self.Header.addWidget(self.TableHeader)
        self.Header.addWidget(self.RowHeader)

        self.subHeader = QHBoxLayout()
        self.subHeader.addStretch()
        self.subHeader.addWidget(self.Instructions)

        self.hboxCOMP1 = QHBoxLayout()
        #self.hboxCOMP1.addStretch()
        self.hboxCOMP1.addWidget(self.TableRowEntry1)
        self.hboxCOMP1.addStretch()

        self.hboxCOMP2 = QHBoxLayout()
        #self.hboxCOMP2.addStretch()
        self.hboxCOMP2.addWidget(self.TableRowEntry2)
        self.hboxCOMP2.addStretch()

        self.hboxCOMP3 = QHBoxLayout()
        #self.hboxCOMP3.addStretch()
        self.hboxCOMP3.addWidget(self.TableRowEntry3)
        self.hboxCOMP3.addStretch()

        self.hboxPlotBtns = QHBoxLayout()
        self.hboxPlotBtns.addWidget(self.BoxPlot)
        self.hboxPlotBtns.addWidget(self.ScatterPlot)
        self.hboxPlotBtns.addStretch()

        self.hboxRAND = QHBoxLayout()
        self.hboxRAND.addWidget(self.Label)

        ### ADD TO PAGE ###
        self.VboxCOMP1.addLayout(self.Header)
        self.VboxCOMP1.addLayout(self.subHeader)
        self.VboxCOMP1.addLayout(self.hboxCOMP1)
        self.VboxCOMP1.addLayout(self.hboxCOMP2)
        self.VboxCOMP1.addLayout(self.hboxCOMP3)
        self.VboxCOMP1.addLayout(self.hboxPlotBtns)
        self.VboxCOMP1.addLayout(self.hboxRAND)
        # </editor-fold>

    def onChanged(self,text):
        """
        Current prototype method I'm trying to implement returns a nonetype,
        however self.entry is a string in this method and properly is passed
        to the QLabel and can be seen on my Compare-UI window.
        :param text:
        :return:
        """
        self.Label.setText(text)
        ###self.Entry returns a none-type###
        self.Entry1 = self.Label.text()
        print(self.Entry1)
        print(type(self.Entry1))
        #outText = self.Label.text()
        #return(outText)


    def TextAssign(self, EntryNum):
        """
        Old Method that I tried to implement had the same problem as new method onChanged

        :param EntryNum:
        :return:
        """
        print("text changed")
        if EntryNum == 1:
            self.text = self.TableRowEntry1.text()
        elif EntryNum == 2:
            self.text = self.TableRowEntry2.text()
        elif EntryNum == 3:
            self.text = self.TableRowEntry3.text()

        else:
            print("Not currently avaliable")
            #error msg cells not provided proper information
            #improper inputs
            #erorr msg output string output for both cells
        #print("TEXT IS HERE and the string is.... {}".format(text))
        self.Entry1 = self.text
        #print(self.Entry1)


    def BoxPlotCall(self, Entry1, Entry2, Entry3):
        print("Box Plot called")
        if Entry1 == "First Table":
            print("ENTRY is first???")
            pass
        else:
            print("preforms parsing")
            print(Entry1)


        ### COMMENTED OUT FOR CONVIENCE: code is for parsing string on quotations
            #print(shlex.split(Entry1))
            #string = 'this is "a test" of shlex'
            #print(shlex.split(string))
            #tableNUM = Entry1.split(',')
            #print(tableNUM)
            #print(RowNums)
            #throw an error for if the data type is not a integer

    def ScatterPlotCall(self, TEntry1, TEntry2, TEntry3, REntry1, REntry2, REntry3):
        print("scatter plot called")


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Perspective")

        self.initializeUI()

        self.compareWin = CompareWindow()
        self.compareWin.resize(350,200)
        self.compareWin.setMaximumSize(500,250)

    def initializeUI(self):

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        #CREATION OF WIDGETS
        # <editor-fold desc="Widgets Creation Site">

        ###first file###
        #buttons associated with the first browse button
        """
            Buttons related to the first file being uploaded
        """
        self.FileNmLabel = QLabel('FileName')
        self.FileNameEdit = QLineEdit('"Filename"')
        self.FileNameEdit.setMaximumSize(200,20)
        self.BrowseBtn = QPushButton('Browse')
        self.BrowseBtn.setMaximumSize(80,20)

        self.OpacityLabel = QLabel('Opacity')
        self.OpacitySlider = QSlider(Qt.Horizontal)
        self.OpacitySlider.setMinimum(0)
        self.OpacitySlider.setMaximum(100)
        self.OpacitySlider.setValue(100)
        self.OpacitySlider.setTickInterval(10)
        self.OpacitySlider.setTickPosition(QSlider.TicksBelow)
        self.OpacitySlider.setMaximumSize(200,20)

        self.ShowChkbx = QCheckBox('show')


        ###Overlay Plot###
        #checkbox to give user ability to overlay data
        self.Overlay = QCheckBox('Overlay Plots')

        self.comparison = QPushButton('Compare')


        #Button Functionality___________________________________________________________________________________________
        # <editor-fold desc="Button Functionality">

        self.BrowseBtn.clicked.connect(self.import1)

        self.OpacitySlider.valueChanged.connect(self.OpacityVal)


        self.comparison.clicked.connect(self.OpenCompare)

        # </editor-fold>_____________________________________________________________________END OF BUTTON FUNCTIONALITY

        # Widget Layout
        # <editor-fold desc="Layout">


        self.hMAIN = QHBoxLayout(self.main_widget)

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


        ###OverLay###
        self.hbox5 = QHBoxLayout()
        self.hbox5.addWidget(self.Overlay)
        self.hbox5.addWidget(self.comparison)



        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox5)

        self.vboxRIGHT = QVBoxLayout()

        self.HboxGraph = QHBoxLayout()
        #self.HboxGraph.addWidget(self.canvas)

        # self.vboxGraph = QVBoxLayout()
        # self.vboxGraph.addWidget(self.canvas)

        self.vboxNavBar = QVBoxLayout()
        #self.vboxNavBar.addWidget(self.NavBar)

        self.vboxData = QVBoxLayout()

        # self.vboxRIGHT.addLayout(self.vboxGraph)
        self.vboxRIGHT.addLayout(self.vbox)
        self.vboxRIGHT.addLayout(self.HboxGraph)
        self.vboxRIGHT.addLayout(self.vboxNavBar)
        self.vboxRIGHT.addLayout(self.vboxData)

        self.hMAIN.addLayout(self.vbox)
        self.hMAIN.addLayout(self.vboxRIGHT)

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
            self.Table.dataSignal.connect(self.initiatePlot)
            self.vboxData.addWidget(self.Table)


    def TitleClicked(self):
        print("Enter Title")
        sender = self.sender()
        if sender.text() == "Enter":
            ax.set_title(self.TitlEdit.text())
            self.canvas.draw()
    def OpacityVal(self):
        OpacitySignal = pyqtSignal(int)
        print("Opacity value is being changed")

    def OpenCompare(self):
        print("opening compare window")
        self.compareWin.show()



    def initiatePlot(self,x,y,PlotVal):
        print("emit signal")
        print(x)
        print(y)
        f = createFIG()
        f.plotData(x, y, PlotVal)


class CreateTable(QTableWidget): #QTableWidget
    dataSignal = pyqtSignal(list, np.ndarray, str)
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
        graphAction = menu.addAction("Graph") #Boxplt
        compareAction = menu.addAction("Compare")
        scatterAction = menu.addAction("Scatter Plot")
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

            #self.Graph = Plotter(self.selected, self.ColHeader)
            print(type(self.selected), type(self.ColHeader))

            #self.plotbtn.clicked.connect(partial(self.initiatePlot, xdata, ydata))
            self.PlotVal = "box"
            self.dataSignal.emit(self.selected, self.ColHeader, self.PlotVal)
        elif action == scatterAction:
            self.selected = self.selectedItems()
            n = len(self.selected)
            for i in range(n):
                self.selected[i] = str(self.selected[i].text())
            for i in range(n):
                self.selected[i] = float(self.selected[i])
            print("right before plotter called")

            # self.Graph = Plotter(self.selected, self.ColHeader)
            print(type(self.selected), type(self.ColHeader))

            self.PlotVal = "scatter"
            self.dataSignal.emit(self.selected, self.ColHeader, self.PlotVal)



            #self.vboxRight.addWidget(self.Graph)
        else:
            print("u clicked something other than quit")



def main():
        # main loop
        app = QApplication(sys.argv)
        # instance
        window = MainWindow()
        window.show()
        # appWindow = MainWindow()
        sys.exit(app.exec_())

if __name__ == "__main__":
    main()