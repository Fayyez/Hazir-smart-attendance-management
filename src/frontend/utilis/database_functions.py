from frontend.utilis.facial_recognition import *
import pandas as pd
import mysql.connector
# will be used in login screen
def verification(user_id, user_password, login_with_face):
    if login_with_face:
        verified,teacher_id = verify_face_teacher() # returns true if face is verified and teacher id
        # if true then teacher id
        
    else:
     mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='m_1234gQ',
        database='hazir'  # Replace 'your_database' with your actual database name
    )
    mycursor = mydb.cursor()

    username = user_id  # Replace with the username you want to check
    entered_password = user_password  # Replace with the entered password

    query = "SELECT username, password FROM Teacher WHERE username = %s"
    mycursor.execute(query, (username,))  # Need to pass parameters as a tuple

    user_data = mycursor.fetchone()
   
    print(user_data)
    if user_data:
        # If the username exists, verify the password
        db_password = user_data[1]  # Access the password from the fetched data
        if db_password == entered_password:
            print("Login successful!")
            query = "SELECT t_id FROM Teacher WHERE username = %s"
        
        # Execute the query with the provided username
            mycursor.execute(query, (username,))
        
        # Fetch the t_id
    
            teacher_id = mycursor.fetchone()
            print(teacher_id[0])
            return True, teacher_id[0] 
        else:
            print("Incorrect password")
    else:
        print("Username not found")

    mydb.close()  # Close the database connection
    return False, None # if not verified then return false and None

    
def mark_attendance(present_ids):
    class_num = 2  # Assuming class number 2 is being considered

    # Establish connection to MySQL server
    mydb = mysql.connector.connect(host='localhost', user='root', password='m_1234gQ', database='Hazir')
    mycursor = mydb.cursor()

    # Fetch student data for the specified class
    mycursor.execute(f"SELECT * FROM Student WHERE class_id={class_num}")
    student_list = mycursor.fetchall()

    marked_attendance = []
    for student in student_list:
        # Assuming 'id', 'name', 'roll_no', and 'class_id' are column indices in the fetched tuple
        if student[0] in present_ids:  # Assuming 'id' is the first column in the SELECT query result
            student_status = {
                'id': student[0],
                'name': student[1],
                'roll_no': student[2],
                'class_id': student[3],
                'status': 'Present'
            }
        else:
            student_status = {
                'id': student[0],
                'name': student[1],
                'roll_no': student[2],
                'class_id': student[3],
                'status': 'Absent'
            }
        marked_attendance.append(student_status)

        # Insert each student's attendance into the 'Attendance' table
        for v in marked_attendance:
            mycursor.execute("INSERT INTO Attendance (st_id, name, rollno, class_id, attendance) "
                             "VALUES (%s, %s, %s, %s, %s)",
                             (v['id'], v['name'], v['roll_no'], v['class_id'], v['status']))

    # Commit changes to the database
    mydb.commit()

    # Close cursor and connection
    mycursor.close()
    mydb.close()
    return marked_attendance

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

# add main function here
