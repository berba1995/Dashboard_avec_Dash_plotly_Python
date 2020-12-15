import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import callbacks
from pages.header import navbar
from pages.layout_dashboard import layout_dashboard
from pages.layout_acceuil import layout_acceuil
from app import app,server


#layout rendu par l'application
app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    navbar,
    html.Div(id='page-content')
])

#callback pour mettre à jour les pages
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname=='/acceuil' or pathname=='/':
        return layout_acceuil
    elif pathname=='/dashboard':
        return layout_dashboard


if __name__ == '__main__':
    app.run_server(debug=True)
