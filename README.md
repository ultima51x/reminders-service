# Reminders

This is used for my personal use to keep a list of stuff to do on an Airtable spreadsheet.

Tasks have an interval (example: done every N days).

When I'm supposed to do something, it sends an email with a link.  When I complete it, it pushes back the next time I get reminded N days.

This is written in Python with some type annotations (mypy).

Services used include:
* Airtable (my data, in lieu of a standalone database)
* AWS Lambda (where the code runs)
* AWS API Gateway (endpoint for marking a task as completed)
* AWS CloudWatch Events (triggers Lambda to determine whether I get reminded)

There's a lot more stuff I can do, but this is mostly a toy project, but one I make use of, and hopefully it doesn't cost too much in cloud hosting (my hope).

## Setup

It's best to make a virtual environment.  This used Python 3.7.

```sh
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

within the directory

## Development

It's best to use a virtual environment.
```sh
source env/bin/activate
```

To get out of the virtual environemnt
```sh
deactivate
```

This project attempts to use python type annotations.  One can check them using mypy.
```sh
mypy .
```

There are a few automated tests.
```sh
pytest
```

Adding a requirement
```sh
pip freeze > requirements.txt
git add requirements.txt
git commit
```

I like using IPython for development.  To enable IPython code reloading, check out
https://stackoverflow.com/questions/5364050/reloading-submodules-in-ipython

## Debugging

To bypass Lambda and run this locally, can try something like:

```
from reminders.lambda_functions import daily_task

daily_task()
```

## Environment Variables

This app relies on envrionment variables to run.  Need to import settings.py `import settings` to locally source environment variables within Python.  A file of dummy environment variables is in `.env.dummy`.

## Deploy

If everything is setup correctly, run script `./package.sh`.

This requires aws-cli.

