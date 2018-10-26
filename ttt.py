
import pymysql
import random
from random import randint
from datetime import datetime
import time

# Connect to the database.

connectionObject = pymysql.connect(host='192.168.1.6',
                             user='karthik',
                             password='Karthik123',
                             db='temp',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

print("connect successful!!")
try:
    cursorobject=connectionObject.cursor()
    sqlcmd="CREATE TABLE sensorvalues(rnd_values int, dtime  timestamp )"
    cursorobject.execute(sqlcmd)

    with connectionObject.cursor() as cursor:
        for i in range (1, 10):
            start = time.clock()
            while time.clock() - start < 1:


               j=random.randrange(1,100)

            sql = "INSERT INTO temp.sensorvalues(rnd_values,dtime) VALUES (%s,%s)"

            k=datetime.now()

            cursor.execute(sql,(j,k))
            connectionObject.commit()


finally:
    connectionObject.close()