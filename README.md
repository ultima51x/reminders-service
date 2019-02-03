# Reminders

Python code which interfaces with a spreadsheet on Airtable.

I'm not sure what it will do quite yet.

## Development

To install packages locally:

```sh
pipenv install -e .
```

To launch a shell within the pipenv for development:
```sh
pipenv shell
```

This project attempts to use python type annotations.  One can check them using mypy.
```sh
mypy reminders tests
```

There are a few automated tests.
```sh
pytest
```

I like using IPython for development

Enabling Ipython code reloading
https://stackoverflow.com/questions/5364050/reloading-submodules-in-ipython
