# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DAS.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DAS(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1532, 961)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background: white\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(0, 690, 811, 111))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("chunk::background: blue\n"
"")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 810, 811, 141))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background: rgb(236, 236, 236)")
        self.pushButton.setObjectName("pushButton")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 811, 681))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 2, 1, 1)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_2.setLineWidth(2)
        self.lcdNumber_2.setDigitCount(3)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.gridLayout.addWidget(self.lcdNumber_2, 2, 1, 1, 1)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_3.setLineWidth(2)
        self.lcdNumber_3.setDigitCount(3)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.gridLayout.addWidget(self.lcdNumber_3, 2, 2, 1, 1)
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_4.setLineWidth(2)
        self.lcdNumber_4.setDigitCount(3)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.gridLayout.addWidget(self.lcdNumber_4, 5, 0, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber.setLineWidth(2)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(3)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout.addWidget(self.lcdNumber, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lcdNumber_5.setFont(font)
        self.lcdNumber_5.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumber_5.setLineWidth(2)
        self.lcdNumber_5.setDigitCount(3)
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.gridLayout.addWidget(self.lcdNumber_5, 5, 1, 1, 1)
        self.lcdNumber_6 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_6.sizePolicy().hasHeightForWidth())
        self.lcdNumber_6.setSizePolicy(sizePolicy)
        self.lcdNumber_6.setMinimumSize(QtCore.QSize(0, 40))
        self.lcdNumber_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lcdNumber_6.setBaseSize(QtCore.QSize(0, 0))
        self.lcdNumber_6.setLineWidth(2)
        self.lcdNumber_6.setSmallDecimalPoint(False)
        self.lcdNumber_6.setDigitCount(3)
        self.lcdNumber_6.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_6.setProperty("value", 0.0)
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        self.gridLayout.addWidget(self.lcdNumber_6, 5, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 4, 2, 1, 1)
        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 6)
        self.gridLayout.setRowStretch(3, 2)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setRowStretch(5, 6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1532, 20))
        self.menubar.setObjectName("menubar")
        self.menuDAS = QtWidgets.QMenu(self.menubar)
        self.menuDAS.setObjectName("menuDAS")
        self.menuLog = QtWidgets.QMenu(self.menubar)
        self.menuLog.setObjectName("menuLog")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuDAS.menuAction())
        self.menubar.addAction(self.menuLog.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PADA Release"))
        self.label_8.setText(_translate("MainWindow", "(ft)"))
        self.label_7.setText(_translate("MainWindow", "(ft)"))
        self.label_9.setText(_translate("MainWindow", "(mph)"))
        self.label.setText(_translate("MainWindow", "Altitude"))
        self.label_2.setText(_translate("MainWindow", "PADA Drop"))
        self.label_3.setText(_translate("MainWindow", "Velocity"))
        self.label_5.setText(_translate("MainWindow", "Pitch"))
        self.label_6.setText(_translate("MainWindow", "Yaw"))
        self.label_4.setText(_translate("MainWindow", "Roll"))
        self.label_10.setText(_translate("MainWindow", "(deg)"))
        self.label_11.setText(_translate("MainWindow", "(deg)"))
        self.label_12.setText(_translate("MainWindow", "(deg)"))
        self.menuDAS.setTitle(_translate("MainWindow", "DAS"))
        self.menuLog.setTitle(_translate("MainWindow", "Log"))