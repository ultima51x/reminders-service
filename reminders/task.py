from datetime import date, timedelta
from typing import List
import os
import settings


class Task:
    def __init__(self, id: str, name: str, date_done: date, num_days: int,
                 **kwargs):
        self.id: str = id
        self.name: str = name
        self.date_done: date = date_done
        self.num_days = num_days
        self.description: str = kwargs.get('description') or self.name
        self.pending: bool = kwargs.get('pending') or False
        self.current_task: int = kwargs.get('current_task') or 0
        self.tasks: List[str] = kwargs.get('tasks') or []

    def subject(self) -> str:
        if self.tasks:
            return self.tasks[self.current_task - 1]
        else:
            return self.name

    def date_due(self) -> date:
        return self.date_done + timedelta(days=self.num_days)

    def due(self) -> bool:
        return date.today() >= self.date_due()

    def num_tasks(self) -> int:
        return len(self.tasks)

    def __repr__(self):
        return "<Task %s>" % str(self.__dict__)

    def completion_url(self) -> str:
        return os.environ['API_GATEWAY_BASE_URL'] + '/' + self.id + '/complete'

    def email_subject(self) -> str:
        return "Reminder: " + self.subject()

    def email_body(self) -> str:
        return "Description: " + self.description + "\n" + "Link: " + self.completion_url()
