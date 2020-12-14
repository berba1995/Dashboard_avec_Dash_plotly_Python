import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pages.header import navbar
from pages.layout_dashboard import layout_dashboard
from pages.layout_acceuil import layout_acceuil
from datetime import date, timedelta
from datetime import datetime as dt

import pandas as pd
import io
import xlsxwriter
from flask import send_file
import dash
import dash_bootstrap_components as dbc
# see https://dash.plot.ly/external-resources to alter header, footer and favicon
from components.functions import df_pc
from components.functions import update_first_datatable, update_graph_1,df_pc,update_pie


app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP,'https://use.fontawesome.com/releases/v5.9.0/css/all.css'])

server = app.server
app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    navbar,
    #dcc.Storage(id='session', storage_type='session'),
    html.Div(id='page-content')
])

app.config['suppress_callback_exceptions']=True
# Update page
# # # # # # # # #
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname=='/acceuil' or pathname=='/':
        return layout_acceuil
    elif pathname=='/dashboard':
        return layout_dashboard



@app.callback(
   Output('publishing', 'figure'),
   [Input('radio-button-publishing', 'value')])

def update_publishing(value):
    start_date=(df_pc['dates'].max() - timedelta(28)).date()
    start_date= dt.strftime(start_date, '%Y-%m-%d')
    end_date=df_pc['dates'].max().date()
    end_date= dt.strftime(end_date, '%Y-%m-%d')
    if value=='all':
        start_date=df_pc['dates'].min().date()
        start_date= dt.strftime(start_date, '%Y-%m-%d')
        end_date=df_pc['dates'].max().date()
        end_date= dt.strftime(end_date, '%Y-%m-%d')
        fig=update_graph_1(start_date, end_date,'trafic')
        return fig
    elif value=='trois_mois':
        end_date_obj= dt.strptime(end_date, '%Y-%m-%d')
        start_date=end_date_obj.date()-timedelta(92)
        start_date=start_date.strftime("%Y-%m-%d")
        fig = update_graph_1(start_date, end_date,'trafic')
        return fig
    elif value=='six_mois':
        end_date_obj= dt.strptime(end_date, '%Y-%m-%d')
        start_date=end_date_obj.date()-timedelta(186)
        start_date=start_date.strftime("%Y-%m-%d")
        fig = update_graph_1(start_date, end_date,'trafic')
        return fig
    elif value=='un_an':
        end_date_obj= dt.strptime(end_date, '%Y-%m-%d')
        start_date=end_date_obj.date()-timedelta(365)
        start_date=start_date.strftime("%Y-%m-%d")
        fig = update_graph_1(start_date, end_date,'trafic')
        return fig

    else:
	    fig = update_graph_1(start_date, end_date,'trafic')
	    return fig




@app.callback(Output('table', 'data'),
	[Input('my-date-picker-range-publishing', 'start_date'),
	 Input('my-date-picker-range-publishing', 'end_date')
     ])
def update_data_1(start_date, end_date):

	data_table = update_first_datatable(start_date, end_date,'defaut')
	return data_table


@app.callback(
   Output('pieGraph', 'figure'),
   [Input('radio-button-publishing', 'value')])

def update_publishing(value):
    start_date=(df_pc['dates'].max() - timedelta(28)).date()
    start_date= dt.strftime(start_date, '%Y-%m-%d')
    end_date=df_pc['dates'].max().date()
    end_date= dt.strftime(end_date, '%Y-%m-%d')
    if value=='all':
        start_date=df_pc['dates'].min().date()
        start_date= dt.strftime(start_date, '%Y-%m-%d')
        end_date=df_pc['dates'].max().date()
        end_date= dt.strftime(end_date, '%Y-%m-%d')
        fig=update_pie(start_date, end_date,'trafic')
        return fig
    elif value=='trois_mois':
        end_date_obj= dt.strptime(end_date, '%Y-%m-%d')
        start_date=end_date_obj.date()-timedelta(92)
        start_date=start_date.strftime("%Y-%m-%d")
        fig = update_pie(start_date, end_date,'trafic')
        return fig
    elif value=='six_mois':
        end_date_obj= dt.strptime(end_date, '%Y-%m-%d')
        start_date=end_date_obj.date()-timedelta(186)
        start_date=start_date.strftime("%Y-%m-%d")
        fig = update_pie(start_date, end_date,'trafic')
        return fig
    elif value=='un_an':
        end_date_obj= dt.strptime(end_date, '%Y-%m-%d')
        start_date=end_date_obj.date()-timedelta(365)
        start_date=start_date.strftime("%Y-%m-%d")
        fig = update_pie(start_date, end_date,'trafic')
        return fig

    else:
	    fig = update_pie(start_date, end_date,'trafic')
	    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
