#upper(),--change lower case letter into uppercase  letter (if any)
#ex. Bhopal-->BHOPAL

# Lower case ()--> change upper  case letter into lowercase  letter (if any)
#ex. Bhopal-->bhopal
'''
a="Bhopal"
print(a.lower())#bhopal
'''
# Strip()
#unnecesaary space hata deta h

#print(ch.strip())

'''

print("enter among the folowing options")
print("bhopal,jaipur,mumbai,pipariya")

ch=input("enter your choice :")
ch=ch.strip()# unnecessary space remove 

if ch.lower()=="bhopal":
    print("tajul masjid")
elif ch.lower()=="jaipur":
    print("hawamahal")

elif ch.lower()=="pipariya":
    print("mehak")

else:
    print("invalid choice")

   '''
'''
   #QUESTION------  WAP to determine whether the character isvowel/consant/number/special charatcter....


  
ch=input("enter any character")
if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
    print("vowel")
else:
    print("consonant")
    '''

    # or
'''
ch=input("enter any character")
v="AEIOUaeiou"

if ch in v:
    print("vowel")
elif ch>='A' and ch<='Z':
    print("uppercase consonant")

elif ch>='a' and ch<='z':
    print("lowercase")

elif ch>='0' and ch<='9':
    print("digits")

else:
    print("special character")

                                    #loops 

#for--->iteration depended loop
#while--->condition depended loop

 #for
   # 1 range()
    #2iteration(list, tuple, string, dict)

#range(a,b,c)
    #a---->starting point
    #b---->ending point(excluded)
    #c----->jump(updation)
                       #loop by 1 parameter
for i in range(5):
    print("welcome")
    print("to")
    print("bhopal")

print("out of loop")

                      #  loop by  2  parameter
for i in range(25,15):
print("welcome",i)

                             #increment loop by 3 parameters
range(start,end,jump)
by default----->start ------->start
end----->end  


for i in range(15,25,3):
    print("welcome",i)

                          #decrement loop by 3 parameters
for i in range(25,15,-1):
    print("welcome",i)


             #iterable

             #sting
             
s="mehak"
for i in s:
    print("welcome",i)



# list


li=[1,2,3,4,5,6]
for i in li:
    print(i)


sum=0
n=int(input("enter limit"))
for i in range(n):
    num=int(input("enter  a no"))
    sum=sum+num


print("submit:",sum)

                        # fibanocci series


limit= int(input("enter a limit:"))
n1=0
n2=1
print(n1,n2,end=" ")
for i in range(limit-2):
    n3=n1+n2
    print(n3,end=" ")
    n1=n2
    n2=n3



#pass statement

a=90
if a>10:
    pass

for i in range(10):
    pass
print("welcome")
def f1():
    pass
    


#break sttatement

for i in range(10):
    print(i)
    if i==5:
        break


for i in "python":
    print(i)
    if i=="o":
        break



lis=[2,33,4,"apple",5,434,-90,"banana",88,900]

a=lis[:4]
b=lis[7:]
c=a+b
print(c)

lis[3]="python"
print(lis)

#function()
#append(),extend(),index()
a=lis.append("end of list")
print(lis)
print(a)

lis.extend([2,3,4])
#lis.append([2,3,4])
print(lis)'''

n=int(input("enter range"))
lis=[]
#lis=list()
while n>0:
    num=int(input("enter range:"))
    if num%2==0:
        lis.append(num)
        n=n-1

print(lis)        
























