import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
# from dash.dependencies import Input, Output

colors = {
    'background': '#000000',
    'text': '#7FDBFF'
}

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

body = html.Div([
                    html.H1(children="Bootstrap Responsive Dashboard Example"),
                    html.Div(dbc.Alert("A single row")),
                    html.H2("Columns with no_gutters = False"),
                    dbc.Row(
                        [
                            dbc.Col(html.Div(dbc.Alert("Column 1")), width=4),
                            dbc.Col(html.Div(dbc.Alert("Column 2")), width=4),
                            dbc.Col(html.Div(dbc.Alert("Column 3")), width=4)
                        ]
                    ),
                    html.H2("Columns with no_gutters = True"),
                    dbc.Row(
                        [
                            dbc.Col(html.Div(dbc.Alert("Column 1")), width=4),
                            dbc.Col(html.Div(dbc.Alert("Column 2")), width=4),
                            dbc.Col(html.Div(dbc.Alert("Column 3")), width=4)
                        ],
                        no_gutters=True
                    ),
                    html.H2("Columns with justify = start"),
                    dbc.Row(
                        [
                            dbc.Col(html.Div(dbc.Alert("Column 1")), width=2),
                            dbc.Col(html.Div(dbc.Alert("Column 2")), width=2),
                            dbc.Col(html.Div(dbc.Alert("Column 3")), width=2)
                        ],
                        justify='start'
                    ),
                    html.H2("Columns with justify = end"),
                    dbc.Row(
                        [
                            dbc.Col(html.Div(dbc.Alert("Column 1")), width=2),
                            dbc.Col(html.Div(dbc.Alert("Column 2")), width=2),
                            dbc.Col(html.Div(dbc.Alert("Column 3")), width=2)
                        ],
                        justify='end'
                    ),
                    html.H2("Columns with justify = center"),
                    dbc.Row(
                        [
                            dbc.Col(html.Div(dbc.Alert("Column 1")), width=2),
                            dbc.Col(html.Div(dbc.Alert("Column 2")), width=2),
                            dbc.Col(html.Div(dbc.Alert("Column 3")), width=2)
                        ],
                        justify='center'
                    ),
                    html.H2("Columns with justify = between"),
                    dbc.Row(
                        [
                            dbc.Col(html.Div(dbc.Alert("Column 1")), width=2),
                            dbc.Col(html.Div(dbc.Alert("Column 2")), width=2),
                            dbc.Col(html.Div(dbc.Alert("Column 3")), width=2)
                        ],
                        justify='between'
                    ),
                    html.H2("Columns with justify = around"),
                    dbc.Row(
                        [
                            dbc.Col(html.Div(dbc.Alert("Column 1")), width=2),
                            dbc.Col(html.Div(dbc.Alert("Column 2")), width=2),
                            dbc.Col(html.Div(dbc.Alert("Column 3")), width=2)
                        ],
                        justify='around'
                    ),
                    html.H2("Specify widths for different size-devices:"),
                    dbc.Row(
                        [
                            dbc.Col(html.Div(dbc.Alert("Column 1")), lg=4, md=6, xs=12),
                            dbc.Col(html.Div(dbc.Alert("Column 2")), lg=4, md=6, xs=12),
                            dbc.Col(html.Div(dbc.Alert("Column 3")), lg=4, md=6, xs=12)
                        ],
                        justify='around'
                    )
                ]
            )

app.layout = html.Div([body])

if __name__ == '__main__':
    app.run_server(debug=True)