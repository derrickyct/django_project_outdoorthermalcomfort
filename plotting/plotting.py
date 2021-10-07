# import dash_core_components as dcc
from dash import dcc
# from dash_core_components.Dropdown import Dropdown
# import dash_html_components as html
from dash import html
from dash.dependencies import Input, Output
# import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
import pandas as pd
import plotly.express as px
# import dash_table

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('SimpleExample', external_stylesheets=external_stylesheets)

df = pd.read_csv('ShinyData_updated_v2.csv')

choices = [i for i in df.head()]

x_axis_choices = ['Air Temperature', 'Relative Humidity', 'Wind Speed', 'Globe Temperature', 'Mean Radiant Temeprature',
                  'Radiation', 'PET', 'UTCI']

y_axis_choices = ['Thermal Sensation Vote (7-pt)', 'Thermal Sensation Vote (9-pt)', 'Thermal Comfort Vote',
                  'Thermal Preferance Vote (7-pt)', 'Thermal Preference (3-pt scale)', 'Thermal Acceptance',
                  'Wind Sensation Vote', 'Solar Sensation Vote', 'Humidity Sensation Vote']


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
            options=[
                {'label': 'Jitter', 'value': 'jitter'},
                {'label': 'Smooth', 'value': 'smooth'},
                {'label': 'Bin', 'value': 'bin'},
                {'label': 'Raw', 'value': 'raw'}
            ],
            value='raw'
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
        # dcc.Graph(figure=fig),
    ])
])


@app.callback(Output('scatterPlot', 'figure'), [Input('xAxis', 'value'), Input('yAxis', 'value'),
                                                Input('color', 'value'), Input('graphMethod', 'value'),
                                                Input('facetCol', 'value'), Input('facetRow', 'value')])
def display_scatter(xAxis, yAxis, color, graphMethod, facetCol, facetRow):
    if graphMethod == 'raw':
        print('this is raw plot', graphMethod)
        if facetCol != 'None' and facetRow != 'None' and color != 'None':
            print(facetCol, facetRow, color)
            fig = px.scatter(df, x=xAxis, y=yAxis, color=color, facet_col=facetCol, facet_row=facetRow)
        elif facetCol != 'None' and facetRow != 'None' and color == 'None':
            print(facetCol, facetRow, color)
            fig = px.scatter(df, x=xAxis, y=yAxis, facet_col=facetCol, facet_row=facetRow)
        elif facetCol != 'None' and facetRow == 'None' and color != 'None':
            print(facetCol, facetRow, color)
            fig = px.scatter(df, x=xAxis, y=yAxis, color=color, facet_col=facetCol)
        elif facetCol != 'None' and facetRow == 'None' and color == 'None':
            print(facetCol, facetRow, color)
            fig = px.scatter(df, x=xAxis, y=yAxis, facet_col=facetCol)
        elif facetCol == 'None' and facetRow != 'None' and color != 'None':
            print(facetCol, facetRow, color)
            fig = px.scatter(df, x=xAxis, y=yAxis, color=color, facet_row=facetRow)
        elif facetCol == 'None' and facetRow != 'None' and color == 'None':
            print(facetCol, facetRow, color)
            fig = px.scatter(df, x=xAxis, y=yAxis, facet_row=facetRow)
        elif facetCol == 'None' and facetRow == 'None' and color != 'None':
            print(facetCol, facetRow, color)
            fig = px.scatter(df, x=xAxis, y=yAxis, color=color)
        else:
            print(facetCol, facetRow, color)
            fig = px.scatter(df, x=xAxis, y=yAxis)
        return fig
    elif graphMethod == 'bin':
        print('this is bin plot', graphMethod)


    elif graphMethod == 'smooth':
        print('this is smooth plot', graphMethod)
        if facetCol != 'None' and facetRow != 'None' and color != 'None':
            print(facetCol, facetRow, color)
            fig = px.scatter(df, x=xAxis, y=yAxis, color=color, facet_col=facetCol, facet_row=facetRow, trendline="ols")
        elif facetCol != 'None' and facetRow != 'None' and color == 'None':
            print(facetCol, facetRow, color)
            fig = px.scatter(df, x=xAxis, y=yAxis, facet_col=facetCol, facet_row=facetRow, trendline="ols")
        elif facetCol != 'None' and facetRow == 'None' and color != 'None':
            print(facetCol, facetRow, color)
            fig = px.scatter(df, x=xAxis, y=yAxis, color=color, facet_col=facetCol, trendline="ols")
        elif facetCol != 'None' and facetRow == 'None' and color == 'None':
            print(facetCol, facetRow, color)
            fig = px.scatter(df, x=xAxis, y=yAxis, facet_col=facetCol, trendline="ols")
        elif facetCol == 'None' and facetRow != 'None' and color != 'None':
            print(facetCol, facetRow, color)
            fig = px.scatter(df, x=xAxis, y=yAxis, color=color, facet_row=facetRow, trendline="ols")
        elif facetCol == 'None' and facetRow != 'None' and color == 'None':
            print(facetCol, facetRow, color)
            fig = px.scatter(df, x=xAxis, y=yAxis, facet_row=facetRow, trendline="ols")
        elif facetCol == 'None' and facetRow == 'None' and color != 'None':
            print(facetCol, facetRow, color)
            fig = px.scatter(df, x=xAxis, y=yAxis, color=color, trendline="ols")
        else:
            print(facetCol, facetRow, color)
            fig = px.scatter(df, x=xAxis, y=yAxis, trendline="ols")
        return fig
    elif graphMethod == 'jitter':
        print('this is jitter plot', graphMethod)
        fig = px.strip(df, x=xAxis, y=yAxis)
        return fig


# # @app.callback(Output('scatterPlot', 'figure'), [Input('xAxis', 'value'), Input('yAxis', 'value'),
# #                                                 Input('facetRow', 'value'), Input('facetCol', 'value')])
# @app.callback(Output('scatterPlot', 'figure'), [Input('xAxis', 'value'), Input('yAxis', 'value')])
# def display_value(xAxis, yAxis):
#     if xAxis == 'Relative Humidity':
#         print('here it is')
#
#     graph = go.Scatter(
#         x=df['UTCI'],
#         y=df['VP'],
#         # line={'color':'black','dash':'solid'},
#         name='Manipulate Graph',
#         mode='markers+lines',
#         marker=go.Marker(color='rgb(255, 127, 14)'),
#     )
#     try:
#         layout = go.Layout(
#             paper_bgcolor='#D6EAF8',
#             plot_bgcolor='#D6EAF8',
#             xaxis=dict(range=[min(df[xAxis]), max(df[xAxis])]),
#             yaxis=dict(range=[min(df[yAxis]), max(df[yAxis])]),
#             font=dict(color='#000000'),
#         )
#     except:
#         print('no')
#     return {'data': [graph], 'layout': layout}
