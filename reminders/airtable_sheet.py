from reminders.task import Task
from datetime import date, datetime
from typing import List, Dict
import requests


class AirtableSheet:
    def __init__(self, sheet_url: str, api_key: str):
        self.sheet_url = sheet_url
        self.default_headers = {
            'Authorization': 'Bearer ' + api_key,
            'Content-Type': 'application/json'
        }

    def get_tasks(self) -> List[Task]:
        resp = requests.get(self.sheet_url, headers=self.default_headers)
        return [self.__record_to_task(r) for r in resp.json()['records']]

    def update_record(self, airtable_record_id: str, attributes: Dict):
        resp = requests.patch(self.sheet_url + '/' + airtable_record_id,
                              headers=self.default_headers,
                              json={'fields': attributes})

    def __record_to_task(self, record: Dict):
        fields = record['fields']

        attrs = {}
        attrs['description'] = fields.get('description')
        attrs['pending'] = fields.get('pending')
        # attrs['num_tasks'] = fields.get('num_tasks')  # NOTE: might be useless
        attrs['next_task'] = fields.get('next_task')
        attrs['tasks'] = [v for k, v in fields.items() if k.find('task_') == 0]
        date_done: date = datetime.strptime(
            fields['date_done'], '%Y-%m-%d').date()

        return Task(record['id'], fields['name'], date_done, fields['num_days'], **attrs)
