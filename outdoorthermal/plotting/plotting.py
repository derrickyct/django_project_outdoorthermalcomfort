# import dash_core_components as dcc
from dash import dcc
# from dash_core_components.Dropdown import Dropdown
# import dash_html_components as html
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('SimpleExample', external_stylesheets=external_stylesheets)

df = pd.read_csv('ShinyData.csv')

choices = [i for i in df.head()]

x_axis_choices = ['Air Temperature', 'Relative Humidity', 'Wind Speed', 'Globe Temperature', 'Mean Radiant Temperature',
                  'Radiation', 'PET', 'UTCI']

y_axis_choices = ['Thermal Sensation Vote', 'Thermal Comfort Vote', 'Thermal Preferance Vote',
                  'Thermal Preference Vote (3-pt scale)', 'Thermal Acceptance', 'Wind Sensation Vote',
                  'Solar Sensation Vote', 'Humidity Sensation Vote']

app.layout = html.Div([
    html.Div([  # sidebar part
        html.H4('x-axis'),
        dcc.Dropdown(
            id='xAxis',
            options=[{'label': i, 'value': i} for i in x_axis_choices],
            value=x_axis_choices[0],
            placeholder='Select x-axis'
        ),
        html.H4('y-axis'),
        dcc.Dropdown(
            id='yAxis',
            options=[{'label': i, 'value': i} for i in y_axis_choices],
            value=y_axis_choices[0],
            placeholder='Select y-axis'
        ),
        html.H4('Color'),
        dcc.Dropdown(id='color',
                     options=[{'label': i, 'value': i} for i in ['None'] + choices],
                     value='None',
                     placeholder='None'
                     ),
        dcc.RadioItems(
            id='graphMethod',
            options=[{'label': 'Jitter',
                      'label': 'Smooth',
                      'label': 'Bin',
                      'label': 'Raw'}]
        ),
        html.H4('Facet row'),
        dcc.Dropdown(id='facetRow',
                     options=[{'label': i, 'value': i} for i in ['None'] + choices],
                     value='None',
                     placeholder='Select Facet Row'
                     ),
        html.H4('Facet col'),
        dcc.Dropdown(id='facetCol',
                     options=[{'label': i, 'value': i} for i in ['None'] + choices],
                     value='None',
                     placeholder='Select Facet Col'
                     ),
    ]),
    html.Div([  # content part
        html.Br(),
        dcc.Graph(id='scatterPlot', animate=True, style={'height': 800}),
        # html.H4('Sample Size'),
        # dcc.Slider(
        #     id='sampleSize',
        #     marks={i: '{}'.format(i) for i in range(len(df))},
        #     max=len(df),
        #     value=min(22705,len(df)),
        #     step=500,
        #     updatemode='drag',
        # ),
    ])
])


@app.callback(Output('scatterPlot', 'figure'), [Input('xAxis', 'value'), Input('yAxis', 'value')])
def display_value(xAxis, yAxis):
    graph = go.Scatter(
        x=df[xAxis],
        y=df[yAxis],
        name='Manipulate Graph',
        mode='markers'
    )
    try:
        layout = go.Layout(
            paper_bgcolor='#D6EAF8',
            plot_bgcolor='#D6EAF8',
            xaxis=dict(range=[min(df[xAxis]), max(df[xAxis])]),
            yaxis=dict(range=[min(df[yAxis]), max(df[yAxis])]),
            font=dict(color='#000000'),
        )
    except:
        print('no')
    return {'data': [graph], 'layout': layout}
