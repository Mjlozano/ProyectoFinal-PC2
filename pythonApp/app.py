import dash
import dash_core_components as dccomp
import dash_html_components as html
import flask
import plotly.express as pex
from sqlalchemy import create_engine
import pandas as pnd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

engine = create_engine('postgresql://postgres:password@postgres_pc2:5432/pc2_db')
datos = pnd.read_sql_table("iris", engine)

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server,external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True


if __name__ == '__main__':
    app.run_server(host='0.0.0.0',debug=True, port=8060)