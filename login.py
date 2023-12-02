from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input_email = QtWidgets.QLineEdit(self.centralwidget)
        self.input_email.setGeometry(QtCore.QRect(270, 250, 201, 31))
        self.input_email.setObjectName("input_email")
        self.input_password = QtWidgets.QLineEdit(self.centralwidget)
        self.input_password.setGeometry(QtCore.QRect(270, 300, 201, 31))
        self.input_password.setObjectName("input_password")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(290, 390, 131, 31))
        self.login_button.setMouseTracking(False)
        self.login_button.setObjectName("login_button")
        self.forgot_pass_button = QtWidgets.QLineEdit(self.centralwidget)
        self.forgot_pass_button.setEnabled(False)
        self.forgot_pass_button.setGeometry(QtCore.QRect(270, 340, 101, 22))
        self.forgot_pass_button.setObjectName("forgot_pass_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect the login button to the login function
        self.login_button.clicked.connect(self.login)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.input_email.setText(_translate("MainWindow", "Email"))
        self.input_password.setText(_translate("MainWindow", "password"))
        self.login_button.setText(_translate("MainWindow", "Log in"))
        self.forgot_pass_button.setText(_translate("MainWindow", "forgot password"))

    def login(self):
        # Function to handle login button click
        # Check login credentials (e.g., against a database)
        email = self.input_email.text()
        password = self.input_password.text()

        # For simplicity, check if email is not empty
        if email:
            # If login is successful, open the home page
            self.open_home_page()
        else:
            QMessageBox.warning(None, "Login Failed", "Invalid email or password")

    def open_home_page(self):
        # Open the home page window
        self.home_page = QtWidgets.QMainWindow()
        ui_home = Ui_HomePage()
        ui_home.setupUi(self.home_page)
        self.home_page.show()
        MainWindow.hide()  # Hide the login window

class Ui_HomePage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 200, 221, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Home Page"))
        self.label.setText(_translate("MainWindow", "Welcome to the Home Page"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
