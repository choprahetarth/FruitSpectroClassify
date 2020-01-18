from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QAction, QMdiSubWindow, QTextEdit
from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
import sys
 
class MDIWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mdi = QMdiArea() # adds the multiwindow display area
        self.setCentralWidget(self.mdi) # adds the central widget
        bar = self.menuBar() # adds the bar
        ############## code for all menu bars ################
        file = bar.addMenu("File") # adds the file menu
        file.addAction("ESCAPE") 
        file.triggered[QAction].connect(self.escapeCode)
        ############## code for all buttons ##################
        button1 = QPushButton('Mode A', self)
        button1.setToolTip('Choose This to Select the Mode A')
        button1.move(0,0)
        button1.resize(100,64)
        button2 = QPushButton('Mode B', self)
        button2.setToolTip('Choose This to Select the Mode B')
        button2.move(100,0)
        button2.resize(100,64)
        button1.clicked.connect(self.windowTrigModeA)
        button2.clicked.connect(self.windowTrigModeB)
        ############## Application Title ####################
        self.setWindowTitle("MDI Application")
 
    def windowTrigModeA(self):
        sub = QMdiSubWindow()
        sub.setWidget(QTextEdit())
        sub.setWindowTitle("Sub Window")
        self.mdi.addSubWindow(sub)
        sub.show()
    
    def windowTrigModeB(self, q):
        sub = QMdiSubWindow()
        sub.setWidget(QTextEdit())
        sub.setWindowTitle("Sub Window")
        self.mdi.addSubWindow(sub)
        sub.show()
        

    def escapeCode(self, m):
        if m.text() == "ESCAPE":
            self.exit()


 
app = QApplication(sys.argv)
mdi = MDIWindow()
mdi.show()
app.exec_()