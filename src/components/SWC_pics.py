from dash import html, dcc, callback
from dash.dependencies import Input, Output

import base64



ImageBrackets = html.Div(className="col-md-12 col-lg-12 mb-md-0 mb-4 card-chart-container",
                       children=[

                           html.Div(
                               className="card-chart",
                               children=[
                                   html.H4("World Cup Brackets",
                                           className="card-header card-m-0 me-2 pb-3"),
                                   html.Img(id = 'bracket_image',height = '500px' ,width='auto', className="img-fluid")
                               ]
                           )

                       ],
                       )



@callback(
    Output("bracket_image", "src"),
    Input("query-team-select", "value"),
)
def update_image(query_team):
    image_path = rf"G:\ai & ML ITI 9 month\fifa-worldcup-dashboard-main\fifa-worldcup-dashboard-main\src\assets\images\WC {query_team}.jpeg"
    encoded_image = base64.b64encode(open(image_path, 'rb').read())
    return 'data:image/jpeg;base64,{}'.format(encoded_image.decode())


