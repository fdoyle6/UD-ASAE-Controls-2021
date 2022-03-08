#ASAE GUI Code
#Team Members: Frank Doyle - Captain, Chris Czerwinski, Mike Rosen, Jack Swift
#Team Github:

#PyQt5 stuff
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

#Useful Libraries
from PIL import Image
from threading import Thread
from math import *
import sys
import os
import io
import serial as sr
import time
import csv

#UI Files
from LoadScreen import Ui_LoadScreen
from DAS import Ui_DAS
from DASnoGPS import Ui_MainWindow



# Arguments !!! THESE MUST BE CHANGED WHEN RAN ON A DIFFERENT COMPUTER
#upper left latitude and longitude of picture
ul_lat_lon = (39.6816628374625, -75.75363767585272)#(39.68180233022854, -75.75196397747506)#(39.6816628374625, -75.75363767585272)-Benny;(32.61267,-97.48776) - map
#lower right latitude and longitude of picture
lr_lat_lon = (39.67454497595476, -75.74301612795641)#(39.68070781834817, -75.74960457883779)#(39.67454497595476, -75.74301612795641)-Benny;(32.60752,-97.48138) - map
map =  'Benny.png'#path to picture
chopHelper = 100 #varies depending on screen size
bottom = 250 #varies depending on screen size
COM = 'COM5' #'COM5' -Duino   'COM7' - Feather varies depending on which COM port the GroundStation operates off of
baud =9600 #9600- Duino 115200 - Feather
GPS_h_w = (1270,760) # I truly have no idea where these numbers come from, play around with new point statments until you find the lr corner
playBackMode = input("Playback mode (Type yes/y or no/n): ") #true to read in last csv as if it were real time data
if playBackMode == 'yes' or playBackMode =='y':
    playBackMode = True
else:
    playBackMode = False

def findImageSize(img_path):
    pil = Image.open(img_path)
    return (pil.size[0],pil.size[1])

def rollPitchYaw(magX,magY,magZ,accX,accY,accZ):
    pitch = 180 * atan2(accX, sqrt(accY * accY + accZ * accZ)) / pi
    roll = 180 * atan2(accY, sqrt(accX * accX + accZ * accZ)) / pi
    mag_x = magX * cos(pitch) + magY * sin(roll) * sin(pitch) + magZ * cos(roll) * sin(pitch)
    mag_y = magY * cos(roll) - magZ * sin(roll)
    yaw = 180 * atan2(-mag_y, mag_x) / pi
    return roll,pitch,yaw #all angles between 0 and 360

def scale_to_img(lat_lon, h_w, ul_lat_lon, lr_lat_lon):
    """
    Conversion from latitude and longitude to the image pixels.
    It is used for drawing the GPS records on the map image.
    :param lat_lon: GPS record to draw (lat1, lon1).
    :param h_w: Size of the map image (w, h).
    :return: Tuple containing x and y coordinates to draw on map image.
    """
    # https://gamedev.stackexchange.com/questions/33441/how-to-convert-a-number-from-one-min-max-set-to-another-min-max-set/33445
    old = (lr_lat_lon[0], ul_lat_lon[0])
    new = (0, h_w[1])
    y = ((lat_lon[0] - old[1]) * (new[1] - new[0]) / (old[0] - old[1]))
    old = (ul_lat_lon[1], lr_lat_lon[1])
    new = (0, h_w[0])
    x = ((lat_lon[1] - old[0]) * (new[1] - new[0]) / (old[1] - old[0]))
    # y must be reversed because the orientation of the image in the matplotlib.
    # image - (0, 0) in upper left corner; coordinate system - (0, 0) in lower left corner
    return (int(x), int(y))

#PyQt5 Main Display Window
class MainWindow(QMainWindow):
    def __init__(self, width, height):
        super(MainWindow, self).__init__()
        self.width = width
        self.height = height
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
        self.GPS = Widget(self.width,self.height)
        if(playBackMode):
            print("Rerunning last flight")
            self.Playback = PlayBack(self)
            self.Playback.start()
        else:
            print("Beginning new flight")
            self.DataHandler = DataHandler(self)
            self.DataHandler.start()
            self.main_ui.StopButton.clicked.connect(self.DataHandler.stop)



