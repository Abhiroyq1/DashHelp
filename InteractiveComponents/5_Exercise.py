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
        value=[-1, 1],
        marks={
            i: str(i) for i in range(-10,11)
        }
    ),
    html.H1(id='Product')
])

@app.callback(Output(component_id='Product', component_property='children'),
             [Input(component_id='my-range-slider', component_property='value')])
def update_output_div(input_value):
    return str(int(input_value[0])*int(input_value[1]))

if __name__=='__main__':
    app.run_server(debug=True)

