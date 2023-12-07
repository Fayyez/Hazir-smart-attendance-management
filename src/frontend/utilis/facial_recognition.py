import numpy as np
import face_recognition
import cv2
import mysql.connector
import mysql
from frontend.utilis.Mysql import *

def teacher_encodes():
    # will return an array consisting of the encodings of the teachers
    # Establish a connection to your MySQL server
    mydb = mysql.connector.connect(
        host="localhost",      # Replace with your host
        user="root",           # Replace with your username
        password="m_1234gQ",   # Replace with your password
        database="hazir"       # Replace with your database name
    )
    # Create a cursor object
    mycursor = mydb.cursor()
    # Execute a SELECT query to fetch the desired attribute from the Teacher table
    mycursor.execute("SELECT face FROM Teacher")
    # Fetch all rows from the result
    result = mycursor.fetchall()
    result = loadteacherencodes()
    
    return result
def student_encodes():
   mydb = mysql.connector.connect(
        host="localhost",      # Replace with your host
        user="root",           # Replace with your username
        password="m_1234gQ",   # Replace with your password
        database="hazir"       # Replace with your database name
    )
    # Create a cursor object
   mycursor = mydb.cursor()
    # Execute a SELECT query to fetch the desired attribute from the Teacher table
   mycursor.execute("SELECT face FROM Teacher")

    # Fetch all rows from the result
   result = mycursor.fetchall()
   result = loadstudentencodes()
   return result
def anyindex(result):
    for index in range(len(result)):
        if result[index]:
            return index
    return -1
def verify_face_teacher():
    # camera opened
    capImg = cv2.VideoCapture(0)  
    capImg.set(cv2.CAP_PROP_FPS, 120)
    count = 0
    flag = False
    while flag == False:
            ret, img = capImg.read()  # Capture a frame from the camera
            count+=1
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(img)  # Detecting the face

            if count > 40: # to ensure that the face has been tested multiple times
              break
                         
            top, right, bottom, left = face_locations[0]
            face_encodings = face_recognition.face_encodings(img, face_locations) # Encoding the detected face
            result = face_recognition.compare_faces(teacher_encodes(), face_encodings, tolerance=0.5) # comparing with the saved encoded data of teachers and captured frame data
            print(result)
            index = anyindex(result)
            cv2.imshow('result', img)
            if cv2.waitKey(1) & 0xFF == 27: # to end the show 
             break
            if index >=0:
                flag = True
                cv2.putText(img, 'Face Verified', (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                return True, index 
    capImg.release()
    cv2.destroyAllWindows()        
    cv2.putText(img, 'Face Not Verified', (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    return flag, -1 #and sentinental value indicating that teacher is not found at any index
               
     
def verify_face_students():
    # camera opened
    capImg = cv2.VideoCapture(0)  
    capImg.set(cv2.CAP_PROP_FPS, 120)

    Attendance = [] # index of students verified as they are places in the database
    while True:
            ret, img = capImg.read()  # Capture a frame from the camera
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(img)  # Detecting the face

            for face_location in face_locations:
                top, right, bottom, left = face_location
                face_encodings = face_recognition.face_encodings(img, [face_location])  # Encoding the detected face

                if len(face_encodings) > 0:
                    img_encode = face_encodings[0]  # first detected face
                    result = face_recognition.compare_faces(student_encodes(), img_encode, tolerance=0.5)  # comparing with the saved encoded data and captured frame data
                    index = anyindex(result) # return the index in the result list where true with respect to the student_encodes() array
                    if index in Attendance:
                       cv2.putText(img, 'student already Verified', (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                    else:    
                     if index >= 0:
                        cv2.putText(img, 'student Verified', (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                        Attendance.append(index)
                        break
                     else:
                        cv2.putText(img, 'student not verified', (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            cv2.imshow('result', img)
            if cv2.waitKey(1) & 0xFF == 27: # to end the show 
             break
    capImg.release()
    cv2.destroyAllWindows()
    return Attendance

if __name__ == "__main__":
 d = verify_face_students()
 print (d)
#   student_encodes()
#   print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&77')
#   teacher_encodes()    
  