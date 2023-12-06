import facial_recognition
import pandas as pd
# will be used in login screen
def verification(user_id, user_password, login_with_face):
    if login_with_face:
        verified,teacher_id = facial_recognition.verify_face_teacher() # returns true if face is verified and teacher id
        
        # if true then teacher id
        
    else:
        # user_id and user_password will be verified
        # if true then return teacher id
        pass
    return False, None # if not verified then return false and None
def mark_attendance(Verified_students):
 # mark the attendance of the verified students in the database
 pass
def generate_report(student_data, file_name):
    # we will have to get the student data from the database in the form of a list of list as shown below
    # students = [
    #     ['Alice', 101, 'Present'],
    #     ['Bob', 102, 'Absent'],
    #     ['Charlie', 103, 'Present'],
    #     ['David', 104, 'Present'],
    #     ['Eve', 105, 'Absent'],
    #     ['Frank', 106, 'Present'],
    #     ['George', 107, 'Present'],
    #     ['Harry', 108, 'Present'],
    #     ['Ivan', 109, 'Absent'],
    #     ['Julia', 110, 'Present']
    # ]
    # Create a DataFrame from the student data
    df = pd.DataFrame(student_data, columns=['Name', 'Roll No', 'Attendance'])

    # Save the DataFrame to an Excel file
    excel_file_path = f'{file_name}.xlsx'  # File name for the Excel file
    df.to_excel(excel_file_path, index=False)
    
    print(f"Excel file '{excel_file_path}' has been generated successfully.")
    # how to display this in screen need to be implemnted
def get_classrooms(teacher_id):
    # get the classrooms from the database with respect to teacher id
    # will be returning a list of classrooms
    # this same function will also be required by the dashboard screen so that 
    # it can display the classroom cards
    pass
def get_students(classroom_id):
    # get the students from the database with respect to classroom id
    # will be returning a list of students
    # this same function will also be required by the room info page to add the total count of students
    pass