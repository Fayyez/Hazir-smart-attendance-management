import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import cv2
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox


class PasswordDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Password Confirmation")
        self.setFixedSize(300, 100)

        self.label = QLabel("Enter Password:", self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        self.confirm_button = QPushButton("Confirm", self)
        self.confirm_button.clicked.connect(self.check_password)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.confirm_button)

    def check_password(self):
        if self.password_input.text() == "1234":
            self.accept()
        else:
            QMessageBox.warning(self, "Wrong Password", "Incorrect password. Please try again.")

    def get_password_confirmation(self):
        return self.exec_() == QDialog.Accepted


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Set main window size
        self.setGeometry(300, 300, 1000, 700)
        self.setWindowTitle("My Application")

        # Create a camera frame
        self.camera_frame = QtWidgets.QFrame(self)
        self.camera_frame.setGeometry(QtCore.QRect(30, 30, 581, 361))

        # Initialize camera capture
        self.cap = cv2.VideoCapture(0)

        # Set camera timer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_camera_frame)
        self.timer.start(1)

        # Create QLabel for displaying the camera feed
        self.camera_label = QtWidgets.QLabel(self.camera_frame)
        self.camera_label.setGeometry(QtCore.QRect(0, 0, 581, 361))

        # Create heading
        self.heading = QtWidgets.QLabel(self)
        self.heading.setText("Manual Entry")
        self.heading.setFont(QtGui.QFont("Arial", 18))
        self.heading.setGeometry(QtCore.QRect(120, 430, 311, 41))

        # Create input boxes
        self.input_box1 = QtWidgets.QLineEdit(self)
        self.input_box1.setGeometry(QtCore.QRect(120, 490, 341, 41))
        self.input_box2 = QtWidgets.QLineEdit(self)
        self.input_box2.setGeometry(QtCore.QRect(120, 560, 341, 41))

        # Create enter button
        self.enter_button = QtWidgets.QPushButton(self)
        self.enter_button.setGeometry(QtCore.QRect(490, 510, 71, 61))
        self.enter_button.setText("Enter")

        # Create close button
        self.close_button = QtWidgets.QPushButton(self)
        self.close_button.setGeometry(QtCore.QRect(910, 10, 71, 61))
        self.close_button.setText("Close")

        # Connect button clicks to functions
        self.enter_button.clicked.connect(self.enter_button_click)
        self.close_button.clicked.connect(self.close_button_click)

        # Show the main window
        self.show()

    def update_camera_frame(self):
        # Capture frame-by-frame
        ret, frame = self.cap.read()

        # Convert frame to RGB format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Resize frame to fit the camera frame size
        frame = cv2.resize(frame, (581, 361))

        # Convert frame to QImage
        image = QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], frame.strides[0], QtGui.QImage.Format_RGB888)

        # Display the frame in the camera label
        self.camera_label.setPixmap(QtGui.QPixmap.fromImage(image))

    def enter_button_click(self):
        # Check password confirmation
        password_dialog = PasswordDialog(self)
        if not password_dialog.get_password_confirmation():
            return

        # Get the input from the boxes
        input1 = self.input_box1.text()
        input2 = self.input_box2.text()

        # Placeholder for processing the input values (replace with your logic)
        if input1 and input2:
            self.process_input_values(input1, input2)
            QMessageBox.information(self, "Success", "Inputs processed successfully.")
        else:
            QMessageBox.warning(self, "Error", "Please fill in both input boxes.")

    def process_input_values(self, input1, input2):
        # Placeholder for processing input values (replace with your logic)
        print(f"Processing Input 1: {input1}")
        print(f"Processing Input 2: {input2}")

    def close_button_click(self):
        password_dialog = PasswordDialog(self)
        if not password_dialog.get_password_confirmation():
            return
        # Stop the camera timer
        self.timer.stop()

        # Release the camera capture
        self.cap.release()

        # Close the application
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
