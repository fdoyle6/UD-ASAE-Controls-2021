# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DASnoGPS.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1532, 957)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background: white\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1241, 641))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.PDHUnit = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.PDHUnit.setFont(font)
        self.PDHUnit.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.PDHUnit.setObjectName("PDHUnit")
        self.gridLayout.addWidget(self.PDHUnit, 1, 1, 1, 1)
        self.AltUnit = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.AltUnit.setFont(font)
        self.AltUnit.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.AltUnit.setObjectName("AltUnit")
        self.gridLayout.addWidget(self.AltUnit, 1, 0, 1, 1)
        self.VelUnit = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.VelUnit.setFont(font)
        self.VelUnit.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.VelUnit.setObjectName("VelUnit")
        self.gridLayout.addWidget(self.VelUnit, 1, 2, 1, 1)
        self.AltTitle = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.AltTitle.setFont(font)
        self.AltTitle.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.AltTitle.setObjectName("AltTitle")
        self.gridLayout.addWidget(self.AltTitle, 0, 0, 1, 1)
        self.PDHTitle = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.PDHTitle.setFont(font)
        self.PDHTitle.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.PDHTitle.setObjectName("PDHTitle")
        self.gridLayout.addWidget(self.PDHTitle, 0, 1, 1, 1)
        self.VelTitle = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.VelTitle.setFont(font)
        self.VelTitle.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.VelTitle.setObjectName("VelTitle")
        self.gridLayout.addWidget(self.VelTitle, 0, 2, 1, 1)
        self.PitchTitle = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.PitchTitle.setFont(font)
        self.PitchTitle.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.PitchTitle.setObjectName("PitchTitle")
        self.gridLayout.addWidget(self.PitchTitle, 3, 1, 1, 1)
        self.YawTitle = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.YawTitle.setFont(font)
        self.YawTitle.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.YawTitle.setObjectName("YawTitle")
        self.gridLayout.addWidget(self.YawTitle, 3, 2, 1, 1)
        self.RollTitle = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.RollTitle.setFont(font)
        self.RollTitle.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.RollTitle.setObjectName("RollTitle")
        self.gridLayout.addWidget(self.RollTitle, 3, 0, 1, 1)
        self.RollUnit = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.RollUnit.setFont(font)
        self.RollUnit.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.RollUnit.setObjectName("RollUnit")
        self.gridLayout.addWidget(self.RollUnit, 4, 0, 1, 1)
        self.PitchUnit = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.PitchUnit.setFont(font)
        self.PitchUnit.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.PitchUnit.setObjectName("PitchUnit")
        self.gridLayout.addWidget(self.PitchUnit, 4, 1, 1, 1)
        self.YawUnit = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.YawUnit.setFont(font)
        self.YawUnit.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.YawUnit.setObjectName("YawUnit")
        self.gridLayout.addWidget(self.YawUnit, 4, 2, 1, 1)
        self.AltValue = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(144)
        self.AltValue.setFont(font)
        self.AltValue.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.AltValue.setObjectName("AltValue")
        self.gridLayout.addWidget(self.AltValue, 2, 0, 1, 1)
        self.VelValue = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(144)
        self.VelValue.setFont(font)
        self.VelValue.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.VelValue.setObjectName("VelValue")
        self.gridLayout.addWidget(self.VelValue, 2, 2, 1, 1)
        self.RollValue = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(144)
        self.RollValue.setFont(font)
        self.RollValue.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.RollValue.setObjectName("RollValue")
        self.gridLayout.addWidget(self.RollValue, 5, 0, 1, 1)
        self.PitchValue = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(144)
        self.PitchValue.setFont(font)
        self.PitchValue.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PitchValue.setObjectName("PitchValue")
        self.gridLayout.addWidget(self.PitchValue, 5, 1, 1, 1)
        self.YawValue = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(144)
        self.YawValue.setFont(font)
        self.YawValue.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.YawValue.setObjectName("YawValue")
        self.gridLayout.addWidget(self.YawValue, 5, 2, 1, 1)
        self.PDHValue = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(144)
        self.PDHValue.setFont(font)
        self.PDHValue.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PDHValue.setObjectName("PDHValue")
        self.gridLayout.addWidget(self.PDHValue, 2, 1, 1, 1)
        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 6)
        self.gridLayout.setRowStretch(3, 2)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setRowStretch(5, 6)
        self.StopButton = QtWidgets.QPushButton(self.centralwidget)
        self.StopButton.setGeometry(QtCore.QRect(440, 640, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.StopButton.setFont(font)
        self.StopButton.setStyleSheet("background: rgb(255, 0, 0)")
        self.StopButton.setObjectName("StopButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PDHUnit.setText(_translate("MainWindow", "(ft)"))
        self.AltUnit.setText(_translate("MainWindow", "(ft)"))
        self.VelUnit.setText(_translate("MainWindow", "(mph)"))
        self.AltTitle.setText(_translate("MainWindow", "Altitude"))
        self.PDHTitle.setText(_translate("MainWindow", "Drop"))
        self.VelTitle.setText(_translate("MainWindow", "Velocity"))
        self.PitchTitle.setText(_translate("MainWindow", "Pitch"))
        self.YawTitle.setText(_translate("MainWindow", "Yaw"))
        self.RollTitle.setText(_translate("MainWindow", "Roll"))
        self.RollUnit.setText(_translate("MainWindow", "(deg)"))
        self.PitchUnit.setText(_translate("MainWindow", "(deg)"))
        self.YawUnit.setText(_translate("MainWindow", "(deg)"))
        self.AltValue.setText(_translate("MainWindow", "0"))
        self.VelValue.setText(_translate("MainWindow", "0"))
        self.RollValue.setText(_translate("MainWindow", "0"))
        self.PitchValue.setText(_translate("MainWindow", "0"))
        self.YawValue.setText(_translate("MainWindow", "0"))
        self.PDHValue.setText(_translate("MainWindow", "0"))
        self.StopButton.setText(_translate("MainWindow", " Halt Data"))