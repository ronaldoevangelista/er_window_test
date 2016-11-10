import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Help import HelpWindow


class EndorMainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.title = 'Endor Viewer'
        self.initEndorUI()
    
    def initEndorHelpWindow(self):
        self.helpwindow = HelpWindow()
        self.helpwindow.initWindow()
        self.helpwindow.center()

    def window(self):
        self.win = QWidget()
        b1 = QPushButton("Button1")
        b2 = QPushButton("Button2")

        vbox = QVBoxLayout()
        vbox.addWidget(b1)
        vbox.addStretch()
        vbox.addWidget(b2)
        hbox = QHBoxLayout()

        b3 = QPushButton("Button3")
        b4 = QPushButton("Button4")
        hbox.addWidget(b3)
        hbox.addStretch()
        hbox.addWidget(b4)

        vbox.addStretch()
        vbox.addLayout(hbox)
        self.win.setLayout(vbox)
    
    def initEndorUI(self):
        self.initToolbar()
        self.initMenubar()
        self.statusBar().showMessage('Ready')
        self.window()
        self.setGeometry(100,100,1030,800)
        self.setWindowTitle(self.title) 
        self.show()
    
    def openFileMission(self):
        self.homeFolder = os.getenv('HOME')
        self.frame = QFileDialog.getOpenFileName(self, 'Open file', self.homeFolder,"Endor files (*.endor)")
        ##develompent
    
    ##not work
    def initMenubar(self):
        self.menubar = QMenuBar()
        file = self.menubar.addMenu("File")
        edit = self.menubar.addMenu("Edit")
        view = self.menubar.addMenu("View")

    def initToolbar(self):
        self.toolbar = self.addToolBar("Options")

        self.letfSpace = QWidget()
        self.letfSpace.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.helpAction = QAction(QIcon('icons/ic_help_black_48dp_2x.png'), '&Help', self)        
        self.settingsAction = QAction(QIcon('icons/ic_build_black_48dp_2x.png'), '&Settings', self) 
        self.missionAction = QAction(QIcon('icons/ic_description_black_48dp_2x.png'), '&Mission', self) 
        self.openAction = QAction(QIcon('icons/ic_folder_open_black_48dp_2x.png'), '&Open', self) 

        self.toolbar.addWidget(self.letfSpace)
        self.toolbar.addAction(self.openAction)
        self.toolbar.addAction(self.missionAction)
        self.toolbar.addAction(self.settingsAction)
        self.toolbar.addAction(self.helpAction)
        
        self.helpAction.setShortcut('Ctrl+H')
        self.helpAction.setStatusTip('Help')
        self.helpAction.triggered.connect(self.initEndorHelpWindow)
 
        self.settingsAction.setShortcut('Ctrl+S')
        self.settingsAction.setStatusTip('Settings')

        self.missionAction.setShortcut('Ctrl+M')
        self.missionAction.setStatusTip('Mission')

        self.openAction.setShortcut('Ctrl+O')
        self.openAction.setStatusTip('Open')
        self.openAction.triggered.connect(self.openFileMission)

    
