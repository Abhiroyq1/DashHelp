import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import base64

app = dash.Dash()

app.layout = html.Div([
    dcc.RangeSlider(
        id='my-range-slider',
        min=-5,
        max=6,
        step=1,
        value=[-2, 3],
        marks=[{
            str(i): i
        } for i in range(-5,7)]
    ),
    html.Div(id='output-container-range-slider', style={'fontSize':10})
])

if __name__=='__main__':
    app.run_server(debug=True)

