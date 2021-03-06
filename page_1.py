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
from dash import dash_table
#from dash_table.Format import Group` with 
from dash.dash_table.Format import Group

#path="https://github.com/MdioufDataScientist/Projet-Visualisation/blob/main/COVID-19-geographic-disbtribution-worldwide%20-%20COVID-19-geographic-disbtributi.csv"
path1="/home/mdiouf/Bureau/Projet-Visualisation/Data_covid.csv"
data=pd.read_csv("Data_covid.csv")
dfTable=data.groupby(['countriesAndTerritories'])['cases'].sum().reset_index()
dfTable=dfTable.sort_values(by=['cases'],ascending=False)
dfMort=data.groupby(['countriesAndTerritories'])['deaths'].sum().reset_index()
dfMort=dfMort.sort_values(by=['deaths'],ascending=False)
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
             dash_table.DataTable(
                id='datatable',
                columns=[
                    {"name": i, "id": i, "deletable": True, "selectable": True} for i in dfTable.columns
                ],
                data=dfTable.to_dict('records'),
                page_size=10,
                style_cell={'textAlign': 'center'},
                style_header={
        'backgroundColor': 'white',
        'color': 'black',
        'fontWeight': 'bold'
    },
    style_data={
        'backgroundColor': 'rgb(50, 50, 50)',
        'color': 'white'
    },
            )        
        ], width={'size':8,'offset':2}
        )      
    ]),
    dbc.Row([
         dbc.Col([
            html.Br(),
             dash_table.DataTable(
                id='datatable2',
                columns=[
                    {"name": i, "id": i, "deletable": True, "selectable": True} for i in dfMort.columns
                ],
                data=dfMort.to_dict('records'),
                page_size=10,
                #style_cell={'textAlign': 'left','background-color':'gray','color':'black'}
                style_cell={'textAlign': 'center'},
                style_header={
        'backgroundColor': 'white',
        'color': 'black',
        'fontWeight': 'bold'
    },
    style_data={
        'backgroundColor': 'rgb(50, 50, 50)',
        'color': 'white'
    },
            )        
        ], width={'size':8,'offset':2}
        )  
    ])
          
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
[Output('fig_1', 'figure'),
Output('fig_2', 'figure'),
Output('fig_3', 'figure'),
Output('fig_4', 'figure'),
Output('fig_5', 'figure'),
Output('fig_6', 'figure'),

],
[Input('plage_de_date', 'start_date'),
Input('plage_de_date', 'end_date'),
Input('d_drp','value')
])
def update(debut,fin,pays):
    if pays:
        if debut:
            if fin:
                df=creer_datafram(debut,fin,pays)
                cov = df.groupby('month')['cases'].sum().reset_index()
                fig_1 = px.bar(cov,x='month',y='cases',title=f'nombre total de cas par mois : {pays}',color='month')
                cov_2 = df.groupby('month')['deaths'].sum().reset_index()
                fig_2= px.bar(cov_2,x='month',y='deaths',title=f'nombre total de morts par mois : {pays}',color='month')
                #fig_2=px.scatter(cov_2,x='month',y='deaths',size='deaths',color="month",title=f"nombre total de morts par mois : {pays}")
                fig_3=px.scatter(df,x='day',y='cases',title=f"tendance des nouveaux cas par jour: {pays}",size='cases',color="cases")
                #fig_3=px.scatter(df,x='month',y='deaths',size='deaths',color="month",title=f"nombre total de morts par mois : {pays}")
                #manipulations pour obtenir la somme cumul??
                cum_1=pd.DataFrame(df.groupby('month')['cases'].sum())
                cum_1=cum_1['cases'].cumsum().reset_index()
              
                fig_4=px.scatter(df,x='day',y='deaths',title=f"tendance des Morts par jour : {pays}",size='deaths',color="deaths")
        
                cum_2=pd.DataFrame(df.groupby('month')['deaths'].sum())
                cum_2=cum_2['deaths'].cumsum().reset_index()
                fig_5=px.line(cum_2,x='month',y='deaths',markers=True,title=f"cumul des Morts par mois : {pays}")
                fig_6=px.line(cum_1,x='month',y='cases',markers=True,title=f"cumul des cas par mois : {pays}")

                #fig1=px.pie(df,values='cases',names='dateRep',color_discrete_sequence=px.colors.sequential.RdBu,title=f"Nombre de cas par Jour : {pays}")
                return fig_1,fig_2,fig_3,fig_4,fig_5,fig_6
    else:
        fig_1={}  
        fig_2={}
        fig_3={}
        fig_4={}
        fig_5={}
        fig_6={}
        return fig_1,fig_2,fig_3,fig_6,fig_4,fig_5


app.run_server(debug=True)
