
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class HelpWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.vbox = QVBoxLayout() 
        self.center()
    
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

    def helpBar(self):
        self.exit = QAction("Quit", self) 
        self.menu_bar = self.menuBar()
        self.menu_bar.setNativeMenuBar(True)

        self.file = self.menu_bar.addMenu("&File") 
        self.file.addAction(self.exit) 
        self.setMenuBar(self.menu_bar)       
        
    def initWindow(self):
        self.setGeometry(100,100,800,600)
        self.setWindowTitle('Help Endor')  
        self.statusBar()
        self.helpBar()
        self.show()

