import plotly.plotly as py
from plotly.graph_objs import *
import pymysql
import pandas as pd
py.sign_in("karthiknair", "zQYKNr4byMCtTBVp9Yg1")

connectionobject = pymysql.connect(host='192.168.0.102',
                             user='karthik',
                             password='Karthik123',
                             db='temp',

                             )
cursor=connectionobject.cursor()
cursor.execute(' select rnd_values, dtime from sensorvalues')
rows=cursor.fetchall()
df = pd.DataFrame( [[ij for ij in i] for i in rows] )
df.rename(columns={0: 'rnd_values', 1: 'dtime'}, inplace=True);

trace1 = Scatter(
     x=df['dtime'],
     y=df['rnd_values'],

     mode='markers'
)
layout = Layout(
     xaxis=XAxis(title='Time' ),
     yaxis=YAxis(type='log', title='Sensorvalues' )
)
data = Data([trace1])
fig = Figure(data=data, layout=layout)
py.plot(fig, filename='Sensor values')