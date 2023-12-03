# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\src\frontend\roomInfo.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_a(object):
    def setupUi(self, a):
        a.setObjectName("a")
        a.resize(1000, 700)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        a.setPalette(palette)
        a.setFocusPolicy(QtCore.Qt.WheelFocus)
        a.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(a)
        self.centralwidget.setObjectName("centralwidget")
        self.Horizontal_line_at_top_1 = QtWidgets.QFrame(self.centralwidget)
        self.Horizontal_line_at_top_1.setGeometry(QtCore.QRect(0, 42, 1001, 16))
        self.Horizontal_line_at_top_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.Horizontal_line_at_top_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Horizontal_line_at_top_1.setObjectName("Horizontal_line_at_top_1")
        self.navigation_bar = QtWidgets.QLabel(self.centralwidget)
        self.navigation_bar.setGeometry(QtCore.QRect(10, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.navigation_bar.setFont(font)
        self.navigation_bar.setObjectName("navigation_bar")
        self.Horizontal_line_at_top_2 = QtWidgets.QFrame(self.centralwidget)
        self.Horizontal_line_at_top_2.setGeometry(QtCore.QRect(6, 112, 1001, 16))
        self.Horizontal_line_at_top_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.Horizontal_line_at_top_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Horizontal_line_at_top_2.setObjectName("Horizontal_line_at_top_2")
        self.room_title_heading = QtWidgets.QLabel(self.centralwidget)
        self.room_title_heading.setGeometry(QtCore.QRect(10, 60, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.room_title_heading.setFont(font)
        self.room_title_heading.setObjectName("room_title_heading")
        self.room_name = QtWidgets.QLabel(self.centralwidget)
        self.room_name.setGeometry(QtCore.QRect(185, 60, 351, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.room_name.setFont(font)
        self.room_name.setObjectName("room_name")
        self.memebr_count_heading = QtWidgets.QLabel(self.centralwidget)
        self.memebr_count_heading.setGeometry(QtCore.QRect(670, 60, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.memebr_count_heading.setFont(font)
        self.memebr_count_heading.setObjectName("memebr_count_heading")
        self.total_students = QtWidgets.QLabel(self.centralwidget)
        self.total_students.setGeometry(QtCore.QRect(870, 60, 51, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.total_students.setFont(font)
        self.total_students.setObjectName("total_students")
        self.m_user_icon_image_box = QtWidgets.QLabel(self.centralwidget)
        self.m_user_icon_image_box.setGeometry(QtCore.QRect(940, 60, 51, 51))
        self.m_user_icon_image_box.setText("")
        self.m_user_icon_image_box.setPixmap(QtGui.QPixmap(".\\src\\frontend\\../../../../../Downloads/multiple_user_icon.png"))
        self.m_user_icon_image_box.setScaledContents(True)
        self.m_user_icon_image_box.setObjectName("m_user_icon_image_box")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(930, 2, 61, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
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
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
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
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
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
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
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
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
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
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
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
        self.pushButton.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\src\\frontend\\../assets/hamburgerr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(80, 60))
        self.pushButton.setObjectName("pushButton")
        self.background_frame_top_1 = QtWidgets.QFrame(self.centralwidget)
        self.background_frame_top_1.setGeometry(QtCore.QRect(0, 0, 1001, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(226, 226, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(226, 226, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(226, 226, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        self.background_frame_top_1.setPalette(palette)
        self.background_frame_top_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background_frame_top_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background_frame_top_1.setObjectName("background_frame_top_1")
        self.Hazirio_logo_atTop = QtWidgets.QLabel(self.background_frame_top_1)
        self.Hazirio_logo_atTop.setGeometry(QtCore.QRect(380, 10, 221, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 240, 24))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 240, 24))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.Hazirio_logo_atTop.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Hazirio_logo_atTop.setFont(font)
        self.Hazirio_logo_atTop.setObjectName("Hazirio_logo_atTop")
        self.start_attendance_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_attendance_button.setGeometry(QtCore.QRect(570, 200, 271, 111))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.start_attendance_button.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.start_attendance_button.setFont(font)
        self.start_attendance_button.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.start_attendance_button.setAcceptDrops(True)
        self.start_attendance_button.setAutoDefault(False)
        self.start_attendance_button.setDefault(True)
        self.start_attendance_button.setFlat(False)
        self.start_attendance_button.setObjectName("start_attendance_button")
        self.get_last_report_button = QtWidgets.QPushButton(self.centralwidget)
        self.get_last_report_button.setGeometry(QtCore.QRect(600, 360, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.get_last_report_button.setFont(font)
        self.get_last_report_button.setObjectName("get_last_report_button")
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(600, 460, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.back_button.setFont(font)
        self.back_button.setObjectName("back_button")
        self.room_detail_heading = QtWidgets.QLabel(self.centralwidget)
        self.room_detail_heading.setGeometry(QtCore.QRect(30, 160, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.room_detail_heading.setFont(font)
        self.room_detail_heading.setObjectName("room_detail_heading")
        self.romm_details_self_write = QtWidgets.QTextBrowser(self.centralwidget)
        self.romm_details_self_write.setGeometry(QtCore.QRect(30, 220, 311, 171))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.romm_details_self_write.setPalette(palette)
        self.romm_details_self_write.setObjectName("romm_details_self_write")
        self.calender_icon = QtWidgets.QLabel(self.centralwidget)
        self.calender_icon.setGeometry(QtCore.QRect(190, 460, 71, 61))
        self.calender_icon.setText("")
        self.calender_icon.setPixmap(QtGui.QPixmap(".\\src\\frontend\\../../../../../Downloads/calender.png"))
        self.calender_icon.setScaledContents(True)
        self.calender_icon.setObjectName("calender_icon")
        self.current_date_text = QtWidgets.QLabel(self.centralwidget)
        self.current_date_text.setGeometry(QtCore.QRect(60, 460, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.current_date_text.setFont(font)
        self.current_date_text.setObjectName("current_date_text")
        self.background_frame_top_2 = QtWidgets.QFrame(self.centralwidget)
        self.background_frame_top_2.setGeometry(QtCore.QRect(0, 50, 1001, 71))
        self.background_frame_top_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background_frame_top_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background_frame_top_2.setObjectName("background_frame_top_2")
        self.user_icon_button = QtWidgets.QPushButton(self.centralwidget)
        self.user_icon_button.setGeometry(QtCore.QRect(870, 0, 57, 50))
        self.user_icon_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\src\\frontend\\../assets/user_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.user_icon_button.setIcon(icon1)
        self.user_icon_button.setIconSize(QtCore.QSize(58, 54))
        self.user_icon_button.setObjectName("user_icon_button")
        self.background_frame_top_1.raise_()
        self.background_frame_top_2.raise_()
        self.user_icon_button.raise_()
        self.Horizontal_line_at_top_1.raise_()
        self.navigation_bar.raise_()
        self.Horizontal_line_at_top_2.raise_()
        self.room_title_heading.raise_()
        self.room_name.raise_()
        self.memebr_count_heading.raise_()
        self.total_students.raise_()
        self.m_user_icon_image_box.raise_()
        self.pushButton.raise_()
        self.start_attendance_button.raise_()
        self.get_last_report_button.raise_()
        self.back_button.raise_()
        self.room_detail_heading.raise_()
        self.romm_details_self_write.raise_()
        self.calender_icon.raise_()
        self.current_date_text.raise_()
        a.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(a)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        a.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(a)
        self.statusbar.setObjectName("statusbar")
        a.setStatusBar(self.statusbar)

        self.retranslateUi(a)
        QtCore.QMetaObject.connectSlotsByName(a)

    def retranslateUi(self, a):
        _translate = QtCore.QCoreApplication.translate
        a.setWindowTitle(_translate("a", "attendance"))
        self.navigation_bar.setText(_translate("a", "home -> roomInfo"))
        self.room_title_heading.setText(_translate("a", "Room Title : "))
        self.room_name.setText(_translate("a", "Probability an dstatistics"))
        self.memebr_count_heading.setText(_translate("a", "Student Count :"))
        self.total_students.setText(_translate("a", "88"))
        self.Hazirio_logo_atTop.setText(_translate("a", "Room Info Page"))
        self.start_attendance_button.setText(_translate("a", "Start Attendance"))
        self.get_last_report_button.setText(_translate("a", "Get last Report"))
        self.back_button.setText(_translate("a", "Back"))
        self.room_detail_heading.setText(_translate("a", "Room Details : "))
        self.romm_details_self_write.setHtml(_translate("a", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">askdaksdkdsa</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sdkaskdksad</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">dkjaksdhjkhsad</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">akjdskjhajkshd</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.current_date_text.setText(_translate("a", "07/12/2023"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    a = QtWidgets.QMainWindow()
    ui = Ui_a()
    ui.setupUi(a)
    a.show()
    sys.exit(app.exec_())
