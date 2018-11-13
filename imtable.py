import pymysql
from PIL import Image





dbconnection=pymysql.connect(user='root',password='mypass',database='spor')
print('connected')


cursor=dbconnection.cursor()
sql="SELECT image FROM imtable where category='plants'  "
cursor.execute(sql)
data=cursor.fetchall()
l=[]
for i in data:
    c=i[0]
    print(c)
    
    l.append(c)
    
print(l)
    
    
    

dbconnection.commit()
cursor.close()
dbconnection.close()



            
    

