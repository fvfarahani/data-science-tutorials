from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import requests as rq
import bs4
import os

# read the web page into data
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
page = rq.get(url)

# read the page into bs4, then find the table in the page
bs4page = bs4.BeautifulSoup(page.text, 'html.parser')
tables = bs4page.find('table',{'class':"wikitable"})

# create GDP dataframe
GDP = pd.read_html(str(tables), header=[1])[0]
GDP.columns=["Country","Region","IMF_Estimate","IMF_Year","UN_Estimate","UN_Year","WB_Estimate","WB_Year"]
GDP = GDP[['Country','Region', "IMF_Estimate", "UN_Estimate", "WB_Estimate"]]

app = Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(options = [
            {'label' : 'IMF', 'value' : "IMF_Estimate"},
            {'label' : 'United Nations', 'value' : "UN_Estimate"},
            {'label' : 'World Bank', 'value' : "WB_Estimate"}
        ],
        value = "IMF_Estimate", id = 'input-level'
                ),
    dcc.Graph(id = 'output-graph')
])

@app.callback(
    Output('output-graph', 'figure'),
    Input('input-level', 'value'))
def update_figure(selected_estimate):
    fig = px.bar(GDP, x="Region", y=selected_estimate, color="Country", barmode = 'stack')
    fig.update_layout(title_text=selected_estimate, title_x=0.5)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True, host = '127.0.0.1')
    #app.run_server(debug=True, host='jupyter.biostat.jhsph.edu', port = os.getuid() + 30)