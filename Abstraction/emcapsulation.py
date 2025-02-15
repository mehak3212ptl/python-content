class Student:
    school="SHSS"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def deatils(self):
        print("Name",self.__name)
        print("age",self.__age)
        print("school",Student.school)
class Marks(Student):
    def marks(self,hindi,math):
        self.hindi=hindi
        self.math=math
    def complete_details(self):
        print("name",self.__name)
        print("age",self.__age)
        print("school",Student.school)
        print("hindi",self.__hindi)
        print("hindi",self.__math)

obj=Marks("neeraj",37)



