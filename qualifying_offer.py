import click

from average_salary import get_salary_data, top_salaries, average, standard_deviation


@click.group()
@click.option('-t', 'top', type=int, default=125,
              help='Number of salaries to average. Defaults to 125.')
@click.option('--no-duplicates', 'no_duplicates', is_flag=True,
              help='Flag that determines whether to include duplicates or use unique values. Default uses duplicates.')
@click.pass_context
def cli(ctx, top, no_duplicates):
    ctx.obj['top'] = top
    ctx.obj['duplicates'] = not no_duplicates


@cli.command('calculate')
@click.pass_obj
def calculate(obj):
    # Retrieve the salary data from the database
    df = get_salary_data()

    # Get the top n salaries, either with or without duplicates
    salaries = top_salaries(df, obj['top'], obj['duplicates'])

    # Calculate the qualifying offer and the standard deviation
    qualifying_offer = average(salaries)
    stddev = standard_deviation(salaries)

    # Display the data
    print('The qualifying offer is ${:,} \xB1 ${:,}'.format(qualifying_offer, stddev))


if __name__ == '__main__':
    cli(obj={})
