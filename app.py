import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from average_salary import get_salary_data, filter_year, top_salaries, average, standard_deviation

# Retrieve the salary data from the database
df = get_salary_data()

# Create the application
app = dash.Dash('qualifying_offer')
server = app.server

# Define the webpage layout
app.layout = html.Div([
    html.H1(children='Calculate Qualifying Offer'),
    html.H2(children='Select year and the number of salaries to average'),
    html.Div([
        # Choose what year to get qualifying offer for
        html.Label('Year'),
        dcc.Dropdown(
            id='year-dropdown',
            options=[{'label': str(year), 'value': year} for year in df.Year.unique()],
            clearable=False,
            value=df.Year.drop_duplicates().max(),

        ),

        # Checkbox to determine whether to use duplicates
        html.Label('Select number of salaries to average: '),
        dcc.Input(id='qualifying-limit', type='number', value=125)
    ], style={'margin': 'auto', 'width': '49%'}),
    html.H2(children='Qualifying Offer'),
    html.Div(id='qualifying-offer'),
    html.H2(children='Salary histogram'),
    dcc.Graph(id='salary-distribution')
])

@app.callback(
    dash.dependencies.Output('qualifying-offer', 'children'),
    [dash.dependencies.Input('year-dropdown', 'value'),
    dash.dependencies.Input('qualifying-limit', 'value')])
def calculate(year, nlargest):
    # Filter salaries by year
    filtered = filter_year(df, year)

    # Get the top n salaries, either with or without duplicates
    salaries = top_salaries(filtered, top=nlargest)

    # Calculate the qualifying offer and the standard deviation
    qualifying_offer = average(salaries)
    stddev = standard_deviation(salaries)

    # Display the data
    return 'The qualifying offer is ${:,.2f} \xB1 ${:,.2f}'.format(qualifying_offer, stddev)


@app.callback(
    dash.dependencies.Output('salary-distribution', 'figure'),
    [dash.dependencies.Input('year-dropdown', 'value')])
def update_graph(year):
    """
    Update the histogram
    """
    # Filter the salaries by year
    filtered = filter_year(df, year)

    # Get the unique salaries for this year
    sorted_salaries = df.Salary.sort_values(ascending=False).dropna()
    unique_salaries = sorted_salaries.drop_duplicates()

    groups = sorted_salaries.groupby(pd.cut(sorted_salaries, 5))

    # Convert the bins to strings
    index = groups.size().index.map('(${0.left:,.2f}, ${0.right:,.2f}]'.format)

    return {
        'data': [
            {'x': index.tolist(),
            'y': groups.size().values.tolist(),
            'type': 'bar',
            'name': year}
        ]
    }


if __name__ == '__main__':
    app.run_server(debug=True)
