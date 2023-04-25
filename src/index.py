from dash import callback
from pages.team_analysis import team_analysis_page_content
from dash.dependencies import Input, Output
from pages.worldcup_analysis import worldcup_page_content




@callback(
    Output(component_id='page-content', component_property='children'),
    Input(component_id='url', component_property='pathname')
)
def routing(path):
    if path == "/":
        return worldcup_page_content
    elif path == "/single-analysis":
        return team_analysis_page_content

