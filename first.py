'''
#modules
#file name is  first.py
x=10
def sum(a,b):
    print("sum of two value",(a+b))
def multiplication(a,b):
    print("multipication of two value",(a*b))
    
import first as mod
mod.sum(10,30)
import first as p
print(10+p.x)
'''
def factorial (x):
    if x==1:
       return 1
    else:
      return(x*factorial(x-1))
num=int(input("enter your num"))
print("factorial",num,"is",factorial(num))
'''


#genrator
def my_fun(x,y):
    while x<=y:
        yield x
        x+1=1
         
var=my_fun(5,10)
for y in var:
    print(y)
    

def my_fun (x,y):
    while x<=y:
        yield x
        x=x+1
var=my_fun(5,10)
print("first object from genrator:",next(var))
print("second object from genrator:",next(var))
for y in var:
    print(y)
    '''

    

        

