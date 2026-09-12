class Student:
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark
    

    def cal_average(self):
        sum = 0
        for i in self.mark:
            sum += i
        return sum/len(self.mark)


name1= input("Enter the name of student: ")
range_mark = int(input("Enter the number of subjects: "));

list_1 = []
for i in range(range_mark):
    mark = int(input("Enter the marks of student: "))
    list_1.append(mark)
s1 = Student(name1,list_1)
average = s1.cal_average()
print(f"The average mark of {s1.name} is {average}")


