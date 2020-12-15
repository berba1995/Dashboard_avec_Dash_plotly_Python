import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

LOGO = "https://i2.wp.com/ledatascientist.com/wp-content/uploads/2019/01/31934826_632207023790117_7976915477504983040_o.png?fit=1638%2C1638&ssl=1"

navbar = dbc.Navbar(
    [
        html.A(
            # Alignement vertical de l'image et de l'acceuil
            dbc.Row(
                [   #logo
                    dbc.Col(html.Img(src=LOGO, height="40px")),
                    #Navlink Acceuil
                    dbc.NavLink("Acceuil", href="/acceuil",style={'color':'white'}),
                    #Navlink dashbord
                    dbc.NavLink("Dashbsoard", href="/dashboard",style={'color':'white'})
                ],
                align="cesnter",
                no_gutters=True,
            ),
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
    ],
    color="dark",
    dark=True,
)
