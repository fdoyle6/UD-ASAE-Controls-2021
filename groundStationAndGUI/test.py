# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 1200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #Grid For Data Streams
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1200, 662))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.YawValue = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.YawValue.setFont(font)
        self.YawValue.setAlignment(QtCore.Qt.AlignCenter)
        self.YawValue.setObjectName("YawValue")
        self.gridLayout.addWidget(self.YawValue, 4, 2, 1, 1)
        self.PitchLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.PitchLabel.setFont(font)
        self.PitchLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.PitchLabel.setObjectName("PitchLabel")
        self.gridLayout.addWidget(self.PitchLabel, 3, 1, 1, 1)
        self.YawLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.YawLabel.setFont(font)
        self.YawLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.YawLabel.setObjectName("YawLabel")
        self.gridLayout.addWidget(self.YawLabel, 3, 2, 1, 1)
        self.PitchValue = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.PitchValue.setFont(font)
        self.PitchValue.setAlignment(QtCore.Qt.AlignCenter)
        self.PitchValue.setObjectName("PitchValue")
        self.gridLayout.addWidget(self.PitchValue, 4, 1, 1, 1)
        self.RollLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.RollLabel.setFont(font)
        self.RollLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.RollLabel.setObjectName("RollLabel")
        self.gridLayout.addWidget(self.RollLabel, 3, 0, 1, 1)
        self.RollValue = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.RollValue.setFont(font)
        self.RollValue.setAlignment(QtCore.Qt.AlignCenter)
        self.RollValue.setObjectName("RollValue")
        self.gridLayout.addWidget(self.RollValue, 4, 0, 1, 1)
        self.MainAltLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.MainAltLabel.setFont(font)
        self.MainAltLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.MainAltLabel.setObjectName("MainAltLabel")
        self.gridLayout.addWidget(self.MainAltLabel, 0, 0, 1, 1)
        self.VelocityLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.VelocityLabel.setFont(font)
        self.VelocityLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.VelocityLabel.setObjectName("VelocityLabel")
        self.gridLayout.addWidget(self.VelocityLabel, 0, 2, 1, 1)
        self.PADAAltLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.PADAAltLabel.setFont(font)
        self.PADAAltLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.PADAAltLabel.setObjectName("PADAAltLabel")
        self.gridLayout.addWidget(self.PADAAltLabel, 0, 1, 1, 1)
        self.PADAAltValue = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.PADAAltValue.setFont(font)
        self.PADAAltValue.setAlignment(QtCore.Qt.AlignCenter)
        self.PADAAltValue.setObjectName("PADAAltValue")
        self.gridLayout.addWidget(self.PADAAltValue, 1, 1, 1, 1)
        self.VelocityValue = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.VelocityValue.setFont(font)
        self.VelocityValue.setAlignment(QtCore.Qt.AlignCenter)
        self.VelocityValue.setObjectName("VelocityValue")
        self.gridLayout.addWidget(self.VelocityValue, 1, 2, 1, 1)
        self.MainAltUnit = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.MainAltUnit.setFont(font)
        self.MainAltUnit.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.MainAltUnit.setObjectName("MainAltUnit")
        self.gridLayout.addWidget(self.MainAltUnit, 2, 0, 1, 1)
        self.MainAltValue = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.MainAltValue.setFont(font)
        self.MainAltValue.setAlignment(QtCore.Qt.AlignCenter)
        self.MainAltValue.setObjectName("MainAltValue")
        self.gridLayout.addWidget(self.MainAltValue, 1, 0, 1, 1)
        self.PADAHeightUnit = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.PADAHeightUnit.setFont(font)
        self.PADAHeightUnit.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.PADAHeightUnit.setObjectName("PADAHeightUnit")
        self.gridLayout.addWidget(self.PADAHeightUnit, 2, 1, 1, 1)
        self.VelocityUnit = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.VelocityUnit.setFont(font)
        self.VelocityUnit.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.VelocityUnit.setObjectName("VelocityUnit")
        self.gridLayout.addWidget(self.VelocityUnit, 2, 2, 1, 1)
        self.RollUnit = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.RollUnit.setFont(font)
        self.RollUnit.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.RollUnit.setObjectName("RollUnit")
        self.gridLayout.addWidget(self.RollUnit, 5, 0, 1, 1)
        self.PitchUnit = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.PitchUnit.setFont(font)
        self.PitchUnit.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.PitchUnit.setObjectName("PitchUnit")
        self.gridLayout.addWidget(self.PitchUnit, 5, 1, 1, 1)
        self.YawUnit = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.YawUnit.setFont(font)
        self.YawUnit.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.YawUnit.setObjectName("YawUnit")
        self.gridLayout.addWidget(self.YawUnit, 5, 2, 1, 1)
        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(1, 3)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 2)
        self.gridLayout.setRowStretch(4, 3)
        self.gridLayout.setRowStretch(5, 1)
        #Battery Bar
        self.BatteryBar = QtWidgets.QProgressBar(self.centralwidget)
        self.BatteryBar.setGeometry(QtCore.QRect(10, 700, 1200, 240))
        self.BatteryBar.setProperty("value", 24)
        self.BatteryBar.setObjectName("BatteryBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #PADA Drop Button
        self.PADA_Drop = QtWidgets.QPushButton(self.centralwidget)
        self.PADA_Drop.setGeometry(QtCore.QRect(10, 950, 441, 131))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.PADA_Drop.setFont(font)
        self.PADA_Drop.setObjectName("PADA_Drop")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PADA_Drop.setText(_translate("MainWindow", "PADA Drop"))
        self.PADA_Drop.adjustSize()
        self.YawValue.setText(_translate("MainWindow", "N/A"))
        self.YawValue.adjustSize()
        self.PitchLabel.setText(_translate("MainWindow", "Pitch"))
        self.PitchLabel.adjustSize()
        self.YawLabel.setText(_translate("MainWindow", "Yaw"))
        self.YawLabel.adjustSize()
        self.PitchValue.setText(_translate("MainWindow", "N/A"))
        self.PitchValue.adjustSize()
        self.RollLabel.setText(_translate("MainWindow", "Roll"))
        self.RollLabel.adjustSize()
        self.RollValue.setText(_translate("MainWindow", "N/A"))
        self.RollValue.adjustSize()
        self.MainAltLabel.setText(_translate("MainWindow", "Altitude"))
        self.MainAltLabel.adjustSize()
        self.VelocityLabel.setText(_translate("MainWindow", "Velocity"))
        self.VelocityLabel.adjustSize()
        self.PADAAltLabel.setText(_translate("MainWindow", "PADA Drop"))
        self.PADAAltLabel.adjustSize()
        self.PADAAltValue.setText(_translate("MainWindow", "N/A"))
        self.PADAAltValue.adjustSize()
        self.VelocityValue.setText(_translate("MainWindow", "N/A"))
        self.VelocityValue.adjustSize()
        self.MainAltUnit.setText(_translate("MainWindow", "ft"))
        self.MainAltUnit.adjustSize()
        self.MainAltValue.setText(_translate("MainWindow", "N/A"))
        self.MainAltValue.adjustSize()
        self.PADAHeightUnit.setText(_translate("MainWindow", "ft"))
        self.PADAHeightUnit.adjustSize()
        self.VelocityUnit.setText(_translate("MainWindow", "mph"))
        self.VelocityUnit.adjustSize()
        self.RollUnit.setText(_translate("MainWindow", "R"))
        self.RollUnit.adjustSize()
        self.PitchUnit.setText(_translate("MainWindow", "P"))
        self.PitchUnit.adjustSize()
        self.YawUnit.setText(_translate("MainWindow", "Y"))
        self.YawUnit.adjustSize()