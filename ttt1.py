import pymysql
from tkinter import *
import pandas as pd
import plotly.plotly as py
from plotly.graph_objs import *


tk = Tk()
tk.configure(background="light green")
tk.geometry("265x125")


connectionObject = pymysql.connect(host='192.168.1.5',
                             user='karthik',
                             password='karthik123',
                             db='temps',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

sql = "select * from sensorvalues"

try:
    cursorobject=connectionObject.cursor()
    cursorobject.execute(sql)
    rows = cursorobject.fetchall()

    df = pd.DataFrame([[ij for ij in i] for i in rows])
    df.rename(columns={0: 'rnd_values', 1: 'dtime'}, inplace=True);
    df = df.sort(['rnd_values'], ascending=[1]);
    df.head()








    trace1 = Scatter(
    x=df['rnd_values'],
    y=df['dtime'],
    text=sensor_values,
    mode='markers'
 )
    layout = Layout(
    title='Random Sensor values',
    xaxis=XAxis(type='log', title='Time' ),
    yaxis=YAxis(title='Sensor values' ),
)
    data = Data([trace1])
    fig = Figure(data=data, layout=layout)
    py.iplot(fig, filename='Random sensorvalues')

finally:
    # Close connection.
    connectionObject.close()

