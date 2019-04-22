#!/bin/bash
source .env

# This script just zips up the whole site-packages directory
SITE_PACKAGES=$VIRTUAL_ENV/lib/python3.7/site-packages
echo "Library Location: $SITE_PACKAGES"
DIR=$(pwd)
cd $SITE_PACKAGES
zip -r9 $DIR/package.zip *

# Add reminders to the zip
cd $DIR
zip -g package.zip reminders/*
zip -g package.zip templates/*
zip -g package.zip settings.py

# This is for use with lambda, assuming the name is remindersAirtableFunction
AWS_PROFILE=$AWS_PROFILE aws lambda update-function-code --function-name $AWS_LAMBDA_FCN_NAME --zip-file fileb://package.zip

rm package.zip
