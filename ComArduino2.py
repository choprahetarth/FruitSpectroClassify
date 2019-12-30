import serial
import os, sys
from PyQt5.QtWidgets import QApplication, QLabel

class communicatorClassInititation:
  def __init__(self):
      self.ser = serial.Serial()
  
class communicator(communicatorClassInititation):
  def parameterize(self,name,baud1):
      self.ser.port = name
      self.ser.baudrate = baud1
      self.ser.bytesize = serial.EIGHTBITS #number of bits per bytes
      self.ser.parity = serial.PARITY_NONE #set parity check: no parity
      self.ser.stopbits = serial.STOPBITS_TWO #number of stop bits
      self.ser.open()
      self.initilizer = 0
  def outFlow(self,value):
      self.value = value
      self.ser.write(self.value)
  def inFlow(self):
      self.data = self.ser.readline()[:-2]

if __name__ == "__main__":
  print("this is invoked automatically")
  fileOpen = os.open('/Users/hetarth/Desktop/example_code/new.txt', os.O_RDWR|os.O_CREAT)
  app = QApplication([])
  label = QLabel('Ripeness Tester')

  try:
    C = communicatorClassInititation()
    B = communicator()
    B.parameterize("/dev/cu.usbmodem14201",9600)
    readOnceFlag = 1
    while True:
      val = input("Please enter the character")
      B.outFlow(val.encode())
      B.inFlow()
      label = input ("Please enter the label")
      print(B.data.decode()+label)
      writeVariable = (b'\n'+B.data+label.encode())
      if (val == 'r'):
        print("Writing to File")
        os.write(fileOpen, writeVariable)
        
        
  except KeyboardInterrupt:
    exit()
