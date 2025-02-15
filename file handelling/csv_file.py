# f = open("Sample.csv",'r')
# data = f.read()[0:15]
# print(data)


import csv
with open('Sample.csv', mode ='r')as file:
#   csvFile = csv.reader(file)
    x = csv.DictReader(file)
    for i in x:
        print(i)
