from dash import Dash, dcc, html, Input, Output
import numpy as np
import pandas as pd
import plotly.express as px
import os

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Logistic Curve"),
    dcc.Graph(id='graph'),
    html.Label([
        "beta0",
        dcc.Slider(-10, 10, 1, 
                   value=0,
                   id='beta0') 
    ]),
    html.Label([
        "beta1",
        dcc.Slider(0, 20, 1, 
                   value=10,
                   id='beta1') 
    ]),
])

@app.callback(
    Output('graph', 'figure'),
    Input('beta0', 'value'),
    Input('beta1', 'value'))
def update_figure(beta0, beta1):
    n = 1000
    x = np.linspace(-1, 1, n)
    eta = beta0 + beta1 * x
    y = 1 / (1 + np.exp(-eta))
    df = pd.DataFrame(zip(x, y), columns=['x','y'])
    fig = px.bar(df, x="x", y='y')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True, host = '127.0.0.1')
    #app.run_server(debug=True, host='jupyter.biostat.jhsph.edu', port = os.getuid() + 35)