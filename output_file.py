import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QGroupBox, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt, QRect

class Ui_loginpage(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, loginpage):
        loginpage.setObjectName("loginpage")
        loginpage.resize(1058, 812)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(0, 255, 0))
        loginpage.setPalette(palette)

        self.groupBox = QGroupBox(loginpage)
        self.groupBox.setGeometry(QRect(170, 300, 721, 311))
        self.groupBox.setObjectName("groupBox")

        self.label = QLabel(self.groupBox)
        self.label.setGeometry(QRect(20, 50, 111, 21))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText("Username:")

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setGeometry(QRect(20, 130, 121, 21))
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Password:")

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QRect(20, 80, 271, 31))
        font = QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QRect(20, 160, 271, 31))
        font = QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setEchoMode(QLineEdit.Password)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setGeometry(QRect(390, 260, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Login")

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QRect(280, 260, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText("Sign Up!")

        self.retranslateUi(loginpage)
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.sign_up)

    def retranslateUi(self, loginpage):
        _translate = QApplication.translate
        loginpage.setWindowTitle(_translate("loginpage", "Frame"))
        self.groupBox.setTitle(_translate("loginpage", "Credentials"))
        self.label.setText(_translate("loginpage", "Username:"))
        self.label_2.setText(_translate("loginpage", "Password:"))

    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_3.text()

        # Add your login authentication logic here
        # For demonstration purposes, check if username is "admin" and password is "password"
        if username == "admin" and password == "password":
            QMessageBox.information(self, "Login", "Login successful!")
        else:
            QMessageBox.warning(self, "Login", "Invalid username or password!")

    def sign_up(self):
        # Add your sign-up logic here, if required
        QMessageBox.information(self, "Sign Up", "Sign-up functionality not implemented yet!")

def main():
    app = QApplication(sys.argv)
    loginpage = Ui_loginpage()
    loginpage.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
