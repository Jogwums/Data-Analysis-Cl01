import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns

from dash import Dash
from dash import dcc
from dash import html

print("ready")

url = "../datasets/avocado.csv"

df = pd.read_csv(url, index_col=0)

df.head()

df = df.query("type == 'conventional' and region == 'Albany'")
df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")
df.sort_values("Date", inplace=True)

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Avocado Analytics",),
        html.P(
            children="Analyze the behavior of avocado prices "
            "and the number of avocados sold in the US "
            "between 2015 and 2018"
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": df["Date"],
                        "y": df["AveragePrice"],
                        "type": "lines",
                    },
                ],
                "layout": {"title":"Average Price of Avocados"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": df["Date"],
                        "y": df["Total Volume"],
                        "type": "lines",
                    },
                ],
                "layout": {"title":"Avocados Sold"},
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True) # enables hot reload