# OBJECT ORIENTED #

                 #class

#WAP to create a class named Employee having attribute- name ,eid
#working_days , salary, department behaviour- salary(),promotion()
#display()
'''

class employee:
    def __init__(self):
        self.name=input("enter name ")
        self.eid=int(input("enter eid"))
        self.salary=int(input("enter salary"))
        self.working_days=int(input("enter working days "))

    def display(self):
           print(self.name)
           print(self.eid)
           print(self.salary)
           print(self.working_days)

e1=employee()
e1.display()
'''

#WAP class name circle constructed  by a radius and the two methods
#which will compute the area and the perimeter of a cirle?


class circle:
    def __init__(self,r):
        self.radius=r
    def area (self):
        print("area:",3.14*self.radius*self.radius)
    def perimeter (self):
        print("perimeter:",2*3.14*self.radius)

c1=circle(45)
c1.area()
c1.perimeter()

#WAP  swapping by class?
'''

class swap:
    def __init__(self,a,b):
        self.n1=a
        self.n2=b
    def Swap(self):
        self.n1,self.n2=self.n2,self.n1
    def display(self):
        print("n1",self.n1)
        print("n2",self.n2)



s=swap(34,1)
s.Swap()
s.display()


#WAP to create a class  Book .
#data member: int Bid,Quantity;
#member function: parameterized_constructor(),void Purchase() 
#,void Sale(), void currentstock().
# first user intitailized data members with input values.
# purchase can add books quantity
# sale can decremented books quantity.
'''
'''
class Book:
    def __init__(self,n,bid,q):
        self.name=n
        self.bid=bid
        self.quantity=q
    def purchase(self,n):
        self.quantity+=n
    def sales(self,n):
        self.quantity-=n
    def display (self):
        print(self.name,self.bid,self.quantity)
        
c1=Book("mehak",900,20)
c1.purchase(30)
c1.display()
'''

        
#VARIABLES

class Academy:
    inistitute_name="cybrom"
    def __init__(self):
        self.name=input("enter your name")
        self.course=input("enter your course")
    def display(self):
        self.random=900
        print()


Academy.inistitute_name="cy"
e=Academy()
e.inistitute_name="cyb"
e.display()







