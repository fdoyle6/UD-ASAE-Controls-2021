# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#PyQt5 stuff
from PyQt5 import QtCore, QtGui, QtWidgets # import PyQt5 widgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

#Ground Station Stuff
import sys
import os
import io
import serial.tools.list_ports
import serial as sr
import time
from serial.threaded import LineReader, ReaderThread
import csv

#UI Files
from LoadScreen import Ui_LoadScreen
from DAS import Ui_DAS

class PrintLines(LineReader):

    def connection_made(self, transport):
        super(PrintLines, self).connection_made(transport)
        print("port opened")

    def handle_line(self, data):
        print(data)

    def connection_lost(self, exc):
        print("port closed")

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.main_ui = Ui_DAS()
        self.main_ui.setupUi(self)

        #LoRa
        self.lora = sr.Serial('COM6', baudrate=57600)
        self.protocol = ReaderThread(self.lora, PrintLines).__enter__()
        self.protocol.write_line("sys set pindig GPIO10 0")
        self.main_ui.LoRa_TX = transmitter(self.protocol)
        self.main_ui.LoRa_RX = receiver(self.protocol)
        self.main_ui.LoRa_RX.start()
        self.main_ui.PDButton.clicked.connect(self.main_ui.LoRa_TX.start)

        #LoRa 1-Thread way(comment out all above)
        #self.main_ui.lora = transceiver()
        #self.main_ui.lora.start()
        #self.main_ui.PDButton.clicked.connect(self.main_ui.lora.transmit)


class transmitter(QThread):
    protocol = None
    def __init__(self,protocol):
        super().__init__()
        self.protocol = protocol

    def run(self):
        self.protocol.write_line("sys set pindig GPIO10 1")
        print("PADA deployed")
        time.sleep(5)
        self.stop()

    def stop(self):
        print("Transmission complete")

class receiver(QThread):
     protocol = None
     def __init__(self, protocol):
         super().__init__()
         self.protocol = protocol

     def run(self):
         self.ThreadActive = True
         while (self.ThreadActive):
            print("receiving")
            time.sleep(1)

     def stop(self):
         self.ThreadActive = False



# class transceiver(QThread):
#     lora = sr.Serial('COM6', baudrate=57600)
#     try:
#         print("attempting to connect...")
#         protocol = ReaderThread(lora, PrintLines).__enter__()
#         print("connected")
#         protocol.write_line("sys set pindig GPIO10 1")
#         protocol.write_line("radio set freq 915000000")
#         print("LoRa initialized ...")
#
#     except:
#         print("ERROR")
#     def run(self):
#         self.ThreadActive = True
#         while self.ThreadActive:
#             #self.protocol.write_line() #receiving loop
#             print("Receiving")
#             time.sleep(1)
#     def transmit(self):
#         self.protocol.write_line("sys set pindig GPIO10 1") #transmitting
#         print("PADA Dropped")
#         time.sleep(3)
#     def stop(self):
#         self.ThreadActive = False



def main():
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"]='1'
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

