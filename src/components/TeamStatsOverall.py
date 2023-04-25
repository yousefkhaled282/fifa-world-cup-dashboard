from dash.dependencies import Input, Output, State
import pandas as pd
import dash_bootstrap_components as dbc
from dash import html, dcc
import dash_loading_spinners as dls
import src.utils.theme as theme
from dash import callback
from src.utils.consts import *

from src.utils.consts import Maps as stadium_df
stadium_df['year'] = stadium_df['tournament_id'].str.split('-',expand = True)[1]
years = stadium_df['year'].unique()

from src.utils.consts import Award as df_award


def award_winner(df,award_name):
    df = df[df['award_name'] == award_name]
    df_filtered = df.groupby(['family_name','given_name'])['award_name'].size().reset_index().sort_values(by='award_name', ascending=False)
    df_filtered["player_name"] = df_filtered['given_name'] + ' '+df_filtered['family_name']
    return df_filtered[["player_name","award_name"]].head(1)




TeamStatsOverall = dbc.Row(children=[
    html.Div(className="col-lg-3 col-md-8 col-sm-13 card-chart-container", children=[html.Div(className="card", children=[
        html.Div(className="card-body", children=[
            html.Div(className="d-flex justify-content-between", children=[
                html.Div(className="card-info",
                         children=[
                             dbc.Select(
                                 id="query-team-select",
                                 value="",
                                 options=[
                                     {"label": year, "value": year} for year in years
                                 ],
                                 style={"width": "10rem"}
                             ),
                             html.P(className="card-text mb-1 mt-1 fs-sm",
                                    id="team-code-text",
                                    children=[f"Golden Ball: "]),
                             html.P(className="card-text mb-1 fs-sm",
                                    id="team-region-text",
                                    children=[f"Golden Glove:"]),
                             html.P(className="card-text mb-1 fs-sm",
                                    id="team-confederation-text",
                                    children=[f"Golden Boot: "]),

                         ]),
            ])
        ])
    ], style={"min-height": "5rem"})]
    ),
])

@callback(
    Output("team-code-text", "children"),
    Output("team-region-text", "children"),
    Output("team-confederation-text", "children"),

    Input("query-team-select", "value"),
)

def update_team_select(query_team):
    Golden_Ball = award_winner(df_award[df_award['tournament_name'] == query_team+' FIFA World Cup'], 'Golden Ball')['player_name'].values[0]
    Golden_Glove = award_winner(df_award[df_award['tournament_name'] == query_team+' FIFA World Cup'], 'Golden Glove')['player_name'].values[0]
    Golden_Boot = award_winner(df_award[df_award['tournament_name'] == query_team+' FIFA World Cup'], 'Golden Boot')['player_name'].values[0]
    return f"Golden Ball: {Golden_Ball}",f"Golden Glove: {Golden_Glove}",f"Golden Boot: {Golden_Boot}"