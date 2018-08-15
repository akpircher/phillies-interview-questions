import click
import numpy as np

from average_salary import get_salary_data, filter_year, top_salaries, average, standard_deviation


@click.group()
@click.option('-t', '--top', type=int, default=125, show_default=True,
              help='Number of salaries to average.')
@click.option('-y', '--year', type=int, default=2016, show_default=True,
              help='Year to calculate qualifying offer for.')
@click.pass_context
def cli(ctx, top, year):
    ctx.obj['top'] = top
    ctx.obj['year'] = year


@cli.command('calculate')
@click.pass_obj
def calculate(obj):
    # Retrieve the salary data from the database
    df = get_salary_data()

    # Remove dataframe rows not equal to given year
    filtered = filter_year(df, obj['year'])

    # Get the top n salaries
    salaries = top_salaries(filtered, obj['top'])

    # Calculate the qualifying offer and the standard deviation
    qualifying_offer = average(salaries)
    stddev = standard_deviation(salaries)

    qo_str = ('There is not enough data to calculate a qualifying offer for the given parameters.\n'
        + '[year = {year}, number of salaries to average = {top}]').format(**obj)
    if qualifying_offer is not np.nan:
        qo_str = 'The qualifying offer is ${:,} \xB1 ${:,}'.format(qualifying_offer, stddev)

    # Display the data
    print(qo_str)


if __name__ == '__main__':
    cli(obj={})
