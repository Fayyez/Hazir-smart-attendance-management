import numpy as np
import face_recognition
import cv2

def teacher_encodes():
    # will return an array consisting of the encodings of the teachers    
    pass

def student_encodes():
    # will return an array consisting of the encodings of the students
   # print(encodesaves)
    encodesaves = np.loadtxt('all_encoding.txt', delimiter=',')
    return encodesaves
    pass
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
            result = face_recognition.compare_faces(student_encodes(), face_encodings, tolerance=0.5) # comparing with the saved encoded data of teachers and captured frame data
            print(result)
            index = anyindex(result)
            cv2.imshow('result', img)
            if cv2.waitKey(1) & 0xFF == 27: # to end the show 
             break
            if index >=0:
                flag = True
                cv2.putText(img, 'Face Verified', (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                 # flag and return the teacher id present at that index in the database
                 #    
    capImg.release()
    cv2.destroyAllWindows()        
    cv2.putText(img, 'Face Not Verified', (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    return flag #and sentinental value indicating that teacher is not found at any index
               
     
def verify_face_students():
    # camera opened
    capImg = cv2.VideoCapture(0)  
    capImg.set(cv2.CAP_PROP_FPS, 120)

    students_verified = [] # index of students verified as they are places in the database
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
                    if index in students_verified:
                       cv2.putText(img, 'student already Verified', (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                    else:    
                     if index >= 0:
                        cv2.putText(img, 'student Verified', (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                        students_verified.append(index)
                        break
                     else:
                        cv2.putText(img, 'student not verified', (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            cv2.imshow('result', img)
            if cv2.waitKey(1) & 0xFF == 27: # to end the show 
             break
    capImg.release()
    cv2.destroyAllWindows()
    return students_verified

