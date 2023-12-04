import numpy as np
import face_recognition
import cv2
import os

def anyindex(result):
    for index in range(len(result)):
        if result[index]:
            return index
    return -1
matchedname = ['zohaib marked present', 'fayeez marked present', 'uffan marked present',
               'danish marked present', 'eehab marked present']

def load_encodings(filename):
    # yahan per root directory k path peche attack ia he, only filename enough nahi!
    filepath = os.path.join(os.path.dirname(__file__), filename)
    # numpy ki zarorat nahi, python khud hi read krleti he
    with open(filepath, 'r') as file:
        content = file.read()
        encodesaves = content.split(',')
    return encodesaves # tahan per list of strings return ho rahi he where each string is basically a float
## agey isko jese deal krna wo dekhlo

save_filename = 'all_encodings.txt'
loaded_encodesaves = load_encodings(save_filename)
print(loaded_encodesaves)

# camera opened
capImg = cv2.VideoCapture(0)  
capImg.set(cv2.CAP_PROP_FPS, 120)

while True:
    ret, img = capImg.read()  # Capture a frame from the camera
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(img)  # Detecting the face

    for face_location in face_locations:
        top, right, bottom, left = face_location
        face_encodings = face_recognition.face_encodings(img, [face_location])  # Encoding the detected face

        if len(face_encodings) > 0:
            img_encode = face_encodings[0] # first detetced face
            # comparing with the saved encoded data and captured frame data
            result = face_recognition.compare_faces(loaded_encodesaves, img_encode, tolerance=0.5) 
            match = anyindex(result)  # return the index in the result list where true ??
            
            if match>=0:
                text = matchedname[match]
                cv2.putText(img, text, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                cv2.rectangle(img, (left, top), (right, bottom), (255, 0, 0), 2)
            else:
                text = "student not found"
                cv2.putText(img, text, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                cv2.rectangle(img, (left, top), (right, bottom), (255, 0, 0), 2)

    cv2.imshow('result', img)
    if cv2.waitKey(1) & 0xFF == 27: # to end the show 
        break

capImg.release()
cv2.destroyAllWindows()
