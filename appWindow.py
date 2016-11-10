#!/usr/bin/python3
# -*- coding: utf-8 -*-

#import sys
#from PyQt5.QtWidgets import (QMainWindow, QAction, QWidget, QStyleFactory, QApplication)
#from PyQt5 import QtCore, QtGui, QtWidgets

#from PyQt5.QtGui import QIcon
#from PyQt5.QtCore import Qt

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        

    def initToolbar(self):
        
        left_spacer = QWidget()
        left_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.toolbar = self.addToolBar("Options")

        self.helpAction = QAction(QIcon('icons/ic_help_black_48dp_2x.png'), '&Help', self)        
        self.settingsAction = QAction(QIcon('icons/ic_build_black_48dp_2x.png'), '&Settings', self) 
        self.missionAction = QAction(QIcon('icons/ic_description_black_48dp_2x.png'), '&Mission', self) 
        self.openAction = QAction(QIcon('icons/ic_folder_open_black_48dp_2x.png'), '&Open', self) 

        self.toolbar.addWidget(left_spacer)

        self.helpAction.setShortcut('Ctrl+H')
        self.helpAction.setStatusTip('Help')
        #exitAction.triggered.connect(self.close)

        self.settingsAction.setShortcut('Ctrl+S')
        self.settingsAction.setStatusTip('Settings')

        self.missionAction.setShortcut('Ctrl+M')
        self.missionAction.setStatusTip('Mission')

        self.openAction.setShortcut('Ctrl+O')
        self.openAction.setStatusTip('Open')
        self.openAction.triggered.connect(self.showDialog)


        self.toolbar.addAction(self.openAction)
        self.toolbar.addAction(self.missionAction)
        self.toolbar.addAction(self.settingsAction)
        self.toolbar.addAction(self.helpAction)
        
        self.addToolBarBreak()
    
        for action in self.toolbar.actions():
            widget = self.toolbar.widgetForAction(action)
    
    def showDialog(self):
            text, ok = QInputDialog.getText(self, 'Input Dialog','Enter your name:')

    def initUI(self):               

        self.initToolbar()
        self.statusBar().showMessage('Ready')

       # self.menubar = self.menuBar()
       # self.fileMenu = self.menubar.addMenu('&File')
       # self.fileMenu.addAction(exitAction)

        #self.toolbar = self.addToolBar('Exit')
        #self.toolbar.addAction(exitAction)
        
        self.setGeometry(100,100,1030,800)
        self.setWindowTitle('Endor Viewer')    
        self.show()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
