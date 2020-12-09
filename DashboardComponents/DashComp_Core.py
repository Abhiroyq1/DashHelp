import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

app = dash.Dash()

app.layout = html.Div([
                        html.Label('DropDown'),
                        dcc.Dropdown(
                            options=[{
                                'label': 'New York City',
                                'value': 'NYC'
                            },{
                                'label':'San Fransisco',
                                'value':'SF'
                            }],
                            value='SF'
                        ),
                        html.Label('Slider'),
                        dcc.Slider(min=-10,
                                   max=10,
                                   step=0.5,
                                   value=0,
                                   marks={i: str(i) for i in range(-10,10)}),
                        html.Label('Some Radio items'),
                        dcc.RadioItems(options=[{
                                'label': 'New York City',
                                'value': 'NYC'
                            },{
                                'label':'San Fransisco',
                                'value':'SF'
                        }],
                        value='SF')
])

if __name__=='__main__':
    app.run_server(debug=True)