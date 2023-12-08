import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import cv2
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import face_recognition

def student_encodes():
   return [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]

def anyindex(result) -> int :
    return 5


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
    cap = None
    timer = None
    heading = None

    def __init__(self):
        super().__init__()
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

    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = MainWindow()
    Attendance = [] # index of students verified as they are places in the database
    # ui.setupUi(window)
    ui.show()
    while True:
        ret, img = ui.cap.read()  # Capture a frame from the camera
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(img)  # Detecting the face

        for face_location in face_locations:
            top, right, bottom, left = face_location
            face_encodings = face_recognition.face_encodings(img, [face_location])  # Encoding the detected face

            if len(face_encodings) > 0:
                img_encode = face_encodings[0]  # first detected face
                # result = face_recognition.compare_faces(student_encodes(), img_encode, tolerance=0.5)  # comparing with the saved encoded data and captured frame data
                # index = anyindex(result) # return the index in the result list where true with respect to the student_encodes() array
                if 1 in Attendance:
                   print("student already Verified")
                else:    
                    print("student Verified")
                    
        # cv2.imshow('result', img)
        if cv2.waitKey(1) & 0xFF == 27: # to end the show 
            break

    ui.cap.release()
    cv2.destroyAllWindows()

    sys.exit(app.exec_())#

