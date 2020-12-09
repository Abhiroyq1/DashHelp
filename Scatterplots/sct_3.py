# Plotly intermediate-Plotting scatter-plot with axis naming
# and enlarging value points
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)

random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

data = [go.Scatter(x=random_x,
                   y=random_y,
                   mode='markers',
                   marker=dict(
                       size=12,
                       color="rgb(51,204,153)",
                       symbol='pentagon',
                       line=dict(
                           width=2
                       )
                   ))]
layout = go.Layout(title="Hello Plot",
                   xaxis={'title': 'X'},
                   yaxis={'title':'Y'},
                   hovermode='closest')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="Sct_3.html")