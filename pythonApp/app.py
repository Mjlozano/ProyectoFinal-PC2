# importing main libraries
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import flask
import plotly.express as px
from sqlalchemy import create_engine
import dash

# external stylesheets for dash style
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

engine = create_engine('postgresql://postgres:password@postgres_pc2:5432/pc2_db') # extracting engine for collect database connection
df = pd.read_sql_table("iris", engine) # extract data information from database and converting it into a pandas dataframe


app = dash.Dash(__name__, server=server,external_stylesheets=external_stylesheets) # creating dash instance
server = app.server
#app.config.suppress_callback_exceptions = True # ignoring some not necessary alerts from dash callbacks

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

# running all program
if __name__ == '__main__':
    app.run_server(host='0.0.0.0',debug=False, port=8060)