
import pymysql
#import mosquitto
import json
import time
import paho.mqtt.client as paho


#mosquitto broker config
broker = 'test.mosquitto.org'
broker_port = 1883
broker_topic = 'tests/locations'
#broker_clientid = 'mqttuide2mysqlScript'
#mysql config
mysql_server = '192.168.31.246'
mysql_username = 'root'
mysql_passwd = 'mypass'
mysql_db = 'spor'
#change table below.

# Open database connection
db=pymysql.connect(user='root',password='mypass',database='spor')
# prepare a cursor object using cursor() method
cursor = db.cursor()

def on_connect(mosq, obj, rc):
    print("rc: "+str(rc))
    


def on_message(mosq, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    
    q = []
    r = []
    list = []
    list = json.loads(msg.payload)
    for key,value in list.iteritems():
        print("")
        print(key,value)
        if key=='image':
            print(type(value))
            q.append(value.encode('ascii', 'ignore'))
            r.append(key.encode('ascii', 'ignore'))
        #else:
            #print('error')
        try:
            
            #Execute the SQL command
            # change locations to the table you are using
            queryText = "INSERT INTO imtable(%s) VALUES %r"
            queryArgs = (keys_to_sql, tuple(vars_to_sql))
            cursor.execute(queryText % queryArgs)
            print('Successfully Added record to mysql')
            db.commit()
            
        except:
            print("try again")#
            

    



    


def on_publish(mosq, obj, mid):
    
    print("mid: "+str(mid))

def on_subscribe(mosq, obj, mid, granted_qos):
    
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_log(mosq, obj, level, string):
    print(string)

# If you want to use a specific client id, use
#mqttc = mosquitto.Mosquitto(broker_clientid)
# but note that the client id must be unique on the broker. Leaving the client
# id parameter empty will generate a random id for you.
mqttc = paho.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# Uncomment to enable debug messages
mqttc.on_log = on_log

mqttc.connect(broker, broker_port, 60)
mqttc.subscribe(broker_topic, 0)

rc = 0
while rc == 0:
       rc = mqttc.loop()
print("rc: "+str(rc))
    


   

# disconnect from server
print ('Disconnected, done.')
db.close()
