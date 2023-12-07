# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addStudent.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setStyleSheet("background-color:#8d5293")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.user_icon_button = QtWidgets.QPushButton(self.centralwidget)
        self.user_icon_button.setGeometry(QtCore.QRect(870, 0, 57, 50))
        self.user_icon_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/user_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.user_icon_button.setIcon(icon)
        self.user_icon_button.setIconSize(QtCore.QSize(58, 54))
        self.user_icon_button.setObjectName("user_icon_button")
        self.hamburger_button = QtWidgets.QPushButton(self.centralwidget)
        self.hamburger_button.setGeometry(QtCore.QRect(940, 0, 54, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 82, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 82, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 82, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 82, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 82, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 82, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 82, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 82, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 82, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.hamburger_button.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.hamburger_button.setFont(font)
        self.hamburger_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../assets/hamburgerr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hamburger_button.setIcon(icon1)
        self.hamburger_button.setIconSize(QtCore.QSize(80, 60))
        self.hamburger_button.setObjectName("hamburger_button")
        self.Horizontal_line_at_top_1 = QtWidgets.QFrame(self.centralwidget)
        self.Horizontal_line_at_top_1.setGeometry(QtCore.QRect(0, 42, 1001, 16))
        self.Horizontal_line_at_top_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.Horizontal_line_at_top_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Horizontal_line_at_top_1.setObjectName("Horizontal_line_at_top_1")
        self.navigation_bar = QtWidgets.QLabel(self.centralwidget)
        self.navigation_bar.setGeometry(QtCore.QRect(10, 10, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.navigation_bar.setFont(font)
        self.navigation_bar.setStyleSheet("color:white")
        self.navigation_bar.setObjectName("navigation_bar")
        self.background_frame_top_1 = QtWidgets.QFrame(self.centralwidget)
        self.background_frame_top_1.setGeometry(QtCore.QRect(0, 0, 1001, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(141, 82, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(226, 226, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 82, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 82, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 82, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(226, 226, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 82, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 82, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 82, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(226, 226, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 82, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 82, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        self.background_frame_top_1.setPalette(palette)
        self.background_frame_top_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background_frame_top_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background_frame_top_1.setObjectName("background_frame_top_1")
        self.add_student_logo_atTop = QtWidgets.QLabel(self.background_frame_top_1)
        self.add_student_logo_atTop.setGeometry(QtCore.QRect(380, 10, 271, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.add_student_logo_atTop.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.add_student_logo_atTop.setFont(font)
        self.add_student_logo_atTop.setStyleSheet("border: 2px solid white; \n"
"color: white;\n"
"background-color: black;\n"
"border-radius:10px")
        self.add_student_logo_atTop.setObjectName("add_student_logo_atTop")
        self.widget_registration_portal = QtWidgets.QWidget(self.centralwidget)
        self.widget_registration_portal.setGeometry(QtCore.QRect(40, 80, 921, 581))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.widget_registration_portal.setFont(font)
        self.widget_registration_portal.setStyleSheet("border: 2px solid white; \n"
"color: white;\n"
"background-color: black;\n"
"border-radius:20px")
        self.widget_registration_portal.setObjectName("widget_registration_portal")
        self.name_input_box = QtWidgets.QLineEdit(self.widget_registration_portal)
        self.name_input_box.setGeometry(QtCore.QRect(40, 140, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.name_input_box.setFont(font)
        self.name_input_box.setStyleSheet("border: 2px solid white; \n"
"color: white;\n"
"background-color: black;\n"
"border-radius:10px")
        self.name_input_box.setText("")
        self.name_input_box.setObjectName("name_input_box")
        self.name_heading = QtWidgets.QLabel(self.widget_registration_portal)
        self.name_heading.setGeometry(QtCore.QRect(0, 90, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.name_heading.setFont(font)
        self.name_heading.setStyleSheet("border:none\n"
"")
        self.name_heading.setObjectName("name_heading")
        self.id_heading = QtWidgets.QLabel(self.widget_registration_portal)
        self.id_heading.setGeometry(QtCore.QRect(10, 190, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.id_heading.setFont(font)
        self.id_heading.setStyleSheet("border:none")
        self.id_heading.setObjectName("id_heading")
        self.id_input_box = QtWidgets.QLineEdit(self.widget_registration_portal)
        self.id_input_box.setGeometry(QtCore.QRect(40, 240, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.id_input_box.setFont(font)
        self.id_input_box.setStyleSheet("border: 2px solid white; \n"
"color: white;\n"
"background-color: black;\n"
"border-radius:10px")
        self.id_input_box.setText("")
        self.id_input_box.setObjectName("id_input_box")
        self.or_heading = QtWidgets.QLabel(self.widget_registration_portal)
        self.or_heading.setGeometry(QtCore.QRect(190, 440, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.or_heading.setFont(font)
        self.or_heading.setStyleSheet("border: 2px solid black; \n"
"color: white;\n"
"background-color:black ;\n"
"border-radius:10px")
        self.or_heading.setObjectName("or_heading")
        self.enter_button = QtWidgets.QPushButton(self.widget_registration_portal)
        self.enter_button.setGeometry(QtCore.QRect(102, 310, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.enter_button.setFont(font)
        self.enter_button.setStyleSheet("border: 2px solid black; \n"
"color: white;\n"
"background-color:#8d5293 ;\n"
"border-radius:10px")
        self.enter_button.setObjectName("enter_button")
        self.upload_pic_button = QtWidgets.QPushButton(self.widget_registration_portal)
        self.upload_pic_button.setGeometry(QtCore.QRect(20, 400, 131, 121))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.upload_pic_button.setFont(font)
        self.upload_pic_button.setObjectName("upload_pic_button")
        self.gridBox_cameraView = QtWidgets.QGroupBox(self.widget_registration_portal)
        self.gridBox_cameraView.setGeometry(QtCore.QRect(500, 30, 401, 271))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.gridBox_cameraView.setPalette(palette)
        self.gridBox_cameraView.setObjectName("gridBox_cameraView")
        self.gridLayout = QtWidgets.QGridLayout(self.gridBox_cameraView)
        self.gridLayout.setObjectName("gridLayout")
        self.useCamera_heading = QtWidgets.QLabel(self.widget_registration_portal)
        self.useCamera_heading.setGeometry(QtCore.QRect(240, 510, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.useCamera_heading.setFont(font)
        self.useCamera_heading.setStyleSheet("border:none")
        self.useCamera_heading.setObjectName("useCamera_heading")
        self.status_heading = QtWidgets.QLabel(self.widget_registration_portal)
        self.status_heading.setGeometry(QtCore.QRect(680, 310, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.status_heading.setFont(font)
        self.status_heading.setStyleSheet("border:none")
        self.status_heading.setObjectName("status_heading")
        self.add_button = QtWidgets.QPushButton(self.widget_registration_portal)
        self.add_button.setGeometry(QtCore.QRect(740, 490, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.add_button.setFont(font)
        self.add_button.setMouseTracking(True)
        self.add_button.setAutoFillBackground(False)
        self.add_button.setStyleSheet("border: 2px solid black; \n"
"color: white;\n"
"background-color:#8d5293 ;\n"
"border-radius:10px")
        self.add_button.setObjectName("add_button")
        self.face_detected_heading = QtWidgets.QLabel(self.widget_registration_portal)
        self.face_detected_heading.setGeometry(QtCore.QRect(630, 360, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.face_detected_heading.setFont(font)
        self.face_detected_heading.setStyleSheet("border: 2px solid black; \n"
"color: white;\n"
"background-color:#8d5293 ;\n"
"border-radius:10px")
        self.face_detected_heading.setObjectName("face_detected_heading")
        self.registration_portal_heading = QtWidgets.QLabel(self.widget_registration_portal)
        self.registration_portal_heading.setGeometry(QtCore.QRect(170, 10, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.registration_portal_heading.setFont(font)
        self.registration_portal_heading.setStyleSheet("color: white;\n"
"background-color: black;\n"
"border:none")
        self.registration_portal_heading.setObjectName("registration_portal_heading")
        self.label_6 = QtWidgets.QLabel(self.widget_registration_portal)
        self.label_6.setGeometry(QtCore.QRect(270, 430, 81, 71))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../../Users/Zulfiqar/Pictures/cameraicon.PNG"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.background_frame_top_1.raise_()
        self.user_icon_button.raise_()
        self.hamburger_button.raise_()
        self.Horizontal_line_at_top_1.raise_()
        self.navigation_bar.raise_()
        self.widget_registration_portal.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.navigation_bar.setText(_translate("MainWindow", "Home -> RoomInfo-> Registration"))
        self.add_student_logo_atTop.setText(_translate("MainWindow", "      Add Student Page"))
        self.name_input_box.setPlaceholderText(_translate("MainWindow", "Enter Name"))
        self.name_heading.setText(_translate("MainWindow", "       Name "))
        self.id_heading.setText(_translate("MainWindow", "      Roll Number"))
        self.id_input_box.setPlaceholderText(_translate("MainWindow", "Enter Roll Number"))
        self.or_heading.setText(_translate("MainWindow", "OR"))
        self.enter_button.setText(_translate("MainWindow", "Enter"))
        self.upload_pic_button.setText(_translate("MainWindow", "\n"
"Click here \n"
" to\n"
"upload picture\n"
" "))
        self.useCamera_heading.setText(_translate("MainWindow", "  Use camera "))
        self.status_heading.setText(_translate("MainWindow", " Status"))
        self.add_button.setText(_translate("MainWindow", "Add"))
        self.add_button.setShortcut(_translate("MainWindow", "Return"))
        self.face_detected_heading.setText(_translate("MainWindow", "Face Detetcted"))
        self.registration_portal_heading.setText(_translate("MainWindow", "Registration Portal "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())