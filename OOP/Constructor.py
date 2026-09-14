#constructor is _init_
class Student:
    name = 'bipin'
    def __init__(self):
        
        print("This is a constructor")
    @staticmethod
    def hello():
        print("Hello Welcome");

s1 = Student()
s1.hello()


