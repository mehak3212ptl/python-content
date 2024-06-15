

                          #dictionery
#key should be unique
#new key valur pair  overwrite old key value pair 
'''d={1:"mon",2:"tue" ,1:"jan"}
print(type(d))
print (d)


d={1:"mon",2:"mon"}
print(d)'''

#acces dict
'''
d={1:"mon",2:"tue" ,3:"wed",4:"thur"}
print(d)
print(d[3])'''

#nested dict
'''
d={"months":{1:"jan",2:"feb"},"days":{1:"mon",2:"tue" ,3:"wed",4:"thur"}}
print(d["months"])#full months dict print
print(d["months"][2])'''

#element add
'''
d={"months":{1:"jan",2:"feb"}}

d[3]="march"
d[4]="april"
print(d)'''


#methods
'''
d={1:"mon",2:"tue" ,3:"wed",4:"thur"}


for i in d:
    #print(i)
    print(d[4])'''

#values

'''
d={1:"mon",2:"tue" ,3:"wed",4:"thur"}
k=d.keys()
v=d.values()

for i in v:
    print(v)'''
#items()
'''
d={1:"mon",2:"tue" ,3:"wed",4:"thur"}

k_v=d.items()
print(k_v)


for i ,j in d.items():
    print(i,j)'''


#lis in loop

'''lis=[[1,2,'a'],[3,4,'w'],[6,7,'s']]
for i,j,k in lis:
    print(j)'''


#get()
'''
d={1:"mon",2:"tue" ,3:"wed",4:"thur"}

a=d.get(4)
print(a)
b=d.get(30)
print(b)'''

#update()
'''
d={1:"mon",2:"tue" ,3:"wed",4:"thur"}

d1={5:"fri",6:"sat"}

d.update(d1)
print(d)

d.update({2:"aaaaa"})
print(d)'''

#setdefault(),pop(),pop,popitem()
#setdefault(key,vaalue)
#key is not present---> no changes
#return value
'''
d={1:"mon",2:"tue",3:"wed"}

value=d.setdefault(2,"abc")
print(d)

print("value:",value)'''
#setdefault(),pop(),popitem()

d={1:"mon",2:"tue",3:"wed"}
#d.popitem()#last key ,value remove
'''
d.pop(2)
print(d)

#print("value:",value)

week={1:"mon",2:"tue",3:"wed",6:"sat",7:"sun"}

d={4:"thus",5:"fri"}
a={}

for i in  week:#1,2,3,5,7,week[i]="mon"
    a[i]=week[i]
    if i==3:
        a.update(d)
        print(a)

d={23:"ajay",34:"vijay",-1:"sagar"}
r=sorted(d.value())
print(r)

d1{}
for i in r:
    for i,j in d.item():
        if k==j:
            d1[i]=j
            print(d1)'''


                                           # function

                           #WAP to cretae a list pf n no. and find the max. and min. in list using functions ?
 
    #multiple value return
                                          
def list_create(lis,n):
    for i in range(n):
        num=int(input("enter number:"))
        lis.append(num)
    return lis,max(lis),min(lis),"FINISH"
l=[]
limit=int(input("enter range"))

return_value=list_create(l,limit)
print(return_value)
          








        
    



















































   















