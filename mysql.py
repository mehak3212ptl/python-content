import pymysql
import pandas as pd

connection= pymysql.connect(
    host='localhost',
    user='root',
    password='mehak@2003',
    database='dummy'
)
with connection.cursor() as cursor:
    cursor.execute("select * from customers")
    columns=[col[0] for col in cursor.description]
    data=cursor.fetchall()

df=pd.DataFrame(data,columns=columns)
print(df) #

# df.head(10)   
# df.tail() #move gthe cursor 
# df.info()  #gave the information 
# df.describe()   # describe the whole  data
df.to_csv("output.csv",index=False)  # gave the path   and create the csv file in excel format
connection.close()