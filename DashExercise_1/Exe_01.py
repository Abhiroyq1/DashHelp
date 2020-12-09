import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
import pandas as pd

app = dash.Dash()

data = pd.read_csv('../../Plotly-Dashboards-with-Dash-master/Data/OldFaithful.csv')
# print(data.head(4))

app.layout = html.Div([
                    dcc.Graph(
                        id='Scatterplot',
                        figure={'data':[
                            go.Scatter(
                                x=data['X'],
                                y=data['Y'],
                                mode='markers',
                                marker={
                                  'size':12,
                                  'color':'rgb(51,100,153)',
                                  'symbol':'circle',
                                  'line':{'width':2}
                              }
                            )
                        ],
                        'layout':go.Layout(title='Old Faithful Eruption Interval vs Durations',
                                             xaxis={'title':'Duration of eruption(Minutes)'},
                                             yaxis={'title':'Interval to next eruption(minutes)'})}
                    )
])

if __name__=='__main__':
    app.run_server(debug=True)