
#!/usr/bin/python3
# -*- coding: iso-8859-1 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My window app")
        label = QLabel("this is awesome")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

        print ("hello")
    
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()