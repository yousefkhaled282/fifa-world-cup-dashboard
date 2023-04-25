from dash import html
import dash_bootstrap_components as dbc
from src.components.TeamTopScorers import TeamTopScorers
from src.components.TeamMatchesResults import TableFrequence_goal_perQuarter
from src.components.TeamGoalsStats import TableFrequence_MostFrequentGoal
from src.components.TeamStatsOverall import TeamStatsOverall
from src.components.TeamGoalsCountPerMin import WC_MAP
from src.components.SWC_pics import ImageBrackets


team_analysis_page_content = html.Div(children=[
    TeamStatsOverall,

    dbc.Row(children=[
        ImageBrackets,

    ]),
    dbc.Row(children=[
        WC_MAP,

    ]),

    dbc.Row(children=[

        TableFrequence_goal_perQuarter,
        TableFrequence_MostFrequentGoal,
        TeamTopScorers

    ]),


], style={"padding-top": "2rem"})
