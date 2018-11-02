import pymysql
from PIL import Image
import base64
import os
#import cStringIO

dbconnection=pymysql.connect(user='root',password='mypass',database='spor')
print('connected')
try:
    cursor=dbconnection.cursor()
    

    path='.'
    exts = ["jpg", "bmp", "png", "gif", "jpeg"]
    
    images = [fn for fn in os.listdir(path) if any(fn.endswith(ext) for ext in exts)]
    for i in images:
        with open(i, 'rb')as f:
            photo=f.read()
            encodestring=base64.b64encode(photo)
            sql="INSERT INTO spor.slider(images) VALUES(%s)"
         
            cursor.execute(sql,(encodestring))
    dbconnection.commit()
        
    
    
   

finally:
    dbconnection.close()