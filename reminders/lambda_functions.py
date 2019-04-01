from reminders.airtable_client import AirtableClient
from reminders.reminders_sheet import RemindersSheet
from reminders.task import Task
from reminders.ses_mailer import send_email
import os
import settings
import json

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def reminders_handler(event, context):
    logger.info('reminders - event is {}'.format(event))

    if 'pathParameters' in event.keys():
        task_id = event['pathParameters']['task_id']
        return mark_task_as_done(task_id)

    event_name = event['event']
    if event_name == 'daily_task':
        return daily_task()
    elif event_name == 'weekly_task':
        return weekly_task()


def daily_task():
    logger.info('reminders - daily task')
    tasks = get_sheet().mark_new_tasks()
    t: Task
    for t in tasks:
        send_email(t.email_subject(), t.email_body())
    return True


def weekly_task():
    logger.info('reminders - weekly task')
    tasks = get_sheet().tasks_due()

    if tasks:
        t: Task
        task_strings = [t.subject() for t in tasks]
        send_email("Reminder: Weekly Stuff To Do", "\n".join(task_strings))

    return True


def mark_task_as_done(task_id):
    logger.info('reminders - mark task as done' + task_id)
    task: Task = get_sheet().mark_task_as_done(task_id)
    return {  # response for AWS API Gateway
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({'date_due': str(task.date_due()), 'current_task': task.current_task_name()}),
    }


def get_sheet():
    at = AirtableClient(os.environ['AIRTABLE_SHEET_URL'], os.environ['AIRTABLE_API_KEY'])
    return RemindersSheet(at)
