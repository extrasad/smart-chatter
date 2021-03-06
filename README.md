# SmartChatter

[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Description
SmartChatter is a project to practice rest and graphql implementation of the library chatterbot.
Just fork and add your custom .yml file with the train data and start using it.

## Installation
It requires Python 3.6 or higher.

#### Virtual Environment
Create a virtualenv to isolate package dependencies locally 
```sh
poetry install
```

#### Installing dependencies
To install the dependencies use the Pipfile.

```sh
$ pipenv install
```

#### Apply migrations
To apply migrations run this command
```sh
$ python manage.py migrate
```

#### Creating SuperUser
Create superuser by running this
```sh
$ python manage.py createsuperuser --email admin@example.com --username admin
```

#### Running the server
We're now ready to test the API. Let's fire up the server from the command line.
```sh
$ python manage.py runserver
```
### Database
We are using Sqlite3 for development related efficacy.

### Continuous testing

We are using the package coverage to run the tests.

Read coverage doc: https://coverage.readthedocs.io/en/coverage-4.5.1/

# Running the tests

Run the unit tests with this command.
```sh
$ coverage run manage.py test -v 2
```
To see coverage report,in a html presentation,about the results of the test, run this command
```sh
$ coverage html
```
That command will generate a folder named "htmlcov", open it, look in it for the "index.html" file and open it in a browser to check the results.