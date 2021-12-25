from dash import dcc
from dash import html
import dash
from dash.dependencies import Input, Output, State
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
#print(data.head(5))
total=data['cases'].sum()
total=str(total)
morts=data['deaths'].sum()
morts=str(morts)
load_figure_template("cyborg")
app=dash.Dash(__name__,external_stylesheets=[dbc.themes.CYBORG])
app.layout=dbc.Container([
    dbc.Row([
        dbc.Col(html.Div([
                html.H1("COVID DASHBOARD",style={'fontWeight':'bold','textAlign':'center'})
            ]
                
            ))
    ]),
    dbc.Row([       
            dbc.Col([
                dcc.DatePickerRange(
            id="plage_de_date",
            #display_format="DD/M/YYYY",
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
            ], width={'size':6}),
            
        ]
        ),
        dbc.Row([
        dbc.Col([
            html.Br(),
            html.Div([
                html.H1("Total Cas : "+total,style={'color': 'green','fontWeight':'bold','textAlign':'left'})
            ]
                
            )
            
        ], width={'size':5}
        ),
        dbc.Col([
            html.Br(),
            html.Div([
                html.H1("Total Morts : "+morts,style={'color': 'red','fontWeight':'bold','textAlign':'right'})
            ]
                
            )
        ], width={'size':6}
        )       
    ]),
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
data['dateRep']=pd.to_datetime(data['dateRep'])
def creer_datafram(debut,fin,pays):
    df=data[data['countriesAndTerritories']==pays]
    mask = (df['dateRep'] >= debut) & (df['dateRep'] <= fin)
    df_filtrer=df.loc[mask]
    df_filtrer.sort_values(by="dateRep",ascending=True)
    print(type(debut))
    #print(df_filtrer)
    return df_filtrer

@app.callback(
Output('fig_1', 'figure'),
[Input('plage_de_date', 'start_date'),
Input('plage_de_date', 'end_date'),
Input('d_drp','value')
])
def update(debut,fin,pays):
    if pays:
        if debut:
            if fin:
                df=creer_datafram(debut,fin,pays)
                fig1=px.pie(df,values='cases',names='dateRep',color_discrete_sequence=px.colors.sequential.RdBu,title=f"Nombre de cas pa Jour : {pays}")
                return fig1
    else:
        fig1={}  
        return fig1

app.run_server(debug=True)