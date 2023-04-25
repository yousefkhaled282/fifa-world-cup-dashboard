import plotly.express as px
from dash import html, dcc, callback
import src.utils.theme as theme
from dash.dependencies import Input, Output, State
import dash_loading_spinners as dls
from src.utils.consts import Maps as stadium_df


def plot_stadium_map(data_cup, Lat, lon, zoom=5):
    data_cup['hover_text'] = "Country Name: " + data_cup['country_name'] + '<br>' + "Stadium Name: " + data_cup[
        'stadium_name']
    print(data_cup['hover_text'])
    my_list = [0.5 for i in range(len(data_cup))]

    data_cup['marker_size'] = my_list
    print(data_cup['latitude_stadium'])
    fig = px.scatter_mapbox(data_cup, lat='latitude_stadium', lon='longitude_stadium',
                            center={'lat': Lat, 'lon': lon},
                            hover_name='hover_text',
                            hover_data={'latitude_stadium': False, 'longitude_stadium': False, 'marker_size': False},
                            zoom=zoom,

                            color_discrete_sequence=theme.COLOR_PALLETE,
                            size='marker_size',height=600, width=1200
                            )

    return fig


WC_MAP = html.Div(className="col-md-12 col-lg-12 mb-md-0 mb-4 card-chart-container",
                       children=[

                           html.Div(
                               className="card-chart",
                               children=[
                                   html.H4("Stadiums",
                                           className="card-header card-m-0 me-2 pb-3"),
                                   dls.Triangle(
                                       id="team-goals-count-per-minute",
                                       children=[

                                       ], debounce=theme.LOADING_DEBOUNCE
                                   )
                               ]
                           )

                       ],
                       )


@callback(
    Output("team-goals-count-per-minute", "children"),
    Input("query-team-select", "value"),
)
def update_figures(query_team):

    grouped_df = stadium_df.groupby(['tournament_name', 'stadium_name', 'country_name', 'latitude', 'longitude', 'latitude_stadium',
         'longitude_stadium'])['tournament_id'].unique().reset_index()


    grouped_df = grouped_df[grouped_df['tournament_name'] == query_team + " FIFA World Cup"]

    return dcc.Graph(figure = plot_stadium_map(grouped_df,
                     grouped_df['latitude_stadium'].iloc[1],
                     grouped_df['longitude_stadium'].iloc[1], zoom=3).update_layout(mapbox_style="open-street-map"))


