from dash import html, callback
import dash_bootstrap_components as dbc
from dash import Output,Input
from src.components.WC_Header import WCHeaderCard
from src.components.WCWinnerRegionSunburst import WCWinnerRegion
from src.components.WCComponents import *
from src.utils.consts import Rank as world_ranking

world_ranking['Continent'] = world_ranking['confederation'].replace({
    'UEFA' : 'Europe',
    'CAF' : 'Africa',
    'AFC' : 'Asia',
    'CONCACAF': 'North & Central America',
    'CONMEBOL': 'South America',
    'OFC' : 'Oceania'
})

rank_years = world_ranking['rank_date'].str[:4].unique().tolist()


worldcup_page_content = html.Div([


    dbc.Row([
        WCHeaderCard
    ]),
    dbc.Row([
        WCMaps

    ],style={"align-text": "center"}),
    dbc.Row([
        WCWinnersBar,
        WCWinnerRegion,
        dbc.Col([
        MatchesCountBar])

    ]),
    dbc.Row([
        StadiumsBar,
        TotalAttendanceLine,

    ]),
    dbc.Row([

        dbc.Col([GoalsCountPerTourLine,
                 ], className="m-0 p-0")
    ]),

    dbc.Row([
        dbc.Col([CountriesTotalGoalsBar
                 ], className="m-0 p-0"),

        TopWcScorersBar,
    ]),


    dbc.Row([

        html.Div(
                html.Div(
                    className="card-chart",

                    children=[
                        html.H4("Top 10 Ranked Teams",
                                className="card-header card-m-0 me-2 pb-3", style={"font-size": "1.5vw"}),
                        dcc.Dropdown(
                                id='year-dropdown',
                                options=[{'label': year, 'value': year} for year in rank_years],
                                value='2022'
                            ),
                        dcc.Graph(id='rank-graph')
                    ],
                ), className="col-md-12 col-lg-12 mb-md-0 mb-4 card-chart-container"
            )

    ]),
], style={"padding-top": "40px"})

@callback(
    Output('rank-graph', 'figure'),
    Input('year-dropdown', 'value')
)
def update_graph(selected_year):
    wc_rank = world_ranking[(world_ranking['rank'] <= 10) & (world_ranking['rank_date'].str.startswith(selected_year))].tail(10).sort_values('rank', ascending=False)
    fig = px.bar(data_frame=wc_rank, y='country_full', x='total_points', orientation='h', color='Continent')
    fig.update_layout(
        title={
            'text': f'Top 10 Ranked Teams in {selected_year}',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        yaxis=dict(
            title='Country',
            autorange='reversed',
            categoryarray=wc_rank['country_full'][::-1].tolist()
        ),
        xaxis=dict(title='Total Points'),
        height=600,
        legend=dict(
            title=dict(text='Continent'),
            traceorder='reversed',
            yanchor='top',
            y=0.99,
            xanchor='right',
            x=1.3
        )
    )
    return fig
