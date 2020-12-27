# import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
# from dash.dependencies import Input, Output
import portfolio_lib as pl

colors = {
    'background': '#000000',
    'text': '#7FDBFF'
}

################################ Data Processing for ETF portfolio #####################################################
(df_etf_init, df_orders_init, _, _) = pl.load_data()
(df_orders, _) = pl.preprocess_orders(df_orders_init)
df_etf = pl.preprocess_etf_masterdata(df_etf_init)
orders_etf = pl.enrich_orders(df_orders, df_etf)
portfolio = pl.get_current_portfolio(orders_etf)

unique_etfs = orders_etf[["ISIN", "Name"]].drop_duplicates().sort_values("ISIN").reset_index(drop=True)

### ------------------- Portfolio of monthly savings plan ------------------
group_cols = ["Region", "Type"]
compute_cols = ["Betrag", "Betrag"]
agg_functions = ["sum", "sum"]
grouped_portfolio = pl.compute_percentage_per_group(portfolio, group_cols, compute_cols, agg_functions)


################################ Define Dash App configuration ### #####################################################
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

body = html.Div([
                    html.H1(children="Bootstrap Responsive Dashboard Example"),

                    html.H2("Columns with justify = around"),
                    dbc.Row(
                        [
                            dbc.Col(html.Div(dbc.Alert("Column 1")), width=6),
                            dbc.Col(html.Div(dbc.Alert("Column 3")), width=6)
                        ],
                        justify='around'
                    ),
                    html.H2("Columns with rows in it"),
                    dbc.Row(
                        [
                            dbc.Col(html.Div([html.Div("Text"),html.Br(), html.Div("Text"),
                                              html.Br(), html.Div("Text"),html.Br(), html.Div("Text"),
                                              html.Br(), html.Div("Text"),html.Br(), html.Div("Text")]), width=6),
                            dbc.Col([
                                    dbc.Row([
                                        dbc.Col(html.Div([html.Div("Text"),html.Br(), html.Div("Text"),
                                              html.Br(), html.Div("Text"),html.Br(), html.Div("Text")])
                                            , width=6),
                                        dbc.Col(html.Div(dbc.Alert("Column 2")), width=6)
                                    ]),
                                    dbc.Row([
                                        dbc.Col(html.Div(dbc.Alert("Column 1")), width=6),
                                        dbc.Col(html.Div(dbc.Alert("Column 2")), width=6)
                                    ])
                                ],
                                width=6
                            )
                        ],
                        justify='start'
                    ),
                html.Div(dbc.Alert("Next row!"))
                ]
            )

app.layout = html.Div([body])

if __name__ == '__main__':
    app.run_server(debug=True)