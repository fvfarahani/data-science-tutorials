from dash import Dash, dcc, html, Input, Output
import os

app = Dash(__name__)

app.layout = html.Div([
    html.H1("This is a BMI Calculator!"),
    html.Div([
        html.H2('Do you wish to enter metric units [kg, meter] or imperial units [lb, feet]?'),
        dcc.RadioItems(options = [{'label': 'Metric Units', 'value': 'm'},{'label': 'Imperial Units', 'value': 'i'}],
                       value = 'm',
                       id = 'units'),
        html.H2('Enter your weight:'),
        dcc.Input(id = 'weight', value = 95, type = 'number'),
        html.H2('Enter your height:'),
        dcc.Input(id = 'height', value = 1.81, type = 'number'),
        
    ]),
    html.Br(),
    html.H1("Your estimated BMI is: "),
    html.H1(id = 'bmi'),

])


@app.callback(
    Output(component_id = 'bmi'   , component_property = 'children'),
    Input(component_id  = 'weight', component_property = 'value'),
    Input(component_id  = 'height', component_property = 'value'),
    Input(component_id  = 'units'   , component_property = 'value')
)
def update_output_div(weight, height, units):
    if units == 'm':
        rval = weight/(height*height)
    if units == 'i':
        rval = (weight*703)/(height*height)
    return rval

if __name__ == '__main__':
    app.run_server(debug=True, host = '127.0.0.1')
    #app.run_server(debug=True, host='jupyter.biostat.jhsph.edu', port = os.getuid() + 32)