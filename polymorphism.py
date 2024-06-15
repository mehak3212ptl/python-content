# class A:
#     def new(self,a,b):
#         return a+b
#     def new(self,x,y,z):
#         return  x+y+z     function overloading
# obj=A()
# print(obj.new(5,6))
# print(obj.new(5,6,7))


# class A:
#     def new(self,x=0,y=0,z=0):
#         return x+y+z
# obj=A()
# print(obj.new(5,6))
# print(obj.new(5,6,5))  default calling
# print(obj.new(5))


# from multipledispatch import dispatch
# class A:
#     @dispatch(int,int)
#     def add(self,x,y):
#         print(x+y)
#     @dispatch(int,int,int)
#     def add(self,x,y,z):
#         print(x+y+z)    #python overloading support nhi krta  agr support karbana h toh multipledispatch package dowload krna padhta h 


# obj=A()
# obj.add(5,6)
# obj.add(5,6,7)



#FUNCTION OVER RIDING 

class A:
    def add(self,a,b):
        print("o/p from parent class")
class B(A):
    def  add(self,x,y):
        print("o/p from child class")
obj=B()
obj.add(5,6)