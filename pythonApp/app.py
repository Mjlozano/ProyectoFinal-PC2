from dash import dcc
from dash import html
import pandas as pd
import flask
import plotly.express as px
from sqlalchemy import create_engine
import dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

engine = create_engine('postgresql://postgres:password@postgres_pc2:5432/pc2_db')
df = pd.read_sql_table("iris", engine)

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server,external_stylesheets=external_stylesheets,suppress_callback_exceptions=True)

app.layout = html.Div(children=[
     html.H1("Iris Flower Dataset"),

    html.H4("Scatter Plot"),
    dcc.Graph(
        id="scatter-plot",
        figure = px.scatter(df, x="sepal_w", y="sepal_l", color="class")
    ),

    html.H4("Scatter and Violin Diagram Plot"),
    dcc.Graph(
        id="scatter-and-violin",
        figure = px.scatter(df, x="sepal_w", y="sepal_l", color="class", marginal_y="violin", marginal_x="box", trendline="ols", template="simple_white")
    ),

    html.H4("Scatter Matrix"),
    dcc.Graph(
        id="scatter-matrix-plot",
        figure = px.scatter_matrix(df, dimensions=["sepal_w", "sepal_l", "petal_w", "petal_l"], color="class")
    )
])


if __name__ == '__main__':
    app.run_server(host='0.0.0.0',debug=True, port=8060)