# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Hazir-smart-attendance-management\src\home_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Classes.classes import ClassRoom, Student, Teacher
import sys, os, json

# getting the directory path
folder_path = os.getcwd() + "/src"



class Ui_homepage(object):
    currentwindow =None

    classrooms = None
    x=0;
    y=0;
    
    def setupUi(self, mainwindow, classrooms: dict):
        print(classrooms)
        self.classrooms = classrooms
        self.currentwindow = mainwindow
        mainwindow.setObjectName("homepage")
        mainwindow.resize(1000, 700)
        font = QtGui.QFont()
        font.setPointSize(11)
        mainwindow.setFont(font)
        mainwindow.setStyleSheet("background-color:#2f3c7e")
        self.verticalScrollBar = QtWidgets.QScrollBar(mainwindow)
        self.verticalScrollBar.setGeometry(QtCore.QRect(980, 0, 21, 701))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.search_line_edit = QtWidgets.QLineEdit(mainwindow)
        self.search_line_edit.setGeometry(QtCore.QRect(260, 90, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.search_line_edit.setFont(font)
        self.search_line_edit.setStyleSheet("border-radius:10px;\n"
"background-color:#fbeaeb")
        self.search_line_edit.setObjectName("search_line_edit")

        # search completer
        # get a list of class titles from class room dict values
        classTitiles = [classrooms[classs].title for classs in classrooms]
        completer = QtWidgets.QCompleter(classTitiles)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.search_line_edit.setCompleter(completer)
        self.top_widget_2 = QtWidgets.QWidget(mainwindow)
        self.top_widget_2.setGeometry(QtCore.QRect(0, 0, 981, 61))
        self.top_widget_2.setStyleSheet("background-color:#fbeaeb")
        self.top_widget_2.setObjectName("top_widget_2")
        self.back_button = QtWidgets.QPushButton(self.top_widget_2)
        self.back_button.setGeometry(QtCore.QRect(10, 10, 61, 41))
        self.back_button.setIconSize(QtCore.QSize(30, 30))

        back_icon = QtGui.QIcon()
        back_icon.addPixmap(QtGui.QPixmap(folder_path+"/assets/previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_button.setIcon(back_icon)
        self.back_button.setText("")
        self.back_button.setObjectName("back_button")
        self.back_button.clicked.connect(self.backbutton)
        self.hamburegr_button = QtWidgets.QPushButton(self.top_widget_2)
        self.hamburegr_button.setGeometry(QtCore.QRect(920, 10, 51, 41))
        hamburger_icon = QtGui.QIcon()
        hamburger_icon.addPixmap(QtGui.QPixmap(folder_path+"/assets/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # increase the size of the icon
        self.hamburegr_button.setIconSize(QtCore.QSize(40, 40))
        self.hamburegr_button.setIcon(hamburger_icon)
        self.hamburegr_button.setText("")
        self.hamburegr_button.setObjectName("hamburegr_button")
        self.homepageLabel = QtWidgets.QLabel(self.top_widget_2)
        self.homepageLabel.setGeometry(QtCore.QRect(410, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.homepageLabel.setFont(font)
        self.homepageLabel.setObjectName("homepageLabel")
       
        self.x=119
        self.y=170
        # create push buttons labeled as the title of the Classroom against each classroom in the clasroooms dict
        # the widhth of the button should be 500 with 200 height
        # the button should be rounded
        # background of each card should be cream: #fbeaeb
        # font size of the text in button should be big and bold
        j=0
        for classs in classrooms:
                self.class_button = QtWidgets.QPushButton(mainwindow)
                self.class_button.setGeometry(QtCore.QRect(self.x, self.y + j*self.y, 500, 150))
                self.class_button.setText(f"{classrooms[classs].title}\n Students: {classrooms[classs].studentcount}")
                self.class_button.setStyleSheet("border-radius: 10px; background-color: #fbeaeb;")
                self.class_button.clicked.connect(self.cardclicked)
                j+=1
        
        self.car_button = QtWidgets.QPushButton()
        self.car_button.setStyleSheet("border-radius: 10px;")

        ## adding the classrooms to the grid layout
        #create two cards of fisrt 2 value of the classroom dict

        self.filter_button = QtWidgets.QPushButton(mainwindow)
        self.filter_button.setGeometry(QtCore.QRect(545, 88, 51, 45))
        filter_icon = QtGui.QIcon()
        filter_icon.addPixmap(QtGui.QPixmap(folder_path+"/assets/filter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # increase the size of the icon
        self.filter_button.setIconSize(QtCore.QSize(40, 40))
        self.filter_button.setIcon(filter_icon)
        self.filter_button.setText("")
        self.filter_button.setObjectName("filter_button")
        self.add_room_pushButton = QtWidgets.QPushButton(mainwindow)
        self.add_room_pushButton.setGeometry(QtCore.QRect(780, 350, 91, 81))
        add_roon_icon = QtGui.QIcon()
        add_roon_icon.addPixmap(QtGui.QPixmap(folder_path+"/assets/u2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # increase the size of the icon
        self.add_room_pushButton.setIconSize(QtCore.QSize(60, 60))
        self.add_room_pushButton.setIcon(add_roon_icon)

        self.add_room_pushButton.setText("")
        self.add_room_pushButton.setObjectName("add_room_pushButton")
        self.homepageLabel_2 = QtWidgets.QLabel(mainwindow)
        self.homepageLabel_2.setGeometry(QtCore.QRect(750, 440, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.homepageLabel_2.setFont(font)
        self.homepageLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.homepageLabel_2.setObjectName("homepageLabel_2")

        self.retranslateUi(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

    def retranslateUi(self, homepage):
        _translate = QtCore.QCoreApplication.translate
        homepage.setWindowTitle(_translate("homepage", "Home Page"))
        self.search_line_edit.setPlaceholderText(_translate("homepage", " Search......"))
        self.homepageLabel.setText(_translate("homepage", "Home Page"))
        self.homepageLabel_2.setText(_translate("homepage", "+ Add Room"))
        # create a boundary for homepageLabel_2
        self.homepageLabel_2.setStyleSheet("border: 2px solid black; border-radius: 10px; background-color: #fbeaeb;")

    def cardclicked(self) :
        # close the current window and open room info page in the new window
        from room_infromation import Ui_RoomInfo
        app = QtWidgets.QApplication(sys.argv)
        # create nee window
        window = QtWidgets.QDialog()
        # load next page
        page = Ui_RoomInfo()
        # setup
        page.setupUi(window, self.classrooms)
        self.currentwindow.close() # close the last window 
        window.show()
        window.exec_()
        sys.exit(app.exec_())

    def backbutton(self):
        # go back to the login page
        from login_screen import LoginPage
        app = QtWidgets.QApplication(sys.argv)
        self.currentwindow.close()
        window = QtWidgets.QDialog()
        ui = LoginPage()
        ui.setupUi(window)
        self.currentwindow.close()
        window.show()
        window.exec_()
        sys.exit(app.exec_())