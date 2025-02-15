user=input("enter younstring")
x=('a','e','i','o','u','A','E','I','O','U')
vowels=0
conso=0
space=0

for i in user:
    z=ord(i)
    if i in x:
        vowels=vowels+1
    elif z==32:
        space=space+1
    else:
        conso=conso+1
print(vowels,"vowels")
print(conso,"consonnt")
        

        
 
