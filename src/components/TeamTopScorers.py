import plotly.express as px
from dash import html, dcc
import src.utils.theme as theme
from dash.dependencies import Input, Output, State
import dash_loading_spinners as dls
from dash import callback
from src.utils.consts import Goals as df_G

def Player_Scores(df,title):
    df = df.sort_values(by='goals', ascending=False)
    df['given_name'] = df['given_name'].replace('not applicable','')
    df['player_name'] = df['given_name'] + df['family_name']
    fig = px.bar(df.head(10).sort_values(by='goals',ascending=True), y='player_name', x='goals',
                 labels={"player_name": "Player Name",
                         "goals": "Goals"},
                 title=title)
    return fig



TeamTopScorers = html.Div(className="card-chart-container col-lg-4 md-6 sm-12",
                          children=[

                              html.Div(
                                  className="card-chart",
                                  children=[
                                      html.H4("Top Scorers",
                                              className="card-header card-m-0 me-2 pb-3"),
                                      dls.Triangle(
                                          id="team-top-scorers",
                                          children=[


                                          ], debounce=theme.LOADING_DEBOUNCE
                                      )
                                  ]
                              )

                          ],
                          )


@callback(
    Output("team-top-scorers", "children"),
    Input("query-team-select", "value"),
    State("goals-df", "data")
)
def update_figures(query_team, goals_df):
    df_2022 = df_G[df_G['tournament_name'] == query_team+' FIFA World Cup']
    df_player_scored = df_2022.groupby(['given_name', 'family_name'])['goals'].sum().reset_index()
    return dcc.Graph(figure=Player_Scores(df_player_scored,'').update_layout(paper_bgcolor="rgb(0,0,0,0)",
                                    plot_bgcolor="rgb(0,0,0,0)",
                                    legend=dict(
                                        bgcolor=theme.LEGEN_BG),
                                    font_family=theme.FONT_FAMILY
                                    ),
                     config={
        "displayModeBar": False},
        style=theme.CHART_STYLE

    )
