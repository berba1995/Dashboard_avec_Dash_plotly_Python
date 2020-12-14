import dash_core_components as dcc
import dash_html_components as html
import dash_table
from datetime import datetime as dt
from datetime import date, timedelta
import pandas as pd
import time
from components.functions import df_pc
import dash
import dash_bootstrap_components as dbc

color_l=['info',"secondary","success","warning","danger"]
def create_card(title, content,color):
    card = dbc.Card(
        dbc.CardBody(
            [
                html.H4(title, className="card-title"),
                html.Br(),
                html.H2(content, className="card-subtitle"),
                html.Br(),

                ]
        ),
        color=color, inverse=True
    )
    return(card)

acces_number=df_pc.sum(axis=0)

card1 = create_card("Nombre d'accès Android", acces_number[0],color_l[0])
card2 = create_card("Nombre d'accès Autres PC", acces_number[1],color_l[1])
card3 = create_card("Nombre d'accès Iphone", acces_number[2],color_l[2])
card4 = create_card("Nombre d'accès Mac", acces_number[3],color_l[3])

graphRow0 = dbc.Row([dbc.Col(id='card1', children=[card1], md=3), dbc.Col(id='card2', children=[card2], md=3), dbc.Col(id='card3', children=[card3], md=3), dbc.Col(id='card4', children=[card4], md=3)])


piegraph=dcc.Graph(id='pieGraph')
pie = dcc.Graph(
        id = "pieG",
        figure = {
          "data": [
            {
              "values": [800, 345, 500],
              "labels": [
                "Positive",
                "Negative",
                "Neutral"
              ],
              "name": "Sentiment",
              "hoverinfo":"label+name+percent",
              "hole": .7,
              "type": "pie"
              #"marker" : dict(colors['#05C7F2','#D90416','#D9CB04'])
}],
          "layout": {
                "title" : dict(text ="Sentiment Analysis",
                               font =dict(
                               size=20,
                               color = 'white')),
                "paper_bgcolor":"#111111",
                "width": "2000",
                "annotations": [
                    {
                        "font": {
                            "size": 20
                        },
                        "showarrow": False,
                        "text": "",
                        "x": 0.2,
                        "y": 0.2
                    }
                ],
                "showlegend": False
              }
        }
)




radio_item=dcc.RadioItems(
  options=[
      #{'label': 'choix date', 'value': 'choix'},
      {'label': '3 Mois', 'value': 'trois_mois'},
      {'label': '6 Mois', 'value': 'six_mois'},
      {'label': '1 An', 'value': 'un_an'},
      {'label': 'All', 'value': 'all'}

  ], #value='choix',
  labelStyle={'display': 'inline-block', 'width': '20%','color': 'blue','marginTop': 13},
  id='radio-button-publishing'
  )



filtre_label =html.H2("Select date range : ",style={'color':'blue'})
filtre_line = dbc.Row([dbc.Col(filtre_label , lg=3,width=6), dbc.Col(radio_item, lg=6, width=6)])

graph=dcc.Graph(id='publishing')

graph_line = dbc.Row([dbc.Col(graph, lg=8), dbc.Col(piegraph, lg=4)])

#table_line= dbc.Row([dbc.Col(date_picker, md=4),dbc.Col(table, md=8)],justify="center")
footer =dbc.Row(
        dbc.Col(
            html.P(
                [
                    html.Span('Auteur : Wilfried Kouadio', className='mr-2'),
                    html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/berba1995/Dashboard_avec_Dash_plotly_Python'),
                    html.A(html.I(className='fab fa-linkedin mr-1'), href='https://www.linkedin.com/in/wilfried-kouadio/'),
                ],
                className='lead'
            )
        ,lg=12)
    )


layout_dashboard  = html.Div([html.Br(),graphRow0, html.Br(), filtre_line ,html.Br(), graph_line,html.Br(),footer],style={"height": "100vh"})










######################## START Log action sur site ########################
