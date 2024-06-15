
#SINGLE LEVEL INHERITANCE#
# class A:
#     name="mehak"
#     def m1(self):
#         return "this is m1 method"
    
# class B(A):
#     def m2(self):
#         print("name",A.name)
#         print(self.m1())

# obj=B()
# obj.m2()

#MULTI LEVEL  INHERITANCE 

# class A:
#     name="mehak"
#     def m1(self):
#         return "this is m1 method"
    
# class B(A):
#     age=32
#     def m2(self):
#         print("name",A.name)
#         print(self.m1())

# class C(B):
#     def m3(self):
#         print(B.age)
#         self.m2()
# obj=C()
# obj.m3()

#MRO CONCEPT

# class Parent1():
#     def m1(self):
#         print("parent1 method ")

# class Parent2:
#     def m1(self):
#         print("parent2 ")

# class Child(Parent2,Parent1):   # MRO method resolution method 
#                                 # called left to right and  depth first 
#     def m2(self):
#         self.m1()

# obj=Child()
# obj.m2()


#MULTIPLE INHERITANCE 

# class Parent1():
#     def m1(self):
#         print("parent1 method ")


# class Parent2:
#     def m2(self):
#         print("parent2 ")

# class Child(Parent2,Parent1):   # MRO method resolution method 
#                                 # called left to right and  depth first 
#     def m3(self):
#         self.m1()
#         self.m2()
#         print("childs")

# obj=Child()
# obj.m3()


# SUPER METHOD USE ///// METHOD OVERRIDE 
class A:
    def m1(self):
        print("m1")

class B(A) :
    def m1(self):
        print("m1 b")
        super().m1() 

obj=B()
obj.m1()
       



