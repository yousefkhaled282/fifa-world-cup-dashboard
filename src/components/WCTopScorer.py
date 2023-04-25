import dash_bootstrap_components as dbc
from src.utils.consts import Goals as df_goals
import pandas as pd
import plotly.express as px

df_goals['goals'] = df_goals['home_team']+df_goals['away_team']


def Player_Scores(df,title):
    df = df.sort_values(by='goals', ascending=False)
    df['given_name'] = df['given_name'].replace('not applicable','')
    df['player_name'] = df['given_name'] + df['family_name']
    # create a bar chart using plotly
    fig = px.bar(df.head(10), y='player_name', x='goals',orientation='h',title=title)
    return fig


df_player_scored = df_goals.groupby(['given_name','family_name'])['goals'].sum().reset_index()


