from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(813, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Array of class names
        class_names = ["Math", "Physics", "Chemistry", "Biology", "History", "English", "Computer Science", "Geography"]

        # Create class buttons dynamically
        self.class_buttons = []
        for i, class_name in enumerate(class_names):
            button = QtWidgets.QPushButton(self.centralwidget)
            button.setGeometry(QtCore.QRect(110 + (i % 2) * 380, 240 + (i // 2) * 170, 171, 91))
            button.setCheckable(False)
            button.setObjectName(f"pushButton_{i}")
            button.setText(class_name)
            self.class_buttons.append(button)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 100, 301, 22))
        self.lineEdit.setObjectName("lineEdit")

        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(780, 10, 16, 541))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.verticalScrollBar.setValue(self.verticalScrollBar.maximum())  # Start at the bottom

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 813, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect the search bar
        self.lineEdit.returnPressed.connect(self.filter_classes)

        # Connect the vertical scrollbar
        self.verticalScrollBar.valueChanged.connect(self.scroll_classes)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def filter_classes(self):
        # Filter classes based on the search bar input
        text = self.lineEdit.text()
        for button in self.class_buttons:
            if text.lower() in button.text().lower():
                button.show()
            else:
                button.hide()
        # Reset scroll position to bottom
        self.verticalScrollBar.setValue(self.verticalScrollBar.maximum())

    def scroll_classes(self, value):
        # Ensure the vertical scrollbar does not allow scrolling upward
        self.verticalScrollBar.setValue(min(value, self.verticalScrollBar.maximum()))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
