#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QMainWindow, QAction, QWidget, QStyleFactory, QApplication)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initToolbar(self):
        self.newAction = QAction(QIcon('icons/ic_help_black_48dp_2x.png'), 'Help', self)        

        self.toolbar = self.addToolBar("Options")
        self.toolbar.addAction(self.newAction)
        self.toolbar.addSeparator()

        self.addToolBarBreak()

    def initUI(self):               
        
        self.initToolbar()
        
        #exitAction = QAction(QIcon('exit.png'), '&Exit', self)        
        #exitAction.setShortcut('Ctrl+Q')
        #exitAction.setStatusTip('Exit application')
        #exitAction.triggered.connect(self.close)

        self.statusBar().showMessage('Ready')

       # self.menubar = self.menuBar()
       # self.fileMenu = self.menubar.addMenu('&File')
       # self.fileMenu.addAction(exitAction)

        #self.toolbar = self.addToolBar('Exit')
        #self.toolbar.addAction(exitAction)
        
        self.setGeometry(100,100,1030,800)
        self.setWindowTitle('window')    
        self.show()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
