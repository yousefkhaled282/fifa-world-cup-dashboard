import plotly.express as px

import plotly.graph_objects as go
from dash import html, dcc
import dash_bootstrap_components as dbc
import src.utils.theme as theme
from src.utils.consts import tours, goals, award_winners,Country_data
from src.utils.consts import Goals as df_goals
from src.utils.consts import Award as df_award


def create_card(fig, class_name, title="Title"):
    return html.Div(
        html.Div(
            className="card-chart",
            children=[
                html.H4(title,
                        className="card-header card-m-0 me-2 pb-3", style={"font-size": "1.5vw"}),
                dcc.Graph(
                    figure=fig.update_layout(
                        paper_bgcolor="rgb(0,0,0,0)",
                        plot_bgcolor="rgb(0,0,0,0)",
                        legend=dict(bgcolor=theme.LEGEN_BG),
                        font_family=theme.FONT_FAMILY,
                    ),
                    config={"displayModeBar": False},
                )
            ],
        ), className=class_name
    )


df_goals['goals'] = df_goals['home_team']+df_goals['away_team']


def Player_Scores(df):
    df = df.sort_values(by='goals', ascending=False)
    df['given_name'] = df['given_name'].replace('not applicable','')
    df['player_name'] = df['given_name'] + df['family_name']
    # create a bar chart using plotly
    fig = px.bar(df.head(10).sort_values('goals', ascending=True), y='player_name', x='goals',text='goals',
                 height=theme.MAX_CHART_HEIGHT,
                color_discrete_sequence=theme.COLOR_PALLETE)
    fig.update_xaxes(title_text='Goals')
    fig.update_yaxes(title_text='Player Name')
    return fig

def award_winner(df,award_name):
    df = df[df['award_name'] == award_name]
    df_filtered = df.groupby(['family_name','given_name'])['award_name'].size().reset_index().sort_values(by='award_name', ascending=False)
    df_filtered["player_name"] = df_filtered['given_name'] + ' '+df_filtered['family_name']
    return df_filtered[["player_name","award_name"]].head(1)




WCWinnersBar = create_card(class_name="card-chart-container col-lg-3 col-md-12 col-sm-12",
                           title="World Cup Holders",
                           fig=px.bar(
                               tours.groupby("winner", as_index=False).size().sort_values(by='size',ascending=True),
                               y="winner",
                               x="size",
                               height=theme.MAX_CHART_HEIGHT,
                               text="size",
                               color_discrete_sequence=theme.COLOR_PALLETE,
                               labels={"value": "Country",
                                       "size": "", "winner": "Winner"},
                           ).update_xaxes(categoryorder="total descending",
                                          ).update_layout(margin={"r": 20, "l": 30}))


tmp_tours = tours
tmp_tours["year"] = tours["year"].astype("str")
HostsCountriesBar = create_card(class_name="card-chart-container col-lg-5 col-md-12 col-sm-12",
                                title="World Cup Hosts",
                                fig=px.bar(tmp_tours.groupby("host_country", as_index=False).agg({"year": " - ".join, "winner": "size"}),
                                           x="host_country", y="winner", text="year",
                                           height=theme.MAX_CHART_HEIGHT,
                                           color_discrete_sequence=theme.COLOR_PALLETE,
                                           labels={
                                               "host_country": "Host Country", "winner": "Hosting Times"}
                                           ).update_xaxes(categoryorder="total descending",
                                                          ).update_layout(margin={"r": 20, "t": 10}))

df_goals['team_name'].replace('East Germany','Germany',inplace=True)
df_goals['team_name'].replace('West Germany','Germany',inplace=True)
CountriesTotalGoalsBar = create_card(class_name="card-chart-container col-lg-12 col-md-12 col-sm-12",
                                     title="Countries Goals in World Cups (Top 20)",
                                     fig=px.bar(df_goals.groupby("team_name", as_index=False).size().sort_values(by="size", ascending=False)[:20],
                                                x="team_name", y="size", text_auto=True, color_discrete_sequence=theme.COLOR_PALLETE,
                                                labels={"team_name": "Country", "size": "Goals Count"}, height=theme.MAX_CHART_HEIGHT,
                                                ).update_layout(margin={"r": 20})
                                     )


TotalAttendanceLine = create_card(class_name="card-chart-container col-lg-7 col-md-12 col-sm-12",
                                  title="Total and Average Attendance",
                                  fig=px.line(tours.rename(columns={"total_attendance": "Total"}),
                                              x="year", y="Total",
                                              labels={
                                                  "year": "Year"},
                                              color_discrete_sequence=theme.COLOR_PALLETE,
                                              height=theme.MAX_CHART_HEIGHT,).update_xaxes(type='category').update_xaxes(type='category', tickangle=45))

StadiumsBar = create_card(class_name="card-chart-container col-lg-5 col-md-12 col-sm-12",
                                 title="Stadiums",
                                 fig=px.bar(tours, x=tours["year"],
                                                  y="venues",
                                                  barmode="group",text = "venues", labels={"year": "Year", "venues": "Stadiums"},
                                                  color_discrete_sequence=theme.COLOR_PALLETE,
                                                  height=theme.MAX_CHART_HEIGHT,
                                                  ).update_layout(yaxis_title=""))



df_player_scored = df_goals.groupby(['given_name','family_name'])['goals'].sum().reset_index()
Top_ten_Scored = Player_Scores(df_player_scored)
TopWcScorersBar = create_card(class_name="card-chart-container col-lg-5 col-md-12 col-sm-12",
                              title="Top (10) Scorers in World Cups",
                              fig=Top_ten_Scored
                              )


df_goals['year'] = df_goals['tournament_id'].str.split('-',expand = True)[1]
GoalsCountPerTourLine = create_card(class_name="card-chart-container col-lg-12 col-md-12 col-sm-12",
                                    title="Goals Count in Each Tour",
                                    fig=px.line(df_goals.groupby(
                                        "year", as_index=False).size(), x="year", y="size",
                                        labels={"year": "Year",
                                                "size": "Count"},
                                        height=theme.MAX_CHART_HEIGHT,
                                        color_discrete_sequence=theme.COLOR_PALLETE,))



MatchesCountBar = create_card(class_name="card-chart-container col-lg-12 col-md-12 col-sm-12",
                              title="Matches Count in Each Tour",
                              fig=px.bar(tours, x="year", y="matches", color_discrete_sequence=theme.COLOR_PALLETE,
                                         height=theme.MAX_CHART_HEIGHT,
                                         text_auto=True,
                                         labels={
                                             "matches": "Matches Count", "year": ""}
                                         ).update_xaxes(type="category",
                                                        ).update_layout(margin={"r": 30}))



WCMaps = create_card(class_name="col-md-12 col-lg-12 mb-md-0 mb-4 card-chart-container",
                            title="WorldCups Map",
                            fig=px.scatter_mapbox(Country_data, lat='latitude', lon='longitude',
                     hover_name='hover_text',size='score',
                     size_max=10,hover_data = {'latitude': False, 'longitude': False,'score':False}, color_discrete_sequence=theme.COLOR_PALLETE
                     ,zoom=0.7,height=600, width=1200,template="plotly_dark" ).update_layout(mapbox_style="open-street-map", dragmode=False)

                     )


