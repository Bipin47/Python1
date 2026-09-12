class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Name is "+ str(self.name) + " & Age is " + str(self.age))


name1 = input("Enter name: ")
age1 = int(input("Enter age: "))
s1 = Student(name1, age1)
