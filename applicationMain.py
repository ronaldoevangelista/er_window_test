
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from MainWindow import EndorMainWindow

if __name__ == '__main__':
    application = QApplication(sys.argv)
    endorUI = EndorMainWindow()
    sys.exit(application.exec_())


