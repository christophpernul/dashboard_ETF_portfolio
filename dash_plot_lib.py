import plotly.express as px
import dash_table
import dash_core_components as dcc
import dash_html_components as html

def show_dataframe(df, style_dict):
    return(html.Div(dash_table.DataTable(
                        id='table',
                        columns=[{"name": i, "id": i} for i in df.columns],
                        data=df.to_dict('records'),
                        style_cell={'textAlign': 'left',
                                    'background': style_dict['background'],
                                    'color': style_dict['text'],
                                    'padding-left': '10px'},
                        style_header={
                            'fontWeight': 'bold'
                        },
                        style_as_list_view=True
                )
            )
    )
def show_piechart(df, chart_description):
    return(html.Div(dcc.Graph(figure = px.pie(df,
                                     values=chart_description['values'],
                                     names=chart_description['names'],
                                     title=chart_description['title']
                                     ).update_layout(paper_bgcolor='#000000',
                                                     font_color='#FFFFFF',
                                                     font_size=17,
                                                     title_font_size=22
                                                     )
                             )
                    )
           )