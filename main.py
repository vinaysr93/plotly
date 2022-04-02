import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd


df=pd.read_excel('export.xlsx')

xaxis=df['date']
yaxis=df['tavg']

tmin=df['tmin']
tmax=df['tmax']

print(df.head())



trace1=go.Scatter(x=xaxis,y=yaxis,mode='lines+markers',name='Avg Temperature')

trace2=go.Scatter(x=xaxis,y=tmin,mode='lines+markers',name='Minimum Temperature')

trace3=go.Scatter(x=xaxis,y=tmax,mode='lines+markers',name='Maximum Temperature')

data=[trace1,trace2,trace3]


layout=go.Layout(title='Temperature Plot for the Last 5 Years',xaxis={'title':'Year'},
                 yaxis=dict(title='Temperature'),hovermode='closest')

fig=go.Figure(data=data,layout=layout)

pyo.plot(fig,filename='scatter.html')