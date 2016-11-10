
#!/usr/bin/python3
# -*- coding: iso-8859-1 -*-

from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout)
  
  
class Dialog(QDialog):
    NumGridRows = 3
    NumButtons = 4
  
    def __init__(self):
        super(Dialog, self).__init__()
    
        self.createGridGroupBox()
        self.createFormGroupBox()
  
        bigEditor = QTextEdit()
        bigEditor.setPlainText("This widget takes up all the remaining space in the top-level layout.")
  
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
  
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
  
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.gridGroupBox)
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(bigEditor)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
  
        self.setWindowTitle("Basic Layouts")
   
    def createGridGroupBox(self):
        self.gridGroupBox = QGroupBox("Grid layout")
        layout = QGridLayout()
  
        for i in range(Dialog.NumGridRows):
            label = QLabel("Line %d:" % (i + 1))
            lineEdit = QLineEdit()
            layout.addWidget(label, i + 1, 0)
            layout.addWidget(lineEdit, i + 1, 1)
  
        self.smallEditor = QTextEdit()
        self.smallEditor.setPlainText("This widget takes up about two thirds "
                "of the grid layout.")
  
        layout.addWidget(self.smallEditor, 0, 2, 4, 1)
  
        layout.setColumnStretch(1, 10)
        layout.setColumnStretch(2, 20)
        self.gridGroupBox.setLayout(layout)
  
    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Form layout")
        layout = QFormLayout()
        layout.addRow(QLabel("Line 1:"), QLineEdit())
        layout.addRow(QLabel("Line 2, long text:"), QComboBox())
        layout.addRow(QLabel("Line 3:"), QSpinBox())
        self.formGroupBox.setLayout(layout)
  
  
if __name__ == '__main__':
  
    import sys
  
    app = QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())