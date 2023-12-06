import sys
import dlib
import face_recognition
from PyQt5 import QtWidgets, QtCore, QtGui
import cv2
import numpy as np

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

        # Load known face encodings
        self.known_encodings = self.load_known_encodings()

        # Show the main window
        self.show()

    def update_camera_frame(self):
        # Capture frame-by-frame
        ret, frame = self.cap.read()

        # Convert frame to RGB format
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Resize frame to fit the camera frame size
        rgb_frame = cv2.resize(rgb_frame, (581, 361))

        # Find face locations and encodings
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        # Compare faces to known encodings
        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(self.known_encodings, face_encoding)
            if any(matches):
                # Face recognized
                print("Marked Present")
                # You can add your logic here to display the name or perform other actions
                # Example: self.display_name(input_name)
                break

        # Convert frame to QImage
        image = QtGui.QImage(rgb_frame.data, rgb_frame.shape[1], rgb_frame.shape[0], rgb_frame.strides[0], QtGui.QImage.Format_RGB888)

        # Display the frame in the camera label
        self.camera_label.setPixmap(QtGui.QPixmap.fromImage(image))

    def load_known_encodings(self):
        # Load known encodings from file
        known_encodings = []
        with open("all_encodings.txt", "r") as f:
            encodings = f.readlines()
            known_encodings = [np.array([float(x) for x in encoding.split(",")[:-1]]) for encoding in encodings]
        return known_encodings

    def enter_button_click(self):
        # Get the input from the boxes
        input1 = self.input_box1.text()
        input2 = self.input_box2.text()

        # Perform some action based on the input
        print(f"Input 1: {input1}")
        print(f"Input 2: {input2}")

    def close_button_click(self):
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
