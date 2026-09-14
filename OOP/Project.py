class Student:
    def __init__(self,Name,RollNo,Marks,Section):
        self.Name = Name
        self.RollNo = RollNo
        self.Marks = Marks
        self.Section = Section

    
    def display(self):
        print("Student Name is :", self.Name)
        print("Student Roll Number is :", self.RollNo)
        print("Student Marks is :", self.Marks)
        print("Student Section is :", self.Section)

    def search(self,RollNo):
        if self.RollNo == RollNo:
            print("Find name is" +Name)
        else:
            print("No match")




studentonj = []

def add_student(studentonj, Name, RollNo,Marks,Section):
    student = Student(Name, RollNo, Marks, Section) #here student act as a object of class so i can use it to access any thing in class
    studentonj.append(student)


number_of_students = int(input("Enter the number of students you want to add: "))

for i in range(number_of_students):
    Name = input("Enter the name of student: ")
    RollNo = input("Enter the roll number of student: ")
    Marks = float(input("Enter the marks of student: "))
    Section = input("Enter the section of student: ")
    add_student(studentonj, Name, RollNo, Marks, Section) #to enter details



searchh = int(input("Enter the roll number of the student you want to search"))
last_index = len(studentonj) - 1



    








    