This repository has two functionalities:
1. To provide the web-app source code for displaying the qualifying offer for a given year
2. To provide a command line interface for calculating the qualifying offer

WEB APP INSTRUCTIONS:
1. Go to https://secure-wildwood-80146.herokuapp.com/
2. Select the year you want to calculate the qualilfying offer for from the available years
3. Select the how many salaries you want to average based on the qualifying offer rule (default is 125)

Notes:
    The graph will update only when the year is changed.
    The qualifying offer calculation will update when either the year or the number of salaries to average changes.

COMMAND LINE INTERFACE INSTRUCTIONS:
Create and prepare the environment:
1. Install pipenv to your local python installation
    python -m pip install pipenv
2. Clone the git repository:
    git clone https://github.com/akpircher/phillies-interview-questions.git
    cd phillies-interview-questions
3. Install the requirements (this could take a while because of dash libraries)
    pipenv sync

Command Line Option 1 (non-configurable):
This option will calculate the qualifying offer for the latest year in the database for the top 125 salaries.
1. In the command line type the following and hit enter
    pipenv run average_salary

Command Line Option 2 (configurable):
This command line takes options for year and number of salaries to average

1. To use this option with defaults, type the following in the command line and hit enter
    pipenv run qualifying_offer calculate

2. To see information on how to use the CLI, type the following and hit enter
    pipenv run qualifying_offer

How to use the configurable options (numbers provided are examples, any number will work)
1. To calculate the qualifying offer for 2017, type the following and hit enter
    pipenv run qualifying_offer --year 2017 calculate
    - or -
    pipenv run qualifying_offer -y 2017 calculate

2. To change the number of salaries to average to 250, type the following and hit enter
    pipenv run qualifying_offer --top 250 calculate
    - or -
    pipenv run qualifying_offer -t 250 calculate
