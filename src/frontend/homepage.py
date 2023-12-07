import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QScrollBar, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

class ClassDetailsDialog(QtWidgets.QDialog):
    def __init__(self, class_num, parent=None):
        super(ClassDetailsDialog, self).__init__(parent)
        self.setWindowTitle(f"Class {class_num} Details")
        self.setGeometry(100, 100, 300, 200)

        # You can add widgets here to display class details
        details_label = QtWidgets.QLabel(f"Details for Class {class_num}", self)
        details_label.setAlignment(QtCore.Qt.AlignCenter)
        details_label.setGeometry(QtCore.QRect(50, 50, 200, 100))

class Ui_homepage(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Ui_homepage, self).__init__(parent)

    def setupUi(self, homepage, num_classes):
        homepage.setStyleSheet("background-color: black;")
        homepage.setObjectName("homepage")
        homepage.resize(1000, 700)

        top_widget = QtWidgets.QWidget(homepage)
        top_widget.setGeometry(QtCore.QRect(-1, -1, 1001, 61))
        top_widget.setStyleSheet("background-color: #8d5293;")

        self.scroll_area = QtWidgets.QScrollArea(homepage)
        self.scroll_area.setGeometry(QtCore.QRect(0, 150, 1000, 500))
        self.scroll_area.setWidgetResizable(True)

        self.gridLayoutWidget = QtWidgets.QWidget()
        self.scroll_area.setWidget(self.gridLayoutWidget)

        label = QtWidgets.QLabel("Homepage", top_widget)
        label.setGeometry(QtCore.QRect(420, 5, 161, 51))
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setStyleSheet("color: white; background-color: black;border-radius: 15px;")
        font = QtGui.QFont("Yu Gothic UI Semibold", 16)
        label.setFont(font)

        search_bar = QtWidgets.QLineEdit(homepage)
        search_bar.setGeometry(QtCore.QRect(330, 80, 301, 41))
        search_bar.setPlaceholderText("Search")
        search_bar.setStyleSheet("background-color: #8d5293; color: white; border: 2px solid #8d5293; border-radius: 10px;")
        font = QtGui.QFont("Yu Gothic UI", 12)
        search_bar.setFont(font)


        # change the title here as well in scroll search bar
        completer = QtWidgets.QCompleter([f"Classe {class_num}" for class_num in range(1, num_classes + 1)], search_bar)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        search_bar.setCompleter(completer)

        grid_width = 500
        grid_height = 500

        self.classcards = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.classcards.setContentsMargins(100, 100, 100, 100)

        num_rows = (num_classes + 1) // 2
        num_columns = 2

        x = 0
        y = 50

        for class_num in range(1, num_classes + 1):
            # here room details or title will be entered

            class_card = QtWidgets.QPushButton(f"Classe {class_num}")
            class_card.setFixedSize(150, 150)
            class_card.setStyleSheet(
                "background-color: black; color: white; border: 1px solid white; border-radius: 15px;"
            )
            font = QtGui.QFont("Yu Gothic UI Semibold", 16)
            class_card.setFont(font)

            class_card.clicked.connect(lambda checked, num=class_num: self.class_card_clicked(num))

            row_position = (class_num - 1) // num_columns
            column_position = (class_num - 1) % num_columns + 100

            self.classcards.addWidget(class_card, row_position, column_position, 1, 1)

            x += 400
            if x + 400 > grid_width:
                x = 0
                y += 400

        scrollbar = QtWidgets.QScrollBar(QtCore.Qt.Vertical, homepage)
        scrollbar.setGeometry(QtCore.QRect(980, 150, 20, 500))
        scrollbar.valueChanged.connect(self.scroll_area.verticalScrollBar().setValue)


        self.retranslateUi(homepage)
        QtCore.QMetaObject.connectSlotsByName(homepage)

    def search_classes(self, search_term,num_classes):
        for class_num in range(1, self.num_classes + 1):
            class_card = self.classcards.itemAt(class_num - 1).widget()

            # change the room title here as well
            class_name = f"Classet {class_num}"

            if search_term.lower() in class_name.lower():
                class_card.show()
            else:
                class_card.hide()

    def class_card_clicked(self, class_num):

        # change title here as well
        print(f"Class {class_num} card clicked!")
        index = class_num
        print(index)
        # here index is found so call the detail room info screen of given index of array

    def retranslateUi(self, homepage):
        _translate = QtCore.QCoreApplication.translate
        homepage.setWindowTitle(_translate("homepage", "Dialog"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    homepage = QtWidgets.QDialog()
    ui = Ui_homepage()
    num_classes = 10
    ui.setupUi(homepage, num_classes)
    homepage.show()
    sys.exit(app.exec_())
