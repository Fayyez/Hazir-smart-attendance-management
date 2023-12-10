# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import json
from Classes.classes import Teacher
from home_page_ui import Ui_homepage

# global variables
# path to directory
folder_path = os.getcwd() + "/src"
# all teahers data
teachers = {}
teacher_json_path = folder_path + "/records/teachers_data.json"
# reading all the teachers
with open(teacher_json_path, "r") as f:
    data = json.load(f)
teachers = {teacher['username']: Teacher(teacher['name'], teacher['username'], teacher['password'], teacher['face']) for teacher in data}

print(teachers)

class LoginPage(object):
    loginbutton=None
    
    def setupUi(self, logo_picture):
        logo_picture.setObjectName("logo_picture")
        logo_picture.resize(900, 700)
        logo_picture.setLayoutDirection(QtCore.Qt.LeftToRight)
        logo_picture.setStyleSheet("background-color:#2f3c7e\n" "")
        self.widget = QtWidgets.QWidget(logo_picture)
        self.widget.setGeometry(QtCore.QRect(420, 30, 441, 641))
        self.widget.setStyleSheet("background-color:#fbeaeb;\n" "border-radius:30px;")
        self.widget.setObjectName("widget")
        self.usernameLabel = QtWidgets.QLabel(self.widget)
        self.usernameLabel.setGeometry(QtCore.QRect(150, 60, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordlabel = QtWidgets.QLabel(self.widget)
        self.passwordlabel.setGeometry(QtCore.QRect(150, 200, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.passwordlabel.setFont(font)
        self.passwordlabel.setObjectName("passwordlabel")
        self.usernamebox = QtWidgets.QLineEdit(self.widget)
        self.usernamebox.setGeometry(QtCore.QRect(100, 100, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.usernamebox.setFont(font)
        self.usernamebox.setStyleSheet("border: 1px solid black;  /* or your desired color */\n"
"    border-top: none;\n"
"    border-left: none;\n"
"    border-right: none;\n"
"   \n"
"   border-bottom-width: 1px;\n"
"    border-radius: 0; ")
        self.usernamebox.setObjectName("usernamebox")
        self.usernamebox_2 = QtWidgets.QLineEdit(self.widget)
        self.usernamebox_2.setGeometry(QtCore.QRect(90, 250, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.usernamebox_2.setFont(font)
        self.usernamebox_2.setStyleSheet("border: 1px solid black;  /* or your desired color */\n"
"    border-top: none;\n"
"    border-left: none;\n"
"    border-right: none;\n"
"   \n"
"   border-bottom-width: 1px;\n"
"    border-radius: 0; ")
        self.usernamebox_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.usernamebox_2.setObjectName("usernamebox_2")
        self.userpic = QtWidgets.QLabel(self.widget)
        self.userpic.setGeometry(QtCore.QRect(20, 100, 71, 61))
        self.userpic.setText("")
        self.userpic.setPixmap(QtGui.QPixmap(f"{folder_path}/assets/usericon-removebg-preview.png"))
        self.userpic.setScaledContents(True)
        self.userpic.setObjectName("userpic")
        self.passwordpic = QtWidgets.QLabel(self.widget)
        self.passwordpic.setGeometry(QtCore.QRect(20, 250, 71, 61))
        self.passwordpic.setText("")
        self.passwordpic.setPixmap(QtGui.QPixmap(f"{folder_path}/assets/passwordicon-removebg-preview.png"))
        self.passwordpic.setScaledContents(True)
        self.passwordpic.setObjectName("passwordpic")
        self.loginbutton = QtWidgets.QPushButton(self.widget)
        self.loginbutton.setGeometry(QtCore.QRect(240, 350, 141, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 60, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 60, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 60, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 60, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 60, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 60, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 60, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 60, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 60, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.loginbutton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.loginbutton.setFont(font)
        self.loginbutton.setStyleSheet("background-color:#2f3c7e;\n"
"color: white;\n"
"border-radius:10px;\n"
"")
        self.loginbutton.setObjectName("loginbutton")
        self.loginbutton.clicked.connect(self.login())
        self.loginbuttonwithcamera = QtWidgets.QPushButton(self.widget)
        self.loginbuttonwithcamera.setGeometry(QtCore.QRect(130, 480, 191, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 60, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 60, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 60, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 60, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 60, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 60, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 60, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 60, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 60, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.loginbuttonwithcamera.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.loginbuttonwithcamera.setFont(font)
        self.loginbuttonwithcamera.setStyleSheet("background-color:#2f3c7e;\n"
"color: white;\n"
"border-radius:10px;\n"
"")
        self.loginbuttonwithcamera.setObjectName("loginbuttonwithcamera")
        self.usernameLabel_2 = QtWidgets.QLabel(self.widget)
        self.usernameLabel_2.setGeometry(QtCore.QRect(200, 430, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.usernameLabel_2.setFont(font)
        self.usernameLabel_2.setObjectName("usernameLabel_2")
        self.registerbutton = QtWidgets.QPushButton(self.widget)
        self.registerbutton.setGeometry(QtCore.QRect(60, 360, 151, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 234, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 234, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 234, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 234, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 234, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 234, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 234, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 234, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 234, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.registerbutton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.registerbutton.setFont(font)
        self.registerbutton.setStyleSheet("color:black;")
        self.registerbutton.setObjectName("registerbutton")
        self.passwordpic_2 = QtWidgets.QLabel(self.widget)
        self.passwordpic_2.setGeometry(QtCore.QRect(20, 480, 71, 61))
        self.passwordpic_2.setText("")
        # self.passwordpic_2.setPixmap(QtGui.QPixmap("../../Users/Zulfiqar/Downloads/camera_icon(new).png"))
        self.passwordpic_2.setScaledContents(True)
        self.passwordpic_2.setObjectName("passwordpic_2")
        self.logo_label = QtWidgets.QLabel(logo_picture)
        self.logo_label.setGeometry(QtCore.QRect(100, 340, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.logo_label.setFont(font)
        self.logo_label.setObjectName("logo_label")
        self.logo_subtext = QtWidgets.QLabel(logo_picture)
        self.logo_subtext.setGeometry(QtCore.QRect(100, 420, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(16)
        font.setUnderline(True)
        self.logo_subtext.setFont(font)
        self.logo_subtext.setObjectName("logo_subtext")
        self.label = QtWidgets.QLabel(logo_picture)
        self.label.setGeometry(QtCore.QRect(130, 150, 171, 161))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.setPixmap(QtGui.QPixmap(f"{folder_path}/assets/logo.jpg"))
        self.label.setScaledContents(True)
        self.retranslateUi(logo_picture)
        QtCore.QMetaObject.connectSlotsByName(logo_picture)

    def login(self):
        username = self.usernamebox.text()
        password = self.usernamebox_2.text()
        # get text from user
        if username in teachers: # if username macthed
            if teachers[username].password == password:
                print("Login Successful")        

    def retranslateUi(self, logo_picture):
        _translate = QtCore.QCoreApplication.translate
        logo_picture.setWindowTitle(_translate("logo_picture", "LoginScreen"))
        self.usernameLabel.setText(_translate("logo_picture", " UserName:"))
        self.passwordlabel.setText(_translate("logo_picture", " Password:"))
        self.usernamebox.setPlaceholderText(_translate("logo_picture", "Enter Username"))
        self.usernamebox_2.setPlaceholderText(_translate("logo_picture", "Enter Password"))
        self.loginbutton.setText(_translate("logo_picture", "Login"))
        self.loginbuttonwithcamera.setText(_translate("logo_picture", " Login With Camera "))
        self.usernameLabel_2.setText(_translate("logo_picture", "OR"))
        self.registerbutton.setText(_translate("logo_picture", "Register now!"))
        self.logo_label.setText(_translate("logo_picture", "       Hazir.io"))
        self.logo_subtext.setText(_translate("logo_picture", "Seamless Attendance"))



