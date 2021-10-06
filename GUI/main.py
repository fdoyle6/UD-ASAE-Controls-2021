# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from PyQt5 import QtCore, QtGui, QtWidgets # import PyQt5 widgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import serial.tools.list_ports
import serial as sr
import csv

#UI Files
from LoadScreen import Ui_LoadScreen
from DAS import Ui_DAS

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.main_ui = Ui_DAS()
        self.main_ui.setupUi(self)



#
first_window.show()

# Run the program
sys.exit(app.exec())
