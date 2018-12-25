from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

requires = ['requests']
tests_require = ['freezegun']

setup(
    name="reminders",
    version="0.0.1",
    author="David Hwang",
    author_email="d.hw4ng@gmail.com",
    description="Reminders",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['reminders'],
    install_requires=requires,
    tests_require=tests_require,
    entry_points={
        'console_scripts': [
            'reminders = runner:main',
        ],
    }
)
