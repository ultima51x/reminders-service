from datetime import date, timedelta
from typing import List


class Task:
    def __init__(self, id: str, name: str, date_done: date, num_days: int,
                 **kwargs):
        self.id: str = id
        self.name: str = name
        self.date_done: date = date_done
        self.num_days = num_days
        self.description: str = kwargs.get('description') or ''
        self.pending: bool = kwargs.get('pending') or False
        # self.num_tasks: int = kwargs.get('num_tasks') or 0
        self.next_task: int = kwargs.get('next_task') or 0
        self.tasks: List[str] = kwargs.get('tasks') or []

    def subject(self) -> str:
        if self.tasks:
            return self.tasks[self.next_task - 1]
        else:
            return self.name

    def date_due(self) -> date:
        return self.date_done + timedelta(days=self.num_days)

    def due(self) -> bool:
        return date.today() >= self.date_due()

    def __repr__(self):
        return "<Task %s>" % str(self.__dict__)