#PyQt5 GPS Window
class Widget(QWidget):
    def __init__(self,width,height):
        super().__init__()
        self.drawing = False
        self.lastPoint = QPoint()
        self.setWindowTitle("GPS")
        self.image = QPixmap(map)
        self.setGeometry(width//2+chopHelper, chopHelper//2, 500, 300)
        self.resize(width // 2 - chopHelper, height - chopHelper//2)
        #self.show() #uncomment when GPS works

    #instantiates map
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image)

    #draws on coordinates
    def newPoint(self,x,y):
        pen = QPen(Qt.red, 13, Qt.SolidLine)
        painter = QPainter(self.image)
        painter.setPen(pen)
        painter.drawPoint(QPoint(x,y))
        self.update()
        print(x,y)


#Thread for taking in data and sending to GUI and GPS
class DataHandler(Thread):
    def __init__(self,ui):
        super().__init__()
        self.ui = ui
        self.f = open('flight.csv', 'w+')


    def run(self):
        writer = csv.writer(self.f)
        self.threadActive = True
        gs = sr.Serial(COM, baud)
        gs.reset_input_buffer()
        while self.threadActive:
            data = gs.readline().rstrip().decode("utf-8")
            if(len(data)>4):
                data_list = data.split(',')
                if(len(data_list)==11):
                    print(data_list)
                    writer.writerow(data_list)
                    self.ui.main_ui.AltValue.setNum(max(round(float(data_list[0]),1),0))
                    if(data_list[10] == '0'):
                        self.ui.main_ui.PDHValue.setText(self.ui.main_ui.AltValue.text())
                    else:
                        self.ui.main_ui.PDHTitle.setStyleSheet("color: 'red'")
                    r,p,y = rollPitchYaw(float(data_list[1]),float(data_list[2]),float(data_list[3]),float(data_list[4]),float(data_list[5]),float(data_list[6]))
                    self.ui.main_ui.RollValue.setNum(int(r))
                    self.ui.main_ui.PitchValue.setNum(int(p))
                    self.ui.main_ui.YawValue.setNum(int(y))
                    if(float(data_list[9])>0.0):
                        self.ui.main_ui.VelValue.setNum(round(float(data_list[9]),1))
                        x,y = scale_to_img((float(data_list[7]),float(data_list[8])),GPS_h_w,ul_lat_lon,lr_lat_lon)
                        self.ui.GPS.newPoint(x,y)

    def stop(self):
        self.threadActive = False
        self.f.close()

class PlayBack(Thread):
    def __init__(self,ui):
        super().__init__()
        self.ui = ui
        self.f = open('flight.csv', 'r')


    def run(self):
        reader = csv.reader(self.f)
        for row in reader:
            time.sleep(0.25)  # data rate is approximately 4 Hz
            if len(row)>4:
                data_list = row
                print(data_list)
                self.ui.main_ui.AltValue.setNum(max(round(float(data_list[0]),1),0))
                if(data_list[10] == '0'):
                    self.ui.main_ui.PDHValue.setText(self.ui.main_ui.AltValue.text())
                else:
                    self.ui.main_ui.PDHTitle.setStyleSheet("color: 'red'")
                r,p,y = rollPitchYaw(float(data_list[1]),float(data_list[2]),float(data_list[3]),float(data_list[4]),float(data_list[5]),float(data_list[6]))
                self.ui.main_ui.RollValue.setNum(int(r))
                self.ui.main_ui.PitchValue.setNum(int(p))
                self.ui.main_ui.YawValue.setNum(int(y))
                if(float(data_list[9])>0.0):
                    self.ui.main_ui.VelValue.setNum(round(float(data_list[9]),1))
                    x,y = scale_to_img((float(data_list[7]),float(data_list[8])),GPS_h_w,ul_lat_lon,lr_lat_lon)
                    self.ui.GPS.newPoint(x,y)
            else:
                pass
        self.f.close()

def main():
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"]='1'
    app = QApplication(sys.argv)
    screen_resolution = app.desktop().screenGeometry()
    width,height = screen_resolution.width(), screen_resolution.height()
    win = MainWindow(width, height)
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

