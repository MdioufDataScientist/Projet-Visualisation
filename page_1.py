from dash import dcc
from dash import html
import dash
from dash.dependencies import Input, Output
from dash.html.Center import Center
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import pandas as pd
from datetime import date

#path="https://github.com/MdioufDataScientist/Projet-Visualisation/blob/main/COVID-19-geographic-disbtribution-worldwide%20-%20COVID-19-geographic-disbtributi.csv"
path1="/home/mdiouf/Bureau/Projet-Visualisation/Data_covid.csv"
data=pd.read_csv(path1)
print(data.head(5))

load_figure_template("cyborg")
app=dash.Dash(__name__,external_stylesheets=[dbc.themes.CYBORG])
app.layout=dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Covid Dashboard",className='text-center font-weight-bold shadow'))
    ]),
    dbc.Row([       
            dbc.Col([
                dcc.DatePickerRange(
            display_format="DD/M/YYYY",
            min_date_allowed=date(2019, 12, 31),
            max_date_allowed=date(2020, 3, 27),
            start_date_placeholder_text="Debut",
            end_date_placeholder_text="Fin",
            calendar_orientation='vertical',
            )
            ], width={'size':6}
            ),
            dbc.Col([
            dcc.Dropdown(id='d_drp',
            options=[{'label':x,'value':x} for x in data['countriesAndTerritories'].unique()],
            placeholder="selectionner le Pays"
            )
            ], width={'size':6}) 
        ]
        ),
        dbc.Row([
        dbc.Col([
            html.Br(),
            dcc.Graph(id="fig_1",figure={})         
        ], width={'size':6}
        ),
        dbc.Col([
            html.Br(),
            dcc.Graph(id="fig_2",figure={})
        ], width={'size':6}
        )       
    ]),
    dbc.Row([
        dbc.Col([
            html.Br(),
            dcc.Graph(id="fig_3",figure={})         
        ], width={'size':6}
        ),
        dbc.Col([
            html.Br(),
            dcc.Graph(id="fig_4",figure={})
        ], width={'size':6}
        )       
    ]),
    dbc.Row([
        dbc.Col([
            html.Br(),
            dcc.Graph(id="fig_5",figure={})         
        ], width={'size':6}
        ),
        dbc.Col([
            html.Br(),
            dcc.Graph(id="fig_6",figure={})
        ], width={'size':6}
        )       
    ]),
    dbc.Row([
        dbc.Col([
            html.Br(),
            dcc.Graph(id="fig_7",figure={})         
        ], width={'size':6}
        ),
        dbc.Col([
            html.Br(),
            dcc.Graph(id="fig_8",figure={})
        ], width={'size':6}
        )       
    ]),
    dbc.Row([
        dbc.Col([
            html.Br(),
            dcc.Graph(id="fig_9",figure={})         
        ], width={'size':6}
        ),
        dbc.Col([
            html.Br(),
            dcc.Graph(id="fig_10",figure={})
        ], width={'size':6}
        )       
    ]),
])

app.run_server(debug=True)