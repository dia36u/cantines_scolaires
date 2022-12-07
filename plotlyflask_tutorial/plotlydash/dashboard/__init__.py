from dash import Dash, html, dcc
import dash
import pandas as pd

def create_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/',
        external_stylesheets=[
            '/static/dist/css/styles.css',
        ]
    )

    # Load DataFrame
    df = pd.read_csv("data/nantes-2011.csv",sep=";")
    print(df)
    # Create Dash Layout
    dash_app.layout = html.Div(
            dcc.Graph(
                id="histogram-graph",
                figure={
                    "data": [
                        {
                            "x": df["Nom du site"],
                            "text": df["Prévision"],
                            "customdata": df["Prévision"],
                            "name": "Cantines Nantes",
                            "type": "histogram",
                        }
                    ],
                    "layout": {
                        "title": "Cantines Nantes",
                        "height": 500,
                        "padding": 150,
                    },
                },
            ),id='dash-container')

    return dash_app.server