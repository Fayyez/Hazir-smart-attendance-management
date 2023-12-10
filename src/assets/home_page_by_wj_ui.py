# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Danish\Documents\GitHub\Hazir-smart-attendance-management\src\assets\home_page_by_wj.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_homepage(object):
    def setupUi(self, homepage):
        homepage.setObjectName("homepage")
        homepage.resize(1000, 700)
        font = QtGui.QFont()
        font.setPointSize(11)
        homepage.setFont(font)
        homepage.setStyleSheet("background-color:#2f3c7e")
        self.verticalScrollBar = QtWidgets.QScrollBar(homepage)
        self.verticalScrollBar.setGeometry(QtCore.QRect(980, 0, 21, 701))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.search_line_edit = QtWidgets.QLineEdit(homepage)
        self.search_line_edit.setGeometry(QtCore.QRect(410, 80, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.search_line_edit.setFont(font)
        self.search_line_edit.setStyleSheet("border-radius:10px;\n"
"background-color:#fbeaeb")
        self.search_line_edit.setObjectName("search_line_edit")
        self.top_widget_2 = QtWidgets.QWidget(homepage)
        self.top_widget_2.setGeometry(QtCore.QRect(0, 0, 981, 41))
        self.top_widget_2.setStyleSheet("background-color:#fbeaeb")
        self.top_widget_2.setObjectName("top_widget_2")
        self.back_button = QtWidgets.QPushButton(self.top_widget_2)
        self.back_button.setGeometry(QtCore.QRect(10, 0, 51, 41))
        self.back_button.setStyleSheet("border-image: url(/Users/Zulfiqar/Pictures/previous.PNG) stretch;\n"
"")
        self.back_button.setText("")
        self.back_button.setObjectName("back_button")
        self.hamburegr_button = QtWidgets.QPushButton(self.top_widget_2)
        self.hamburegr_button.setGeometry(QtCore.QRect(930, 0, 51, 41))
        self.hamburegr_button.setStyleSheet("border-image: url(/Users/Zulfiqar/Pictures/menu.PNG) stretch;\n"
"")
        self.hamburegr_button.setText("")
        self.hamburegr_button.setObjectName("hamburegr_button")
        self.homepageLabel = QtWidgets.QLabel(self.top_widget_2)
        self.homepageLabel.setGeometry(QtCore.QRect(470, 10, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.homepageLabel.setFont(font)
        self.homepageLabel.setObjectName("homepageLabel")
        self.gridLayoutWidget = QtWidgets.QWidget(homepage)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(119, 170, 541, 471))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.filter_button = QtWidgets.QPushButton(homepage)
        self.filter_button.setGeometry(QtCore.QRect(700, 80, 51, 41))
        self.filter_button.setStyleSheet("border-image: url(/Users/Zulfiqar/Pictures/clear.PNG) stretch;\n"
"")
        self.filter_button.setText("")
        self.filter_button.setObjectName("filter_button")
        self.add_room_pushButton = QtWidgets.QPushButton(homepage)
        self.add_room_pushButton.setGeometry(QtCore.QRect(800, 570, 71, 61))
        self.add_room_pushButton.setStyleSheet("border-image: url(/Users/Zulfiqar/Pictures/ad.PNG) stretch;\n"
"")
        self.add_room_pushButton.setText("")
        self.add_room_pushButton.setObjectName("add_room_pushButton")
        self.homepageLabel_2 = QtWidgets.QLabel(homepage)
        self.homepageLabel_2.setGeometry(QtCore.QRect(760, 640, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.homepageLabel_2.setFont(font)
        self.homepageLabel_2.setObjectName("homepageLabel_2")

        self.retranslateUi(homepage)
        QtCore.QMetaObject.connectSlotsByName(homepage)

    def retranslateUi(self, homepage):
        _translate = QtCore.QCoreApplication.translate
        homepage.setWindowTitle(_translate("homepage", "Home Page"))
        self.search_line_edit.setPlaceholderText(_translate("homepage", " Search"))
        self.homepageLabel.setText(_translate("homepage", "Home Page"))
        self.homepageLabel_2.setText(_translate("homepage", "        Add Room"))
