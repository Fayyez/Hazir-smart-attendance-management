import face_recognition

def recognize_faces(image_path, known_faces):
    # Load the image
    image = face_recognition.load_image_file(image_path)

    # Find all the faces in the image
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)

    # Initialize an empty list to store the recognized faces
    recognized_faces = []

    # Iterate over each face encoding
    for face_encoding in face_encodings:
        # Compare the face encoding with the known faces
        matches = face_recognition.compare_faces(known_faces, face_encoding)

        # Check if there is a match
        if True in matches:
            # Find the index of the matched face
            matched_index = matches.index(True)

            # Add the recognized face to the list
            recognized_faces.append(known_faces[matched_index])

    return recognized_faces
