import serial

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
      print(self.data)

if __name__ == "__main__":
  print("this is invoked automatically")
  try:
    C = communicatorClassInititation()
    B = communicator()
    B.parameterize("/dev/cu.usbmodem14201",9600)
    B.outFlow(b'm')
    B.inFlow()
    while True:
      B.inFlow()
      val = input("Please enter the character")
      B.outFlow(val.encode())
  except KeyboardInterrupt:
    exit()
