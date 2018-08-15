import click
import pandas as pd
from pandas import to_numeric


def get_salary_data():
    """
    Pull the salary data from the source, and fix the data
    """
    link = 'https://questionnaire-148920.appspot.com/swe/data.html'
    df = pd.read_html(link, attrs = { 'id': 'salaries-table' }, na_values=['no salary data'])[0]
    df['Salary'] = to_numeric(df.Salary.str.replace(r'[$,]', ''))
    return df


def filter_year(df, year=2016):
    return df.loc[df.Year == year]


def top_salaries(df, top=125):
    return df.Salary.nlargest(top)


def average(salaries):
    return salaries.mean()


def standard_deviation(salaries):
    return salaries.std()


if __name__ == '__main__':
    # Retrieve the salary data from the database
    df = get_salary_data()

    filtered = filter_year(df, df.Year.max())

    # Get the top n salaries, either with or without duplicates
    salaries = top_salaries(filtered)

    # Calculate the qualifying offer and the standard deviation
    qualifying_offer = average(salaries)
    stddev = standard_deviation(salaries)

    # Display the data
    print('The qualifying offer is ${:,.2f} \xB1 ${:,.2f}'.format(qualifying_offer, stddev))
