class car:
    @staticmethod
    def start():
        print("Car is starting")

    def __init__(self,type):
        print("Car type is(Parent class): " + type)


class car2:
    @staticmethod
    def stop():
        print("Car has stoped")

class car3(car,car2):
    print("Hello")

    
    def printt(self,name):
            print("Car name is(Child class): " + name)
    def __init__(self,type):
        
        super().__init__(type)

   
        



x = car3( "Electric");
x.printt("Tesla")
x.start()
x.stop()




    