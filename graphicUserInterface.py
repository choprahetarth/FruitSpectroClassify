from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget,QButtonGroup)
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import serial
import os, sys


###################### COMM CLASS ###############################
#                                                               #
#                                                               #
#################################################################

class communicatorClassInititation: # class for initializing the communication
  def __init__(self):
      self.ser = serial.Serial()
  
class communicator(communicatorClassInititation): # class to run the communication
  def parameterize(self,name,baud1): #function to specify the serial communication
      self.ser.port = name 
      self.ser.baudrate = baud1
      self.ser.bytesize = serial.EIGHTBITS #number of bits per bytes
      self.ser.parity = serial.PARITY_NONE #set parity check: no parity
      self.ser.stopbits = serial.STOPBITS_TWO #number of stop bits
      self.ser.open()
      self.initilizer = 0
  def outFlow(self,value): # function to specify the outflowing characters
      self.value = value
      self.ser.write(self.value)
  def inFlow(self): # function to specify the inflowing charcters
      self.data = self.ser.readline()[:-2]

######################## GUI CLASS ##############################
#                                                               #
#                                                               #
#################################################################
class WidgetGallery(QDialog): 
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)
        
        self.createTopLeftGroupBox() # these functions initiate the four box regions
        self.createTopRightGroupBox()
        self.createBottomLeftTabWidget()
        self.createBottomRightGroupBox()

        firstButton = QPushButton("Choose A mode")
        firstButton.setDefault(True)
        secondButton = QPushButton("Choose B mode")
        firstButton.setDefault(True)
        topLayout = QHBoxLayout()
        topLayout.addWidget(firstButton)
        topLayout.addWidget(secondButton)
        topLayout.addStretch(1)

        firstButton.clicked.connect(self.topRightGroupBox.setEnabled)
        firstButton.clicked.connect(self.topLeftGroupBox.setDisabled)
        secondButton.clicked.connect(self.topRightGroupBox.setDisabled)
        secondButton.clicked.connect(self.topLeftGroupBox.setEnabled)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        mainLayout.addWidget(self.topRightGroupBox, 1, 1)
        mainLayout.addWidget(self.bottomLeftTabWidget, 2, 0)
        mainLayout.addWidget(self.bottomRightGroupBox, 2, 1)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("Styles")


    def createTopRightGroupBox(self):
        self.topRightGroupBox = QGroupBox("CLASSIFY FRUIT RIPENESS - MODE B")
        
        defaultPushButton = QPushButton("Start")
        defaultPushButton.setDefault(True)

        defaultPushButton2 = QPushButton("Stop")
        defaultPushButton2.setDefault(True)

        flatPushButton = QPushButton("Debug Mode")
        flatPushButton.setFlat(True)
        
        layout = QVBoxLayout()
        layout.addWidget(defaultPushButton)
        layout.addWidget(defaultPushButton2)
        layout.addWidget(flatPushButton)
        defaultPushButton.clicked.connect(self.topLeftGroupBox.setEnabled)
        defaultPushButton2.clicked.connect(self.topLeftGroupBox.setDisabled)
        layout.addStretch(1)
        self.topRightGroupBox.setLayout(layout)
    
    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox("CLASSIFY FRUIT TYPES - MODE A ")
        defaultPushButton = QPushButton("Start")
        defaultPushButton.setDefault(True)
        defaultPushButton.clicked.connect(self.startModeA) 
        defaultPushButton1 = QPushButton("Stop")
        defaultPushButton1.setDefault(True)
        flatPushButton = QPushButton("Debug Mode")
        flatPushButton.setFlat(True)
        layout = QVBoxLayout()
        layout.addWidget(defaultPushButton)
        layout.addWidget(defaultPushButton1)
        layout.addWidget(flatPushButton)
        layout.addStretch(1)
        self.topLeftGroupBox.setLayout(layout)    

    def startModeA(self): # MODE A START FUNCTION
        print("I am here")
        val = "a"
        commRunObject.outFlow(val.encode())


    def createBottomLeftTabWidget(self):
        self.bottomLeftTabWidget = QGroupBox("Fruit Image")
        imageView = QLabel()
        imageView.setPixmap(QPixmap("image.jpg"))
       #imageView.setPixmap(QPixmap((anotherFunction())))
        layout = QVBoxLayout()
        layout.addWidget(imageView)
        layout.addStretch()
        self.bottomLeftTabWidget.setLayout(layout)

    def createBottomRightGroupBox(self):
        self.bottomRightGroupBox = QGroupBox("Group 3")
        layout = QVBoxLayout()
        defaultPushButton = QPushButton("Apple")
        defaultPushButton.setDefault(True)

        defaultPushButton1 = QPushButton("Orange")
        defaultPushButton1.setFlat(True)

        flatPushButton = QPushButton("Guava")
        flatPushButton.setFlat(True)

        flatPushButton1 = QPushButton("Peach")
        flatPushButton.setFlat(True)

        layout.addWidget(defaultPushButton)
        layout.addWidget(defaultPushButton1)
        layout.addWidget(flatPushButton1)
        layout.addWidget(flatPushButton)
        layout.addStretch(1)
        self.bottomRightGroupBox.setLayout(layout)


      


if __name__ == '__main__':
    commInitObject = communicatorClassInititation()
    commRunObject = communicator()
    commRunObject.parameterize("/dev/cu.usbmodem14101",9600)
    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec_()) 
