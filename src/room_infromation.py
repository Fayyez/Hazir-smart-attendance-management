from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
from Classes.classes import ClassRoom
from PyQt5.QtWidgets import QMessageBox

folder_path = os.getcwd() + "/src"
sample_classroom = {'sn_123_class_2' : ClassRoom('Human And Computer Interaction', 8, "sn_123", 'sn_123_class_2')}

class Ui_RoomInfo(object):
    currentwindow = None
    classrooms = None

    def setupUi(self, mainwindow, classrooms):
        self.classrooms = sample_classroom
        self.currentwindow = mainwindow
        mainwindow.setObjectName("RoomInfo")
        mainwindow.resize(1000, 700)
        mainwindow.setStyleSheet("background-color:#2f3c7e")
        self.display_card = QtWidgets.QWidget(mainwindow)
        self.display_card.setGeometry(QtCore.QRect(40, 130, 401, 471))
        self.display_card.setStyleSheet("background-color:#fbeaeb;\n" "border-radius:30px;")
        self.display_card.setObjectName("widget")
        self.pushButton_2 = QtWidgets.QPushButton(self.display_card)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 340, 101, 101))
        user_icon = QtGui.QIcon()
        user_icon.addPixmap(QtGui.QPixmap(folder_path+"/assets/u2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_2.setIcon(user_icon)
        self.pushButton_2.clicked.connect(self.addmember)

        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.roomdetailsLabel_2 = QtWidgets.QLabel(self.display_card)
        self.roomdetailsLabel_2.setGeometry(QtCore.QRect(110, 30, 171, 41))
        # allign the text to right
        self.roomdetailsLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.roomdetailsLabel_2.setFont(font)
        self.roomdetailsLabel_2.setStyleSheet("border:2px solid black;\n" "border-radius: 10px;")
        self.roomdetailsLabel_2.setObjectName("roomdetailsLabel_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.display_card)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(29, 110, 341, 211))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        # add room details to the card here
        self.room_title_lable = QtWidgets.QLabel(self.gridLayoutWidget)
        self.room_title_lable.setObjectName("room_title_lable")
        self.room_title_lable.setFont(font)
        self.room_title_lable.setText(f"Title: {classrooms['sn_123_class_2'].title}")
        self.room_title_lable.setStyleSheet("border:none;")
        # increase the size of the label
        self.room_title_lable.setGeometry(QtCore.QRect(65, 220, 300, 300))

        self.addmemberLabel_3 = QtWidgets.QLabel(self.display_card)
        self.addmemberLabel_3.setGeometry(QtCore.QRect(240, 430, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.addmemberLabel_3.setFont(font)
        self.addmemberLabel_3.setStyleSheet("border:none;")
        self.addmemberLabel_3.setObjectName("addmemberLabel_3")
        self.widget_2 = QtWidgets.QWidget(mainwindow)
        self.widget_2.setGeometry(QtCore.QRect(-1, 0, 1001, 51))
        self.widget_2.setStyleSheet("background-color:#fbeaeb")
        self.widget_2.setObjectName("widget_2")
        self.hometitleLabel = QtWidgets.QLabel(self.display_card)
        self.hometitleLabel.setGeometry(QtCore.QRect(20, 80, 281, 230))
        font.setWeight(10)
        self.hometitleLabel.setFont(font)

        self.homepageLabel = QtWidgets.QLabel(self.widget_2)
        self.homepageLabel.setGeometry(QtCore.QRect(410, 10, 201, 31))
        self.homepageLabel.setFont(font)
        self.homepageLabel.setStyleSheet("border:none;")
        self.homepageLabel.setObjectName("homepageLabel")
        self.homepageLabel.setText("Room Information")

        self.hometitleLabel.setText(f"Title: {classrooms['sn_123_class_2'].title}\nNumber of Students: {str(self.classrooms['sn_123_class_2'].studentount)}\nCLass ID: {classrooms['sn_123_class_2'].class_id}")
        self.hometitleLabel.setStyleSheet("QLabel {"
                         "  alignment: left top;"
                         "  padding: 5px;"
                         "  qproperty-wordWrap: true;"
                         " color: black;"
                         "}")
        self.hometitleLabel.setObjectName("hometitleLabel")








        self.hometitleLabel.setObjectName("hometitleLabel")
        self.bread_crumbs_label = QtWidgets.QLabel(self.widget_2)
        self.bread_crumbs_label.setGeometry(QtCore.QRect(80, 10, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.bread_crumbs_label.setFont(font)
        self.bread_crumbs_label.setObjectName("bread_crumbs_label")

        self.hamburegrbutton = QtWidgets.QPushButton(self.widget_2)
        self.hamburegrbutton.setGeometry(QtCore.QRect(940, 0, 61, 51))
        # self.hamburegrbutton.setGeometry(QtCore.QRect(880, 0, 100, 51))
        ham_button_icon = QtGui.QIcon()
        ham_button_icon.addPixmap(QtGui.QPixmap(folder_path+"/assets/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # increase the size of the icon
        self.hamburegrbutton.setIconSize(QtCore.QSize(40, 40))
        self.hamburegrbutton.setIcon(ham_button_icon)

        self.hamburegrbutton.clicked.connect(self.show_hamburger_menu)
        self.hamburegrbutton.setText("")
        self.hamburegrbutton.setObjectName("hamburegrbutton")
        self.back_widget = QtWidgets.QPushButton(self.widget_2)
        self.back_widget.setGeometry(QtCore.QRect(10, 0, 51, 51))
        back_icon = QtGui.QIcon()
        back_icon.addPixmap(QtGui.QPixmap(folder_path+"/assets/previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_widget.setIconSize(QtCore.QSize(45, 45))
        self.back_widget.setIcon(back_icon)
        self.back_widget.setIconSize(QtCore.QSize(30, 30))

        self.back_widget.clicked.connect(self.backbutton)

        self.back_widget.setText("")
        self.back_widget.setObjectName("pushButton")
        self.start_seesion_button = QtWidgets.QPushButton(mainwindow)
        self.start_seesion_button.setGeometry(QtCore.QRect(620, 260, 241, 81))
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
        self.start_seesion_button.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.start_seesion_button.setFont(font)
        self.start_seesion_button.setStyleSheet("background-color:#fbeaeb;\n"
"color: black;\n"
"border-radius:10px;\n"
"border:none;\n"
"")
        self.start_seesion_button.setObjectName("start_seesion_button")
        self.get_last_report_button = QtWidgets.QPushButton(mainwindow)
        self.get_last_report_button.setGeometry(QtCore.QRect(620, 400, 241, 81))
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
        self.get_last_report_button.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.get_last_report_button.setFont(font)
        self.get_last_report_button.setStyleSheet("background-color:#b1b40a;\n"
"color: black;\n"
"border-radius:10px;\n"
"border:none;\n"
"")
        self.get_last_report_button.setObjectName("get_last_report_button")
        self.get_last_report_button.clicked.connect(self.getreport)

        self.userpic = QtWidgets.QLabel(mainwindow)
        self.userpic.setGeometry(QtCore.QRect(630, 270, 61, 61))
        self.userpic.setText("")
        self.userpic.setPixmap(QtGui.QPixmap(f"{folder_path}/assets/session.png"))
        self.userpic.setScaledContents(True)
        self.userpic.setObjectName("userpic")
        self.userpic_2 = QtWidgets.QLabel(mainwindow)
        self.userpic_2.setGeometry(QtCore.QRect(630, 410, 61, 61))
        self.userpic_2.setText("")
        self.userpic_2.setPixmap(QtGui.QPixmap(f"{folder_path}/assets/report.png"))
        self.userpic_2.setScaledContents(True)
        self.userpic_2.setObjectName("userpic_2")

        ### setting text and label snames
        self.roomdetailsLabel_2.setText("Room Details")
        self.roomdetailsLabel_2.setText("Room Details")
        self.addmemberLabel_3.setText("Add Member")
        self.bread_crumbs_label.setText("HomePage->RoomInformation")
        self.start_seesion_button.setText("        Start Session")
        self.get_last_report_button.setText("            Get Last Report")
    
    def show_hamburger_menu(self):
        menu = QtWidgets.QMenu(self.widget_2)
        menu.setFixedWidth(150)
        menu.setFixedHeight(150)
        # Adjust the x-coordinate to shift the menu towards the left
        position = QtCore.QPoint(-150, self.hamburegrbutton.height() + 10)
        position = QtCore.QPoint(-25, self.hamburegrbutton.height() + 10)
        edit_profile_action = menu.addAction("Edit Profile")
        add_room_action = menu.addAction("Edit\Add Room")
        add_member_action = menu.addAction("Add Member")
        condition=menu.addAction("Terms and conditions")
        logout_action = menu.addAction("Logout")
        # Set a fixed width and height for the menu
        action = menu.exec_(self.hamburegrbutton.mapToGlobal(position))
      
        # action = menu.exec_(self.hamburegrbutton.mapToGlobal(QtCore.QPoint(0, self.hamburegrbutton.height())))
       
        if action == edit_profile_action:
            # Handle "Edit Profile" action
            print("Edit Profile")
        elif action == add_room_action:
            # Handle "Add Room" action
            print("Add Room")
        elif action == add_member_action:
            # Handle "Add Member" action
            print("Add Member")
        elif action == logout_action:
            # Handle "Logout" action
            print("Logout")
        elif action== condition:
            print("conditions clicked")    

        self.retranslateUi()
       # QtCore.QMetaObject.connectSlotsByName()

    def addmember(self):
        from add_member_page_ui import MemberForm
        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QDialog()
        ui = MemberForm()
        ui.setupUi(window)
        self.currentwindow.close()
        window.show()
        window.exec_()
        sys.exit(app.exec_())

    def startSession(self):
        from attendace_session_final_ui import Ui_Dialog
        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(window)
        self.currentwindow.close()
        window.show()
        window.exec_()
        sys.exit(app.exec_())


    def backbutton(self):
        from home_page_ui import Ui_homepage
        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QDialog()
        ui = Ui_homepage()
        ui.setupUi(window, self.classrooms)
        self.currentwindow.close()
        window.show()
        window.exec_()
        sys.exit(app.exec_())

    def getreport(self):
        msg_box = QMessageBox()
        msg_box.setText("Report was generated successfully and saved in the output folder.")
        msg_box.exec_() 


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        RoomInfo.setWindowTitle(_translate("RoomInfo", "Room Information"))
        self.roomdetailsLabel_2.setText(_translate("RoomInfo", "Room Details"))
        self.addmemberLabel_3.setText(_translate("RoomInfo", "Add Member"))
        self.hometitleLabel.setText(_translate("RoomInfo", "Room Title"))
        self.bread_crumbs_label.setText(_translate("RoomInfo", "HomePage->RoomInformation"))
        self.start_seesion_button.setText(_translate("RoomInfo", "        Start Session"))
        self.get_last_report_button.setText(_translate("RoomInfo", "            Get Last Report"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RoomInfo = QtWidgets.QDialog()
    ui = Ui_RoomInfo()
    ui.setupUi(RoomInfo, sample_classroom)
    RoomInfo.show()
    sys.exit(app.exec_())