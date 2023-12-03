import numpy as np
import face_recognition
import cv2
def save_encodings(encodesaves, filename):
    with open(filename, 'a') as file:
        np.savetxt(file, encodesaves, delimiter=',')
picturefiles =['fayeez.jpeg', 'uffan.jpeg','danish.jpeg','eehab.jpeg']
encodesaves_list = []
for file in picturefiles:
    img = face_recognition.load_image_file(file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    faceloc = face_recognition.face_locations(img)[0]
    encodesave = face_recognition.face_encodings(img, [faceloc])[0]
    encodesaves_list.append(encodesave)
save_filename = 'all_encodings.txt'
save_encodings(encodesaves_list, save_filename)
print(picturefiles)