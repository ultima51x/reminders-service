#!/bin/bash

# Make sure pipenv is good to go
pipenv install

# This script just zips up the whole site-packages directory
SITE_PACKAGES=$(pipenv --venv)/lib/python3.7/site-packages
echo "Library Location: $SITE_PACKAGES"
DIR=$(pwd)
cd $SITE_PACKAGES
zip -r9 $DIR/package.zip *

# Add reminders to the zip
cd $DIR
zip -g package.zip reminders/*

# This is for use with lambda, assuming the name is remindersAirtableFunction
aws lambda update-function-code --function-name $AWS_LAMBDA_FCN_NAME --zip-file fileb://package.zip

rm package.zip
