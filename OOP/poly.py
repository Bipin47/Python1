class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag    
    def shownumber(self):
        print(f"{self.real}i + {self.imag}j")

    def __add__ (num1,num2):
        return complex(num1.real + num2.real, num1.imag + num2.imag)    



num1 = complex(2, 3)
num2 = complex(4, 5)
num1.shownumber()  
num2.shownumber()
num3 = num1 + num2
num3.shownumber()

