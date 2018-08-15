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


def top_salaries(df, top=125, duplicates=True):
    if duplicates:
        return df.Salary.sort_values().head(top)
    return df.Salary.nlargest(top)


def average(salaries):
    return salaries.mean()


def standard_deviation(salaries):
    return salaries.std()


if __name__ == '__main__':
    # Retrieve the salary data from the database
    df = get_salary_data()

    # Get the top n salaries, either with or without duplicates
    salaries = top_salaries(df)

    # Calculate the qualifying offer and the standard deviation
    qualifying_offer = average(salaries)
    stddev = standard_deviation(salaries)

    # Display the data
    print('The qualifying offer is ${:,} \xB1 ${:,}'.format(qualifying_offer, stddev))
