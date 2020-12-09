import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import base64


df = pd.read_csv('../../Plotly-Dashboards-with-Dash-master/Data/wheels.csv')
# print(df)
app = dash.Dash()

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

wheel_options = []
color_options = []

# for wheel in df['wheel'].unique():
#     wheel_options.append({'label':str(wheel), 'value':wheel})
#
# for color in df['color'].unique():
#     color_options.append({'label':str(color), 'value':color})

app.layout = html.Div([
                dcc.RadioItems(id='wheels',
                    options=[{
                        'label':str(i),
                        'value':i
                    } for i in df['wheels'].unique()],
                    value=1
                ),
                html.Div(id='wheels-output'),
                html.Hr(),
                dcc.RadioItems(id='colors',
                               options=[{
                                   'label':i,
                                   'value':i
                               } for i in df['color'].unique()],
                               value='blue'),
                html.Div(id='colors-output'),
                html.Img(id='display-image', src='children', height=300)
], style={
    'fontFamily':'helvetica',
    'fontSize':18
})


@app.callback(Output(component_id='wheels-output', component_property='children'),
              [Input(component_id='wheels', component_property='value')])
def callback_a(wheel_value):
    return f"You chose {wheel_value}"

@app.callback(Output(component_id='colors-output', component_property='children'),
              [Input(component_id='colors', component_property='value')])
def callback_b(color_value):
    return f"You chose {color_value}"

@app.callback(Output('display-image', 'src'),
              [Input('wheels','value'),
               Input('colors', 'value')])
def callback_image(wheel, color):
    path = r"../../Plotly-Dashboards-with-Dash-master/Data/Images/"
    return encode_image(path+df[(df['wheels']==wheel) & (df['color']==color)]['image'].values[0])

if __name__ == '__main__':
    app.run_server(debug=True)