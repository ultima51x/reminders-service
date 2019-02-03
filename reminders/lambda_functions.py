from reminders.airtable_client import AirtableClient
from reminders.reminders_sheet import RemindersSheet
from reminders.task import Task
from reminders.ses_mailer import send_email
import os

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def reminders_handler(event, context):
    logger.info('reminders - event is {}'.format(event))

    if 'task_id' in event.keys():
        task_id = event['task_id']
        mark_task_as_done(task_id)
        return

    event_name = event['event']
    if event_name == 'daily_task':
        daily_task()
    elif event_name == 'weekly_task':
        weekly_task()


def daily_task():
    logger.info('reminders - daily task')
    tasks = get_sheet().mark_new_tasks()
    t: Task
    for t in tasks:
        send_email(t.email_subject(), t.email_body())


def weekly_task():
    logger.info('reminders - weekly task')
    tasks = get_sheet().tasks_due()
    t: Task
    task_strings = [t.name for t in tasks]
    send_email("Reminder: Weekly Stuff To Do", "\n".join(task_strings))


def mark_task_as_done(task_id):
    logger.info('reminders - mark task as done' + task_id)
    tasks = get_sheet().mark_task_as_done(task_id)
    # respond with something


def get_sheet():
    at = AirtableClient(os.environ['AIRTABLE_SHEET_URL'], os.environ['AIRTABLE_API_KEY'])
    return RemindersSheet(at)
