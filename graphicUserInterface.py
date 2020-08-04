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

###################### IMAGE CLASS ##############################
#                                                               #
#                                                               #
#################################################################

import time
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from datetime import datetime

ENDPOINT = "https://fruit360.cognitiveservices.azure.com/"

# Replace with a valid key
project_id="239a1ed5-b4c0-4c57-b92c-03b0097aaa8e"
training_key = "72a9a9f87ee7484faa9343a727ac11de"
prediction_key = "90b75d8296474fe184e2c4d51c3a4adb"
prediction_resource_id = "/subscriptions/e85fff3e-6fea-46db-8ca2-4c3419470103/resourceGroups/cloud-shell-storage-centralindia/providers/Microsoft.CognitiveServices/accounts/Fruit360-Prediction"
publish_iteration_name = "classifyModel"
# Vision API Setup
trainer = CustomVisionTrainingClient(training_key, endpoint=ENDPOINT)
predictor = CustomVisionPredictionClient(prediction_key,endpoint = ENDPOINT)
project = trainer.get_project(project_id)

# define the retrain function
def retrainerFunction():
    # Now the code to start the training
    print("Training...")
    iteration = trainer.train_project(project.id)
    while (iteration.status != "Completed"):
            iteration = trainer.get_iteration(project_id, iteration.id)
            print("Trianing Status :" + iteration.status)
            time.sleep(1)
    # Now to Publish the trained Iteration
    trainer.publish_iteration(project.id, iteration.id, publish_iteration_name, prediction_resource_id)
    print ("Done!")

# define the predict function
def predictionFunction(filePath):
    # use the open object to open the image as binary 'rb' to the object image_contents
    with open(filePath, "rb") as image_contents:
        results = predictor.classify_image(
            project.id, publish_iteration_name, image_contents.read())
        # Display the results.
        for prediction in results.predictions:
            print("\t" + prediction.tag_name +
                  ": {0:.2f}%".format(prediction.probability * 100))


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
        thirdButton = QPushButton("refreshImage")
        thirdButton.setDefault(True)
        topLayout = QHBoxLayout()
        topLayout.addWidget(firstButton)
        topLayout.addWidget(secondButton)
        topLayout.addWidget(thirdButton)
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
        flatPushButton.clicked.connect(self.startDebugModeA) 
        flatPushButton.setFlat(True)
        layout = QVBoxLayout()
        layout.addWidget(defaultPushButton)
        layout.addWidget(defaultPushButton1)
        layout.addWidget(flatPushButton)
        layout.addStretch(1)
        self.topLeftGroupBox.setLayout(layout)    
    
    def startModeA(self):
        now = datetime.now()
        date_time = now.strftime("%m%d%Y%H%M%S")
        tempVariable = '/picture'+date_time+'.jpg'
        #from picamera import PiCamera
        #from time import sleep
        #camera = PiCamera()
        #camera.start_preview()
        #sleep(5)
        #camera.capture(tempVariable)
        #camera.stop_preview()
        predictionFunction("/Users/hetarth/Desktop/example_code/FruitSpectroClassify/image.jpg")


    def startDebugModeA(self): # MODE A START FUNCTION
        val = "stepper"
        commRunObject.outFlow(val.encode())
        #commRunObject.inFlow()
        #print (commRunObject.data.decode())
        #val = "s"
        #commRunObject.outFlow(val.encode())
        #commRunObject.inFlow()
        #print (commRunObject.data.decode())


    def createBottomLeftTabWidget(self):
        self.bottomLeftTabWidget = QGroupBox("Fruit Image")
        imageView = QLabel()
        imageView.setPixmap(QPixmap("/Users/hetarth/Desktop/example_code/FruitSpectroClassify/image.jpg"))
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
