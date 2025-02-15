#end parameters

'''
name=input("enter your name")
surname=input("enter your srname")
print(name,end=" ")
print(surname)
#____________________________________________________________________
print("i love u jaanu",end=" ")
print("he also loves me ",end=" ")
print("sidd is always mine ")'''

#increments 
'''age=int(input("enter age"))
print(str(age))'''
#________________________________________________________________________
#swaping
'''a=45
b=89
a,b=b,a
print("value of a =:",a)
print("value of b =:",b#
#____________________________________________________________________
a=(input("enter yur name"))
b=(input("enyer your surnme"))
a,b=b,a
print("name:",a)
print("surname :",b)'''

'''c=input("enter you love")
d=input("enter his  name ")
c,d=d,c
print ("love:",c,"name:",d)'''

#_____________________________________________________________________________

#if else statement
                             #voting program
'''age=int(input("enter you age"))

if age>=18:
    print("yes you are eligible")
else:
    print("not")'''
#___________________________________________________________________________
                            #even odd program 
num=int(input("enter a no."))
if num%2==0:
        print("no. is even")
    
else:
        print("odd no.")
#__________________________________________________________________________
                        # divisibility of 7
'''
num=int(input("enter a no "))

if num%7==0:
    print("no is in table")
else:
    print("not ")'''
#_________________________________________________________________________

                            #hello bye 
'''num=int(input("enter a no "))

if num%5==0:
    print("hello")
else:
    print("bye")'''



'''num=int(input("enter a no "))#doubt
print("last ",num%10)'''

#______________________________________________________________________________

                              #marks 
'''num=int(input("enter percentage"))
if num>90:
    print("A")
if num>80 and num<=90:
    print("B")
if num>=60 and num<=80:
    print("C")
if num<60:
    print("D")'''
#_______________________________________________________________________

                                     #weeks 
''''num=int(input("enter no."))
if num==1:
    print("sunday")
elif num==2:
    print("mon")
elif num==3:
    print("tuue")
elif num==4:
    print("weddd")
elif num==5:
    print("thurrr")
elif num==6:
    print("friii")
elif num==7:
    print("satttt")

else :
    print("no. should between the 0 to 7")'''
#________________________________________________________________________

                               #city
'''s=input("enter city")
if s=='delhi':
    print("redfort")
elif s=='agra':
    print("tajmahal")
elif s=='jaipur':
    print("hawamahal")

else :
    print("ente rvalid city")'''


#_____________________________________________________________________

                           #check 3 digit no.
'''n=3
num=int(input("enter a noo."))
if num==n:
    print("three digit no.")
else:
    print("enter three digit no.")'''
#______________________________________________________________________

                          #senior citizen
'''num=int(input("enter a noo."))

if num>=70:
    print("senior")
else :
    print("not")'''

#_______________________________________________________________________

                               #lower no................
'''num=int(input("enter a  1st noo."))
num1=int(input("enter a 2nd noo."))
if num>num1:
    print("lowestno..",num1)
else:
    print("lower ",num)'''
#___________________________________________________________________________

                             #positive and negative 
'''
num=int(input("enter a noo."))
if num<0:
    print("no is negative")
else :
    print("no. is poitive")'''
#_____________________________________________________________________________

                            #divisible by both 2 3
'''
num=int(input("enter a noo."))
if num%2==0 and num%3==0:
    print("no is divisible by both")
else:
    print("not")'''

#________________________________________________________________________

                              #largest in 3 no.
'''
num1=int(input("enter first noo."))
num2=int(input("enter second noo."))
num3=int(input("enter third  noo."))
if num1>num2 and num1>num3:
    print ("greater",num1)
    
if num2>num1 and num2>num3:
     print ("greater",num2)
     
if  num3>num1 and num3>num2 :
     print ("greater",num3)'''

#__________________________________________________________________

'''                        #youngest age 
age1=int(input("enter first noo."))
age2=int(input("enter second noo."))
age3=int(input("enter third  noo."))
age4=int(input("enter fourth noo."))

if age1<age2 and age1<age3 and age1<age4:
    print("smallest", age1)
if age2<age1 and age2<age3 and age2<age4:
    print("smallest", age2)
if age3<age2 and age3<age1 and age3<age4:
    print("smallest", age3)
if age4<age2 and age4<age3 and age4<age1:
    print("smallest", age4)'''

#____________________________________________________________________

                                 #greatest no.
'''
age1=int(input("enter first noo."))
age2=int(input("enter second noo."))
age3=int(input("enter third  noo."))
age4=int(input("enter fourth noo."))

if age1>age2 and age1>age3 and age1>age4:
    print("greatest", age1)
if age2>age1 and age2>age3 and age2>age4:
    print("greatest", age2)
if age3>age2 and age3>age1 and age3>age4:
    print("greatest", age3)
if age4>age2 and age4>age3 and age4>age1:
    print("greatest", age4)'''


#____________________________________________________________________________

                           #vowel consonant
'''
s=input("enter a no")
v="aeiouAEIOU"
if s in v:
    print("it is a vowel")
else :
    print(" consonant")'''

#_______________________________________________________________________

                             #operator program
'''
num1=int(input("enter first noo."))
num2=int(input("enter second noo."))
s=input("enter a operator ")

if s=='+':
    print(num1+num2,"sum")
elif s=='-':
    print(num1-num2,"sub")
elif s=='*':
    print(num1*num2,"multi")
elif s=='/':
    print(num1/num2,"div")
else:
    print("enter valid operator")'''


#__________________________________LOOPS____________________________________


                           #natural no.
'''
n=1
while n<11:
    print(n)
    n=n+1
n=6
for i in range(1,n):
    print(i)
    n=n+1

unit=int(input("enter"))
c=unit*5
print("total",c)
d=c*10/100
print(d)

maths=int(input("enter your maths marks  "))
sci=int(input("enter your sci marks  "))
sst=int(input("enter your sst marks  "))
hindi=int(input("enter your hindi marks  "))
gk=int(input("enter your gk marks  "))

c=maths+sci+sst+hindi+gk
print("tptal",c)
d=c/500*100
print(d)

a=int(input("enter 1 no."))
b=int(input("enter 2 no."))
a,b=b,a
print("a=",a)
print("b=",b)

t=("apple","bananan","orange")
a=list(t)
a.append("mango")
b=tuple(a)
print(b)
s=[]
lis=[1,2,3]
lis[0],lis[2]=lis[2],lis[0]
s.append(lis)
print(s)

s=[]
lis=[1,2,3,4,5]
lis[1],lis[4]=lis[4],lis[1]
s.append(lis)
print(s)

lis=[10,20,30,40]
print(len(lis))

lis=[1,6,3,5,3,4]
if 8 in lis:
    print("true")

else:
    print("not exists ")

lis=[2,3,5,6,7]
print(lis,"before")
lis.clear()
print(lis)


lis=[4,5,6,7,8,9]
new=lis[::-1]
print(new)

lis=["rose","sun","lily","sunflower"]
del(lis[1])
print(lis)
s=[]
lis=[12,15,3,10]

for i in lis:
    if i%5==0:
       # print("new ",list(i'''

s="Geeks123for123Geeks"
m=s.split()
print(m)

<h1> my name is mehak patel</h1>





    
  
    

    
    

 














 




