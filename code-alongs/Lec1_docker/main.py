import plotly_express as px
import numpy as np

# Funkar nog inte för att jag är inte inne i rätt miljö??
from dash import Dash, dcc, html
from dash.html import H1, Div


app = Dash(__name__)

app.layout = html.Div([
    html.H1("Hej")
])



# TODO: Search up this more later, do flashcard on it
if __name__ == '__main__':
    print('Hello from the docker side')


    app.run_server(debug=True)