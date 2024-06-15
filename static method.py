class Student:
    @staticmethod
    def greet():
        print("thanks")

    def greet1():
        print("welcome")

obj=Student
obj.greet()
obj.greet1()
Student.greet()
Student.greet1()
