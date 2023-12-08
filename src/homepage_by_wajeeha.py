import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QLineEdit, QCompleter, QScrollBar, QLabel, QPushButton, QVBoxLayout
# from PyQt5.QtWidgets import QDialog, QLineEdit, QCompleter, QScrollBar, QLabel, QPushButton
from PyQt5.QtGui import QFont



class Ui_homepage(QtWidgets.QDialog,):
    def setupUi(self, homepage, num_classes):
        self.num_classes = num_classes

        homepage.setStyleSheet("background-color: black;")
        homepage.setObjectName("homepage")
        homepage.resize(1000, 700)

        top_widget = QtWidgets.QWidget(homepage)
        top_widget.setGeometry(QtCore.QRect(-1, -1, 1001, 61))
        top_widget.setStyleSheet("background-color: #8d5293;")  # Set the background color of the top widget

        self.gridLayoutWidget = QtWidgets.QWidget(homepage)
        
        hamburger_button = QPushButton(top_widget)
        hamburger_button.setGeometry(QtCore.QRect(925, 20, 51, 31))
        hamburger_icon = QtGui.QIcon("../../Users/Zulfiqar/Pictures/hamburger_icon3.png")
        hamburger_button.setIcon(hamburger_icon)
        hamburger_button.setIconSize(QtCore.QSize(70, 30))
        hamburger_button.setFlat(True)
        hamburger_button.setStyleSheet("QPushButton { background-color: #8d5293; border: 0px; }")

        add_room_button = QPushButton(homepage)
        add_room_button.setGeometry(QtCore.QRect(879, 560, 71, 61))
        add_room_icon = QtGui.QIcon("../../Users/Zulfiqar/Pictures/add_room_icon.png")
        add_room_button.setIcon(add_room_icon)
        add_room_button.setIconSize(QtCore.QSize(71, 61))
        add_room_button.setFlat(True)
        add_room_button.setStyleSheet("QPushButton { background-color: black; border: 0px; }")

        label = QLabel("Homepage", top_widget)
        label.setGeometry(QtCore.QRect(420, 5, 161, 51))
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setStyleSheet("color: white; background-color: black;border-radius: 15px;")
        font = QFont("Yu Gothic UI Semibold", 16)
        label.setFont(font)

        search_bar = QLineEdit(homepage)
        search_bar.setGeometry(QtCore.QRect(330, 80, 301, 41))
        search_bar.setPlaceholderText("Search")
        search_bar.setStyleSheet("background-color: #8d5293; color: white; border: 2px solid #8d5293; border-radius: 10px;")
        font = QFont("Yu Gothic UI", 12)
        search_bar.setFont(font)

    
        completer = QCompleter([f"Class {class_num}" for class_num in range(1, num_classes + 1)], search_bar)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        search_bar.setCompleter(completer)
        

        add_room_label = QLabel("Add Room", homepage)
        add_room_label.setGeometry(QtCore.QRect(879, 625, 71, 20))
        add_room_label.setAlignment(QtCore.Qt.AlignCenter)
        add_room_label.setStyleSheet("color: white; font: 10pt 'Yu Gothic UI Semibold';")

        top_left_button = QPushButton(top_widget)
        top_left_button.setGeometry(QtCore.QRect(8, 20, 51, 31))  # Adjust the size and position as needed
        top_left_button.setIcon(QtGui.QIcon("../../Users/Zulfiqar/Pictures/backbutton2.png"))  # Replace "path/to/your/image.jpg" with the actual path to your image      
        top_left_button.setIconSize(QtCore.QSize(51, 31))  # Set the icon size to match the button size
        top_left_button.setFlat(True)
        top_left_button.setStyleSheet("QPushButton { background-color:  #8d5293; border: 0px; }")

       



        grid_width = 500
        grid_height = 500

        grid_x = 0
        grid_y = homepage.height() - grid_height - 10

        self.gridLayoutWidget.setGeometry(QtCore.QRect(grid_x, grid_y, grid_width, grid_height))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.classcards = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.classcards.setContentsMargins(0, 0, 0, 0)
        self.classcards.setObjectName("classcards")

        num_rows = (num_classes + 1) // 2
        num_columns = 2
        for class_num in range(1, num_classes + 1):
            class_card = QtWidgets.QPushButton(f"Class {class_num}")
            class_card.setFixedSize(150, 150)
            class_card.setStyleSheet("background-color: black; color: white; border: 1px solid white; border-radius: 15px;")
            font = QFont("Yu Gothic UI Semibold", 16)
            class_card.setFont(font)
            class_card.clicked.connect(self.class_card_clicked)
            row_position = (class_num - 1) // num_columns
            column_position = (class_num - 1) % num_columns

            self.classcards.addWidget(class_card, row_position, column_position, 1, 1)

        scrollbar = QScrollBar(QtCore.Qt.Vertical, homepage)
        scrollbar.setGeometry(QtCore.QRect(979, 0, 21, 691))
        
        search_bar.textChanged.connect(lambda text: self.search_classes(text, num_classes))


        self.retranslateUi(homepage)
        QtCore.QMetaObject.connectSlotsByName(homepage)

    def search_classes(self, search_term,num_classes):
        for class_num in range(1, self.num_classes + 1):
            class_card = self.classcards.itemAt(class_num - 1).widget()
            class_name = f"Class {class_num}"

            if search_term.lower() in class_name.lower():
                class_card.show()
            else:
                class_card.hide()

    def class_card_clicked(self):
        print("Class card clicked!")

    def retranslateUi(self, homepage):

        _translate = QtCore.QCoreApplication.translate
        homepage.setWindowTitle(_translate("homepage", "Dialog"))
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    homepage = QtWidgets.QDialog()
    ui = Ui_homepage()
    ui.setupUi(homepage, num_classes=20)
    homepage.show()
    sys.exit(app.exec_())
    
    
 