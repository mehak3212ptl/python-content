                        #WAP to concatnate our name and surname ?(user defined program)
'''
name=input("enter your name :")
surname=input("enter your surname:")
print("full name is :",name,surname)'''

                       #WAP  to concatnate the name and surname by + operator?
'''
name=input("enter your name :")
surname=input("enter your surname:")
print("full name is :"+name+surname)'''

                       #WAP to add +10 i your age?
'''
age=int(input("enter your age"))
age=age+10
print(age)'''


                      #WAP  to create a list with a original list of name ?

'''
names=["ajay","mehak","sidd","om","atul"]

names2=[]

for i in names:
    if i[0]=='a':
    
       names2.append(i)
print(names2)


                   # WAP  to  remove duplicate value in below  list?


lis=[22,3,55,66,22,7,88,99,1,44,22]
lis2=[]

for i in lis:
    if i not in lis2:
        lis2.append(i)

print(lis2)'''    


 '''                      # WAP to create a conquenate the content of two list ?

names=["ajay","sourabh","sumit","atul","aman"]

address=["bhopal","pipariya","ujjain","london","sagar"]
'''

#print(list(zip(names,address)))# zip use kiya h .......
'''
list1=[]

for i in range(len(names)):
    a=[names[i],address[i]]
    list1.append(a)
    print(list1)'''

         '''                   #WAP to manipulate the strings as(OUTPUT=d$v$lopm$nt)
s="development"

e=""
for i in s:
    if i=='e':
        e=e+'$'
    else:
        e=e+i
        print(e)'''

                           #WAP to manipulate the string (OUTPUT=d$v$lopment)
s="development"

a=s.split("e",2)
print(a)'''

                            #WAP to fiind the even no. and odd no. in given list?

'''
lis=[2,3,5,7,8,4,9,10,13,16]

for num in lis:
    if (num %2==0):    
      print("no. is even",num)

else:

    print("no. is odd")
    '''

        #WAP function that takes a list and returns a new list wiyh unique elements of the  first list?
'''
l=[1,2,3,3,3,4,5]

l1=[]

for i in l:
    if i not in l1:
        l1.append(i)
        print(l1)'''
    

                       #WAP to find thr average of n numbers with the help of function add()?
'''
def add(n):
    sum=0
    for i in range(n):
    
     num=int(input("enter a number"))
     sum=sum+num
    return sum
  
n=int(input("enter a range"))
a=add(n)
avg=a/n
print(avg)'''


                 #WAP to perform the arthematic calculations?

'''def arthmetic (a,b):
    return a+b, a-b, a*b,a/b
add,sub,multi,div=arthmetic (4,8)
print(add,sub,multi,div)
           #OR
print("add:" ,add)
print("sub:",sub)
print("multi:",multi)
print("div:",div)
         #OR
a=arthmetic(4,8)
print(a[0])
print(a[1])
print(a[2])
print(a[3])'''


                                     # Assingment questions #


# WAP to concatnate the name and surname having no space between them?
'''
def nam(a,b):
    c=a+b
    print(c)

a=input("enter yur name")
b=input("enter your surname")
nam(a,b)'''

  #WAP that ask the user to input a positive number then print the multiplication table?
                        #parameter=int     no return
'''    
def table(a):
    for i in range(1,11):
        print(a*i)
        
table(2)'''


             #WAP  to find the factorial of any number entered by user ?
'''
def fact(a):
    if a==1:
        return 1
    else:
        return (a*fact(a-1))
num=int(input("enter a no."))
result=fact(num)
print(result)'''

#WAP to find the  area of square of all essential no.  input in function itself?
'''
def area(side):
    a=side*side
    return a


num=int(input("enter a nuo"))
print (area(num))'''


# WAP to calculate the HCF of given no?
'''
def hcf(a,b):
    if a>b:
        smaller=b
    else :
        smaller=a

        for i in range (1,smaller+1):
            if((a%i==0) and (b%i==0)):
                hcf=i
            return hcf

num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))
print(num1,num2,hcf(num1,num2))'''

#WAP  to print weather a number is armstrong number or not ?
'''
def armstrong(start,end):
    l=[]
    for i in range(start,end+1):
        temp=i
        sum=0
        length=len(str(temp))
        while(temp>0):
            last=temp%10
            sum=sum+(last**length)
            temp=temp//10
        if i==sum:
            print(i)
result=armstrong(200,900)
print(result)'''

#WAP to print weather a number is pallindrome or not?
'''
def pln(a):
    s=str(a)
    rev=s[::-1]
    if rev==s:
        return "yes"
    else :
        return "no"
r=pln(1221)
print(r)'''

#WAP to print the fibonaci series of n terms where n is input by user ?

'''def fib(a):
    n1=0
    n2=0
    print(n1,n2, end=" ")

    for i in range(a-2):
        n3=n1+n2
        print(n3, end=" ")

limit=(int(input("enter limit")))
fib(limit)'''

       #WAP to count the number of strings  where the string lenghth is 2 or  more and the first and second letter is same ?
'''
def match(a):
    ctr=0
    for i in a:
        if len(i)>1 and i[0]== i[-1]:          #doubt
            
           ctr+=1
        return ctr

print(match(['abc','xyz','aba','1221']))'''


# WAP to remove duplicate values ?
    
'''def remove(dupli):
    lis2=[]
    
    for i in dupli:
         
         if i not in lis2:
            lis2.append(i)
            v=sorted(lis2)
    return v
my_list=[1,2,3,7,2,1,5,6,4,8,5,4]
print(remove(my_list))'''

# WAP to print the list of words that are longer than the n of given list ?
'''def long(n,list):
        list2=[]

        for i in list:               #doubt
            if len(i) >n:
                list2.append(i)

        return list2
main_list=['abc','xyz','aba','1221']
n=3
result=long(n,main_list)
print(result)'''

#WAP to flatten a shallow list ?
'''
def list(m):
    list2=[]
    for i in m:
        for n in i:

            list2.append(n)
            print(list2)

list([[20,30,70],[30,90,10],[30,20],[70,90,10,80]])'''

#WAP print the list removing even no.?

'''def odd(list):
    for i in list:
        if i % 2!=0:
            print(i,end=" ")


odd([7,32,81,20,25,14,23,27])'''












