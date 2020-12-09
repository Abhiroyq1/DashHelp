# Plotly basic Line plotting
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(56)

x_values = np.linspace(0,1,100)
y_values = np.random.randn(100)

trace = go.Scatter(x=x_values,
                   y=y_values+5,
                   mode='markers',
                   name='markers')

data = [trace]

layout = go.Layout(title='Linecharts')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='Line Plot_1.html')
