class Teacher:
    name = ""
    username = "" # unique_key
    password = ""
    face: float = [] # face float for facial recognition

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def __repr__(self):
        return f"Teacher({self.name}, {self.username}, {self.password})"
    
    
class ClassRoom:
    title: str = ""
    studentount: int = 0
    teacher_id: str = "" # unique_key == teacher.username
    class_id: str = "" # unique_key

    def __init__(self, title, studentcount, teacher_id):
        self.title = title
        self.studentcount = studentcount
        self.teacher_id = teacher_id

    def __repr__(self):
        return f"ClassRoom({self.title}, {self.studentcount}, {self.teacher_id})"
    
class Student:
    name: str
    rollno: int # unique_key
    class_id: str # unique_key == class.class_id
    face: float = [] # face float for facial recognition

    def __init__(self, name, rollno, class_id):
        self.name = name
        self.rollno = rollno
        self.class_id = class_id

    def __repr__(self):
        return f"Student({self.name}, {self.rollno}, {self.class_id})"
