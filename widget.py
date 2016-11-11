import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


app = QApplication(sys.argv)

listWidget = QListWidget()

for i in range(10):
    item = QListWidgetItem("Item %i" % i)
    listWidget.addItem(item)

listWidget.show()
sys.exit(app.exec_())
