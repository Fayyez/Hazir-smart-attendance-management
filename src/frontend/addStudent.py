# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\src\frontend\addStudent.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(999, 688)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.user_icon_button = QtWidgets.QPushButton(self.centralwidget)
        self.user_icon_button.setGeometry(QtCore.QRect(870, 0, 57, 50))
        self.user_icon_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\src\\frontend\\../assets/user_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.user_icon_button.setIcon(icon)
        self.user_icon_button.setIconSize(QtCore.QSize(58, 54))
        self.user_icon_button.setObjectName("user_icon_button")
        self.hamburger_button = QtWidgets.QPushButton(self.centralwidget)
        self.hamburger_button.setGeometry(QtCore.QRect(940, 0, 54, 50))
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
        self.hamburger_button.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.hamburger_button.setFont(font)
        self.hamburger_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\src\\frontend\\../assets/hamburgerr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hamburger_button.setIcon(icon1)
        self.hamburger_button.setIconSize(QtCore.QSize(80, 60))
        self.hamburger_button.setObjectName("hamburger_button")
        self.Horizontal_line_at_top_1 = QtWidgets.QFrame(self.centralwidget)
        self.Horizontal_line_at_top_1.setGeometry(QtCore.QRect(0, 42, 1001, 16))
        self.Horizontal_line_at_top_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.Horizontal_line_at_top_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Horizontal_line_at_top_1.setObjectName("Horizontal_line_at_top_1")
        self.navigation_bar = QtWidgets.QLabel(self.centralwidget)
        self.navigation_bar.setGeometry(QtCore.QRect(10, 10, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.navigation_bar.setFont(font)
        self.navigation_bar.setObjectName("navigation_bar")
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
        self.add_student_logo_atTop = QtWidgets.QLabel(self.background_frame_top_1)
        self.add_student_logo_atTop.setGeometry(QtCore.QRect(380, 10, 271, 31))
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
        self.add_student_logo_atTop.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.add_student_logo_atTop.setFont(font)
        self.add_student_logo_atTop.setObjectName("add_student_logo_atTop")
        self.widget_registration_portal = QtWidgets.QWidget(self.centralwidget)
        self.widget_registration_portal.setGeometry(QtCore.QRect(60, 170, 331, 471))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.widget_registration_portal.setFont(font)
        self.widget_registration_portal.setObjectName("widget_registration_portal")
        self.name_input_box = QtWidgets.QLineEdit(self.widget_registration_portal)
        self.name_input_box.setGeometry(QtCore.QRect(50, 80, 231, 41))
        self.name_input_box.setText("")
        self.name_input_box.setObjectName("name_input_box")
        self.name_heading = QtWidgets.QLabel(self.widget_registration_portal)
        self.name_heading.setGeometry(QtCore.QRect(50, 30, 161, 41))
        self.name_heading.setObjectName("name_heading")
        self.id_heading = QtWidgets.QLabel(self.widget_registration_portal)
        self.id_heading.setGeometry(QtCore.QRect(50, 140, 161, 41))
        self.id_heading.setObjectName("id_heading")
        self.id_input_box = QtWidgets.QLineEdit(self.widget_registration_portal)
        self.id_input_box.setGeometry(QtCore.QRect(50, 190, 231, 41))
        self.id_input_box.setText("")
        self.id_input_box.setObjectName("id_input_box")
        self.or_heading = QtWidgets.QLabel(self.widget_registration_portal)
        self.or_heading.setGeometry(QtCore.QRect(210, 290, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.or_heading.setFont(font)
        self.or_heading.setObjectName("or_heading")
        self.useCamera_heading = QtWidgets.QLabel(self.widget_registration_portal)
        self.useCamera_heading.setGeometry(QtCore.QRect(190, 350, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.useCamera_heading.setFont(font)
        self.useCamera_heading.setObjectName("useCamera_heading")
        self.enter_button = QtWidgets.QPushButton(self.widget_registration_portal)
        self.enter_button.setGeometry(QtCore.QRect(190, 240, 93, 28))
        self.enter_button.setObjectName("enter_button")
        self.upload_pic_button = QtWidgets.QPushButton(self.widget_registration_portal)
        self.upload_pic_button.setGeometry(QtCore.QRect(10, 300, 131, 121))
        self.upload_pic_button.setObjectName("upload_pic_button")
        self.registration_portal_heading = QtWidgets.QLabel(self.centralwidget)
        self.registration_portal_heading.setGeometry(QtCore.QRect(100, 90, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.registration_portal_heading.setFont(font)
        self.registration_portal_heading.setObjectName("registration_portal_heading")
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setGeometry(QtCore.QRect(840, 530, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.add_button.setFont(font)
        self.add_button.setMouseTracking(True)
        self.add_button.setAutoFillBackground(False)
        self.add_button.setStyleSheet("")
        self.add_button.setObjectName("add_button")
        self.gridBox_cameraView = QtWidgets.QGroupBox(self.centralwidget)
        self.gridBox_cameraView.setGeometry(QtCore.QRect(470, 100, 401, 271))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.gridBox_cameraView.setPalette(palette)
        self.gridBox_cameraView.setObjectName("gridBox_cameraView")
        self.gridLayout = QtWidgets.QGridLayout(self.gridBox_cameraView)
        self.gridLayout.setObjectName("gridLayout")
        self.face_detected_heading = QtWidgets.QLabel(self.centralwidget)
        self.face_detected_heading.setGeometry(QtCore.QRect(510, 470, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.face_detected_heading.setFont(font)
        self.face_detected_heading.setObjectName("face_detected_heading")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 410, 71, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.label_2.setPalette(palette)
        self.label_2.setPixmap(QtGui.QPixmap(".\\src\\frontend\\../assets/tick.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.status_heading = QtWidgets.QLabel(self.centralwidget)
        self.status_heading.setGeometry(QtCore.QRect(690, 410, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.status_heading.setFont(font)
        self.status_heading.setObjectName("status_heading")
        self.registration_portal_heading.raise_()
        self.background_frame_top_1.raise_()
        self.user_icon_button.raise_()
        self.hamburger_button.raise_()
        self.Horizontal_line_at_top_1.raise_()
        self.navigation_bar.raise_()
        self.widget_registration_portal.raise_()
        self.add_button.raise_()
        self.gridBox_cameraView.raise_()
        self.face_detected_heading.raise_()
        self.label_2.raise_()
        self.status_heading.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 999, 26))
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
        self.navigation_bar.setText(_translate("MainWindow", "home -> roomInfo-> registration"))
        self.add_student_logo_atTop.setText(_translate("MainWindow", "Add Student Page"))
        self.name_heading.setText(_translate("MainWindow", "Name :"))
        self.id_heading.setText(_translate("MainWindow", "Id/Roll no :"))
        self.or_heading.setText(_translate("MainWindow", "OR"))
        self.useCamera_heading.setText(_translate("MainWindow", "Use camera ->"))
        self.enter_button.setText(_translate("MainWindow", "Enter"))
        self.upload_pic_button.setText(_translate("MainWindow", "\n""Click here \n" " to\n""upload pic\n"" "))
        self.registration_portal_heading.setText(_translate("MainWindow", "Registration Portal : "))
        self.add_button.setText(_translate("MainWindow", "Add"))
        self.add_button.setShortcut(_translate("MainWindow", "Return"))
        self.face_detected_heading.setText(_translate("MainWindow", "Face Detetcted"))
        self.label_2.setText(_translate("MainWindow", "status"))
        self.status_heading.setText(_translate("MainWindow", "Status"))
       # self.upload_pic_button.clicked.connect(self.showDropBox)

    # def showDropBox(self,event):
        
    #     demo = AppDemo()
    #     demo.show()
        
    
        
class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n Drop Image Here \n\n')
        self.setStyleSheet('''
            QLabel{
                border: 4px dashed #aaa
            }
        ''')

    def setPixmap(self, image):
        super().setPixmap(image)

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 400)
        self.setAcceptDrops(True)

        mainLayout = QVBoxLayout()

        self.photoViewer = ImageLabel()
        mainLayout.addWidget(self.photoViewer)

        self.setLayout(mainLayout)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.set_image(file_path)

            event.accept()
        else:
            event.ignore()

    def set_image(self, file_path):
        self.photoViewer.setPixmap(QPixmap(file_path))
       




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
