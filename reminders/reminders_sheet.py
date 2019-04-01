from reminders.task import Task
from reminders.airtable_client import AirtableClient
from datetime import date, datetime
from typing import List, Dict, Any
import requests

DATE_FORMAT = '%Y-%m-%d'


class RemindersSheet:
    def __init__(self, airtable: AirtableClient):
        self.airtable: AirtableClient = airtable
        self.tasks: List[Task] = self.get_tasks()

    def get_tasks(self) -> List[Task]:
        resp = self.airtable.get_records()
        return [self.__record_to_task(r) for r in resp.json()['records']]

    def write_task(self, task: Task, values: Dict[str, Any]) -> Task:
        resp = self.airtable.update_record(task.id, values)
        return self.__record_to_task(resp.json())

    def tasks_due(self) -> List[Task]:
        return [t for t in self.tasks if t.due()]

    def mark_task_as_done(self, id) -> Any:
        index = [t.id for t in self.tasks].index(id)

        if index >= 0:
            t = self.tasks[index]
            values: Dict[str, Any] = {'pending': None, 'date_done': datetime.today().strftime(DATE_FORMAT)}
            if t.num_tasks() > 0:
                if t.current_task >= t.num_tasks():
                    values['current_task'] = 1
                else:
                    values['current_task'] = t.current_task + 1
            return self.write_task(t, values)
        else:
            return None

    def mark_new_tasks(self) -> List[Task]:
        new_tasks = [t for t in self.tasks if t.due() and not t.pending]
        t: Task
        for t in new_tasks:
            self.write_task(t, {'pending': True})
        return new_tasks

    def __record_to_task(self, record: Dict) -> Task:
        fields = record['fields']

        attrs = {}
        attrs['description'] = fields.get('description')
        attrs['pending'] = fields.get('pending')
        attrs['current_task'] = fields.get('current_task')

        task_keys = sorted([k for k, v in fields.items() if k.find('task_') == 0])
        attrs['tasks'] = [fields.get(k) for k in task_keys]

        date_done: date = datetime.strptime(
            fields['date_done'], DATE_FORMAT).date()

        return Task(record['id'], fields['name'], date_done, fields['num_days'], **attrs)
