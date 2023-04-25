
import plotly.graph_objects as go
from dash import html, dcc
import src.utils.theme as theme
import pandas as pd
from dash.dependencies import Input, Output, State
import dash_loading_spinners as dls
from dash import callback


def Plot_Table_frquence(df_freq,width=400, height=350):

    fig = go.Figure(data=[go.Table(header=dict(values=df_freq.columns.to_list()),
                     cells=dict(values=df_freq.values.T))
                         ])
    fig.update_layout(width=width, height=height)
    return fig


TableFrequence_goal_perQuarter = html.Div(className="card-chart-container col-lg-4 md-6 sm-12",
                              children=[

                                  html.Div(
                                      className="card-chart",
                                      children=[
                                          html.H4("Goal Per Quarter",
                                                  className="card-header card-m-0 me-2 pb-3"),
                                          dls.Triangle(
                                              id="team-matches-results",
                                              children=[

                                              ], debounce=theme.LOADING_DEBOUNCE
                                          )
                                      ]
                                  )

                              ],
                              )


@callback(
    Output("team-matches-results", "children"),
    Input("query-team-select", "value")
)
def update_team_matches_result(query_team):

    df_freq = pd.read_csv(f'G:/ai & ML ITI 9 month/fifa-worldcup-dashboard-main/fifa-worldcup-dashboard-main/data/processed/New folder/{query_team}_goal_per_quarter.txt',encoding='latin-1')
    fig = Plot_Table_frquence(df_freq)
    return dcc.Graph(figure=fig.update_layout(paper_bgcolor="rgb(0,0,0,0)",
                                    plot_bgcolor="rgb(0,0,0,0)",
                                    legend=dict(
                                        bgcolor=theme.LEGEN_BG),
                                    font_family=theme.FONT_FAMILY,
                                    margin={"t": 40, "b": 40, "l": 32}
                                    ),
                     config={
        "displayModeBar": False},
        style=theme.CHART_STYLE

    )
