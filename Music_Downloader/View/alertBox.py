# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/que/Programming/Python/Qt/alertBox.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 213)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 212))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 6, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.lbl_alertBox_info = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_alertBox_info.setFont(font)
        self.lbl_alertBox_info.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_alertBox_info.setObjectName("lbl_alertBox_info")
        self.verticalLayout.addWidget(self.lbl_alertBox_info)
        self.lineEdit_alertBox_data = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(11)
        self.lineEdit_alertBox_data.setFont(font)
        self.lineEdit_alertBox_data.setInputMask("")
        self.lineEdit_alertBox_data.setPlaceholderText("")
        self.lineEdit_alertBox_data.setObjectName("lineEdit_alertBox_data")
        self.verticalLayout.addWidget(self.lineEdit_alertBox_data)
        self.comboBox_alertBox_delete = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_alertBox_delete.setObjectName("comboBox_alertBox_delete")
        self.verticalLayout.addWidget(self.comboBox_alertBox_delete)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 7)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 2, 4, 1, 1)
        self.btn_alertBox_enter = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.btn_alertBox_enter.setFont(font)
        self.btn_alertBox_enter.setObjectName("btn_alertBox_enter")
        self.gridLayout.addWidget(self.btn_alertBox_enter, 2, 1, 1, 1)
        self.btn_alertBox_exit = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.btn_alertBox_exit.setFont(font)
        self.btn_alertBox_exit.setObjectName("btn_alertBox_exit")
        self.gridLayout.addWidget(self.btn_alertBox_exit, 2, 5, 1, 1)
        self.comboBox_alertBox_typeOfAction = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.comboBox_alertBox_typeOfAction.setFont(font)
        self.comboBox_alertBox_typeOfAction.setObjectName("comboBox_alertBox_typeOfAction")
        self.gridLayout.addWidget(self.comboBox_alertBox_typeOfAction, 2, 3, 1, 1)
        self.lbl_alertBox_Inserted = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.lbl_alertBox_Inserted.setFont(font)
        self.lbl_alertBox_Inserted.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_alertBox_Inserted.setObjectName("lbl_alertBox_Inserted")
        self.gridLayout.addWidget(self.lbl_alertBox_Inserted, 1, 1, 1, 5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_alertBox_info.setText(_translate("MainWindow", "Enter The Info in the Box Below"))
        self.btn_alertBox_enter.setText(_translate("MainWindow", "ENTER"))
        self.btn_alertBox_exit.setText(_translate("MainWindow", "EXIT"))
        self.lbl_alertBox_Inserted.setText(_translate("MainWindow", "Insert *"))

