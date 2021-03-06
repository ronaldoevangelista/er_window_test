import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class QCustomQWidget (QWidget):
    def __init__ (self, parent = None):
        super(QCustomQWidget, self).__init__(parent)

        self.textQVBoxLayout = QVBoxLayout()

        self.textUpQLabel    = QLabel()
        self.textDownQLabel  = QLabel()

        self.textQVBoxLayout.addWidget(self.textUpQLabel)
        self.textQVBoxLayout.addWidget(self.textDownQLabel)

        self.allQHBoxLayout  = QHBoxLayout()
        self.iconQLabel      = QLabel()

        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)

        self.setLayout(self.allQHBoxLayout)

        self.textUpQLabel.setStyleSheet('color: rgb(0, 0, 255);')
        self.textDownQLabel.setStyleSheet('color: rgb(255, 0, 0);')

    def setTextUp (self, text):
        self.textUpQLabel.setText(text)

    def setTextDown (self, text):
        self.textDownQLabel.setText(text)

    def setIcon (self, imagePath):
        self.iconQLabel.setPixmap(QPixmap(imagePath))

class exampleQMainWindow (QMainWindow):
    def __init__ (self):
        super(exampleQMainWindow, self).__init__()
        self.myQListWidget = QListWidget(self)
        for index, name, icon in [
            ('No.1', 'Meyoko',  'icons/exit.png'),
            ('No.2', 'Nyaruko', 'icons/exit.png'),
            ('No.3', 'Louise',  'icons/exit.png')]:

            myQCustomQWidget = QCustomQWidget()
            myQCustomQWidget.setTextUp(index)
            myQCustomQWidget.setTextDown(name)
            myQCustomQWidget.setIcon(icon)

            myQListWidgetItem = QListWidgetItem(self.myQListWidget)
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())

            self.myQListWidget.addItem(myQListWidgetItem)
            self.myQListWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)
            self.setCentralWidget(self.myQListWidget)

app = QApplication([])
window = exampleQMainWindow()
window.show()
sys.exit(app.exec_())


