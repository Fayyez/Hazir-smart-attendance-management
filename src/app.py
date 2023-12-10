from login_screen import LoginPage
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login_page = LoginPage()
    mainwindow = QtWidgets.QMainWindow()
    login_page.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())
 
